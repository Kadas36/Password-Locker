import random
import pyperclip

class Credential:
    '''
    Will generate new instances of account credentials
    '''
    credential_list = []

    def __init__(self, acc_name, acc_password):
        '''
        Passed in three arguments of the isntances of our variables
        '''
        self.acc_name = acc_name
        self.acc_password = acc_password

    def save_credential(self):
        '''
        saving credential into list
        '''
        Credential.credential_list.append(self)   

    def delete_credential(self):
        '''
        Will delete credential
        '''
        Credential.credential_list.remove(self) 

    @classmethod
    def display_credentials(cls, username):
        """
        this method will take a user_name and
        return credentials that matches that user_name
        """

        for credential in cls.credential_list:
            if credential.username == username:
                return credential 

    @classmethod
    def find_by_acc_name(cls,acc_name):
        '''
        Method that takes in acc_name and returns credentials associated credentials
        '''

        for credential in cls.credential_list:
            if credential.acc_name == acc_name:
                return credential              

    @classmethod
    def copy_acc_password(cls,acc_name):
        credential_found = Credential.find_by_acc_name(acc_name)
        pyperclip.copy(credential_found.acc_password)   

    @classmethod
    def credential_exists(cls,acc_name):
        '''
        Method that checks if a credential exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for credential in cls.credential_list:
            if credential.acc_name == acc_name:
                    return True

        return False                   

   