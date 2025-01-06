from collections import deque

def manage_emr_orders():
    # Initialize the deque with a fixed size
    max_orders = int(input("Enter the maximum number of orders to retain: "))
    orders = deque(maxlen=max_orders)

    while True:
        print("\nOptions:")
        print("1. Add a new order")
        print("2. View all orders")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                # Add a new order
                order_id = input("Enter Order ID: ")
                patient_name = input("Enter Patient Name: ")
                medication = input("Enter Medication Name: ")
                order = {
                    "Order ID": order_id,
                    "Patient Name": patient_name,
                    "Medication": medication
                }
                orders.append(order)
                print("Order added successfully!\n")

            elif choice == 2:
                # View all orders
                if orders:
                    print("\nCurrent Orders in the System:")
                    for idx, order in enumerate(orders, start=1):
                        print(f"Order {idx}: {order}")
                else:
                    print("No orders available.")

            elif choice == 3:
                # Exit the system
                print("Exiting the EMR system. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the EMR order management system
if __name__ == "__main__":
    manage_emr_orders()
