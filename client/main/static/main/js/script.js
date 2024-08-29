function fetchData() {
  $.ajax({
      url: 'http://127.0.0.1:4000/api/ticket',
      method: 'GET',
      success: function(data) {
          var tableBody = $('#data-table tbody');
          tableBody.empty(); // Очистить текущие данные
          data.forEach(function(entry) {
              tableBody.append('<tr><td>' + entry.id + '</td><td>' +
                               entry.name + '</td><td>' + entry.TimeCreate + '</td><td>' + 
                               entry.TimeToResolve + '</td><td>' + 
                               entry.status + '</td></tr>');
          });
      }
  });
}

// Вызывать функцию для получения данных каждые 5 секунд
setInterval(fetchData, 5000);
// Вызовем сразу, чтобы не ждать интервал
fetchData();