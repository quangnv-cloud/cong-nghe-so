/**
 * DTO Master — DATA TRAFFIC ORGANIC, nguồn dữ liệu chung cho Looker Studio.
 *
 * Gắn (bound) vào file "Bản sao của BBH News Queue" qua Tiện ích mở rộng →
 * Apps Script. Chạy MỘT LẦN `setupMaster()` để:
 *   1. tạo 3 tab mới: brands / post_metrics / traffic_daily (+ header)
 *   2. seed bảng `brands`
 *   3. di trú dữ liệu cũ của Kinh Tế Số:
 *        engagement_metrics  → post_metrics   (brand = kinh_te_so)
 *        audience_growth     → traffic_daily  (brand = kinh_te_so, cột followers + delta)
 *
 * KHÔNG xoá tab cũ (engagement_metrics / audience_growth / posts_log / news_queue) —
 * người dùng muốn giữ lại bản chụp lịch sử. Sau khi các Apps Script kênh (Kinh Tế
 * Số + Công Nghệ Số) chạy `mirrorAnalyticsToMaster_()` vài ngày, nếu số liệu cũ đã
 * được cập nhật lại đầy đủ trong post_metrics thì có thể xoá 2 tab cũ thủ công.
 *
 * File này KHÔNG cần trigger — mỗi Apps Script kênh tự đẩy dữ liệu sang (xem
 * `mirrorAnalyticsToMaster_` trong automation/news-fetch-gas/Code.gs).
 */

var BRANDS_SHEET = 'brands';
var POST_METRICS_SHEET = 'post_metrics';
var TRAFFIC_DAILY_SHEET = 'traffic_daily';

var BRANDS_HEADERS = ['brand', 'label', 'emoji', 'order', 'active'];
var BRANDS_SEED = [
  ['kinh_te_so',   'Kinh Tế Số',   '📊', 1, true],
  ['cong_nghe_so', 'Công Nghệ Số', '💻', 2, true]
  // ['ai_marketing',     'AI Marketing',     '🤖', 3, false],   // bật khi dựng kênh
  // ['marketing_online', 'Marketing Online', '📈', 4, false],
];

var POST_METRICS_HEADERS = [
  'brand', 'platform', 'video_project', 'post_type', 'post_id', 'permalink', 'title',
  'posted_at', 'posted_date', 'views', 'likes', 'reactions', 'comments', 'shares', 'last_checked'
];
var TRAFFIC_DAILY_HEADERS = [
  'brand', 'platform', 'date', 'posts_published',
  'views_total', 'views_delta', 'engagement_total', 'engagement_delta',
  'followers', 'followers_delta'
];

// Legacy tab layouts (bản copy từ BBH News Queue).
var LEGACY_ENGAGEMENT_SHEET = 'engagement_metrics';
var LEGACY_ENGAGEMENT_HEADERS = [
  'channel', 'video_project', 'post_type', 'platform_post_id', 'permalink',
  'title', 'posted_at', 'posted_date', 'posted_time',
  'views', 'likes', 'reactions', 'comments', 'shares', 'last_checked', 'notes'
];
var LEGACY_AUDIENCE_SHEET = 'audience_growth';
var LEGACY_AUDIENCE_HEADERS = ['channel', 'checked_at', 'date', 'time', 'followers', 'notes'];

var LEGACY_BRAND = 'kinh_te_so'; // toàn bộ dữ liệu cũ trong file thuộc kênh Kinh Tế Số
var TZ = 'Asia/Ho_Chi_Minh';

function setupMaster() {
  var ss = SpreadsheetApp.getActive();
  var created = [];

  ensureSheetWithHeaders_(ss, BRANDS_SHEET, BRANDS_HEADERS, created);
  var brandsSheet = ss.getSheetByName(BRANDS_SHEET);
  if (brandsSheet.getLastRow() < 2) {
    brandsSheet.getRange(2, 1, BRANDS_SEED.length, BRANDS_HEADERS.length).setValues(BRANDS_SEED);
  }

  ensureSheetWithHeaders_(ss, POST_METRICS_SHEET, POST_METRICS_HEADERS, created);
  ensureSheetWithHeaders_(ss, TRAFFIC_DAILY_SHEET, TRAFFIC_DAILY_HEADERS, created);

  var migPost = migrateLegacyEngagement_(ss);
  var migTraffic = migrateLegacyAudience_(ss);

  var msg = 'setupMaster xong.\n'
    + 'Tab tạo mới: ' + (created.length ? created.join(', ') : '(đã có sẵn)') + '\n'
    + 'brands: ' + BRANDS_SEED.length + ' dòng\n'
    + 'Di trú post_metrics (kinh_te_so): ' + migPost + ' dòng\n'
    + 'Di trú traffic_daily follower history (kinh_te_so): ' + migTraffic + ' dòng';
  Logger.log(msg);
  try { SpreadsheetApp.getUi().alert(msg); } catch (e) { /* chạy không có UI */ }
  return msg;
}

function ensureSheetWithHeaders_(ss, name, headers, createdOut) {
  var sh = ss.getSheetByName(name);
  if (!sh) {
    sh = ss.insertSheet(name);
    if (createdOut) createdOut.push(name);
  }
  var have = sh.getLastColumn() >= headers.length
    ? sh.getRange(1, 1, 1, headers.length).getValues()[0] : [];
  var same = have.length === headers.length && have.every(function (v, i) { return v === headers[i]; });
  if (!same) {
    sh.getRange(1, 1, 1, headers.length).setValues([headers]);
    sh.setFrozenRows(1);
    sh.getRange(1, 1, 1, headers.length).setFontWeight('bold');
  }
  return sh;
}

function migrateLegacyEngagement_(ss) {
  var src = ss.getSheetByName(LEGACY_ENGAGEMENT_SHEET);
  var dst = ss.getSheetByName(POST_METRICS_SHEET);
  if (!src || src.getLastRow() < 2) return 0;

  var rows = src.getRange(2, 1, src.getLastRow() - 1, LEGACY_ENGAGEMENT_HEADERS.length).getValues();
  var col = {};
  LEGACY_ENGAGEMENT_HEADERS.forEach(function (h, i) { col[h] = i; });

  // upsert theo key brand|post_id để chạy lại setupMaster không tạo trùng
  var existing = {};
  if (dst.getLastRow() > 1) {
    dst.getRange(2, 1, dst.getLastRow() - 1, POST_METRICS_HEADERS.length).getValues()
      .forEach(function (r, i) { existing[r[0] + '|' + r[4]] = i + 2; });
  }

  var out = [];
  rows.forEach(function (r) {
    var postId = String(r[col.platform_post_id] || '').trim();
    if (!postId) return;
    var platform = String(r[col.channel] || '').toLowerCase().trim();
    var row = [
      LEGACY_BRAND, platform, r[col.video_project], r[col.post_type], postId,
      r[col.permalink], r[col.title], r[col.posted_at], r[col.posted_date],
      numOrZero_(r[col.views]), numOrZero_(r[col.likes]), numOrZero_(r[col.reactions]),
      numOrZero_(r[col.comments]), numOrZero_(r[col.shares]), r[col.last_checked]
    ];
    var at = existing[LEGACY_BRAND + '|' + postId];
    if (at) dst.getRange(at, 1, 1, row.length).setValues([row]);
    else out.push(row);
  });
  if (out.length) dst.getRange(dst.getLastRow() + 1, 1, out.length, POST_METRICS_HEADERS.length).setValues(out);
  return rows.length;
}

function migrateLegacyAudience_(ss) {
  var src = ss.getSheetByName(LEGACY_AUDIENCE_SHEET);
  var dst = ss.getSheetByName(TRAFFIC_DAILY_SHEET);
  if (!src || src.getLastRow() < 2) return 0;

  var rows = src.getRange(2, 1, src.getLastRow() - 1, LEGACY_AUDIENCE_HEADERS.length).getValues();
  var col = {};
  LEGACY_AUDIENCE_HEADERS.forEach(function (h, i) { col[h] = i; });

  // (platform, date) -> followers, chọn dòng mới nhất nếu trùng ngày
  var byKey = {};
  rows.forEach(function (r) {
    var platform = String(r[col.channel] || '').toLowerCase().trim();
    var d = asDate_(r[col.date]);
    if (!platform || !d) return;
    byKey[platform + '|' + d] = numOrZero_(r[col.followers]);
  });

  // sắp theo platform + date để tính followers_delta
  var keys = Object.keys(byKey).sort();
  var lastByPlatform = {};
  var out = [];

  // upsert theo key brand|platform|date
  var existing = {};
  if (dst.getLastRow() > 1) {
    dst.getRange(2, 1, dst.getLastRow() - 1, TRAFFIC_DAILY_HEADERS.length).getValues()
      .forEach(function (r, i) { existing[r[0] + '|' + String(r[1]).toLowerCase() + '|' + asDate_(r[2])] = i + 2; });
  }

  keys.forEach(function (k) {
    var parts = k.split('|');
    var platform = parts[0], d = parts[1];
    var followers = byKey[k];
    var prev = lastByPlatform[platform];
    var delta = (prev === undefined) ? '' : followers - prev;
    lastByPlatform[platform] = followers;

    // cột metric bài đăng để trống cho dòng lịch sử (chỉ có follower history)
    var row = [LEGACY_BRAND, platform, d, '', '', '', '', '', followers, delta];
    var at = existing[LEGACY_BRAND + '|' + platform + '|' + d];
    if (at) dst.getRange(at, 1, 1, row.length).setValues([row]);
    else out.push(row);
  });
  if (out.length) dst.getRange(dst.getLastRow() + 1, 1, out.length, TRAFFIC_DAILY_HEADERS.length).setValues(out);
  return keys.length;
}

function numOrZero_(v) { return (v === '' || v === undefined || v === null || isNaN(v)) ? 0 : Number(v); }
function asDate_(v) {
  return v instanceof Date ? Utilities.formatDate(v, TZ, 'yyyy-MM-dd') : String(v || '').slice(0, 10);
}
