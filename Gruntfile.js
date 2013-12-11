/* Test */

module.exports = function(grunt) {
  grunt.registerTask('default', function() {
    grunt.log.writeln('Starting ...');
  });
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    copy : {
        font: {
            expand : true,
            cwd : 'bower_components/font-awesome/',
            src : [ 'fonts/*'],
            dest : 'dist'
        }
    },
    recess : {
            testless : {
              options : {
                compile : true,
                compress : false
              },
            src : ['less/font-awesome.less'],
            dest : 'dist/font-awesome.css'
            },
    },

    watch: {
      files: ['less/*.less'],
      tasks: ['recess']
    }
  });

  // CSS distribution task.
  // grunt.registerTask('test',['css']),
  grunt.registerTask('default', ['recess', 'copy']);
  // Load the plugin that provides the "Watch" task.
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-recess');
  grunt.loadNpmTasks('grunt-contrib-copy');
};
