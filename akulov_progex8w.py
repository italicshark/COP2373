import csv

def write_grades():
    num_students = int(input("How many students? "))

    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Write the column headers
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Enter information for each student
        for i in range(num_students):
            print(f"\nStudent {i + 1}")

            first_name = input("First name: ")
            last_name = input("Last name: ")
            exam1 = int(input("Exam 1 grade: "))
            exam2 = int(input("Exam 2 grade: "))
            exam3 = int(input("Exam 3 grade: "))

            # Write the student's information
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print("\nGrades saved to grades.csv")


def main():
    write_grades()


main()
