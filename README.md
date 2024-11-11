# Email Generator

This project provides an interactive tool to generate customized emails based on templates. The user can add new templates, variations, and generate emails with placeholders that can be replaced by user input.

## Features
- **Add new email templates**: Create custom email templates with subject lines, body content, and required fields.
- **Generate emails**: Based on the available templates, generate emails with the required information.
- **Add variations to templates**: Add new variations to existing email templates.
- **Template with placeholders**: Use placeholders (variables) within the template to dynamically replace with user input.
- **Save and load templates**: Templates are saved in a JSON file, which can be loaded when the program starts.

## Usage

### Running the Application

1. Clone this repository to your local machine.
2. Make sure Python 3.x is installed on your system.
3. Install the necessary dependencies using:
   ```bash
   pip install -r requirements.txt
Run the application using:
bash
python app.py
Main Menu Options
The application presents the following menu options:

Generate email: Choose an email template and provide the required information to generate an email.
Add new template type: Add a new template to the system.
Add template variation: Add a new variation (body) to an existing template.
Exit: Exit the application.
Example: Using Template Variables
When creating templates, you can use placeholders (variables) inside both the subject and body of the email. Placeholders are defined using curly braces {}, for example, {place}, {start_date}, {manager_name}.

Example template:

Subject: "Going to {place} - Trip Notification"
Body:
css
Hello {manager_name},

I wanted to keep you updated on my upcoming trip to {place}.
- Trip Location: {place}
- Start Date: {start_date}
- End Date: {end_date}

Best regards,
{sender_name}
Required Fields
Each template can define a list of required fields. These fields are placeholders in the template that need to be filled by the user when generating an email. For the example above, the required fields would be:

place
start_date
end_date
sender_name
manager_name
Template Example
Adding a Template:
Template Name: leave_for_trip
Subject Line(s):
"Going to {place} - Trip Notification"
"Traveling to {place} - {start_date} to {end_date}"
"Upcoming Trip to {place} - {start_date} to {end_date}"
Body:
vbnet
Hello {manager_name},

I wanted to keep you updated on my upcoming trip to {place}.
- **Trip Location**: {place}
- **Start Date**: {start_date}
- **End Date**: {end_date}

Looking forward to sharing more updates upon my return.

Best regards,
{sender_name}
Generating an Email:
When generating the email using the leave_for_trip template, the user will be prompted to provide values for the required fields like place, start_date, end_date, sender_name, and manager_name.

For example:

place = Ayodhya
start_date = 27/12/2024
end_date = 04/01/2025
sender_name = Nisarg
manager_name = Yash
This would generate an email like:

Subject: "Traveling to Ayodhya - 27/12/2024 to 04/01/2025"

Body:

vbnet
Hello Yash,

I wanted to keep you updated on my upcoming trip to Ayodhya.
- **Trip Location**: Ayodhya
- **Start Date**: 27/12/2024
- **End Date**: 04/01/2025

Looking forward to sharing more updates upon my return.

Best regards,
Nisarg
Template Types
Some example template types included in the project:

sick_leave
performance_review
vacation_leave
meeting_invitation
resignation_letter
work_from_home
wedding_leave
leave_for_trip (new template added in this example)
Adding New Templates
To add a new template type, the program prompts you for the following details:

Template name: A unique identifier for the template.
Subject lines: Multiple subject options for the email.
Required fields: Variables used in the email (e.g., {place}, {manager_name}).
Email body template: The body of the email where placeholders can be used.
After entering all the information, the new template is saved in a JSON file and can be used for generating emails.

Adding Variations to Templates
You can add variations (alternate body templates) to existing templates. The process is similar to adding a new template, but only the body is modified.

File Structure
bash
.
├── app.py               # Main application file
├── trainModel.py        # Email Generator Logic
├── email_templates.json # Stores email templates in JSON format
├── requirements.txt     # List of dependencies
└── README.md            # This file
License
This project is open-source and available under the MIT License.

perl


This `README.md` file provides an overview of your email generation system, instructions for use, and examples for template creation, including how to use variables for dynamic email generation.
