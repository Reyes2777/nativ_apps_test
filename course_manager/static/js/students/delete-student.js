function deleteStudent(studentId){
    if (confirm('¿Desea eliminar el estudiante?')) {
      $.ajax({
        url: `/courses/delete-student/${studentId}/`,
        type: 'POST',
        beforeSend: function(xhr, settings) {
      xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
    },
        success: function(response) {
          if (response.success) {
            alert('El estudiante se ha eliminado correctamente.');
            location.reload();
          } else {
            alert('No se ha podido eliminar el estudiante. Intente de nuevo.');
          }
        },
        error: function() {
          alert('No se ha podido eliminar el estudiante. Intente de nuevo.');
        }
      });
    }
    };
