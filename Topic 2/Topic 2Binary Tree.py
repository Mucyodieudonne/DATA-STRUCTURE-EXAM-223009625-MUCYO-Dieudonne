class PatientRecord:
    def __init__(self, patient_id, name, age, medical_history):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.medical_history = medical_history

    def __str__(self):
        return f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, History: {self.medical_history}"


class TreeNode:
    def __init__(self, key, record):
        self.key = key
        self.record = record
        self.left = None
        self.right = None


class BinaryTreeEMR:
    def __init__(self):
        self.root = None

    def insert(self, key, record):
        def _insert(node, key, record):
            if not node:
                return TreeNode(key, record)
            if key < node.key:
                node.left = _insert(node.left, key, record)
            elif key > node.key:
                node.right = _insert(node.right, key, record)
            else:
                raise ValueError("Duplicate keys are not allowed.")
            return node

        self.root = _insert(self.root, key, record)

    def search(self, key):
        def _search(node, key):
            if not node:
                return None
            if key == node.key:
                return node.record
            elif key < node.key:
                return _search(node.left, key)
            else:
                return _search(node.right, key)

        return _search(self.root, key)

    def delete(self, key):
        def _min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        def _delete(node, key):
            if not node:
                return node

            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                # Node with only one child or no child
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left

                # Node with two children
                temp = _min_value_node(node.right)
                node.key = temp.key
                node.record = temp.record
                node.right = _delete(node.right, temp.key)

            return node

        self.root = _delete(self.root, key)

    def inorder_traversal(self):
        result = []

        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.record)
                _inorder(node.right)

        _inorder(self.root)
        return result


# Example Usage
emr_system = BinaryTreeEMR()

while True:
    print("\nElectronic Medical Record System")
    print("1. Add Patient Record")
    print("2. Search Patient Record")
    print("3. Delete Patient Record")
    print("4. View All Records")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        patient_id = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        age = int(input("Enter Patient Age: "))
        medical_history = input("Enter Medical History: ")
        try:
            emr_system.insert(patient_id, PatientRecord(patient_id, name, age, medical_history))
            print("Patient record added successfully.")
        except ValueError as e:
            print(e)
    elif choice == "2":
        patient_id = int(input("Enter Patient ID to search: "))
        record = emr_system.search(patient_id)
        if record:
            print("Patient Record Found:")
            print(record)
        else:
            print("No record found with the given ID.")
    elif choice == "3":
        patient_id = int(input("Enter Patient ID to delete: "))
        emr_system.delete(patient_id)
        print("Patient record deleted successfully (if it existed).")
    elif choice == "4":
        print("All Patient Records:")
        for record in emr_system.inorder_traversal():
            print(record)
    elif choice == "5":
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")
