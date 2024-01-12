import requests
import json
from fhir.resources.bundle import Bundle, BundleEntry
from fhir.resources.immunization import Immunization

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

# Splitting example_vaccination_data into batches of 100 records each
batch_size = 100
batches = [example_vaccination_data[i:i + batch_size] for i in range(0, len(example_vaccination_data), batch_size)]

def generate_api_url(host='localhost', port=5000):
    return f'http://{host}:{port}/api/vaccinations'

# Generate API URL
api_url = generate_api_url()  # Generate the URL
print("API URL:", api_url)  # Print the generated URL to the terminal

# Stream the data from the API endpoint
response = requests.get(api_url)

# Check the response status and process the data if needed
if response.status_code == 200:
    streamed_data = response.json()
    # Process the streamed data as required (or skip processing if not needed)
else:
    print("Failed to fetch data")

