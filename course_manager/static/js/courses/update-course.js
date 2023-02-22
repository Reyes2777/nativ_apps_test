function showEditCourseModal(courseId) {
    $('#edit-course-modal').modal('show');
    $("#edit-course-form").attr('data-course-id', courseId);
}

function updateCourse(courseId, formData) {
    const url = `/courses/update/${courseId}/`;
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
}
