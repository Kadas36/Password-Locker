from user import User
from credential import Credential
import random
import string

def create_user(username, password):
    '''
    creates a user
    '''
    new_user = User(username, password)
    return new_user

def save_user(user):
    '''
    will save new_users
    '''
    user.save_user()   

def user_exists(username):
    '''
    will search for user using username
    '''
    return User.user_exists(username)

def create_credential(acc_name, acc_password):
    """
    Function to save new_profile
    """
    new_account = Credential(acc_name, acc_password)
    return new_account  

def save_credential(credential):
    """
    Will save a user credentials
    """
    credential.save_credential   

def password_generator():
    """
    A function that generates a random password
    """
    S = string.ascii_uppercase + string.ascii_lowercase + string.digits
    print("input preferred password length")
    pass_Length = int(input())
    password = "".join(random.choices(S, k=pass_Length))

    return password  

def display_credential():
    """
    Function to use credentials
    """
    return Credential.display_credentials()

def delete_credential(credential):
    """
    delete a credential
    """
    Credential.delete_credential()   

def main():
    print("Hello! Welcome to Password Locker. What is your name?")
    name = input().title()

    print(f"Hi {name}, Type n to create a new password locker account")

    while True:
        short_code = input().lower()
        if short_code == "n":
            print('__'*30)
            
            print("Enter your preferred username")
            username = input()

            print("We can generate a password for you or you can set it by yourself")
            print("""Use:
                    g-To automatically generate a password for you
                    m-To input your own password""")
            code = input().lower()
            print ("\n")
            if code =="m":
                print("input your password")
                password = input()
            elif code == "g":
                password = password_generator()
                print(f"Your password is {password}")
                break
            else:
                print("Please type m for your own password or g for a generated password")
                break
        save_user(create_user(username,password))
        break

    print(f"User-{username}, password-{password}")
    print("You have successfully created your password-locker account")
    print("__" * 16)

    print("You can now add and view saved password locker accounts and passwords")
    while True:
            print("""Use:
                  np - create password credential
                  dp - display password locker credentials
                  """)
            short_codes = input().lower()
            if short_codes == "np":
                print("""Type in one of the short_codes,
                write - make a password so that we can store it for you,
                generate - we will randomize a password for you
                """)
                acc_reply = input().lower()

                if acc_reply == "write":
                    print("Enter a name of the account you wish to create")
                    acc_name = input()
                    print("Enter a password for the account")
                    security_code = input()

                elif acc_reply == "generate":
                    print("Enter a name of the account you wish to create")
                    acc_name = input()
                    security_code = password_generator()
                    print(f"We have stored your credentials as account name - {acc_name} and password - {security_code}")

                else:
                    print("Use one of the short codes")
                save_credential(create_credential(acc_name, password))
                break
                print("Account credentials stored")
                print("__" * 30)

            elif short_codes == "dp":
                print("Enter an account name to search for credentials")
                src = input().lower()
                if src == acc_name:
                    for credential in display_credential():
                        print(f"{acc_name}, {security_code}")
                else:
                    print("The account does not exist")
                break
            else:
                print("wrong input, kindly check on your input")
            break
    print("__" * 25)


if __name__ == '__main__':
    main()           