import requests
import json




def convert_to_fhir_bundle(existing_vaccination_data):
    bundle = {
        "resourceType": "Bundle",
        "type": "transaction",  # or "collection" depending on your use case
        "entry": []
    }

    for vaccination_record in existing_vaccination_data:
        fhir_immunization = {
            "resourceType": "Immunization",
            "status": "completed",
            "occurrenceDateTime": vaccination_record["date"],
            "vaccineCode": {
                "text": f"COVID-19 Vaccine ({vaccination_record['total_vaccinations']})"
            },
            "patient": {
                "reference": f"Location/{vaccination_record['iso_code']}"
            },
            "doseQuantity": {
                "value": vaccination_record['total_vaccinations'],
                "unit": "doses"
            },
            "note": [
                {
                    "text": f"Location: {vaccination_record['location']}"
                },
                {
                    "text": f"Continent: {vaccination_record['continent']}"
                },
                {
                    "text": f"Total Cases: {vaccination_record['total_cases']}"
                },
                {
                    "text": f"Population: {vaccination_record['population']}"
                },
                {
                    "text": f"People Vaccinated: {vaccination_record['people_vaccinated']}"
                },
                {
                    "text": f"People Fully Vaccinated: {vaccination_record['people_fully_vaccinated']}"
                },
                {
                    "text": f"Total Vaccinations Per Hundred: {vaccination_record['total_vaccinations_per_hundred']}"
                },
                {
                    "text": f"People Vaccinated Per Hundred: {vaccination_record['people_vaccinated_per_hundred']}"
                },
                {
                    "text": f"People Fully Vaccinated Per Hundred: {vaccination_record['people_fully_vaccinated_per_hundred']}"
                }
                # You can add more fields or notes from your dataset here
            ]
            # Add more fields from your dataset as required by FHIR Immunization resource
        }
        # Add Immunization resource to the Bundle
        bundle["entry"].append({
            "resource": fhir_immunization,
            "request": {
                "method": "POST",  # or "PUT" if updating existing resources
                "url": "Immunization"  # The FHIR resource type
            }
        })

    yield bundle

# Reading existing vaccination data from data.json
try:
    with open('static/data.json', 'r') as file:
        existing_vaccination_data = json.load(file)
except FileNotFoundError:
    print('data.json not found')
    existing_vaccination_data = []

# Example vaccination data creation (you may replace this with your actual data)
example_vaccination_data = list(convert_to_fhir_bundle(existing_vaccination_data))

# Generate API URL
api_url = 'http://localhost:5000/api/vaccinations'  # Adjust the URL based on your server setup
print("API URL:", api_url)  # Print the generated URL to the terminal

# POST request to upload FHIR Bundle
response = requests.post(api_url, json={"entry": example_vaccination_data})

# Check the response status and process the data if needed
if response.status_code == 200:
    print("Data successfully uploaded")
else:
    print(f"Failed to upload data. Status code: {response.status_code}")

# GET request to fetch FHIR data with streaming
response = requests.get(api_url, stream=True)

# Check the response status and process the data if needed
if response.status_code == 200:
    print("FHIR Data:")
    for chunk in response.iter_content(chunk_size=1024):
        # Process each chunk as needed (e.g., display, analyze, etc.)
        print(chunk.decode('utf-8')[:100])  # Print only the first 100 characters of each chunk
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
