# Define the PatientRecord class
class PatientRecord:
    def __init__(self, patient_id, name, age, condition):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.condition = condition

    def __str__(self):
        return f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Condition: {self.condition}"


# Binary Search Tree (BST) implementation
class TreeNode:
    def __init__(self, record):
        self.record = record
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, record):
        if not self.root:
            self.root = TreeNode(record)
        else:
            self._insert(self.root, record)

    def _insert(self, node, record):
        if record.patient_id < node.record.patient_id:
            if node.left:
                self._insert(node.left, record)
            else:
                node.left = TreeNode(record)
        else:
            if node.right:
                self._insert(node.right, record)
            else:
                node.right = TreeNode(record)

    def search(self, patient_id):
        return self._search(self.root, patient_id)

    def _search(self, node, patient_id):
        if not node:
            return None
        if node.record.patient_id == patient_id:
            return node
        if patient_id < node.record.patient_id:
            return self._search(node.left, patient_id)
        return self._search(node.right, patient_id)


# Menu-driven program
def menu():
    print("\n--- Electronic Medical Record (EMR) System ---")
    print("1. Insert Patient Record")
    print("2. Search Patient Record")
    print("3. Exit")
    print("---------------------------------------------")


# Main function
def main():
    bst = BinarySearchTree()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # Insert a new patient record
            try:
                patient_id = int(input("Enter Patient ID: "))
                name = input("Enter Patient Name: ")
                age = int(input("Enter Patient Age: "))
                condition = input("Enter Patient Condition: ")

                new_record = PatientRecord(patient_id, name, age, condition)
                bst.insert(new_record)
                print(f"Patient {name} added successfully!")
            except ValueError:
                print("Invalid input. Please enter valid data.")
        
        elif choice == "2":
            # Search for a patient record
            try:
                search_id = int(input("Enter Patient ID to search: "))
                result = bst.search(search_id)
                if result:
                    print("Patient Found:")
                    print(result.record)
                else:
                    print("Patient not found!")
            except ValueError:
                print("Invalid input. Please enter a valid ID.")

        elif choice == "3":
            # Exit the program
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()
