function createStudent() {
  $.ajax({
    type: 'POST',
    url: 'create-student',
    data: $('#create-student-form').serialize(),
    success: function(data) {
      $('#create-student-form')[0].reset();
      addStudentToTable(data);
    },
    error: function(xhr, status, error) {
      alert(xhr.responseText);
    }
  });
}

function addStudentToTable(data) {
  $('#student-table > tbody').append(
    '<tr>' +
      '<td>' + data.name + '</td>' +
      '<td>' + data.last_name + '</td>' +
      '<td>' + data.age + '</td>' +
      '<td>' + data.email + '</td>' +
      '<td>' + 'Sin Asignar' + '</td>' +
      '<td>' +
        '<button class="btn btn-sm btn-warning edit-student-btn" data-student-id="' + data.id + '">Editar</button>' +
        '<button class="btn btn-sm btn-danger delete-student-btn" data-student-id="' + data.id + '">Eliminar</button>' +
        '<button class="btn btn-sm btn-info subscribe-btn" data-student-id="' + data.id + '">Suscribirse</button>' +
      '</td>' +
    '</tr>'
  );
}
