def calculate_emi(principal, annual_rate, tenure_years):
    monthly_rate = annual_rate / (12 * 100)  # Monthly interest rate
    tenure_months = tenure_years * 12  # Loan tenure in months

    emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / ((1 + monthly_rate) ** tenure_months - 1)
    return round(emi, 2)

def main():
    try:
        principal = float(input("Enter the principal loan amount (₹): "))
        annual_rate = float(input("Enter the annual interest rate (%): "))
        tenure_years = int(input("Enter the loan tenure (years): "))

        emi = calculate_emi(principal, annual_rate, tenure_years)
        print(f"Your EMI is: ₹{emi}")
    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()
