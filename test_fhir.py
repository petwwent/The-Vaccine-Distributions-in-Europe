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
        fhir_data.append(fhir_immunization)

    return fhir_data

# Generate API URL
api_url = 'http://localhost:5000/api/vaccinations'
print("API URL:", api_url)  # Print the generated URL to the terminal

# Example GET request
response_get = requests.get(api_url)

if response_get.status_code == 200:
    # Handle the streamed data from the GET request
    streamed_data_get = response_get.iter_lines()
    for line in streamed_data_get:
        fhir_data = json.loads(line)
        # Process the FHIR-formatted data as needed
        print(fhir_data)
else:
    print(f"Failed to fetch data. Status code: {response_get.status_code}")

# Example POST request
existing_data = []  # Replace this with your actual data
post_data = convert_to_fhir_vaccination(existing_data)

response_post = requests.post(api_url, json=post_data)

if response_post.status_code == 200:
    # Handle the streamed data from the POST request
    streamed_data_post = response_post.iter_lines()
    for line in streamed_data_post:
        fhir_data = json.loads(line)
        # Process the FHIR-formatted data as needed
        print(fhir_data)
else:
    print(f"Failed to post data. Status code: {response_post.status_code}")
