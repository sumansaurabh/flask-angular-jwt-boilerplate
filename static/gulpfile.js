/* jshint node:true */
'use strict';

var gulp = require('gulp'),
    useref = require('gulp-useref'),
    gulpif = require('gulp-if'),
    uglify = require('gulp-uglify'),
    $ = require('gulp-load-plugins')({lazy: true});


gulp.task('partials', function () {
    return gulp.src(['app/views/**/*'])
        .pipe(gulp.dest('dist/views'));
});


gulp.task('build_styles', function() {
  return gulp.src('app/styles/main.less')
    .pipe($.plumber())
    .pipe($.less())
    .pipe($.autoprefixer({browsers: ['last 1 version']}))
    .pipe(gulp.dest('app/styles'));
});

gulp.task('styles',['build_styles'], function() {
    return gulp.src([
        'app/styles/main.css',
    ], {
        dot: true
    }).pipe(gulp.dest('dist/styles'));
});



gulp.task('fonts', function() {
  return gulp.src(require('main-bower-files')().concat('app/fonts/**/*')
    .concat('bower_components/bootstrap/fonts/*'))
    .pipe($.filter('**/*.{eot,svg,ttf,woff,woff2}'))
    .pipe($.flatten())
    .pipe(gulp.dest('dist/fonts'))
    .pipe(gulp.dest('.tmp/fonts'));
});

gulp.task('images', function() {
    return gulp.src([
        'app/images/*',
    ], {
    dot: true
    }).pipe(gulp.dest('dist/images'));
});

gulp.task('extras', function() {
  return gulp.src([
    'app/*.*',
    '!app/*.html',
    'node_modules/apache-server-configs/dist/.htaccess'
  ], {
    dot: true
  }).pipe(gulp.dest('dist'));
});


gulp.task('clean', require('del').bind(null, ['.tmp', 'dist']));

// gulp.task('serve', ['wiredep', 'connect', 'fonts', 'watch'], function() {
// 	if (argv.open) {
// 		require('opn')('http://localhost:8000');
// 	}
// });

// gulp.task('watch', ['connect'], function() {
// 	$.livereload.listen();

// 	// watch for changes
// 	gulp.watch([
// 		'app/**/*.html',
// 		'.tmp/styles/**/*.css',
// 		'app/scripts/**/*.js',
// 		'app/images/**/*'
// 	]).on('change', $.livereload.changed);

// 	gulp.watch('app/styles/**/*.less', ['styles']);
// 	// gulp.watch('bower.json', ['wiredep']);
// });

gulp.task('builddist',['partials', 'styles', 'fonts', 'extras', 'images'], function(){

    var assets = $.useref.assets({searchPath: './app/'});

    return gulp
        .src('./app/index.html')
        .pipe(assets)
        .pipe(assets.restore())
        .pipe($.useref())
        .pipe(gulp.dest('./dist'));
});

gulp.task('build', ['clean'], function() {
	gulp.start('builddist');
});