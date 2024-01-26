from fhir.resources.bundle import Bundle, BundleEntry
from fhir.resources.immunization import Immunization
from flask import Flask, request, jsonify, redirect, url_for
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
import json
from flask import send_file
from uuid import uuid4

app = Flask(__name__)
app.config['SPEC_FORMAT'] = 'yaml'
app.config['OPENAPI_VERSION'] = '3.0.2'
app.config['OPENAPI_URL_PREFIX'] = '/docs'

spec = APISpec(
    title="Your API",
    version="1.0.0",
    openapi_version=app.config['OPENAPI_VERSION'],
    plugins=[MarshmallowPlugin()],
)

# Existing data (if any)
existing_data = []

@app.route('/api/vaccinations', methods=['POST'])
def receive_fhir_bundles():
    try:
        fhir_bundles = request.json  # Assuming the FHIR Bundles are sent as JSON

        # Extract and convert FHIR Bundles to JSON
        extracted_data = extract_and_convert(fhir_bundles)

        # Check for duplicates and mismatch before storing
        check_for_duplicates(extracted_data)
        check_for_mismatch(extracted_data)

        # Store the extracted data in static/data.json
        save_to_data_json(extracted_data)

        return redirect(url_for('success'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Change the endpoint name for the /api/get_data route
@app.route('/api/get_data', methods=['GET'], endpoint='get_data_endpoint')
def get_data():
    try:
        return jsonify(existing_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/success')
def success():
    return jsonify({"message": "FHIR Bundles received and processed successfully"}), 200

def extract_and_convert(fhir_bundles):
    extracted_data = []

    for fhir_bundle in fhir_bundles:
        entries = fhir_bundle.get("entry", [])

        for entry in entries:
            if "resource" in entry:
                immunization_resource = entry["resource"]
                extracted_entry = {
                    "iso_code": immunization_resource["extension"][0]["valueString"],
                    "date": immunization_resource["occurrenceDateTime"],
                    "continent": immunization_resource["extension"][1]["valueString"],
                    "location": immunization_resource["extension"][2]["valueString"],
                    "total_cases": immunization_resource["extension"][3]["valueDecimal"],
                    "population": immunization_resource["extension"][4]["valueInteger"],
                    "total_vaccinations": immunization_resource["extension"][5]["valueInteger"],
                    "people_vaccinated": immunization_resource["extension"][6]["valueInteger"]
                }
                extracted_data.append(extracted_entry)

    return extracted_data

def check_for_duplicates(new_entries):
    for new_entry in new_entries:
        if new_entry in existing_data:
            raise ValueError("Duplicate entry detected. Entry already exists in the data.")

def check_for_mismatch(entries):
    # Assuming all entries should have the same fields, you can customize this check based on your requirements
    fields = set(entries[0].keys())

    for entry in entries:
        if set(entry.keys()) != fields:
            raise ValueError("Field mismatch detected. Fields in the entry do not match the expected structure.")

def save_to_data_json(data):
    existing_data.extend(data)
    with open('static/data.json', 'w') as data_file:
        json.dump(existing_data, data_file, indent=2)
# Route for serving index.html
@app.route('/')
def index():
    return send_file('templates/index.html')

# Route for serving script.js
@app.route('/script.js')
def get_script():
    return send_file('static/script.js')

# Route for serving dough.js
@app.route('/dough.js')
def get_dough_script():
    return send_file('static/dough.js')


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
