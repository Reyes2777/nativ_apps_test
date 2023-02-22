function loadStudentList() {
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
}
