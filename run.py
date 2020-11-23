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

def display_credentials():
    """
    Function to use credentials
    """
    return Credential.display_credentials()

def delete_credential(credential):
    """
    delete a credential
    """
    Credential.delete_credential()   

def check_existing_credentials(acc_name):
        '''
        Function that check if a credential exists with that acc_name and return a Boolean
        '''
        return Credential.credential_exists(acc_name)     

def find_credential(acc_name):
    '''
    Function that finds credential by acc_name and returns the credential
    '''
    return Credential.find_by_acc_name(acc_name)

def main():
    print("Hello! Welcome to Password Locker. What is your name?")
    name = input()
    
    print(f"Hi {name.title()},")
    print("Use n - create a new password-locker account")

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
                  nc - create credential
                  dc - display credentials
                  fc - find credential
                  """)
            short_codes = input().lower()
            if short_codes == "nc":
                print("""Type in one of the short_codes,
                w - make a password so that we can store it for you,
                g - we will randomize a password for you
                """)
                acc_reply = input().lower()

                if acc_reply == "w":
                    print("Enter a name of the account you wish to create")
                    acc_name = input()
                    print("Enter a password for the account")
                    passW = input()

                elif acc_reply == "g":
                    print("Enter a name of the account you wish to create")
                    acc_name = input()
                    passW = password_generator()
                    print(f"We have stored your credentials as account name - {acc_name} and password - {passW}")

                else:
                    print("Use one of the short codes")
                save_credential(create_credential(acc_name, password))
                break

                print("Account credentials stored")
                print("__" * 30)

            elif short_code == "dc":

                if display_credentials():
                    print("Here is a list of all your credentials")
                    print('\n')

                    for credential in display_credentials():
                        print(
                        f"{credential.acc_name} .....{credential.acc_password}")

                        print('\n')
                else:
                    print('\n')
                    print("You dont seem to have any contacts saved yet")
                    print('\n')    

            elif short_codes == "fc":
                print("Enter an account name to search for credentials")
                src = input().title()
                if check_existing_credentials(src):
                    search_credential = find_credential(src)
                    print(f"{search_credential.acc_name} {search_credential.acc_password}")
                    print('-' * 20)
                else:
                    print("The account does not exist")
                break
            else:
                print("wrong input, kindly check on your input")
            break
    print("__" * 25)


if __name__ == '__main__':
    main()           