import json
import os

# Define an empty list to store prescriptions
prescriptions = []

# Function to add a prescription
def add_prescription(patient_name, medication, dosage, age, disease, date, gender):
    # Create a prescription dictionary and append it to the 'prescriptions' list
    prescription = {
        "Patient Name": patient_name,
        "Medication": medication,
        "Dosage": dosage,
        "Age": age,
        "Disease": disease,
        "Date": date,
        "Gender": gender
    }
    prescriptions.append(prescription)

# Function to display all prescriptions
def display_prescriptions():
    # Check if there are any prescriptions in the list
    if len(prescriptions) == 0:
        print("No prescriptions available.")
    else:
        # Iterate through the 'prescriptions' list and display each prescription's details
        for i in prescriptions:
            print(f"Prescription {i}:")
            for key, value in i.items():
                print(f"{key}: {value}")
            print("\n")

# Function to search for prescriptions by patient name
def search_prescription(patient_name):
    found_prescriptions = []
    for prescription in prescriptions:
        # Check if the patient name matches  and add matching prescriptions to 'found_prescriptions'
        if prescription["Patient Name"].lower() == patient_name.lower():
            found_prescriptions.append(prescription)
    if found_prescriptions:
        # Display found prescriptions
        for prescription in found_prescriptions:
            print("Prescription found:")
            for key, value in prescription.items():
                print(f"{key}: {value}")
            print("\n")
    else:
        print("Prescription not found.")

# Function to remove a prescription
def remove_prescription(patient_name):
    global prescriptions # Access the global 'prescriptions' list
    updated_prescriptions = [p for p in prescriptions if p["Patient Name"].lower() != patient_name.lower()]
    # If any prescription was removed, update the 'prescriptions' list
    if len(updated_prescriptions) < len(prescriptions):
        prescriptions = updated_prescriptions
        print("Prescription removed successfully.")
    else:
        print("Prescription not found.")

# Function to analyze prescriptions by age
def analysis_by_age():
    ages = [i["Age"] for i in prescriptions] # Extract ages from prescriptions
    c1=c2=c3=c4=0
    print(ages)
    for j in ages:
        # Categorize patients into age groups and count them
        if j <= 20:
            c1 = c1 + 1
        elif j > 20 and j <= 40:
            c2 = c2 + 1
        elif j > 40 and j <= 60:
            c3 = c3 + 1
        elif j > 60:
            c4 = c4 + 1
    # Display the counts for each age group
    print("AGE:<=20     -> ", c1)
    print("AGE:21-40    -> ", c2)
    print("AGE:41-60    -> ", c3)
    print("AGE:60 above -> ", c4)

# Function to analyze prescriptions by disease type
def analysis_by_diseasetype():
    diseases = [j["Disease"] for j in prescriptions] # Extract disease names from prescriptions
    print(diseases)
    k1=k2=k3=k4=k5=0
    for k in diseases:
        # Count the occurrences of different disease types
        if k == "pneumonia":
            k1 = k1 + 1
        elif k == "arrhythmia":
            k2 = k2 + 1
        elif k == "pericarditis":
            k3 = k3 + 1
        elif k == "Atherosclerosis":
            k4 = k4 + 1
        else:
            k5 = k5 + 1
    # Display the counts for each disease type
    print("pneumonia   -> ", k1)
    print("arrhythmia    -> ", k2)
    print("pericarditis    -> ", k3)
    print("Atherosclerosis -> ", k4)
    print("other disease   -> ", k5)

# Function to load prescriptions from a JSON file
def load_prescriptions_from_file():
    global prescriptions  # Access the global 'prescriptions' list
    if os.path.exists("prescriptions.json"):
        with open("prescriptions.json", 'r') as file:
            prescriptions = json.load(file) # Load prescription data from a JSON file

# Function to save prescriptions to a JSON file
def save_prescriptions_to_file():
    with open("prescriptions.json", 'w') as file:
        json.dump(prescriptions, file,indent=4) # Save prescription data to a JSON file with indentation
        

# Main program loop
load_prescriptions_from_file() # Load existing prescriptions from file

while True:
    # Display a menu for user choices
    print("Prescription Handling System")
    print("1. Add Prescription")
    print("2. Display Prescriptions")
    print("3. Search Prescription")
    print("4. Remove Prescription")
    print("5. Analaysis of the patients with repsect to their Age")
    print("6. Analysis of the patients with respect to theie Disease Type") 
    print("7. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6/7): ")
    # Handle user's choice based on menu selection
    if choice == "1":
        # Prompt the user for prescription details and call 'add_prescription' function
        patient_name = input("Enter patient name: ")
        medication = input("Enter medication: ")
        dosage = input("Enter dosage: ")
        age = int(input("Enter the age of the patient: "))
        disease = input("Enter the disease name: ")
        date = input("Enter the date: ")
        gender = input("Enter the gender of the patient: \n")
        add_prescription(patient_name, medication, dosage, age, disease, date, gender)
        save_prescriptions_to_file() # Save the updated list of prescriptions to file
        print("Prescription added successfully.")
    elif choice == "2":
        display_prescriptions() # Call the function to display all prescriptions
    elif choice == "3":
        patient_name = input("Enter patient name to search for: ")
        search_prescription(patient_name)  # Call the function to search for prescriptions
    elif choice == "4":
        patient_name = input("Enter patient name to remove prescription: ")
        remove_prescription(patient_name) # Call the function to remove a prescription
        save_prescriptions_to_file() # Save the updated list of prescriptions to file
    elif choice == "5":
        analysis_by_age()# Call the function to analyze prescriptions by age
    elif choice == "6":
        analysis_by_diseasetype() # Call the function to analyze prescriptions by disease type
    elif choice == "7":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please choose a valid option.")


### Analysis


