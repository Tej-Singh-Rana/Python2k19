#!/bin/python3

import os
print('''Options:-
. Press 1 Create a new directory.
. Press 2 Create a new file.
. Press 3 Install a new software and to query installed packages.
. Press 4 Create a new user and password.
. Press 5 Display current date & time.
. Press 6 To reboot your machine.
. Press 7 To search in google.
. Press 8 To play a song in system's music player.
. Press 9 To get searched 5 Url on google.
. Press 10 Login your Facebook and Update status.
. Press 11 Send message to your whatsapp.
''')
print("Enter your key value : ")
press=int(input())

if press == 1:
    print("Type name to create a new directory : ")
    os.mkdir(input())
elif press == 2:
    filename=input()
    os.system('touch {}'.format(filename))
elif press == 3:
    print("To install software type 3.1 or To check installed packages type 3.2 ")
    x=float(input())
    if x == 3.1:
        print("Enter the software name to install :")
        software=input()
        os.system('yum install -y {}'.format(software))
    elif x == 3.2:
        print("Enter the package name to query :")
        package=input()
        os.system('rpm -q {}'.format(package))
    else:
        print("type valid press value")
#press 4 for user create & password
elif press == 5:
    os.system("date +'%F %T'")
    
elif press == 6:
    print("are you sure ? y/n")
    access=input()

    if access == "y":
        os.system("reboot")
    elif access == "n":
        print("Process aborted")

        
