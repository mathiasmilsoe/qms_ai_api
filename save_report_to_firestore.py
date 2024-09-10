import firebase_admin
from firebase_admin import credentials, auth, firestore
import random
import string
import os
import json
from base_variables import product_name, model, report_format_version, top_p, temperature  # Importing product_name and model from base_variables
from datetime import datetime

# Initialize Firebase Admin SDK
cred = credentials.Certificate('/Users/mathiasmilsostephensen/Documents/qms_ai_api/lumidocs-firebase-adminsdk-u1zng-28193d06db.json')  # Update with your Firebase credentials file path
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

def generate_random_string(length=6):
    """Generate a random string of given length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def create_user():
    """Prompt for username, create a user in Firebase, and return the user details."""
    username = input("Enter username (leave blank for a random username): ").strip()
    if not username:
        username = generate_random_string()

    password = generate_random_string()
    email = f"{username}@lumidocs.web.app"

    user = auth.create_user(
        email=email,
        password=password
    )

    print(f'Successfully created new user: uuid: {user.uid}, username: {username}')
    return username, password, user.uid

def store_metadata_in_firestore(user_id):
    """Store metadata in Firestore."""
    print("Storing metadata information...")
    comments = input("Comments: ").strip()

    metadata = {
        'createdOn': datetime.now().isoformat(),
        'model': model,  
        'comments': comments,
        'product': product_name,
        'report_format_version': report_format_version,
        'top_p': top_p,
        'temperature': temperature
    }

    try:
        db.collection('metaData').document(user_id).set(metadata)
        print(f"Metadata successfully stored for user ID: {user_id}")
    except Exception as e:
        print(f"Failed to store metadata in Firestore for user ID: {user_id}. Error: {e}")

def store_report_in_firestore(user_id, reports_path):
    """Store the report JSON files in Firestore."""
    print("Storing report in Firestore...")
    reports_dir = reports_path
    report_files = [f for f in os.listdir(reports_dir) if f.endswith('.json')]
    
    for report_file in report_files:
        document_key = report_file.replace('.json', '')
        
        with open(os.path.join(reports_dir, report_file), 'r') as file:
            report_content = json.load(file)
        
        try:
            db.collection('reports').document(user_id).collection('sections').document(document_key).set(report_content)
            print(f"Successfully stored {document_key} report in Firestore under user ID: {user_id}")
        except Exception as e:
            print(f"Failed to store {document_key} report in Firestore under user ID: {user_id}. Error: {e}")

def store_report_abstracts_in_firestore(user_id):
    """Store the report abstracts JSON files in Firestore."""
    print("Storing report abstracts in Firestore...")
    individual_abstracts_path = '/Users/mathiasmilsostephensen/Documents/qms_ai_api/prompt_output/abstracts/individual_abstracts.json'
    consolidated_abstract_path = '/Users/mathiasmilsostephensen/Documents/qms_ai_api/prompt_output/abstracts/report_abstract.json'
    
    try:
        with open(individual_abstracts_path, 'r') as file:
            individual_abstracts_content = json.load(file)
        
        for category, abstract in individual_abstracts_content.items():
            db.collection('report_abstracts').document(user_id).collection('abstracts').document(category).set(abstract)
            print(f"Successfully stored abstract for {category} in Firestore")
    except FileNotFoundError:
        print(f"Individual abstracts file not found at {individual_abstracts_path}. Make sure the file exists.")
    except Exception as e:
        print(f"Failed to store individual abstracts in Firestore. Error: {e}")
    
    try:
        with open(consolidated_abstract_path, 'r') as file:
            consolidated_abstract_content = json.load(file)
        
        db.collection('report_abstracts').document(user_id).collection('abstracts').document('report_abstract').set(consolidated_abstract_content)
        print("Successfully stored consolidated abstract in Firestore")
    except FileNotFoundError:
        print(f"Consolidated abstract file not found at {consolidated_abstract_path}. Make sure the file exists.")
    except Exception as e:
        print(f"Failed to store consolidated abstract in Firestore. Error: {e}")

def save_sign_in_details(username, password, product_name, output_dir):
    """Save the sign-in details to a text file."""
    print("Saving sign-in information...")
    sign_in_info = (
        f"To sign in, please go to https://lumidocs.web.app/\n"
        f"Report ID: {username}\n"
        f"Password: {password}"
    )
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_path = os.path.join(output_dir, f"{product_name}_sign_in.txt")
    
    with open(output_path, 'w') as file:
        file.write(sign_in_info)
    
    print(f"Sign-in details saved to {output_path}")
    
    os.system(f"open {output_path}")

def main():
    # Step 1: Create user
    username, password, user_id = create_user()
    
    # Step 2: Store metadata in Firestore
    store_metadata_in_firestore(user_id)
    
    # Step 3: Store report in Firestore
    reports_path = '/Users/mathiasmilsostephensen/Documents/qms_ai_api/prompt_output'
    store_report_in_firestore(user_id, reports_path)
    
    # Step 4: Store report abstracts in Firestore
    store_report_abstracts_in_firestore(user_id)
    
    # Step 5: Save sign-in details to txt file
    output_dir = '/Users/mathiasmilsostephensen/Documents/qms_ai_api/sign_in_secrets'
    save_sign_in_details(username, password, product_name, output_dir)

if __name__ == "__main__":
    main()
