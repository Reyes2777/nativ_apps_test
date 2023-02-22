
$(document).ready(function() {

  $('#create-student-form').submit(function(event) {
    event.preventDefault();
    createStudent();
  });

  $('table').on('click', 'button.btn-danger', function(event) {
    event.preventDefault();
    const studentId = $(this).data('student-id');
    deleteStudent(studentId);
  });

  $(".edit-student-btn").on('click', function() {
  var studentId = $(this).data('student-id');
  $('#edit-student-modal').modal('show');
  $("#edit-student-form").attr('data-student-id', studentId)
  });


  $("#edit-student-btn").on('click', editStudentModalHandler);

  $(document).on('click', '#update-student-btn', updateStudentHandler);

  $('.subscribe-btn').click(function() {
  var studentId = $(this).data('student-id');
  var courseId = $(this).data('course-id');
  openEditCoursesModal(studentId, courseId);
});

  $('#update-courses-btn').click(subscribeCourse);

});
