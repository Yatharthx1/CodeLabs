student_name = input("Enter Student name: ")
student_age = int(input("Enter Student Age: "))
Mcs = int(input("Enter Marks obtained in CS: "))
Menglish = int(input("Enter Marks obtained in English: "))
Mmaths = int(input("Enter Marks obtained in Maths: "))
Status = "Passed"
if (Mcs < 33) or (Menglish < 33) or (Mmaths < 33):
    Status = "Failed"

def report_card():
    avg = (Mcs + Menglish + Mmaths) / 3
    if Status == "Passed":
        if avg > 80:
            Grade = "A"
        elif avg > 60:
            Grade = "B"
        elif avg > 40:
            Grade = "C"
        else:
            Grade = "D"
    else:
        Grade = "E"

    if Grade == "A":
        print("Message for you: Well Done! Keep up the good work")
    elif Grade == "B":
        print("Message for you: You scored well, just a little more effort and you will be there!")
    elif Grade == "C":
        print("Message for you: You scored pretty Average, a lot more hard work has to be done!")
    elif Grade == "D":
        print("Message for you: Barely passed, you need to put in serious effort.")
    elif Grade == "E":
        print("Message for you: You failed, you have to work much harder and give every little effort possible to succeed")
    print("Student Name:", student_name, ", Age:", student_age, ", Status:", Status)
    print("Average Score:", avg)
    print("Grade:", Grade)

report_card()
