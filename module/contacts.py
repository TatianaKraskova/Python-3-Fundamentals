# Contacts dictionary
contacts = {
    'number': 4,
    'students': [
        {'name': 'Sarah Holderness', 'email': 'sarah@example.com'},
        {'name': 'Harry Potter', 'email': 'harry@example.com'},
        {'name': 'Hermione Granger', 'email': 'hermione@example.com'},
        {'name': 'Ron Weasley', 'email': 'ron@example.com'},
    ]
}

def display_emails(contacts):
    """
    Display the emails of all students in the contacts dictionary.
    """
    print("Student Emails:")
    for student in contacts['students']:
        print(f"- {student['name']}: {student['email']}")

def search_student(contacts, name):
    """
    Search for a student by name and return their contact information.
    """
    for student in contacts['students']:
        if student['name'].lower() == name.lower():
            return student
    return None

def main():
    """
    Main function to interact with the contacts program.
    """
    # Display all student emails
    display_emails(contacts)

    # Search for a student by name
    print("\nSearch for a student:")
    search_name = input("Enter the name of the student: ").strip()
    result = search_student(contacts, search_name)

    if result:
        print(f"\nFound: {result['name']} - {result['email']}")
    else:
        print(f"\nStudent '{search_name}' not found in the contacts.")

# Run the program
if __name__ == "__main__":
    main()
