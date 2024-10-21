##Create functions to validate phone numbers, social security numbers and zip codes using regular expressions.
##Create a main function to get input from a user and then displaying if the phone number, social security number
##and zip code they entered is valid.
##Be sure to test the functions with various inputs, including valid and invalid examples, to ensure the correctness
##of the regular expressions.

import re

def validate_phone(phone):
    #function to validate phone numbers
    #phone number formats: (123) 456-7890, 123-456-7890, 123.456.7890, 1234567890

    pattern = re.compile(r'^(\+?\d{1,2}[\s-]?)?(\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4}$')
    return bool(pattern.match(phone))

def validate_social(social):
   #function to validate social security numbers
   #ssn formats: 123-45-6789

    pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')
    return bool(pattern.match(social))

def validate_zip(zip):
   #function to validate zip codes
   #zip code formats: 12345, 12345-6789

    pattern = re.compile(r'^\d{5}(-\d{4})?$')
    return bool(pattern.match(zip))

def main():
    #get the input from user
    phone = input("Enter desired phone number: ")
    social = input("Enter desired social security number: ")
    zip = input("Enter desired ZIP code: ")

    #display if the users input is valid or invalid
    if validate_phone(phone):
        print("Phone number is valid.")
    else:
        print("Phone number is invalid.")

    if validate_social(social):
        print("Social security number is valid.")
    else:
        print("Social security number is invalid.")

    if validate_zip(zip):
        print("ZIP code is valid.")
    else:
        print("ZIP code is invalid.")

if __name__ == "__main__":
    main()