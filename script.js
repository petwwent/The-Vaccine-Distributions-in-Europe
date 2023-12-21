// Define your variable declarations and constants here
var margin = { top: 50, right: 50, bottom: 0, left: 50 },
  width = 960 - margin.left - margin.right,
  height = 500 - margin.top - margin.bottom;

var formatTickDate = d3.timeFormat("%b %Y"); // Format for ticks (e.g., Jan 2023)
var formatTooltipDate = d3.timeFormat("%A %e %B, %Y - %H:%M"); // Include month and year in the tooltip

var moving = false;
var targetValue = width;
var timer;

// Declare sliderTime variable
var sliderTime;

// Load the data from data.json
d3.json("data.json").then(function(data) {
  // Convert 'date' to a JavaScript Date object and 'total_vaccinations' to numbers
  data.forEach(d => {
    d.date = new Date(d.date);
    d.total_vaccinations = +d.total_vaccinations || 0;
  });

  // Extract dates from the loaded data
  const dates = data.map(item => new Date(item.date));

  // Filter dates to January and July
  const filteredDates = dates.filter(date => {
    const month = date.getMonth();
    return date.getDate() === 1 && (month === 0 || month === 6);
  });

  // Set startDate and endDate based on the loaded data
  const startDate = filteredDates[0]; // First filtered date
  const endDate = filteredDates[filteredDates.length - 1]; // Last filtered date

  // Calculate the duration for 1 month in milliseconds
  const oneMonthDuration = 1000 * 60 * 60 * 24 * 2; // Changed to milliseconds in a month

  // Create or modify sliderTime with new data
  sliderTime = d3
    .sliderBottom()
    .min(startDate.getTime())
    .max(endDate.getTime())
    .tickValues(filteredDates.map(date => date.getTime()))
    .default(startDate.getTime())
    .width(width + margin.left + margin.right - 20)
    .tickFormat(d3.timeFormat("%b %Y")) // Display ticks as Month Year
    .fill('#2196f3')
    .displayFormat(formatTooltipDate)
    .handle(d3.symbol().type(d3.symbolCircle).size(200)())
    .on("onchange", function(val) {
      // Update the label text to include month and year
      d3.select("p#value-time").text(formatTooltipDate(val));
      
      // Get the new start and end dates based on the slider value
      const newStartDate = new Date(val);
      const newEndDate = new Date(val); // You might adjust this based on your logic

      // Update the chart with new start and end dates
      updateChart(newStartDate, newEndDate, data); // Call the updateChart function with new dates and data
    });

  // Append the slider to a group
  var gTime = d3
    .select("div#slider-time")
    .append("svg")
    .attr("width", 1000)
    .attr("height", 100)
    .append("g")
    .attr("transform", "translate(30,30)");

  gTime.call(sliderTime);

  // Apply custom styles to month and year labels on the slider ticks
  d3.selectAll(".tick text")
    .style("font-weight", function(d) {
      // Check if the tick value corresponds to the beginning of the month (Jan 1st or July 1st)
      var tickDate = new Date(d);
      return tickDate.getDate() === 1 ? "bold" : "normal";
    })
    .style("fill", function(d) {
      // Check if the tick value corresponds to the beginning of the month (Jan 1st or July 1st)
      var tickDate = new Date(d);
      return tickDate.getDate() === 1 ? "black" : "#aaa"; // Change to black for Jan 1st and July 1st, grey for other ticks
    });

  // Initialize value-time paragraph
  d3.select("p#value-time").text(formatTooltipDate(sliderTime.value()));
  d3.select(".parameter-value text").attr("y", "-29");
  d3.selectAll(".tick text").style("text-anchor", "start");
  document.querySelector(".parameter-value path").removeAttribute("tabindex");

  var playButton = d3.select("#play-button");

  playButton.on("click", function() {
    var button = d3.select(this);
    if (button.text() == "Pause") {
      resetTimer();
    } else {
      moving = true;
      timer = setInterval(update, 100); // Move by a month every 2 seconds
      button.text("Pause");
    }
  });

  function update() {
    var offset = sliderTime.value().valueOf() + oneMonthDuration; // Move by a month
    sliderTime.value(offset);
    if (offset >= endDate.getTime()) {
      resetTimer();
    }
    // Update the label text to include month and year
    d3.select("p#value-time").text(formatTooltipDate(sliderTime.value()));
  }

  function resetTimer() {
    moving = false;
    clearInterval(timer);
    playButton.text("Play");
  }

  // Function to update the chart based on filtered data
function updateChart(startDate, endDate, data) {
  const filteredData = data.filter(
    d => d.date >= startDate && d.date <= endDate
  );

  // Sort data in descending order of total_vaccinations
  filteredData.sort((a, b) => b.total_vaccinations - a.total_vaccinations);

  // Create a color scale based on population values
  const colorScale = d3.scaleOrdinal()
    .domain(filteredData.map(d => d.population))
    .range(d3.schemeCategory10); // You can use any color scheme you prefer

  // Remove existing chart and legend
  d3.select('#chart').selectAll('*').remove();
  d3.select('#legend').selectAll('*').remove();

    // Chart dimensions and other elements setup
    const margin = { top: 50, right: 50, bottom: 100, left: 150 };
    const width = 1000 - margin.left - margin.right;
    const height = 600 - margin.top - margin.bottom;

    const svg = d3
      .select('#chart')
      .append('svg')
      .attr('width', width + margin.left + margin.right)
      .attr('height', height + margin.top + margin.bottom)
      .append('g')
      .attr('transform', `translate(${margin.left},${margin.top})`);

  // Create scales
  const x = d3.scaleBand()
    .domain(filteredData.map(d => d.location))
    .range([0, width])
    .padding(0.2);

  const y = d3.scaleLinear()
    .domain([0, d3.max(filteredData, d => d.total_vaccinations)])
    .nice()
    .range([height, 0]);

  // Create axes
  const xAxis = d3.axisBottom(x);
  const yAxis = d3.axisLeft(y).ticks(10);

  // Append axes to SVG
  svg.append('g')
    .attr('class', 'x axis')
    .attr('transform', `translate(0, ${height})`)
    .call(xAxis)
    .selectAll('text')
    .attr('transform', 'rotate(-45)')
    .style('text-anchor', 'end');

  svg.append('g')
    .attr('class', 'y axis')
    .call(yAxis);

  // Add axis labels
  svg.append('text')
    .attr('class', 'axis-label')
    .attr('text-anchor', 'middle')
    .attr('x', width / 2)
    .attr('y', height + margin.bottom / 2)
    .text('Location');

  svg.append('text')
    .attr('class', 'axis-label')
    .attr('text-anchor', 'middle')
    .attr('transform', 'rotate(-90)')
    .attr('x', -height / 2)
    .attr('y', -margin.left + 15)
    .text('Total Vaccinations');

    // Create bars based on the sorted data (in descending order) with different colors based on population
  const bars = svg.selectAll('.bar')
  .data(filteredData)
  .enter()
  .append('rect')
  .attr('class', 'bar')
  .attr('x', d => x(d.location))
  .attr('width', x.bandwidth())
  .attr('y', d => y(d.total_vaccinations))
  .attr('height', d => height - y(d.total_vaccinations))
  .attr('fill', d => colorScale(d.population))
  .append('title')
  .text(d => `${d.location}: ${d.total_vaccinations} vaccinations`);

// Legend
const legend = d3.select('#legend')
  .append('svg')
  .attr('width', 150)
  .attr('height', 150)
  .append('g')
  .attr('transform', 'translate(0,20)');

const legendColors = legend.selectAll('.legend-color')
  .data(filteredData.map(d => d.population))
  .enter().append('g')
  .attr('class', 'legend-color')
  .attr('transform', (d, i) => `translate(0,${i * 20})`);

legendColors.append('rect')
  .attr('width', 15)
  .attr('height', 15)
  .attr('fill', colorScale);

legendColors.append('text')
  .attr('x', 20)
  .attr('y', 10)
  .text(d => `Population: ${d}`);

// Usage of the updateChart function
// ... (Call this function with appropriate startDate, endDate, and the loaded data)
}
// Usage of the updateChart function
updateChart(startDate, endDate, data); // Call this function with appropriate startDate, endDate, and the loaded data

// Start the slide play by default when the page loads
d3.select("#play-button").dispatch("click");
});
