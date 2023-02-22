function createStudent() {
  $.ajax({
    type: 'POST',
    url: 'create-student',
    data: $('#create-student-form').serialize(),
    success: function(data) {
      $('#create-student-form')[0].reset();
      location.reload()
    },
    error: function(xhr, status, error) {
      alert(xhr.responseText);
    }
  });
}
