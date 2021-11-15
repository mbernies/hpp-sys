import subprocess
import shlex
import time

subprocess.run("clear", shell=True)

def menu():
    print("CHOOSE FROM THE OPTIONS BELOW:")
    print("[1] Total current email queue")
    print("[2] List email queue")
    print("[3] Top sender on queue")
    print("[4] Purge email queue")
    print("[5] Bounce back recipient")
    print("[6] Clear bounce back emails, '<>'")
    print("[7] Sender IP addresses")
    print("[8] Block spammer IP")
    print("[0] Exit")

#please disregard the line below

'''
def menu2():
    print("[1] Purge emails")
    print("[0] Return main menu")

def exit_menu():
    print("[0] Return main menu")
'''

def option1():
    print()
    mail_queue = subprocess.run("exim -bpc", shell=True, stdout=subprocess.PIPE)
    print(f"Current mail queue: {mail_queue.stdout.decode()}")

def option2():
    print()
    mailqueue = subprocess.run("exim -bp | less", shell=True)
    subprocess.run("clear", shell=True)

def option3():
    print()
    subprocess.run("exim -bp | awk '{print $4}' | sort | uniq -c | sort -n | tail", shell=True)

def option4():
    print()
    email_address = input("Enter email address: ")
    email_id = 'awk {print$3}'
    command = 'exim -bpru | grep {} | ' + email_id + ' | xargs exim -Mrm'.format(shlex.quote(email_address))
    subprocess.run(command, shell=True)
    print(f"\nEmail queue from {email_address} removed!\n")
    mail_queue = subprocess.run("exim -bpc", shell=True, stdout=subprocess.PIPE)
    print(f"Current mail queue: {mail_queue.stdout.decode()}")
    time.sleep(2)
    subprocess.run("clear", shell=True)

def option5():
    print()
    subprocess.run("grep '<= <> ' /var/log/exim_mainlog | tail -500 | awk '{print $1" "$24}' | sort | uniq -c | sort -n | tail", shell=True)

def option6():
    print()
    subprocess.run("exim -bpru | grep '<>' | awk '{print $3}' | xargs exim -Mrm", shell=True)

def option7():
    print()
    subprocess.run("grep 'A=dovecot_' /var/log/exim_mainlog | grep 'T=\"' | tail -1000 | awk '{print $7}' | grep -v 'H\=\|localhost\|mail.\|.com' | sort | uniq -c | sort -n | tail", shell=True)
    print()
    subprocess.run("grep 'A=dovecot_' /var/log/exim_mainlog | grep 'T=\"' | tail -1000 | awk '{print $8}' | grep -v 'localhost\|mail.\|.com' | sort | uniq -c | sort -n | tail", shell=True)
    print()
    subprocess.run("grep 'A=dovecot_' /var/log/exim_mainlog | grep 'T=\"' | tail -1000 | awk '{print $9}' | grep -v 'I\=\|localhost\|mail.\|.com' | sort | uniq -c | sort -n | tail", shell=True)

def option8():
    print()
    ip_address = input("Enter IP address to block: ")
    subprocess.run("csf -d {}".format(shlex.quote(ip_address)), shell=True)
    print(f"\nIP address {ip_address} has been blocked!\n")

def option0():
    print("\n\n")
    mail_queue = subprocess.run("exim -bpc", shell=True, stdout=subprocess.PIPE)
    print(f"Current mail queue: {mail_queue.stdout.decode()}")
    print("\nEXIT!")

menu()
option = int(input("\nEnter your option: "))

while option != 0:
    if option == 1: #Total of the current email queue
        option1()
    elif option == 2: #List current email queue
        option2()
    elif option == 3: #Top email address on queue
        option3()
    elif option == 4: #Purge or clear the email queue of the specified email address
        option4()
    elif option == 5: #List of bounce back recipient, for investigation purposes
        option5()
    elif option == 6: #Clear bounce back emails on queue
        option6()
    elif option == 7: #List of malicious IP address, not 100% guarantee spammers
        option7()
    elif option == 8: #Deny spammer IP in CSF
        option8()
    else:
        print("\nINVALID OPTION!")
    print("\n\n")
    menu()
    option = int(input("\nEnter your option: "))

option0()

