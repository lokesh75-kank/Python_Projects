from cryptography.fernet import Fernet

master_pass = input("Enter the master password: ").lower()

# def write_key():
#     key = Fernet.generate_key()

#     with open("key.key", "wb") as write_kee:
#         write_kee.write(key)  

# write_key()  #once key file is generated we dont need another file.

def load_key():
    file = open("key.key", "rb") 
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user , pasw = data.split("|")
            print("username:", user , "password:", pasw)

def add():
    name = input("Account Name : ")
    password = input("Enter new password: ")
    with open("password.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")


while True:

    mode = input("would you like to view the existing password or add new the password ? or press q to quit ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid option")
        continue

print("Thank you using password manager, Good bye !")