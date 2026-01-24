class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees

    def pay(self, amount):
        self.fees -= amount
        print(f"{self.name} paid {amount}. Remaining: {self.fees}")

students = {
    "Latif": Student("Latif", 500),
    "Ama": Student("Ama", 300)
}

name = input("Enter student name: ")
amount = float(input("Amount paid: "))
students[name].pay(amount)

responses = {
    "hi": "Hello! How can I assist you?",
    "hello": "Hi student!",
    "python": "Python is a powerful programming language.",
    "bye": "Goodbye!"
}

while True:
    msg = input("You: ").lower()

    if msg == "bye":
        print("Bot: Goodbye!")
        break

    print("Bot:", responses.get(msg, "I don't understand that."))




    questions = {
    "What is the capital of Ghana? ": "Accra",
    "What language is used for web styling? ": "CSS",
    "2 + 5 = ? ": "7"
}

score = 0

for q, ans in questions.items():
    user_ans = input(q)
    if user_ans.lower() == ans.lower():
        score += 1
        print("Correct!\n")
    else:
        print("Wrong!\n")

print("Final Score:", score)



def add_student():
    name = input("Enter student name: ")
    score = float(input("Enter score: "))
    with open("students.txt", "a") as f:
        f.write(f"{name},{score}\n")
    print("Student added successfully!")

def view_students():
    print("\n--- Student Records ---")
    with open("students.txt", "r") as f:
        for line in f:
            name, score = line.strip().split(",")
            print(f"Name: {name} | Score: {score}")

def grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

def grade_all():
    print("\n--- Graded Students ---")
    with open("students.txt", "r") as f:
        for line in f:
            name, score = line.strip().split(",")
            g = grade(float(score))
            print(f"{name} => {score} → Grade {g}")

while True:
    print("\n1. Add Student\n2. View Students\n3. Grade Students\n4. Exit")
    choice = input("Choose option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        grade_all()
    else:
        break

