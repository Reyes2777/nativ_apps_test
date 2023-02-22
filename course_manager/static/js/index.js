$(document).ready(function() {
    // Envío del formulario de creación de curso con AJAX
    $('#create-course-form').submit(function(event) {
        event.preventDefault();

        $.ajax({
            type: 'POST',
            url: 'create-course',
            data: $('#create-course-form').serialize(),
            success: function(data) {
                // Limpiar el formulario
                $('#create-course-form')[0].reset();
                console.log(data)
                // Agregar el nuevo curso a la tabla
                $('#course-table > tbody').append(
                    '<tr>' +
                        '<td>' + data.name + '</td>' +
                        '<td>' + data.schedule + '</td>' +
                        '<td>' + data.start_date + '</td>' +
                        '<td>' + data.end_date + '</td>' +
                        '<td>' + data.number_students + '</td>' +
                        '<td>' +
                            '<button class="btn btn-sm btn-warning edit-course-btn" data-course-id="' + data.id + '">Editar</button>' +
                            '<button class="btn btn-sm btn-danger delete-course-btn" data-course-id="' + data.id + '">Eliminar</button>' +
                        '</td>' +

                    '</tr>'
                );
            },
            error: function(xhr, status, error) {
                console.log(xhr.responseText);
            }
        });
    });


  $('table').on('click', 'button.btn-danger', function(event) {
    event.preventDefault();
    const btn = $(this);
    const url = `/courses/delete/${btn.data('course-id')}/`;
    if (confirm('¿Desea eliminar el curso?')) {
      $.ajax({
        url: url,
        type: 'POST',
        beforeSend: function(xhr, settings) {
      xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
    },
        success: function(response) {
          if (response.success) {
            alert('El curso se ha eliminado correctamente.');
            location.reload();
          } else {
            alert('No se ha podido eliminar el curso. Intente de nuevo.');
          }
        },
        error: function() {
          alert('No se ha podido eliminar el curso. Intente de nuevo.');
        }
      });
    }
  });

  $(".edit-course-btn").on('click', function() {
  var courseId = $(this).data('course-id');
  $('#edit-course-modal').modal('show');
  $("#edit-course-form").attr('data-course-id', courseId)

  });

  $(document).on('click', '#update-course-btn', function() {
  var form = $('#edit-course-form');
  var courseId = form.attr('data-course-id');
  console.log(courseId)
  const url = `/courses/update/${courseId}/`;
    const formData = $('#edit-course-form').serialize();
    $.ajax({
      url: url,
      type: 'POST',
      data: formData,
      success: function(response) {
        if (response.success) {
          alert('El curso se ha actualizado correctamente.');
          location.reload();
        } else {
          alert('No se ha podido actualizar el curso. Verifique los errores.');
        }
      },
      error: function() {
        alert('No se ha podido actualizar el curso. Intente de nuevo.');
      }
    });

  });
$(document).ready(function() {
  $('#course-table tbody tr').on('click', function() {
    var courseId = $(this).data('course-id');
    var url = './list-students/' + courseId + '/';
    $.ajax({
      url: url,
      type: 'GET',
      success: function(data) {
        var studentList = $('#student-list');
        studentList.empty();
        $.each(data.students, function(index, student) {
          studentList.append('<li>' + student.name + '</li>');
        });
      },
      error: function() {
        alert('Error al cargar la lista de estudiantes');
      }
    });
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
