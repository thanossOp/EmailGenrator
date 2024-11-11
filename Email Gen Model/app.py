import random
from datetime import datetime, timedelta
import json
import os
from trainModel import EmailGenerator

def main():
    generator = EmailGenerator()
    
    while True:
        print("\n=== Email Generator Menu ===")
        print("1. Generate email")
        print("2. Add new template type")
        print("3. Add template variation")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            print("\nAvailable templates:")
            for template in generator.email_templates.keys():
                print(f"- {template}")
            template_type = input("\nEnter template type: ")
            email = generator.generate_email(template_type)
            if email:
                print("\n=== Generated Email ===")
                print(email)
        
        elif choice == '2':
            generator.add_new_template_type()
        
        elif choice == '3':
            print("\nAvailable templates:")
            for template in generator.email_templates.keys():
                print(f"- {template}")
            template_type = input("\nEnter template type: ")
            generator.add_template_variation(template_type)
        
        elif choice == '4':
            break

if __name__ == "__main__":
    main()