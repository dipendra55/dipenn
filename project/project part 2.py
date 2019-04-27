#author=dipendra ale

def show_menu():
    menu = "choose the option below " + "\n\t1: show_all_employees"\
                                        "\n\t2: show_employee" \
                                        "\n\t3: change salary "\
                                        "\n\t4: add_employee"\
                                        "\n\t5: remove_employee"\
                                        "\n\t6: save_bonus info"\
                                        "\n\t7: generate_report" \
                                        "\n\t8: TO exit"\
                                        "\n==> "

    while True:
        try:
            number = int(input(menu))
            if 1 <= number <= 8:
                break
            else:
                print("Values 1, 2 , 3, 4, 5, 6 or 7..... please")
        except ValueError:
            print("Values 1, 2 , 3, 4, 5, 6 or 7 .... please")

    if number==1:
        show_all_employees()
    elif number==2:
        show_employee()
    elif number==3:
        change_salary()
    elif number==4:
        add_employee()
    elif number==5:
        remove_employee()
    elif number==6:
        save_bonus_info()
    elif number==7:
        generate_report()
    else:
        exit()



def load_data():
    print("load data")
    file = open("emp.txt", 'r')
    employee_id_list = []
    firstname_list= []
    surname_list = []
    salary_list = []
    email_list = []
    while True :
        data = file.read()
        if(data == ''):
            break
        list1 = data.split(",")
        employee_id_list.append(list1[0])
        firstname_list.append(list1[1])
        surname_list.append(list1[2])
        salary_list.append(list1[3])
        email_list.append(list1[4])
    file.close()
    return employee_id_list, firstname_list, surname_list, salary_list, email_list


def save_data():
    print("save data")




def show_all_employees(employee_id_list, firstname_list, surname_list, salary_list, email_list):
    for item in employee_id_list:
        print(item, " ", end="")
    print('\n')
    for item in firstname_list:
        print(item, " ", end="")
    print('\n')
    for item in surname_list:
        print(item, " ", end="")
    print('\n')
    for item in salary_list:
        print(item, " ", end="")
    print('\n')
    for item in email_list:
        print(item, " ", end="")
    print('\n')

def show_employee(


def change_salary():
    print("change salary")



def add_employee():
    print("add employee")


def remove_employee():
    print("remove employee")

def find_employee_pos_in_list(empid, employee_id_list):
    if empid in employee_id_list:
        position = employee_id_list.index(empid)
        return position
    else :
        return -1

def save_bonus_info():
    print("save bonus info")



def generate_report():
    print("generate report")




def main():
    menu = "choose the option below " + "\n\t1: load_data" \
                                        "\n\t2: Show_menu" \
                                        "\n\t3: Save_data" \
                                        "\n\t4: TO EXIT"\
                                        "\n==> "
    while True:
        try:
            number = int(input(menu))
            if 1 <= number <= 4:
                break
            else:
                print("Values 1, 2 or 3 please...")
        except ValueError:
                    print("Values 1, 2 or 3 please...")
    if number==2:
               show_menu()
    elif number==1:
               load_data()
    elif number==3:
             save_data()
    else:
        exit()

main()



