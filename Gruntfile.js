/* Test */

module.exports = function(grunt) {
  grunt.registerTask('default', function() {
    grunt.log.writeln('Starting ...');
  });
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

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
      tasks: ['default']
    }
  });

  // CSS distribution task.
  // grunt.registerTask('test',['css']),
  grunt.registerTask('default', 'recess');
  // Load the plugin that provides the "Watch" task.
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-recess');
};
