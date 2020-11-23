class User:
    """
    Class that generates new instances of users
    """
    user_list = []

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def save_user(self):
        """
        save_user method saves the users object into our user_list
        """
        User.user_list.append(self)

    @classmethod
    def find_by_username(cls, username):
        """
        method to check is a user exists
        """
        for user in cls.user_list:
            if user.username == username:
                return user

    @classmethod
    def user_exists(cls,username):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for user in cls.user_list:
            if user.username == username:
                    return True

        return False             