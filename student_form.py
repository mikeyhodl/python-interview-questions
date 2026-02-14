"""
Student Registration Form
This program collects student details and displays them in a formatted manner.
"""

def main():
    """Main function to collect and display student information."""
    
    print("=" * 60)
    print("STUDENT REGISTRATION FORM".center(60))
    print("=" * 60)
    print()
    
    # Collecting user input
    name = input("What is your name? ")
    reg_number = input("What is your registration number? ")
    department = input("What is your department? ")
    faculty = input("What is your faculty? ")
    course = input("What is your course of study? ")
    level = input("What is your current level of study? ")
    programme = input("What is your programme of study? ")
    state = input("What is your state of residence? ")
    nationality = input("What is your nationality? ")
    
    # Displaying the collected information in a formatted form
    print("\n" + "=" * 60)
    print("STUDENT DETAILS".center(60))
    print("=" * 60)
    print(f"""
Name:                    {name}
Registration Number:     {reg_number}
Department:              {department}
Faculty:                 {faculty}
Course of Study:         {course}
Level:                   {level}
Programme of Study:      {programme}
State of Residence:      {state}
Nationality:             {nationality}
""")
    print("=" * 60)
    print("Thank you for registering!".center(60))
    print("=" * 60)


if __name__ == "__main__":
    main()
