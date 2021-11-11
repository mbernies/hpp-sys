import subprocess
import shlex

def menu():
    print("CHOOSE FROM THE OPTOINS BELOW:")
    print("[1] Total current email queue")
    print("[2] Top email address on queue")
    print("[3] Purge email queue")
    print("[4] Bounce back recipient")
    print("[5] Clear bounce back emails, '<>'")
    print("[6] Sender IP addresses")
    print("[7] Block spammer IP")
    print("[0] Exit")

'''
def menu2():
    print("[1] Purge emails")
    print("[0] Return main menu")

def exit_menu():
    print("[0] Return main menu")
'''

def option1():
    print()
    mail_queue = subprocess.run("exim -bpc", shell=True)
    print(f"Current mail queue: {mail_queue}")

def option2():
    print()
    subprocess.run("exim -bp | awk '{print $4}' | sort | uniq -c | sort -n | tail", shell=True)

def option3():
    print()
    email_address = input("Enter email address: ")
    email_id = 'awk {print$3}'
    command = 'exim -bpru | grep {} | ' + email_id + ' | xargs exim -Mrm'.format(shlex.quote(email_address))
    subprocess.run(command, shell=True)

def option4():
    print()
    subprocess.run("grep '<= <> ' /var/log/exim_mainlog | tail -500 | awk '{print $1" "$24}' | sort | uniq -c | sort -n | tail", shell=True)

def option5():
    print()
    subprocess.run("exim -bpru | grep '<>' | awk '{print $3}' | xargs exim -Mrm", shell=True)

def option6():
    print()
    subprocess.run("grep 'A=dovecot_' /var/log/exim_mainlog | grep 'T=\"' | tail -1000 | awk '{print $8}' | grep -v 'mail.\|.com' | sort | uniq -c | sort -n | tail", shell=True)

def option7():
    print()
    ip_address = input("Enter IP address to block: ")
    subprocess.run("csf -d {}".format(shlex.quote(ip_address)), shell=True)

def option0():
    print("\n\n")
    mail_queue = subprocess.run("exim -bpc", shell=True)
    print(f"Current mail queue: {mail_queue}")
    print("\nEXIT!")

menu()
option = int(input("\nEnter your option: "))

while option != 0:
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    elif option == 4:
        option4()
    elif option == 5:
        option5()
    elif option == 6:
        option6()
    elif option == 7:
        option7()
    else:
        print("\nINVALID OPTION!")
    print("\n\n")
    menu()
    option = int(input("\nEnter your option: "))

option0()
