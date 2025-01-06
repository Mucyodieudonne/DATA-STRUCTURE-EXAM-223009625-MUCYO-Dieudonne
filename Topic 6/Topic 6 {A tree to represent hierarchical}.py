class EMRNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, level=0):
        print("  " * level + self.name)
        for child in self.children:
            child.display(level + 1)

def create_emr_tree():
    # Root node
    emr = EMRNode("Electronic Medical Record")

    # First level nodes
    patient_demographics = EMRNode("Patient Demographics")
    medical_history = EMRNode("Medical History")
    clinical_encounters = EMRNode("Clinical Encounters")
    clinical_documents = EMRNode("Clinical Documents")
    orders_results = EMRNode("Orders & Results")
    medications = EMRNode("Medications")

    emr.add_child(patient_demographics)
    emr.add_child(medical_history)
    emr.add_child(clinical_encounters)
    emr.add_child(clinical_documents)
    emr.add_child(orders_results)
    emr.add_child(medications)

    # Patient Demographics children
    patient_demographics.add_child(EMRNode("Basic demographic"))
    patient_demographics.add_child(EMRNode("Contact details"))
    patient_demographics.add_child(EMRNode("Insurance information"))

    # Medical History children
    medical_history.add_child(EMRNode("Problem list"))
    medical_history.add_child(EMRNode("Surgical history"))
    medical_history.add_child(EMRNode("Family health history"))
    medical_history.add_child(EMRNode("Social history"))
    medical_history.add_child(EMRNode("Allergies"))

    # Clinical Encounters children
    clinical_encounters.add_child(EMRNode("Office visits"))
    clinical_encounters.add_child(EMRNode("Hospital stays"))
    clinical_encounters.add_child(EMRNode("Emergency Visits"))

    # Clinical Documents children
    clinical_notes = EMRNode("Clinical notes")
    clinical_notes.add_child(EMRNode("Progress notes"))
    clinical_notes.add_child(EMRNode("History & Physical examinations"))
    clinical_notes.add_child(EMRNode("Discharge summaries"))

    clinical_documents.add_child(clinical_notes)
    clinical_documents.add_child(EMRNode("Diagnostic reports"))
    clinical_documents.add_child(EMRNode("Imaging studies"))
    clinical_documents.add_child(EMRNode("Consultation notes"))

    # Orders & Results children
    test_results = EMRNode("Test Results")
    test_results.add_child(EMRNode("Pending Tests"))

    orders_results.add_child(test_results)
    orders_results.add_child(EMRNode("Laboratory tests (pending and completed)"))
    orders_results.add_child(EMRNode("Imaging orders"))
    orders_results.add_child(EMRNode("Procedure orders"))

    # Medications children
    medications.add_child(EMRNode("Active medications"))
    medications.add_child(EMRNode("Prescription history"))

    return emr

if __name__ == "__main__":
    emr_tree = create_emr_tree()
    print("Electronic Medical Record Hierarchical Structure:")
    emr_tree.display()
