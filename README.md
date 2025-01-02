# Cafe and Wifi Rating Application

## Description
This project is a web application built using the Flask framework. It allows users to add information about cafes, including their name, location, opening and closing times, and ratings for coffee, wifi, and power outlets. The application stores this data in a CSV file and displays it on a separate page.

## Features
Form Submission: Users can submit information about cafes through a form.

Data Storage: Stores the submitted cafe information in a CSV file.

Data Display: Displays the stored cafe information on a separate page.

Bootstrap Integration: Uses Flask-Bootstrap to style the application.

Form Validation: Validates form inputs using Flask-WTF and WTForms.

## How It Works
Home Page: The home page provides a link to add a new cafe and view the list of cafes.

Add Cafe: The /add route displays a form where users can enter details about a cafe. The form includes fields for the cafe name, location URL, opening and closing times, and ratings for coffee, wifi, and power outlets.

Form Validation: The form validates the inputs to ensure they are correctly formatted. If the form is valid, the data is appended to a CSV file.

View Cafes: The /cafes route reads the data from the CSV file and displays it in a table format on the webpage.
