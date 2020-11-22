import random

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
        saving credential object into object list
        '''
        Credential.credential_list.append(self)    

   