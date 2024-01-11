**Overview**
This is designed to convert existing vaccination data into FHIR (Fast Healthcare Interoperability Resources) Immunization resources. The dataset utilized for this process is large in size and is not stored locally; instead, the data is streamed from a specified URL. The program automatically generates the URL and prints it in the terminal.

![Screenshot 2024-01-11 225825](https://github.com/PrincepaulIzuogu/The-Vaccine-Distributions-in-Europe/assets/123191250/8112b5d0-aa8b-4e91-9d83-ba26c19fc758)

![Screenshot 2024-01-11 225854](https://github.com/PrincepaulIzuogu/The-Vaccine-Distributions-in-Europe/assets/123191250/76e54da5-a13d-4b3c-bd87-9670be176947)


**How It Works**
**Data Conversion:** The program reads existing vaccination data from a file (data.json) and converts it into FHIR Immunization resources using the convert_to_fhir_vaccination() function.

**Streaming Data:** To access the FHIR-formatted data, the program interacts with an API endpoint. The URL for this endpoint is automatically generated and printed in the terminal upon running the program.

**Fetching Data:** After printing the URL, the program fetches the FHIR-formatted vaccination data from the specified endpoint using the Requests library.

**Processing Data:** The fetched data can be processed as per requirements, such as analyzing, visualizing, or integrating it into other systems.

**Important Notes**
**Data Storage:** The program does not save the fetched data locally due to its large size.
**Automatic URL Generation:** The program dynamically generates the URL for accessing the FHIR-formatted data.
**Display Output:** The output is displayed in the terminal, showcasing the generated URL and allowing further processing of the fetched data.
