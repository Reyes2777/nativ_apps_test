function openEditCoursesModal(studentId, courseId) {
  $('#edit-courses-modal').modal('show');
  $('#edit-courses-modal').find('#student-id').val(studentId);
  $('#edit-courses-modal').find('#course-id').val(courseId);
}


function subscribeCourse() {
  const studentId = $('#edit-courses-modal').find('#student-id').val();
  const selectedCourses = $('#edit-courses-modal').find('#courses').val();

  $.ajax({
    url: './subscribe/',
    type: 'POST',
    data: {
      'student_id': studentId,
      'courses': selectedCourses
    },
    beforeSend: function(xhr, settings) {
      xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
    },
    success: function(response) {
      if (response.success) {
        alert('El estudiante se ha suscrito correctamente a los cursos.');
        $('#edit-courses-modal').modal('hide');
        location.reload();
      } else {
        alert('No se ha podido suscribir al estudiante. Verifique los errores.');
      }
    },
    error: function() {
      alert('No se ha podido suscribir al estudiante. Intente de nuevo.');
    }
  });
}
