// Fetching data from data.json in the root directory
d3.json('data.json')
  .then(data => {
    console.log('Data:', data); // Log loaded data to verify

    const svg = d3.select('#chart'),
      margin = { top: 40, right: 40, bottom: 60, left: 60 },
      width = +svg.attr('width') - margin.left - margin.right,
      height = +svg.attr('height') - margin.top - margin.bottom;

    const g = svg.append('g')
      .attr('transform', `translate(${margin.left},${margin.top})`);

    const locations = data.map(d => d.location);
    const totalVaccinations = data.map(d => +d.total_vaccinations || 0);

    const x = d3.scaleBand()
      .domain(locations)
      .range([0, width])
      .padding(0.1);

    const y = d3.scaleLinear()
      .domain([0, d3.max(totalVaccinations)])
      .range([height, 0]);

    g.append('g')
      .attr('transform', `translate(0,${height})`)
      .call(d3.axisBottom(x))
      .selectAll('text')
      .attr('transform', 'rotate(-45)')
      .style('text-anchor', 'end');

    g.append('g')
      .call(d3.axisLeft(y).ticks(10))
      .append('text')
      .attr('transform', 'rotate(-90)')
      .attr('y', 6)
      .attr('dy', '-3em')
      .attr('text-anchor', 'end')
      .text('Total Vaccinations');

    g.selectAll('.bar')
      .data(data)
      .enter().append('rect')
      .attr('class', 'bar')
      .attr('x', d => x(d.location))
      .attr('width', x.bandwidth())
      .attr('y', d => y(+d.total_vaccinations || 0))
      .attr('height', d => height - y(+d.total_vaccinations || 0))
      .attr('fill', 'steelblue');
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
