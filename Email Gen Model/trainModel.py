import random
from datetime import datetime, timedelta
import json
import os


class EmailGenerator:
    def __init__(self, dataset_path="email_templates.json"):
        self.dataset_path = dataset_path
        # Load existing templates or create new if file doesn't exist
        if os.path.exists(dataset_path):
            with open(dataset_path, "r") as f:
                self.email_templates = json.load(f)
            self.save_templates()

    def save_templates(self):
        """Save templates to JSON file"""
        with open(self.dataset_path, "w") as f:
            json.dump(self.email_templates, f, indent=2)

    def add_new_template_type(self):
        """Interactively add a new email template type"""
        print("\n=== Adding New Email Template Type ===")
        template_name = input(
            "Enter template name (e.g., meeting_invitation): "
        ).lower()

        if template_name in self.email_templates:
            print("Template type already exists!")
            return

        # Gather template information
        subjects = []
        print("\nEnter subject lines (empty line to finish):")
        while True:
            subject = input("Subject template (use {field} for variables): ")
            if not subject:
                break
            subjects.append(subject)

        # Get required fields
        print("\nEnter required fields (empty line to finish):")
        required_fields = []
        while True:
            field = input("Field name: ")
            if not field:
                break
            required_fields.append(field)

        # Get email body template
        print("\nEnter email body template (use {field} for variables)")
        print("Type 'END' on a new line when finished:")
        body_template = []
        while True:
            line = input()
            if line == "END":
                break
            body_template.append(line)

        # Save new template
        self.email_templates[template_name] = {
            "subjects": subjects,
            "required_fields": required_fields,
            "templates": ["\n".join(body_template)],
        }
        self.save_templates()
        print(f"\nNew template '{template_name}' added successfully!")

    def generate_email(self, template_type):
        """Generate an email based on template type with user input"""
        if template_type not in self.email_templates:
            print(f"Template type '{template_type}' not found!")
            return None

        template = self.email_templates[template_type]
        subject = random.choice(template["subjects"])
        body = random.choice(template["templates"])

        # Gather required field values
        print(f"\n=== Generating {template_type} email ===")
        print("Please provide the following information:")

        field_values = {}
        for field in template["required_fields"]:
            field_values[field] = input(f"Enter {field}: ")

        # Handle special cases
        if template_type == "sick_leave":
            field_values["date"] = datetime.now().strftime("%Y-%m-%d")
            field_values["symptom"] = random.choice(template["symptoms"])
            field_values["return_date"] = (
                datetime.now() + timedelta(days=random.randint(1, 3))
            ).strftime("%Y-%m-%d")

        # Format subject and body
        try:
            subject = subject.format(**field_values)
            body = body.format(**field_values)
        except KeyError as e:
            print(f"Error: Missing required field {e}")
            return None

        return f"Subject: {subject}\n\n{body}"

    def add_template_variation(self, template_type):
        """Add a new variation to an existing template"""
        if template_type not in self.email_templates:
            print(f"Template type '{template_type}' not found!")
            return

        print(f"\n=== Adding variation to {template_type} template ===")
        print("Enter new email body template (use {field} for variables)")
        print("Type 'END' on a new line when finished:")

        body_template = []
        while True:
            line = input()
            if line == "END":
                break
            body_template.append(line)

        self.email_templates[template_type]["templates"].append(
            "\n".join(body_template)
        )
        self.save_templates()
        print("New variation added successfully!")
