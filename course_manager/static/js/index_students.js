$(document).ready(function() {
    // Escuchar el evento 'submit' del formulario
    $('#create-student-form').submit(function(event) {
        // Prevenir la acción predeterminada del formulario
        event.preventDefault();

        // Enviar la petición AJAX
        $.ajax({
            type: 'POST',
            url: 'create-student',  // Reemplazar con la URL correcta
            data: $('#create-student-form').serialize(),
            success: function(data) {
                // Limpiar el formulario
                $('#create-student-form')[0].reset();

                // Agregar el nuevo estudiante a la tabla
                $('#student-table > tbody').append(
                    '<tr>' +
                        '<td>' + data.name + '</td>' +
                        '<td>' + data.last_name + '</td>' +
                        '<td>' + data.age + '</td>' +
                        '<td>' + data.email + '</td>' +
                        '<td>' + data.courses + '</td>' +
                        '<td>' +
                            '<button class="btn btn-warning edit-student-btn" data-student-id="' + data.id + '">Editar</button>' +
                            '<button class="btn btn-danger delete-student-btn" data-student-id="' + data.id + '">Eliminar</button>' +
                        '</td>' +
                    '</tr>'
                );
            },
            error: function(xhr, status, error) {
                alert(xhr.responseText);
            }
        });
    });

    $('table').on('click', 'button.btn-danger', function(event) {
    event.preventDefault();
    const btn = $(this);
    const url = `/courses/delete-student/${btn.data('student-id')}/`;
    if (confirm('¿Desea eliminar el estudiante?')) {
      $.ajax({
        url: url,
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
  });


  $("#edit-student-btn").on('click', function() {
  var studentId = $(this).data('student-id');
  $('#edit-student-modal').modal('show');
  $("#edit-student-form").attr('data-student-id', studentId)

  });

   $(document).on('click', '#update-student-btn', function() {
  var form = $('#edit-student-form');
  var studentId = form.attr('data-student-id');
  console.log(studentId)
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

  });

});




function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
