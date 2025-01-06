from collections import deque

def manage_emr_data():
    # Initialize the deque with no fixed size (dynamic tracking)
    emr_data = deque()

    while True:
        print("\nOptions:")
        print("1. Add a new record")
        print("2. View all records")
        print("3. Remove the oldest record")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                # Add a new record
                record_id = input("Enter Record ID: ")
                patient_name = input("Enter Patient Name: ")
                Disease= input("Enter a Disease: ")
                medication = input("Enter Medication: ")
                record = {
                    "Record ID": record_id,
                    "Patient Name": patient_name,
                    "Disease": Disease,
                    "Medication": medication
                }
                emr_data.append(record)
                print("Record added successfully!\n")

            elif choice == 2:
                # View all records
                if emr_data:
                    print("\nCurrent Records in the System:")
                    for idx, record in enumerate(emr_data, start=1):
                        print(f"Record {idx}: {record}")
                else:
                    print("No records available.")

            elif choice == 3:
                # Remove the oldest record
                if emr_data:
                    removed_record = emr_data.popleft()
                    print(f"Oldest record removed: {removed_record}")
                else:
                    print("No records to remove.")

            elif choice == 4:
                # Exit the system
                print("Exiting the EMR system. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the EMR data management system
if __name__ == "__main__":
    manage_emr_data()
