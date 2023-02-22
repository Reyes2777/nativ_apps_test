function deleteCourse(courseId) {
    const url = `/courses/delete/${courseId}/`;
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
}
