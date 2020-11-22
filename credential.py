import random

class Credential:
    '''
    Will generate new instances of account credentials
    '''
    credential_list = []

    def __init__(self, username, acc_name, acc_password):
        '''
        Passed in three arguments of the isntances of our variables
        '''
        self.acc_name = acc_name
        self.acc_password = acc_password
        self.username = username

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

   