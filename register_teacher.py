from main import Teacher

try:
    teacher_name = input("Enter name \n")
    teacher_email = input("Enter email \n")
    teacher_subject = input("Enter subject \n")
    teacher_password = input("Enter password \n")

    Teacher.create(teacher_name=teacher_name, teacher_email=teacher_email, teacher_subject=teacher_subject, teacher_password=teacher_password)
    print("successfully creat account")
except:
    print("fail to creat account")