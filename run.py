from user import User
from credential import Credential
import random
import string

def create_user(username, password, email):
    '''
    creates a user
    '''
    new_user = User(username, password, email)
    return new_user