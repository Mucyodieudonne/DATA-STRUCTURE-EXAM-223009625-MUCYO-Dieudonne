from typing import List, Dict
from dataclasses import dataclass
from datetime import datetime

@dataclass
class EMRRecord:
    patient_id: str
    record_type: str
    timestamp: datetime
    priority_level: int
    department: str
    content: Dict

def get_priority(record: EMRRecord, position: int) -> int:
    priority_factors = [
        record.priority_level,
        ["EMERGENCY", "URGENT", "ROUTINE", "FOLLOWUP", "ARCHIVED"].index(record.record_type),
        int(record.timestamp.timestamp())
    ]
    combined_priority = sum(factor * (10 ** i) for i, factor in enumerate(priority_factors))
    return (combined_priority // (10 ** position)) % 10

def radix_sort_emr(records: List[EMRRecord]) -> List[EMRRecord]:
    if not records:
        return records

    max_digits = 10
    for position in range(max_digits):
        buckets: List[List[EMRRecord]] = [[] for _ in range(10)]
        for record in records:
            digit = get_priority(record, position)
            buckets[digit].append(record)
        records = [record for bucket in buckets for record in bucket]
    return records

def get_valid_input(prompt: str, valid_options: List[str] = None) -> str:
    while True:
        user_input = input(prompt).strip().upper()
        if valid_options is None or user_input in valid_options:
            return user_input
        print(f"Invalid input. Please choose from: {', '.join(valid_options)}")

def get_valid_int(prompt: str, min_val: int, max_val: int) -> int:
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Please enter a valid number")

def input_emr_record() -> EMRRecord:
    print("\n=== Enter EMR Record Details ===")
    
    # Get patient ID
    patient_id = get_valid_input("Enter Patient ID: ")
    
    # Get record type
    record_types = ["EMERGENCY", "URGENT", "ROUTINE", "FOLLOWUP", "ARCHIVED"]
    print("\nAvailable Record Types:")
    for i, rtype in enumerate(record_types, 1):
        print(f"{i}. {rtype}")
    record_type = record_types[get_valid_int("Select Record Type (1-5): ", 1, 5) - 1]
    
    # Get priority level
    priority_level = get_valid_int("Enter Priority Level (1-5, 1 being highest): ", 1, 5)
    
    # Get department
    departments = ["ER", "INTERNAL MEDICINE", "CARDIOLOGY", "PEDIATRICS", "ORTHOPEDICS", "OTHER"]
    print("\nAvailable Departments:")
    for i, dept in enumerate(departments, 1):
        print(f"{i}. {dept}")
    department = departments[get_valid_int("Select Department (1-6): ", 1, 6) - 1]
    
    # Get diagnosis/content
    diagnosis = get_valid_input("Enter Primary Diagnosis: ")
    content = {"diagnosis": diagnosis}
    
    return EMRRecord(
        patient_id=patient_id,
        record_type=record_type,
        timestamp=datetime.now(),
        priority_level=priority_level,
        department=department,
        content=content
    )

def print_sorted_records(records: List[EMRRecord]) -> None:
    print("\nSorted EMR Records by Priority:")
    print("-" * 80)
    for record in records:
        print(f"Patient ID: {record.patient_id}")
        print(f"Type: {record.record_type}")
        print(f"Priority: {record.priority_level}")
        print(f"Department: {record.department}")
        print(f"Timestamp: {record.timestamp}")
        print(f"Diagnosis: {record.content['diagnosis']}")
        print("-" * 80)

def main():
    records = []
    while True:
        print("\n=== EMR Record Management System ===")
        print("1. Add new EMR record")
        print("2. View sorted records")
        print("3. Exit")
        
        choice = get_valid_int("Enter your choice (1-3): ", 1, 3)
        
        if choice == 1:
            record = input_emr_record()
            records.append(record)
            print("\nRecord added successfully!")
            
        elif choice == 2:
            if not records:
                print("\nNo records to display.")
                continue
            sorted_records = radix_sort_emr(records)
            print_sorted_records(sorted_records)
            
        else:
            print("\nThank you for using the EMR Record Management System!")
            break

if __name__ == "__main__":
    main()