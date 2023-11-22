document.addEventListener('DOMContentLoaded', function () {
    fetch('/get-choropleth-data')  // Replace this with your actual route to fetch data
        .then(response => response.json())
        .then(data => {
            Plotly.newPlot('visualization', data.data, data.layout);
        })
        .catch(error => console.error('Error:', error));
});
