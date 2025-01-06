class PatientRecord:
    def __init__(self, patient_id, name, age, medical_history):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.medical_history = medical_history

    def __str__(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, History: {self.medical_history}"


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        if self.is_empty():
            print("No patient records found.")
            return
        current = self.head
        while True:
            print(current.data)
            current = current.next
            if current == self.head:
                break

    def search(self, patient_id):
        if self.is_empty():
            return None
        current = self.head
        while True:
            if current.data.patient_id == patient_id:
                return current.data
            current = current.next
            if current == self.head:
                break
        return None

    def delete(self, patient_id):
        if self.is_empty():
            print("No records to delete.")
            return

        current = self.head
        prev = None

        while True:
            if current.data.patient_id == patient_id:
                if prev is None:  # Deleting the head node
                    # Find the last node to update its next pointer
                    last = self.head
                    while last.next != self.head:
                        last = last.next
                    if current.next == self.head:  # Only one node in the list
                        self.head = None
                    else:
                        self.head = current.next
                        last.next = self.head
                else:
                    prev.next = current.next
                print(f"Record with Patient ID {patient_id} deleted.")
                return
            prev = current
            current = current.next
            if current == self.head:
                break

        print(f"Record with Patient ID {patient_id} not found.")

    def update(self, patient_id, new_data):
        record = self.search(patient_id)
        if record:
            record.name = new_data.get("name", record.name)
            record.age = new_data.get("age", record.age)
            record.medical_history = new_data.get("medical_history", record.medical_history)
            print(f"Record with Patient ID {patient_id} updated.")
        else:
            print(f"Record with Patient ID {patient_id} not found.")


# Example Usage
if __name__ == "__main__":
    emr_system = CircularLinkedList()

    # Adding patient records
    emr_system.append(PatientRecord(101, "Alice", 30, "No significant history"))
    emr_system.append(PatientRecord(102, "Bob", 40, "Diabetic"))
    emr_system.append(PatientRecord(103, "Charlie", 25, "Asthma"))

    # Display records
    print("Patient Records:")
    emr_system.display()

    # Search for a patient
    print("\nSearching for Patient ID 102:")
    patient = emr_system.search(102)
    print(patient if patient else "Patient not found.")

    # Update a patient record
    print("\nUpdating Patient ID 102:")
    emr_system.update(102, {"age": 41, "medical_history": "Diabetic, High BP"})

    # Display records after update
    print("\nPatient Records After Update:")
    emr_system.display()

    # Delete a patient record
    print("\nDeleting Patient ID 101:")
    emr_system.delete(101)

    # Display records after deletion
    print("\nPatient Records After Deletion:")
    emr_system.display()
