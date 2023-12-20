// Load data using d3.json
d3.json('data.json').then(data => {
  // Convert 'date' to a JavaScript Date object and 'total_vaccinations' to numbers
  data.forEach(d => {
    d.date = new Date(d.date);
    d.total_vaccinations = +d.total_vaccinations || 0;
  });

  // Obtain min and max dates from the dataset
  const minDate = d3.min(data, d => d.date);
  const maxDate = d3.max(data, d => d.date);

  // Initialize variables for slider and play/pause functionality
  let isPlaying = false;
  let playInterval;

  // Create a date slider
  $("#slider").slider({
    range: true,
    min: minDate.getTime(),
    max: maxDate.getTime(),
    step: 24 * 60 * 60 * 1000,
    values: [minDate.getTime(), maxDate.getTime()],
    slide: function(event, ui) {
      const startDate = new Date(ui.values[0]);
      const endDate = new Date(ui.values[1]);

      $('#startLabel').text(startDate.toDateString());
      $('#endLabel').text(endDate.toDateString());

      if (!isPlaying) {
        updateChart(startDate, endDate, data);
      }
    }
  });

  // Initialize chart with default date range using full dataset
  updateChart(minDate, maxDate, data);

  // Play button click event
  $('#playButton').on('click', function() {
    if (!isPlaying) {
      isPlaying = true;
      playInterval = setInterval(() => {
        const sliderValues = $("#slider").slider('option', 'values');
        const currentEndDate = new Date(sliderValues[1]);
        const nextEndDate = new Date(currentEndDate.getTime() + 24 * 60 * 60 * 1000);

        if (nextEndDate <= maxDate) {
          const startDate = new Date(sliderValues[0]);
          $("#slider").slider('values', [startDate.getTime(), nextEndDate.getTime()]);
          updateChart(startDate, nextEndDate, data);
        } else {
          stopSlider();
        }
      }, 1000);
    }
  });

  // Pause button click event
  $('#pauseButton').on('click', stopSlider);

  // Function to stop the slider
  function stopSlider() {
    clearInterval(playInterval);
    isPlaying = false;
  }

  // Function to update the chart based on filtered data
  function updateChart(startDate, endDate, data) {
    const filteredData = data.filter(d => d.date >= startDate && d.date <= endDate);

    // Sort the filteredData by total_vaccinations in descending order
    filteredData.sort((a, b) => b.total_vaccinations - a.total_vaccinations);


    // Remove existing chart
    d3.select('#chart').selectAll('*').remove();

    // Chart dimensions and other elements setup
    const margin = { top: 50, right: 50, bottom: 100, left: 150 };
    const width = 1000 - margin.left - margin.right;
    const height = 600 - margin.top - margin.bottom;

    const svg = d3.select('#chart')
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

    // Create bars based on the sorted data
  svg.selectAll('.bar')
  .data(filteredData)
  .enter().append('rect')
  .attr('class', 'bar')
  .attr('x', d => x(d.location))
  .attr('width', x.bandwidth())
  .attr('y', d => y(d.total_vaccinations))
  .attr('height', d => height - y(d.total_vaccinations))
  .attr('fill', 'steelblue')
  .append('title')
  .text(d => `${d.location}: ${d.total_vaccinations} vaccinations`);
 }
});
