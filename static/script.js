// Function to generate the default chart
function generateDefaultChart() {
    // Implement logic to fetch default chart data from the server (Flask route: /defaultChartData)
    fetch('/defaultChartData')
        .then(response => response.json())
        .then(data => {
            // Once data is fetched, use D3.js to render the default chart
            renderChart(data, '#defaultChart');
        })
        .catch(error => {
            console.error('Error fetching default chart data:', error);
        });
}

// Function to generate the comparison chart based on user inputs
function generateComparisonChart(location1, location2) {
    // Implement logic to fetch comparison chart data from the server (Flask route: /comparisonChartData)
    const url = `/comparisonChartData?location1=${location1}&location2=${location2}`;
    fetch(url)
        .then(response => response.json())
        .then(data => {
            // Once data is fetched, use D3.js to render the comparison chart
            renderChart(data, '#comparisonChart');
        })
        .catch(error => {
            console.error('Error fetching comparison chart data:', error);
        });
}

// Function to render the chart using D3.js
function renderChart(data, chartContainer) {
    // D3.js chart rendering logic goes here
    // Example: Create a bar chart based on received data

    // Replace this example code with your actual D3.js chart rendering logic
    const svg = d3.select(chartContainer)
        .append('svg')
        .attr('width', 400)
        .attr('height', 300);

    svg.selectAll('rect')
        .data(data)
        .enter()
        .append('rect')
        .attr('x', (d, i) => i * 50)
        .attr('y', (d) => 300 - d.value * 10)
        .attr('width', 40)
        .attr('height', (d) => d.value * 10)
        .attr('fill', (d) => d.color);  // Use the assigned color property for bars
}

// Function to handle comparison form submission
function handleComparisonFormSubmit(event) {
    event.preventDefault();
    const location1 = document.getElementById('location1').value;
    const location2 = document.getElementById('location2').value;

    // Call function to generate comparison chart with selected locations
    generateComparisonChart(location1, location2);
}

// Event listener for form submission (for comparison)
document.getElementById('comparisonForm').addEventListener('submit', handleComparisonFormSubmit);

// Load the default chart when the page is loaded
document.addEventListener('DOMContentLoaded', function () {
    generateDefaultChart();
});
