
loan_data = [
    [101, 'Alice', 5000, 5, 2],
    [102, 'Bob', 10000, 4.5, 5],
    [103, 'Charlie', 3000, 6, 1],
    [104, 'Diana', 8000, 3.5, 4],
    [105, 'Ethan', 4500, 5.2, 3]
]


def calculate_total_loan(data):
    # Initialize total
    total = 0.0

    # Loop through each row of the array
    for row in data:
        # Extract the loan amount (3rd element, index 2)
        loan_amount = float(row[2])
        # Add to running total
        total += loan_amount

    # Return the final total as float with one decimal place
    return round(total, 1)


def find_least_tenure(data):
    # Compare the 5th element of each row
    min_tenure_row = min(data, key=lambda row: row[4])

    # Return the row with the smallest tenure
    return tuple(min_tenure_row)


if __name__ == "__main__":
    print("Loan Management System")
    print("=" * 50)

    print("\nSample Data:")
    print("Customer ID | Name    | Loan Amount | Interest Rate | Tenure (Years)")
    print("-" * 70)
    for row in loan_data:
        print(f"{row[0]:<11} | {row[1]:<7} | {row[2]:<11} | {row[3]:<13} | {row[4]}")

    print(f"\nTask 1 - Total Loan Amount: Rs.{calculate_total_loan(loan_data)}")

    customer_with_least_tenure = find_least_tenure(loan_data)
    print(f"\nTask 2 - Customer with Shortest Tenure:")
    print(f"Name: {customer_with_least_tenure[1]}")
    print(f"Loan Amount: Rs.{customer_with_least_tenure[2]}")
    print(f"Interest Rate: {customer_with_least_tenure[3]}%")
    print(f"Tenure: {customer_with_least_tenure[4]} years")
