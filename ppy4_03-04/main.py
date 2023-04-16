import smtplib
from email.mime.text import MIMEText

def read_file(path):
    st = []

    with open(path) as file:
        for index, line in enumerate(file):
            student_info = line.split(",")
            st.append({"firstName": student_info[1], "lastName": student_info[2], "email": student_info[0],
                       "points": student_info[3].split('\n')[0]})

            if len(student_info) > 4:
                st[index]['grade'] = student_info[4]
                st[index]['status'] = student_info[5]
            else:
                st[index]['grade'] = ''
                st[index]['status'] = ''

    return st


def grade_students(student_list):
    for student in student_list:
        if student['status'] not in ['GRADED', 'MAILED']:
            for grade, threshold in thresholds.items():
                if int(student['points']) >= threshold:
                    student['grade'] = grade
                    student['status'] = 'GRADED'


def add_student(student):
    students.append(student)
    grade_students(students)
    write_to_file(students, "students.txt")


def check_email(em):
    for student in students:
        if em in student.values():
            return True
    return False


def write_to_file(student_list, path):
    with open(path, "w") as file:
        for student in student_list:
            line = ''
            for index, value in enumerate(student.values()):
                line += value + (',' if index < len(student.values()) - 1 else '\n')

            file.write(line)


def print_students(students):
    for index, student in enumerate(students):
        print(f"{index}. {student['firstName']} {student['lastName']}, email: {student['email']}, "
              f"punkty: {student['points']}, ocena: {student['grade']}, status: {student['status']}")

    print("\n")


def send_mails():
    for student in students:
        body = f"Wystawiono ocenę: {student['grade']}"
        sender = "xxx"
        password = "xxx"
        msg = MIMEText(body)
        msg['Subject'] = "Nowa ocena w systemie"
        msg['From'] = "xxx"
        msg['To'] = student['email']
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, student['email'], msg.as_string())
        smtp_server.quit()

    write_to_file()


if __name__ == '__main__':
    students = read_file('students.txt')
    thresholds = {
        '2': 0,
        '3': 51,
        '3.5': 61,
        '4': 71,
        '4.5': 81,
        '5': 91
    }

    grade_students(students)

    user_input = ''

    while user_input != '0':
        user_input = input("0. Wyjście\n1. Dodaj studenta\n2. Usuń studenta\n3. Wyślij maile")

        if user_input == '1':
            first_name = input("Podaj imię: ")
            last_name = input("Podaj nazwisko: ")
            email = input("Podaj email: ")

            email_exists = check_email(email)

            while email_exists:
                print("Ten email jest już zajęty!")
                email = input("Podaj email: ")
                email_exists = check_email(email)

            points = input("Podaj liczbę punktów: ")
            add_student({"firstName": first_name, "lastName": last_name, "email": email, "points": points,
                         'grade': '', 'status': ''})
            print_students(students)

        if user_input == '2':
            print_students(students)

            to_delete = input("Podaj index studenta do usunięcia: ")
            while not to_delete.isdigit():
                to_delete = input("Podaj index studenta do usunięcia: ")

            del students[int(to_delete)]
            write_to_file(students, "students.txt")

        if user_input == '3':
            send_mails()