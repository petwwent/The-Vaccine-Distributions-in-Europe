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

  function createSummaryTable(data) {
    const columns = [
      { key: 'total_cases', label: 'Total-Cases' },
      { key: 'population', label: 'Population' },
      { key: 'total_vaccinations', label: 'Total-vaccinations' },
      { key: 'people_vaccinated', label: 'vaccinated' },
      { key: 'people_fully_vaccinated', label: 'fully_vaccinated' },
      { key: 'total_vaccinations_per_hundred', label: 'Total_v_per_100' },
      { key: 'people_vaccinated_per_hundred', label: 'vaccinated_per_100' },
      { key: 'people_fully_vaccinated_per_hundred', label: 'fully_vaccinated_per100' }
    ];
  
    const locations = Array.from(new Set(data.map(d => d.location)));

  const startDate = new Date(data[0].date);
  const endDate = new Date(data[data.length - 1].date);

  const dateRange = `${startDate.toLocaleString('default', { month: 'short', year: 'numeric' })} - ${endDate.toLocaleString('default', { month: 'short', year: 'numeric' })}`;

  const table = document.createElement('table');
  table.classList.add('summary-table'); // Add a class to the table

  const headerRow = table.insertRow();
  let cell = headerRow.insertCell();
  cell.textContent = 'Location';
  cell.style.fontWeight = 'bold';

  columns.forEach(column => {
    cell = headerRow.insertCell();
    cell.textContent = column.label;
    cell.style.fontWeight = 'bold';
    cell.classList.add('summary-table-cell'); // Add a class to the table cells
  });

  let dateCell = headerRow.insertCell();
  dateCell.textContent = 'Date Range';
  dateCell.style.fontWeight = 'bold';
  dateCell.classList.add('summary-table-cell'); // Add a class to the table cells

  locations.forEach(location => {
    const locationData = data.filter(d => d.location === location);
    const row = table.insertRow();
    let cell = row.insertCell();
    cell.textContent = location;

    columns.forEach(column => {
      cell = row.insertCell();
      const columnData = locationData.map(d => +d[column.key] || 0);
      const total = d3.sum(columnData);
      cell.textContent = total;
      cell.classList.add('summary-table-cell'); // Add a class to the table cells
    });

    let dateCell = row.insertCell();
    dateCell.textContent = dateRange;
    dateCell.classList.add('summary-table-cell'); // Add a class to the table cells
  });

  document.getElementById('summary-table').appendChild(table);
}

// Call the function to create the summary table using the loaded data
createSummaryTable(data); // 'data' is assumed to be the loaded dataset from data.json
  

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


  // Add checkboxes for selecting locations
  const locations = Array.from(new Set(data.map(d => d.location))); // Get unique locations
  const locationCheckboxes = d3.select("#location-checkboxes")
    .selectAll("label")
    .data(locations)
    .enter()
    .append("label")
    .text(d => d)
    .append("input")
    .attr("type", "checkbox")
    .attr("value", d => d)
    .on("change", updateSelectedLocations); // Call the function to update selected locations on change

  // Add functionality for the "Select All" checkbox
  d3.select("#select-all-checkbox").on("change", function() {
    const isChecked = this.checked;

    // Check or uncheck all location checkboxes based on the "Select All" checkbox state
    d3.selectAll("#location-checkboxes input[type=checkbox]")
      .property("checked", isChecked)
      .dispatch("change"); // Trigger the change event for selected locations
  });  

  // Assuming 'data' is the loaded dataset from data.json
const uniqueDates = Array.from(new Set(data.map(d => d.date))); // Extract unique dates

// Filter dates within the specified range (from Jan 2021 to Dec 2023)
const filteredDropdownDates = uniqueDates.filter(date => {
  const year = date.getFullYear();
  return year >= 2021 && year <= 2023; // Filter dates from 2021 to 2023
});

// Create an array to hold all months from Jan to Dec
const allMonths = [
  "January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
];

// Generate dropdown options for each month and year
const dropdownOptions = [];
for (let year = 2021; year <= 2023; year++) {
  for (let month = 0; month < 12; month++) {
    const currentDate = new Date(year, month, 1);
    const formattedDate = currentDate.toLocaleDateString("en-US", { month: "short", year: "numeric" });
    if (filteredDropdownDates.find(date => date.getMonth() === month && date.getFullYear() === year)) {
      dropdownOptions.push({
        date: currentDate,
        label: formattedDate,
        value: currentDate.getTime()
      });
    }
  }
}

// Add an event listener to the search button
d3.select("#search-button").on("click", function() {
  const startDate = new Date(document.getElementById("start-date").value);
  const endDate = new Date(document.getElementById("end-date").value);

  // Check if the entered dates are valid
  if (startDate && endDate && startDate <= endDate) {
    // Perform actions with the selected start and end dates
    console.log("Start Date:", startDate);
    console.log("End Date:", endDate);

    // Stop the chart from playing if it's in a playing state
    if (moving) {
      resetTimer();
    }

    // Update the slider position to the selected date (if sliderTime exists)
    if (sliderTime) {
      sliderTime.value(startDate.getTime());
    }

    // Call a function to update the chart based on the selected date range
    updateChart(startDate, endDate, data);
  } else {
    alert("Please select a valid date range.");
  }
});

  // Function to update selected locations
function updateSelectedLocations() {
  const selectedLocations = d3.selectAll("#location-checkboxes input:checked").nodes().map(node => node.value);

  
  const selectedDate = new Date(d3.select("#search-date").property("value"));

  // Update chart based on selected locations and date
  updateChart(selectedDate, selectedDate, data.filter(d => selectedLocations.includes(d.location)));
}



  /// Function to update the chart based on filtered data
  function updateChart(startDate, endDate, data) {
    let filteredData = data.filter(d => d.date >= startDate && d.date <= endDate);
  
    const selectedLocations = d3.selectAll("#location-checkboxes input:checked").nodes().map(node => node.value);
    
    if (selectedLocations.length > 0) {
      // If locations are selected, filter data based on selected locations
      filteredData = filteredData.filter(d => selectedLocations.includes(d.location));
    }
  
    // Group the filtered data by location and aggregate total vaccinations within the date range
    const aggregatedData = d3.rollup(
      filteredData,
      group => d3.sum(group, d => d.total_vaccinations),
      d => d.location
    );
  
    // Convert the aggregated data back to an array of objects for easier chart rendering
    const aggregatedArray = Array.from(aggregatedData, ([location, total_vaccinations]) => ({
      location,
      total_vaccinations
    }));

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
.append('title') // Append tooltip to show data on hover
.text(d => `${d.location}\nDate Range: ${formatTooltipDate(startDate)} - ${formatTooltipDate(endDate)}\nTotal Vaccinations: ${d.total_vaccinations}`);


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
}
// Usage of the updateChart function
updateChart(startDate, endDate, data); // Call this function with appropriate startDate, endDate, and the loaded data

// Function to update selected locations
function updateSelectedLocations() {
  const selectedLocations = d3.selectAll("#location-checkboxes input:checked").nodes().map(node => node.value);
}

// Start the slide play by default when the page loads
d3.select("#play-button").dispatch("click");
});
