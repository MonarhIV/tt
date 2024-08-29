function fetchData() {
  $.ajax({
    url: 'http://127.0.0.1:4000/api/ticket',
    method: 'GET',
    success: function(response) {
      var tickets = response.tikets; // Достаём массив тикетов из ответа
      var tableBody = $('#data-table tbody');
      tableBody.empty(); // Очистить текущие данные, если это необходимо
      tickets.forEach(function(ticket) {
        tableBody.append('<tr><td>' + ticket.id + '</td><td>' +
                         ticket.name + '</td><td>' +
                         ticket.timeCreate + '</td><td>' + 
                         ticket.timeToResolve + '</td><td>' + 
                         ticket.status + '</td></tr>');
      });
    }
  });
}

// Вызывать функцию для получения данных каждые 5 секунд
setInterval(fetchData, 15000);
// Вызовем сразу, чтобы не ждать интервал
fetchData();