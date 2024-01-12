### App interoperability:
   **Conversion of my Data.json to FHIR Bundle of Immunization structure for my App**

**Overview**
This is designed to convert existing vaccination data into FHIR Bundles of FHIR (Fast Healthcare Interoperability Resources) Immunization resources. The dataset utilized for this process is large in size and is not stored locally; instead, the data is streamed from a specified URL. The program automatically generates the URL and prints it in the terminal.


**my Terminal**

![Screenshot 2024-01-12 155334](https://github.com/PrincepaulIzuogu/The-Vaccine-Distributions-in-Europe/assets/123191250/de797876-4ebb-40b3-9c39-4ac7275a1642)


**my FHIR Bundle immunization data from the url**

![Screenshot 2024-01-12 155353](https://github.com/PrincepaulIzuogu/The-Vaccine-Distributions-in-Europe/assets/123191250/ac0cfc0b-d39f-42b5-a34e-b25bb9192552)


![Screenshot 2024-01-11 225854](https://github.com/PrincepaulIzuogu/The-Vaccine-Distributions-in-Europe/assets/123191250/76e54da5-a13d-4b3c-bd87-9670be176947)


**How It Works**
**Data Conversion:** The program reads existing vaccination data from a file (data.json) and converts it into FHIR Bundles of FHIR Immunization resources using the convert_to_fhir_vaccination() function.

**Streaming Data:** To access the FHIR-formatted data, the program interacts with an API endpoint. The URL for this endpoint is automatically generated and printed in the terminal upon running the program.

**Fetching Data:** After printing the URL, the first and last 5 entries of the data is also printed on the terminal together with the url but the full data can be accessed in the url, the program fetches the FHIR-formatted vaccination data from the specified endpoint using the Requests library.

**Processing Data:** The fetched data can be processed as per requirements, such as analyzing, visualizing, or integrating it into other systems.

**Important Notes**
**Data Storage:** The program does not save the fetched data locally due to its large size.
**Automatic URL Generation:** The program dynamically generates the URL for accessing the FHIR-formatted data.
**Display Output:** The output is displayed in the terminal, showcasing the generated URL and allowing further processing of the fetched data.
