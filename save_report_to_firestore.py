import firebase_admin
from firebase_admin import credentials, auth, firestore
import random
import string
import os
import json
from base_variables import product_name

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
    """Create a user in Firebase and return the user details."""
    print("creating user")
    username = generate_random_string()
    password = generate_random_string()
    email = f"{username}@lumidocs.web.app"
    
    user = auth.create_user(
        email=email,
        password=password
    )
    
    print(f'Successfully created new user: uuid: {user.uid}, username: {username}')
    return username, password, user.uid

def store_report_in_firestore(user_id, reports_path):
    """Store the report JSON files in Firestore."""
    print("storing report in firestore")
    reports_dir = reports_path
    report_files = [f for f in os.listdir(reports_dir) if f.endswith('_consolidated.json')]
    
    for report_file in report_files:
        # Extract the document key from the file name
        document_key = report_file.replace('_consolidated.json', '')
        
        # Load the JSON content
        with open(os.path.join(reports_dir, report_file), 'r') as file:
            report_content = json.load(file)
        
        try:
            # Store each report as a document in Firestore
            db.collection('reports').document(user_id).collection('sections').document(document_key).set(report_content)
            print(f"Successfully stored {document_key} report in Firestore under user ID: {user_id}")
        except Exception as e:
            print(f"Failed to store {document_key} report in Firestore under user ID: {user_id}. Error: {e}")
            
def save_sign_in_details(username, password, product_name, output_dir):
    """Save the sign-in details to a text file."""
    print("saving sign in information")
    sign_in_info = (
        f"To sign in, please go to https://lumidocs.web.app/{username}\n"
        f"Email: {username}@lumidocs.web.app\n"
        f"Password: {password}"
    )
    
    # Check if the directory exists, if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Define the path for saving the sign-in file
    output_path = os.path.join(output_dir, f"{product_name}_sign_in.txt")
    
    # Write sign-in details to the text file
    with open(output_path, 'w') as file:
        file.write(sign_in_info)
    
    print(f"Sign-in details saved to {output_path}")

def main():
    # Step 1: Create user
    username, password, user_id = create_user()
    
    # Step 2: Store report in Firestore
    reports_path = '/Users/mathiasmilsostephensen/Documents/qms_ai_api/prompt_output/consolidated'
    store_report_in_firestore(user_id, reports_path)
    
    # Step 3: Save sign-in details to txt file
    product_name = f"ParagitPX" #type:ignore # Replace with actual product name
    output_dir = '/Users/mathiasmilsostephensen/Documents/qms_ai_api/sign_in_secrets'
    save_sign_in_details(username, password, product_name, output_dir)

if __name__ == "__main__":
    main()