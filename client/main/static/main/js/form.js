document.getElementById('requestForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Предотвращаем отправку формы
    
    var status = document.getElementById('status').value;
    var name = document.getElementById('name').value;
    var time = document.getElementById('time').value;
    const formData = {
        source_system: 'client',
        name: name,
        status: status,
        timeToSolve: time
    };
    if (status === 'solved') {
        alert('Заявка может быть только в статусе Новая и Ожидает ответа');
        
    } else {
        $.ajax({
            url: 'http://127.0.0.1:4000/api/ticket',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function(response) {
                alert('Форма отправлена успешно:', response);
            },
            error: function(xhr) {
                if (xhr.status === 422) {
                    const errorData = xhr.responseJSON;
                    alert(`Ошибка: ${errorData.message}`);
                } else {
                    alert('Произошла ошибка при отправке формы');
                }
            }
        })
    }
});