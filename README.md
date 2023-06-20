## Title: Building a GUI-Based Web App for Amazon Scraper in Python

## Objective of the Project:
The objective of this project is to develop a GUI-based web application in Python that allows users to input an SKU (Stock Keeping Unit) and scrape data from Amazon based on the SKU. The scraped data will then be returned in a CSV format, providing users with a convenient way to extract and analyze information from Amazon.

## Features of the Project:
The web application will include the following features:

GUI-Based Interface: The script will leverage a web framework, such as Flask, to create a user-friendly graphical interface. Users will interact with the application through their web browser.

Input Form: The application will provide a form where users can enter the SKU for which they want to scrape data. The form will validate the input and ensure that it meets the required format or criteria.

Amazon Scraper Integration: The script will integrate an existing Amazon scraper module that can extract data based on the provided SKU. It will invoke the scraper function, passing the SKU obtained from the form, and collect the scraped data.

CSV Output: The scraped data will be formatted as a CSV file. The script will generate this CSV file, including relevant information such as product details, pricing, ratings, and other desired attributes.

Result Display: The web application will display the scraped data to the user in an organized and user-friendly manner. It may use HTML templates to present the data, such as a table or other suitable format.

CSV Download: The application will provide a download link or button for users to obtain the generated CSV file. Clicking the link or button will initiate the download of the CSV file to the user's local machine.

Error Handling: The script will include appropriate error handling mechanisms to handle potential issues, such as invalid input, network errors, or failures during the scraping process. It will display informative error messages to guide users in case of any problems.

By implementing these features, the script will enable users to conveniently retrieve and export data from Amazon based on specific SKUs, making it easier to analyze and utilize the extracted information.
