/**
 * Gulp 依赖
 */
var gulp = require('gulp');

var browser_sync = require('browser-sync').create();
var gulp_uglify   = require('gulp-uglify');
var minify_css   = require('gulp-minify-css');
var rename       = require('gulp-rename');
var sourcemaps   = require('gulp-sourcemaps');

SRC_PATH = 'pamjs/static/pamjs/';
DIST_PATH = 'dist';

JS_SRC_PATH = SRC_PATH + 'js/pam.js';
CSS_SRC_PATH = SRC_PATH + 'css/pam.css';

/**
 * Javascript 压缩
 */
gulp.task('minify_js', function() {
  return gulp.src(JS_SRC_PATH)
      .pipe(sourcemaps.init())
      .pipe(gulp.dest(DIST_PATH))
      .pipe(gulp_uglify())
      .pipe(rename({suffix: '.min'}))
      .pipe(sourcemaps.write('.'))
      .pipe(gulp.dest(DIST_PATH))
});

/**
 * CSS 压缩
 */
gulp.task('minify_css', function () {
    return gulp.src(CSS_SRC_PATH)
        .pipe(sourcemaps.init())
        .pipe(gulp.dest(DIST_PATH))
        .pipe(minify_css())
        .pipe(rename({suffix: '.min'}))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(DIST_PATH))
});

/**
 * 浏览器同步刷新
 */
gulp.task('browser-sync', function() {
    browser_sync.init({
        proxy: 'localhost:9988',
        files: SRC_PATH
    });
});

/**
 * 默认 task
 * 启动 browser-sync 和 watch
 */
gulp.task('default', ['browser-sync'], function() {
  gulp.watch(JS_SRC_PATH, ['minify_js', 'minify_css']);
});
//gulp.task('default', ['browser-sync', 'minify_js', 'minify_css']);
