import sys
import json
import os
import datetime

if not os.path.exists("accounts.json"):
    with open("accounts.json", "w") as file:
        json.dump([], file)

info = []
file = open("accounts.json", 'r')
info = json.load(file)
file.close()


class Task:

    def __init__(self, title, description, due_date, status, task_type):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
        self.task_type = task_type


class Task_manager(Task):

    def __init__(self, title, description, due_date, status, task_type):
        super().__init__(title, description, due_date, status, task_type)

    def validate_date(self, date_str):
        try:
            due_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            if due_date < datetime.datetime.now():
                print("Due date cannot be in the past.")
                return None
            return True
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return None

    def Add_Task(self, task_type):
        self.title = input("Enter Task Title: ")
        self.description = input("Enter Task description: ")

        while True:
            self.due_date = input("Enter Task due date, use format YYYY-MM-DD.: ")
            date_validation = self.validate_date(self.due_date)
            if date_validation:
                break
            else:
                continue

        while True:
            status = input("\nChoose status: \n(1) Incomplete \n(2) Completed \n(3) In progress \n\nYour choice: ")

            if status == "1":
                self.status = "Incomplete"
                break
            elif status == "2":
                self.status = "Completed"
                break
            elif status == "3":
                self.status = "Incomplete"
                break
            else:
                print("Invalid choice. Try again.")
                continue

        new_task = []

        if task_type == "Work Tasks":
            while True:
                importance = input("\nChoose priority:\n"
                                   "(1) Important\n"
                                   "(2) Moderate importance\n"
                                   "(3) Not important\n"
                                   "Choice: ")

                if importance == "1":
                    importance = "Important"
                    break
                elif importance == "2":
                    importance = "Moderate importance"
                    break
                elif importance == "3":
                    importance = "Not important"
                    break
                else:
                    print("Invalid Importance Choice, Try again.\n")
                    continue
            while True:
                urgent_or_not = input("(1) Urgent \n(2) Not Urgent \nChoice: ")

                if urgent_or_not == "1":
                    urgent_or_not = "Urgent"
                    break
                elif urgent_or_not == "2":
                    urgent_or_not = "Not Urgent"
                    break
                else:
                    print("Invalid Urgency Choice, Try again.\n")
                    continue

            Work_Task_obj.priority = f"{importance} - {urgent_or_not}"

            new_task = [self.title, self.description, self.status, self.due_date, Work_Task_obj.priority]

        elif task_type == "Personal Tasks":
            Personal_Task_obj.category = input("Enter task category: ")
            new_task = [self.title, self.description, self.status, self.due_date, Personal_Task_obj.category]

        info[index][mail]["Tasks"][task_type].append(new_task)
        dump_fn()
        print("\nTask Added successfully.")

    def task_search(self, task_type):
        selected_task = 0

        while True:
            try:
                selected_task = int(input("Write number of task you want: ").strip())

            except ValueError:
                print("Invalid task number. try again (*only numbers allowed*).")
                continue
            except KeyboardInterrupt:
                print("\nProcess interrupted by user. Try again.")
                continue

            try:
                if info[index][mail]["Tasks"][task_type][selected_task - 1]:
                    return selected_task - 1
            except IndexError:
                print("Invalid task number. try again.")

    def remove_task(self, task_type):
        self.view_tasks(task_type)
        i = self.task_search(task_type)
        info[index][mail]["Tasks"][task_type].pop(i)
        print("\nTask removed.")
        dump_fn()

    def update_task(self, task_type):
        self.view_tasks(task_type)
        i = self.task_search(task_type)
        task = info[index][mail]["Tasks"][task_type][i]

        print(f"{'\t' * 11}  {'**' * 15}{task[0]}{'**' * 15}\n")
        print(f"Description: \n{task[1]} \nStatus: {task[2]}    Due Date: {task[3]}    Task type: {task_type}")
        if task_type == "Work Tasks":
            print(f"Priority: {task[4]}")
        elif task_type == "Personal Tasks":
            print(f"Category: {task[4]}")
        print(f"\n{'**' * 80}")

        while True:
            print("\nYou want to update what?\n"
                  "(1) description\n"
                  "(2) status\n"
                  "(3) due date")
            if task_type == "Personal Tasks":
                print("(4) Category")
            elif task_type == "Work Tasks":
                print("(4) Priority")

            ch = input("Enter your choice: ")

            if ch == "1":
                edit = input("Enter new description:\n")
                task[1] = edit
                print("\nDescription updated successfully.\n")
                break

            elif ch == "2":
                f = 0
                while f == 0:
                    new_status = input("\nChoose new status: \n(1) Incomplete \n(2) Completed \n(3) In progress \n\nYour choice: ")

                    if new_status == "1":
                        task[2] = "Incomplete"
                        print("\nstatus updated successfully.\n")
                        f = 1
                    elif new_status == "2":
                        task[2] = "Completed"
                        print("\nstatus updated successfully.\n")
                        f = 1
                    elif new_status == "3":
                        task[2] = "In progress"
                        print("\nstatus updated successfully.\n")
                        f = 1

                    else:
                        print("\nInvalid choice. Try again.")
                        continue
                break

            elif ch == "3":
                while True:
                    self.due_date = input("Enter Task due date, use format YYYY-MM-DD.: ")

                    date_validation = self.validate_date(self.due_date)
                    if date_validation:
                        break
                    else:
                        continue

                task[3] = self.due_date

            if task_type == "Personal Tasks":
                if ch == "4":
                    edit = input("Enter new Category:\n")
                    task[4] = edit
                    print("\nCategory updated successfully.\n")
                    break

                else:
                    print("\nInvalid input. try again.")
                    continue

            elif task_type == "Work Tasks":
                if ch == "4":

                    while True:
                        importance = input("\nChoose priority:\n"
                                           "(1) Important\n"
                                           "(2) Moderate importance\n"
                                           "(3) Not important\n"
                                           "Choice: ")

                        if importance == "1":
                            importance = "Important"
                            break
                        elif importance == "2":
                            importance = "Moderate importance"
                            break
                        elif importance == "3":
                            importance = "Not important"
                            break
                        else:
                            print("Invalid Importance Choice, Try again.\n")
                            continue
                    while True:
                        urgent_or_not = input("(1) Urgent \n(2) Not Urgent \nChoice: ")

                        if urgent_or_not == "1":
                            urgent_or_not = "Urgent"
                            break
                        elif urgent_or_not == "2":
                            urgent_or_not = "Not Urgent"
                            break
                        else:
                            print("Invalid Urgency Choice, Try again.\n")
                            continue

                    task[4] = f"{importance} - {urgent_or_not}"
                    print("\nPriority updated successfully.")
                    break

            else:
                print("\nInvalid input. try again.")
                continue

        dump_fn()

    def view_tasks(self, task_type):

        print(f"\n{'**' * 15}{task_type}{'**' * 15}\n")

        c = 1
        for task in info[index][mail]["Tasks"][task_type]:
            print(f"{'\t'*2}{'**' * 10}({c}) {task[0]}{'**' * 10}")
            print(f"Description: {task[1]}\n")
            print(f"Status: {task[2]}    Due Date: {task[3]}    Task type: {task_type}")

            if task_type == "Work Tasks":
                print(f"Priority: {task[4]}")
            elif task_type == "Personal Tasks":
                print(f"Category: {task[4]}")

            c += 1

        print("-" * 90)

    def view_all_tasks(self):
        self.view_tasks("Work Tasks")
        self.view_tasks("Personal Tasks")


class WorkTask(Task):

    def __init__(self, title, description, due_date, status, task_type, priority):
        super().__init__(title, description, due_date, status, task_type)
        self.priority = priority
        self.task_type = "Work Tasks"

    def basic_menu(self):
        basic_menu(self.task_type)

    def Add_Task(self):
        Task_Manager_obj.Add_Task(self.task_type)

    def remove_task(self):
        Task_Manager_obj.remove_task(self.task_type)

    def update_task(self):
        Task_Manager_obj.update_task(self.task_type)


class PersonalTask(Task):
    def __init__(self, title, description, due_date, status, task_type, category):
        super().__init__(title, description, due_date, status, task_type)
        self.category = category
        self.task_type = "Personal Tasks"

    def basic_menu(self):
        basic_menu(self.task_type)

    def Add_Task(self):
        Task_Manager_obj.Add_Task(self.task_type)

    def remove_task(self):
        Task_Manager_obj.remove_task(self.task_type)

    def update_task(self):
        Task_Manager_obj.update_task(self.task_type)

#--------------------------------------------------------------------------------------------------------


def basic_menu(task_type):
    now_obj = 0

    if task_type == "Work Tasks":
        now_obj = Work_Task_obj
    elif task_type == "Personal Tasks":
        now_obj = Personal_Task_obj

    while True:
        try:
            ch = int(input("(1) Add Task\n"
                           "(2) Delete Task\n"
                           "(3) Update Task\n"
                           "(4) View Tasks\n"
                           "(5) View All Tasks\n"
                           "(6) Main menu\n"
                           "(7) Exit\n"
                           "Choice: "))

            if ch == 1:
                now_obj.Add_Task()

            elif ch == 2:
                now_obj.remove_task()

            elif ch == 3:
                now_obj.update_task()

            elif ch == 4:
               Task_Manager_obj.view_tasks(task_type)

            elif ch == 5:
                Task_Manager_obj.view_all_tasks()

            elif ch == 6:
                main_menu()

            elif ch == 7:
                dump_fn()
                print("Good Bye!")
                sys.exit()

            else:
                print("Invalid Choice. Try again.")
                continue

        except ValueError:
            print("Invalid Input. Enter only numbers.\n")
            continue


def dump_fn():
    file = open("accounts.json", 'w')
    json.dump(info, file, indent=2)
    file.close()


def password_conditions(password):
    if len(password) < 8:
        return False

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*" for c in password)

    if sum([has_upper, has_lower, has_digit, has_special]) < 3:
        return False

    common_patterns = ["12345678", "password"]
    if password.lower() in common_patterns:
        return False

    return True


def sign_up():
    while True:
        name = input("Enter Your Name: ")
        mail = input("Enter Your mail: ")
        passw = input("Enter Your Password: ")

        if "@" not in mail or ".com" not in mail:
            print("\nInvalid E-mail address. Please use a valid E-mail account.")
            continue

        if password_conditions(passw):
            new_user = {
                mail: {
                    "name": name,
                    "password": passw,
                    "Tasks": {
                        "Personal Tasks": [],
                        "Work Tasks": []
                    }
                }
            }

            info.append(new_user)
            dump_fn()
            print("User successfully signed up.")
            print(f"\nWelcome {name}!")
            return info.index(new_user), mail

        else:
            print("Weak password. Please choose a stronger one.")


def login():
    for i in range(3):
        mail = input("Enter Your mail: ")
        password = input("Enter Your Password: ")

        flag = False
        for account in info:
            if mail in account:
                if password == account[mail]["password"]:
                    flag = True
                    print(f"\nWelcome back {account[mail]["name"]}!")
                    return info.index(account), mail
                else:
                    continue
            else:
                continue

        if flag == False:
            print(f"Invalid E-mail or password. please try again. you have {2 - i} trials\n")
            continue

    return None


def main_menu():
    while True:
        ch = input("\n(1) Work Tasks\n"
                   "(2) Personal Tasks\n"
                   "(3) Exit\n"
                   "Enter your choice: ")

        if ch == "1":
            Work_Task_obj.basic_menu()

        elif ch == "2":
            Personal_Task_obj.basic_menu()

        elif ch == "3":
            dump_fn()
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. please try again.")
            continue


mail = ""
index = None

while True:
    print("Please choose what you would like to do:")
    print("1. Sign Up")
    print("2. Login")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            index, mail = sign_up()
            break

        elif choice == 2:
            index, mail = login()
            if mail:
                break
            else:
                continue

        elif choice == 3:
            print("Exiting. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

    except ValueError:
        print("Invalid choice. Please try again (**only numbers**).\n")

Task_obj = Task("", "", "", "", "")
Work_Task_obj = WorkTask("", "", "", "", "", "")
Personal_Task_obj = PersonalTask("", "", "", "", "", "")
Task_Manager_obj = Task_manager("", "", "", "", "")
main_menu()

input()
