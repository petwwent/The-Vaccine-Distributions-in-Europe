**Overview**
This program is designed to convert existing vaccination data into FHIR (Fast Healthcare Interoperability Resources) Immunization resources. The dataset utilized for this process is substantial in size and is not stored locally; instead, the data is streamed from a specified URL. The program automatically generates the URL and prints it in the terminal.

**How It Works**
**Data Conversion:** The program reads existing vaccination data from a file (data.json) and converts it into FHIR Immunization resources using the convert_to_fhir_vaccination() function.

**Streaming Data:** To access the FHIR-formatted data, the program interacts with an API endpoint. The URL for this endpoint is automatically generated and printed in the terminal upon running the program.

**Fetching Data:** After printing the URL, the program fetches the FHIR-formatted vaccination data from the specified endpoint using the Requests library.

**Processing Data:** The fetched data can be processed as per requirements, such as analyzing, visualizing, or integrating it into other systems.

**Important Notes**
**Data Storage:** The program does not save the fetched data locally due to its large size.
**Automatic URL Generation:** The program dynamically generates the URL for accessing the FHIR-formatted data.
**Display Output:** The output is displayed in the terminal, showcasing the generated URL and allowing further processing of the fetched data.
