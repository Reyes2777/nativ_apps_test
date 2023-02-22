$(document).ready(function() {
    $('#create-course-form').submit(createCourse);

    $('table').on('click', 'button.btn-danger', function(event) {
        event.preventDefault();
        const btn = $(this);
        deleteCourse(btn.data('course-id'));
    });

    $(".edit-course-btn").on('click', function() {
        var courseId = $(this).data('course-id');
        showEditCourseModal(courseId);
    });

    $(document).on('click', '#update-course-btn', function() {
        var form = $('#edit-course-form');
        var courseId = form.attr('data-course-id');
        console.log(courseId)
        const formData = $('#edit-course-form').serialize();
        updateCourse(courseId, formData);
    });

    $(document).ready(function() {
        $('#course-table tbody tr').on('click', loadStudentList);
    });

});
