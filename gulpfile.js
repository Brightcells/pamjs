var gulp = require('gulp');

var gulp_uglify   = require('gulp-uglify');
var minify_css   = require('gulp-minify-css');
var rename       = require('gulp-rename');
var sourcemaps   = require('gulp-sourcemaps');

SRC_PATH = 'pamjs/static/pamjs/';
DIST_PATH = 'dist';

JS_SRC_PATH = SRC_PATH + 'js/pam.js';
CSS_SRC_PATH = SRC_PATH + 'css/pam.css';

gulp.task('minify_js', function() {
  return gulp.src(JS_SRC_PATH)
      .pipe(sourcemaps.init())
      .pipe(gulp.dest(DIST_PATH))
      .pipe(gulp_uglify())
      .pipe(rename({suffix: '.min'}))
      .pipe(sourcemaps.write('.'))
      .pipe(gulp.dest(DIST_PATH))
});

gulp.task('minify_css', function () {
    return gulp.src(CSS_SRC_PATH)
        .pipe(sourcemaps.init())
        .pipe(gulp.dest(DIST_PATH))
        .pipe(minify_css())
        .pipe(rename({suffix: '.min'}))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(DIST_PATH))
})

//gulp.task('default', function() {
//  gulp.watch(JS_SRC_PATH, ['minify_js']);
//});
gulp.task('default', ['minify_js', 'minify_css']);
