import requests
import json

url = 'http://localhost:5000/api/vaccinations'  # Replace with your Flask app's URL

fhir_immunization_data = [
    {
        "resourceType": "Immunization",
        "id": "ce655d9a-5986-40cb-93e3-728856fb3d61",
        "status": "completed",
        "vaccineCode": {"coding": [{"system": "http://snomed.info/sct", "code": "1119349007"}]},
        "patient": {"reference": "Patient/ALB"},
        "occurrenceDateTime": "2021-01-13",
        "doseQuantity": {"value": 188.0, "unit": "doses"},
        "performer": [
            {
                "function": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v2-0443", "code": "AP"}]},
                "actor": {"reference": "Organization/example"}
            }
        ]
    },
    {
        "resourceType": "Immunization",
        "id": "f61e26b8-177a-4aad-89d6-05fba2af6a55",
        "status": "completed",
        "vaccineCode": {"coding": [{"system": "http://snomed.info/sct", "code": "1119349007"}]},
        "patient": {"reference": "Patient/ALB"},
        "occurrenceDateTime": "2021-01-14",
        "doseQuantity": {"value": 266.0, "unit": "doses"},
        "performer": [
            {
                "function": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v2-0443", "code": "AP"}]},
                "actor": {"reference": "Organization/example"}
            }
        ]
    }
    # Add more Immunization entries as needed
]

# Send a POST request to the Flask app
response = requests.post(url, json=fhir_immunization_data)

# Print the response
print(response.status_code)
print(response.json())
