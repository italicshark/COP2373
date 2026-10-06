import re

# Create the phone validation function
def validate_phone(phone):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return bool(re.fullmatch(pattern, phone))

# Create the SSN validation function
def validate_ssn(ssn):
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.fullmatch(pattern, ssn))

# Create the zip code validation function
def validate_zip(zip_code):
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.fullmatch(pattern, zip_code))

# Main function validating all of the inputs
def main():
    phone = input("Enter a phone number (###-###-####): ")
    ssn = input("Enter a Social Security number (###-##-####): ")
    zip_code = input("Enter a ZIP code (##### or #####-####): ")

    if validate_phone(phone):
        print("Phone number is valid.")
    else:
        print("Phone number is invalid.")

    if validate_ssn(ssn):
        print("Social Security number is valid.")
    else:
        print("Social Security number is invalid.")

    if validate_zip(zip_code):
        print("ZIP code is valid.")
    else:
        print("ZIP code is invalid.")


if __name__ == '__main__':
    main()