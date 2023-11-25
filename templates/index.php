<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The-Vaccine-Distributions-in-Europe From 2021-2023</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="/static/style.css">
    <!-- Include Plotly JavaScript library -->
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>

<body>
    <nav class="navbar navbar-expand-lg">
        <a class="navbar-brand" href="#">The-Vaccine-Distributions-in-Europe From 2021-2023</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item active">
                    <a class="nav-link" href="index.php">Home <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="about us.php">About Us</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="about App.php">About App</a>
                </li>
            </ul>
        </div>
    </nav>
    <div id="choropleth-container"></div>

    <script>
        // Fetch choropleth data from the backend
        fetch('/get-choropleth-data')
            .then(response => response.json())
            .then(data => {
                // Create and render the choropleth map using Plotly
                const container = document.getElementById('choropleth-container');
                Plotly.newPlot(container, JSON.parse(data), {});
            })
            .catch(error => console.error('Error:', error));
    </script>
</body>

</html>
