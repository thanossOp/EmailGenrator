# Email Generator

This project is an **Email Generator** that allows you to create personalized email templates for various situations such as leave requests, meetings, and more. You can add new templates, modify existing ones, and generate emails by providing necessary field inputs.

## Features

- Generate emails from pre-defined templates
- Add new email templates interactively
- Add variations to existing email templates
- Save and load email templates from a JSON file
- Easy-to-use CLI interface

## Prerequisites

Make sure you have Python 3.x installed on your system.

You can download Python from [here](https://www.python.org/downloads/).

## Setup Instructions

1. **Clone the Repository**

   Clone this repository to your local machine using Git.

   ```bash
   git clone https://github.com/your-username/email-generator.git
   cd email-generator
Install Dependencies

No external dependencies are required for this project as it uses Python’s built-in libraries.

Running the Application
Navigate to the Project Folder

Open a terminal (or command prompt) and navigate to the project folder.

bash
cd email-generator
Run the Application

Run the application using the following command:

bash
python app.py
This will launch the Email Generator application and display the main menu.

How to Use
Generate Email

From the menu, select 1. Generate email.
Choose the template you want to generate from the available options.
Enter the required fields when prompted.
The generated email will be displayed in the console.
Add a New Template Type

Select 2. Add new template type from the menu.
Provide a name for the template type.
Enter subject lines, required fields, and the body template.
The new template will be saved in email_templates.json.
Add Template Variation

Select 3. Add template variation from the menu.
Choose the template to which you want to add a variation.
Enter the new body template for the variation.
The variation will be added to the selected template.
Exit

Select 4. Exit to quit the application.
File Structure
bash
email-generator/
├── app.py               # Main application script
├── trainModel.py        # Email Generator class and logic
├── email_templates.json # Stores email templates in JSON format
├── README.md            # Project documentation
Customizing the Templates
You can customize the templates and subject lines in the email_templates.json file. The format for the templates is as follows:

json
{
  "leave_for_trip": {
    "subjects": [
      "Going to {place} - Trip Notification",
      "Traveling to {place} - {start_date} to {end_date}"
    ],
    "required_fields": [
      "place",
      "start_date",
      "end_date",
      "sender_name",
      "manager_name"
    ],
    "templates": [
      "Hello {manager_name},\n\nI wanted to keep you updated on my upcoming trip to {place}.\n\n- **Trip Location**: {place}\n- **Start Date**: {start_date}\n- **End Date**: {end_date}\n\nI’ve organized my responsibilities and briefed the team to ensure there’s no disruption. If you need to reach me during this period, feel free to let me know.\n\nLooking forward to sharing more updates upon my return.\n\nBest regards,\n{sender_name}",
      "Hi {manager_name},\n\nI just wanted to let you know that I’ll be heading to {place} from {start_date} to {end_date}. I’ve taken care of ongoing tasks and coordinated with the team to make sure everything runs smoothly while I’m away.\n\nPlease don’t hesitate to reach out if you need anything in the meantime!\n\nThanks,\n{sender_name}"
    ]
  }
}
subjects: A list of subject lines with placeholders for dynamic fields.
required_fields: A list of fields that need to be provided by the user (e.g., place, start_date, end_date).
templates: A list of email body templates with placeholders for dynamic fields.
Contributing
Feel free to fork this repository and submit pull requests for new features or bug fixes. Please make sure to follow the existing code style and add tests for new features.

License
This project is licensed under the MIT License - see the LICENSE file for details.

vbnet

This `README.md` provides a detailed explanation of how to use the email generator, add new templ