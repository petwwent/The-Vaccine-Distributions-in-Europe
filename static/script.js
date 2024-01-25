d3.json('/static/data.json').then(function (data) {
  var margin = { top: 20, right: 20, bottom: 100, left: 150 },
    width = 1000 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

  var svg = d3
    .select("#chart-container")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  var uniqueDates = [...new Set(data.map((d) => d.date))];
  uniqueDates.sort();

  const dates = data.map((item) => new Date(item.date));

  const filteredDates = dates.filter((date) => {
    const month = date.getMonth();
    return date.getDate() === 1 && (month === 0 || month === 6);
  });

  const startDate = filteredDates[0];
  const endDate = filteredDates[filteredDates.length - 1];

 
  function updateSummaryTable(selectedDate, data) {
    var parsedDate = new Date(selectedDate);
  
    // Filter data based on selected date
    var filteredData = data.filter((d) => {
      var currentDate = new Date(d.date);
      return (
        currentDate.getMonth() === parsedDate.getMonth() &&
        currentDate.getFullYear() === parsedDate.getFullYear()
      );
    });
  
    // Create a map to store aggregated data for each location
    var locationDataMap = new Map();
  
    // Aggregate data for each location
    filteredData.forEach((d) => {
      var locationKey = d.location;
      if (!locationDataMap.has(locationKey)) {
        locationDataMap.set(locationKey, {
          iso_code: d.iso_code,
          date: d.date,
          location: d.location,
          population: d.population,
          total_cases: 0,
          total_vaccinations: 0,
          people_vaccinated: 0,
        });
      }
  
      var locationData = locationDataMap.get(locationKey);
      locationData.total_cases += d.total_cases;
      locationData.total_vaccinations += d.total_vaccinations;
      locationData.people_vaccinated += d.people_vaccinated;
    });
  
    var tableBody = d3.select('#statistics-table tbody');
  
    // Remove existing rows
    tableBody.selectAll('tr').remove();
  
    // Add new rows
    var rows = tableBody
      .selectAll('tr')
      .data(Array.from(locationDataMap.values()))
      .enter()
      .append('tr');
  
    rows.append('td').text((d) => d.iso_code);
    rows.append('td').text((d) => d.date);
    rows.append('td').text((d) => d.location);
    rows.append('td').text((d) => d.population);
    rows.append('td').text((d) => d.total_cases);
    rows.append('td').text((d) => d.total_vaccinations);
    rows.append('td').text((d) => d.people_vaccinated);
  }
   


  var dateDropdown = d3.select('#date-dropdown');

  dateDropdown
    .selectAll('option')
    .data(uniqueDates)
    .enter()
    .append('option')
    .text((d) => new Date(d).toISOString().slice(0, 10))
    .attr('value', (d) => new Date(d).toISOString().slice(0, 10));

  // Initial updateChart call with all locations using the first date in the dataset
  updateChart(uniqueDates[0]);

  var dateScale = d3
    .scaleTime()
    .domain([new Date(d3.min(uniqueDates)), new Date(d3.max(uniqueDates))])
    .range([0, width]);

  var slider = d3
    .sliderBottom(dateScale)
    .step(24 * 60 * 60 * 1000)
    .width(width)
    .tickFormat(d3.timeFormat('%Y-%m-%d'))
    .on('onchange', (val) => {
      var selectedDate = d3.timeFormat('%Y-%m-%d')(val);
      updateChart(selectedDate);
      dateDropdown.property('value', selectedDate);
      d3.select('#selected-date').text('Selected Date: ' + selectedDate);
      updateSummaryTable(startDate, endDate, data);
    });

  d3.select('#slider-container')
    .append('svg')
    .attr('width', width + margin.left + margin.right)
    .attr('height', 70)
    .append('g')
    .attr('transform', 'translate(' + margin.left + ',30)')
    .call(slider);

  var monthDropdown = d3.select('#month-dropdown');
  var yearDropdown = d3.select('#year-dropdown');

  var months = d3.range(1, 13).map((d) => d.toString().padStart(2, '0'));
  monthDropdown
    .selectAll('option')
    .data(months)
    .enter()
    .append('option')
    .text((d) => d)
    .attr('value', (d) => d);

  var years = [...new Set(data.map((d) => new Date(d.date).getFullYear()))];
  yearDropdown
    .selectAll('option')
    .data(years)
    .enter()
    .append('option')
    .text((d) => d)
    .attr('value', (d) => d);

    var locationCheckboxes = d3.select("#location-checkboxes");

    // Add individual location checkboxes
    locationCheckboxes
      .selectAll("label")
      .data([...new Set(data.map((d) => d.location))])
      .enter()
      .append("label")
      .text((d) => d)
      .append("input")
      .attr("type", "checkbox")
      .attr("class", "location-checkbox")
      .attr("value", (d) => d);
    
    // Add "Select All" checkbox
    var selectAllContainer = d3.select("#select-all-container");
    selectAllContainer
      .append("input")
      .attr("type", "checkbox")
      .attr("id", "select-all-checkbox");
    
    selectAllContainer.select("label").attr("for", "select-all-checkbox");
    
    // Add event listener to checkboxes
    locationCheckboxes.selectAll(".location-checkbox").on("change", function () {
      updateChart(slider.value());
    });
    
    // Add functionality for the "Select All" checkbox
    d3.select("#select-all-checkbox").on("change", function () {
      const isChecked = this.checked;
    
      // Check or uncheck all location checkboxes based on the "Select All" checkbox state
      locationCheckboxes.selectAll(".location-checkbox").property("checked", isChecked);
    
      // Update the chart based on the current slider value
      updateChart(slider.value());
    });


  slider.on('onchange', (val) => {
    var selectedDate = d3.timeFormat('%Y-%m-%d')(val);
    updateChart(selectedDate);
    dateDropdown.property('value', selectedDate);
    d3.select('#selected-date').text('Selected Date: ' + selectedDate);
    updateSummaryTable(startDate, endDate, data);
  });

  document.getElementById('month-dropdown').addEventListener('change', function () {
    var selectedMonth = document.getElementById('month-dropdown').value;
    var selectedYear = document.getElementById('year-dropdown').value;
    var targetDate = selectedYear + '-' + selectedMonth + '-01';
    var parsedDate = new Date(targetDate);
    slider.value(parsedDate);
    updateChart(targetDate);
  });

  document.getElementById('year-dropdown').addEventListener('change', function () {
    var selectedMonth = document.getElementById('month-dropdown').value;
    var selectedYear = document.getElementById('year-dropdown').value;
    var targetDate = selectedYear + '-' + selectedMonth + '-01';
    var parsedDate = new Date(targetDate);
    slider.value(parsedDate);
    updateChart(targetDate);
  });


  function updateChart(selectedDate) {
    svg.selectAll('.bar').remove();
    svg.selectAll('.x.axis').remove();
    svg.selectAll('.y.axis').remove();
    svg.selectAll('.axis-label').remove();

    // Convert the selected date to a JavaScript Date object
    var parsedDate = new Date(selectedDate);
  
    // If no selected date is provided, use the slider's current value
  var parsedDate = selectedDate ? new Date(selectedDate) : slider.value();

  // Get the selected checkboxes
  var selectedLocations = d3.selectAll('.location-checkbox:checked').nodes().map((node) => node.value);

  // Filter data based on selected date and locations
  var filteredData = data.filter((d) => {
    var currentDate = new Date(d.date);
    return (
      currentDate.getMonth() === parsedDate.getMonth() &&
      currentDate.getFullYear() === parsedDate.getFullYear() &&
      (!selectedLocations.length || selectedLocations.includes(d.location))
    );
  });

  // Add tooltip container
  var tooltip = d3.select("body").append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);


  var sortedData = filteredData.sort((a, b) => b.total_vaccinations - a.total_vaccinations);

    const x = d3
      .scaleBand()
      .domain(sortedData.map((d) => d.location))
      .range([0, width])
      .padding(0.2);

    const y = d3
      .scaleLinear()
      .domain([0, d3.max(sortedData, (d) => d.total_vaccinations)])
      .nice()
      .range([height, 0]);

    const colorScale = d3.scaleOrdinal().domain(sortedData.map((d) => d.location)).range(d3.schemeCategory10);

    svg.selectAll('.bar')
      .data(sortedData)
      .enter()
      .append('rect')
      .attr('class', 'bar')
      .attr('x', (d) => x(d.location))
      .attr('width', x.bandwidth())
      .attr('y', (d) => y(d.total_vaccinations))
      .attr('height', (d) => height - y(d.total_vaccinations))
      .attr('fill', (d) => colorScale(d.location))
      .on('mouseover', function (event, d) {
        tooltip.transition().duration(200).style('opacity', 0.9);
      
        // Calculate people vaccinated percentage
        const percentageVaccinated = ((d.people_vaccinated / d.population) * 100).toFixed(2);
      
        tooltip.html(
          `<strong>${d.location}</strong><br>
          Date: ${d.date}<br>
          People Vaccinated: ${percentageVaccinated}%<br>
          Total Cases: ${d.total_cases}<br>
          Total Vaccinations: ${d.total_vaccinations}`
        )
        .style('left', (event.pageX) + 'px')
        .style('top', (event.pageY - 28) + 'px');
      })
      .on('mousemove', function (event) {
        tooltip.style('left', (event.pageX) + 'px')
          .style('top', (event.pageY - 28) + 'px');
      })
      .on('mouseout', function () {
        console.log('Mouse out event triggered'); // Debugging line
        tooltip.transition().duration(500).style('opacity', 0);
      });
  
      

    const xAxis = d3.axisBottom(x);
    const yAxis = d3.axisLeft(y).ticks(10);

    svg.append('g').attr('class', 'x axis').attr('transform', `translate(0, ${height})`).call(xAxis).selectAll('text').attr('transform', 'rotate(-45)').style('text-anchor', 'end');

    svg.append('g').attr('class', 'y axis').call(yAxis);

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

    // Append flags on top of each bar
  svg.selectAll('.flag').remove();

  // Remove existing flags
  svg.selectAll('.flag').remove();

  // Create a set to store unique locations
  const uniqueLocations = new Set();

  // Filter data for unique locations
  const uniqueData = sortedData.filter((d) => {
    if (!uniqueLocations.has(d.location)) {
      uniqueLocations.add(d.location);
      return true;
    }
    return false;
  });

  // Append flags for unique locations
  const flagWidth = 10;
  const flagHeight = 15;

  // Update the flags with a slower transition duration
  svg
  .selectAll('.flag')
  .data(uniqueData)
  .enter()
  .append('image')
  .attr('class', 'flag')
  .attr('width', flagWidth)
  .attr('height', flagHeight)
  .attr('x', (d) => x(d.location) + x.bandwidth() / 2 - flagWidth / 2)
  .attr('y', (d) => y(d.total_vaccinations) - flagHeight)
  .attr('xlink:href', (d) => `/flags/${d.location}.png`); 

  


// Update the flags with a slower transition duration
svg.selectAll('.flag')
.data(uniqueData)
.enter()
.append('image')
.attr('class', 'flag')
.attr('width', flagWidth)
.attr('height', flagHeight)
.attr('x', (d) => x(d.location) + x.bandwidth() / 2 - flagWidth / 2)
.attr('y', (d) => y(d.total_vaccinations) - flagHeight)
.attr('xlink:href', (d) => `/flags/${d.location}.png`);


// Update the statistics table
updateSummaryTable(selectedDate, filteredData);
}
});
