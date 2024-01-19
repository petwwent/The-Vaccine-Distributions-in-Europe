from flask import Flask, request, send_file, jsonify
from fhir.resources.bundle import Bundle, BundleEntry
from fhir.resources.immunization import Immunization
from apiflask import APIFlask
import json

app = APIFlask(__name__, spec_path='/openapi.yaml')
app.config['SPEC_FORMAT'] = 'yaml'

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

    return bundle
# Route for serving index.html
@app.route('/')
def index():
    return send_file('templates/index.html')

# Route for serving script.js
@app.route('/script.js')
def get_script():
    return send_file('static/script.js')

# Route for serving styles.css
@app.route('/styles.css')
def get_styles():
    return send_file('static/styles.css')

# Route for serving data.json
@app.route('/data.json')
def get_data():
    return send_file('static/data.json')

# Route for serving flags from the root directory
@app.route('/flags/<filename>')
def get_flag(filename):
    return send_file(f'flags/{filename}')


@app.route('/api/vaccinations', methods=['POST'])
def post_vaccination_data():
    try:
        with open('static/data.json', 'r') as file:
            existing_vaccination_data = json.load(file)
    except FileNotFoundError:
        return jsonify({'error': 'data.json not found'}), 404

    fhir_bundle = convert_to_fhir_bundle(existing_vaccination_data)

    return jsonify(fhir_bundle), 200


@app.route('/api/vaccinations', methods=['GET'])
def get_vaccination_data():
    try:
        with open('static/data.json', 'r') as file:
            existing_vaccination_data = json.load(file)
    except FileNotFoundError:
        return jsonify({'error': 'data.json not found'}), 404

    fhir_vaccination_data = convert_to_fhir_bundle(existing_vaccination_data)

    return jsonify(fhir_vaccination_data), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
