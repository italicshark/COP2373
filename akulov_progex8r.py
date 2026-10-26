import csv

def read_grades():
    with open("grades.csv", "r", newline="") as file:
        reader = csv.reader(file)

        # Print the table headers
        print(f"{'First Name':<15}{'Last Name':<15}{'Exam 1':<10}{'Exam 2':<10}{'Exam 3':<10}")
        print("-" * 60)

        # Skip the header row from the CSV file
        next(reader)

        # Display each student's grades
        for row in reader:
            print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<10}{row[4]:<10}")


def main():
    read_grades()


main()
