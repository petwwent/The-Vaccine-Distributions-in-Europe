import requests
import json

# Function to convert existing vaccination data to FHIR Immunization resource
def convert_to_fhir_vaccination(existing_vaccination_data):
    fhir_data = []

    for vaccination_record in existing_vaccination_data:
        fhir_immunization = {
            "resourceType": "Immunization",
            "status": "completed",
            "occurrenceDateTime": vaccination_record.get("date", ""),
            "vaccineCode": {
                "text": f"COVID-19 Vaccine ({vaccination_record.get('total_vaccinations', 0)})"
            },
            "patient": {
                "reference": f"Location/{vaccination_record.get('iso_code', '')}"
            },
            "doseQuantity": {
                "value": vaccination_record.get('total_vaccinations', 0),
                "unit": "doses"
            },
            "note": [
                {"text": f"Location: {vaccination_record.get('location', '')}"},
                {"text": f"Continent: {vaccination_record.get('continent', '')}"},
                {"text": f"Total Cases: {vaccination_record.get('total_cases', 0)}"},
                {"text": f"Population: {vaccination_record.get('population', 0)}"},
                {"text": f"People Vaccinated: {vaccination_record.get('people_vaccinated', 0)}"},
                {"text": f"People Fully Vaccinated: {vaccination_record.get('people_fully_vaccinated', 0)}"},
                {"text": f"Total Vaccinations Per Hundred: {vaccination_record.get('total_vaccinations_per_hundred', 0)}"},
                {"text": f"People Vaccinated Per Hundred: {vaccination_record.get('people_vaccinated_per_hundred', 0)}"},
                {"text": f"People Fully Vaccinated Per Hundred: {vaccination_record.get('people_fully_vaccinated_per_hundred', 0)}"}
                # You can add more fields or notes from your dataset here
            ]
            # Add more fields from your dataset as required by FHIR Immunization resource
        }
        fhir_data.append(json.dumps(fhir_immunization) + '\n')
    
    return fhir_data

# Load existing vaccination data from data.json
try:
    with open('data.json', 'r') as file:
        existing_vaccination_data = json.load(file)
except FileNotFoundError:
    print('data.json not found')
    existing_vaccination_data = []

# Generate API URL
api_url = 'http://localhost:5000/api/vaccinations'
print("API URL:", api_url)  # Print the generated URL to the terminal

# Example GET request
response_get = requests.get(api_url)

if response_get.status_code == 200:
    # Handle the streamed data from the GET request
    streamed_data_get = response_get.iter_lines()
    for line in streamed_data_get:
        pass  # Do not print or process the data in the terminal
else:
    print(f"Failed to fetch data. Status code: {response_get.status_code}")

# Example POST request with all data
fhir_data_to_post = convert_to_fhir_vaccination(existing_vaccination_data)

response_post = requests.post(api_url, json=fhir_data_to_post)

if response_post.status_code == 200:
    # Handle the streamed data from the POST request
    streamed_data_post = response_post.iter_lines()
    for line in streamed_data_post:
        pass  # Do not print or process the data in the terminal
else:
    print(f"Failed to post data. Status code: {response_post.status_code}")
