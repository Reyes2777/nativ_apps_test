function createCourse(event) {
    event.preventDefault();

    $.ajax({
        type: 'POST',
        url: 'create-course',
        data: $('#create-course-form').serialize(),
        success: function(data) {
            $('#create-course-form')[0].reset();
            console.log(data);
            location.reload()
        },
        error: function(xhr, status, error) {
            console.log(xhr.responseText);
        }
    });
}
