function editStudentModalHandler() {
  var studentId = $(this).data('student-id');
  $('#edit-student-modal').modal('show');
  $("#edit-student-form").attr('data-student-id', studentId);
}

function updateStudentHandler() {
  var form = $('#edit-student-form');
  var studentId = form.attr('data-student-id');
  const url = `/courses/update-student/${studentId}/`;
  const formData = $('#edit-student-form').serialize();

  $.ajax({
    url: url,
    type: 'POST',
    data: formData,
    success: function(response) {
      if (response.success) {
        alert('El estudiante se ha actualizado correctamente.');
        location.reload();
      } else {
        alert('No se ha podido actualizar el estudiante. Verifique los errores.');
      }
    },
    error: function() {
      alert('No se ha podido actualizar el estudiante. Intente de nuevo.');
    }
  });
}
