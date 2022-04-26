## create a class
class User:
    """generate an instance of a class
    """
    user_list=[]#list of users
    def __init__(self,username,password):
        self.username = username
        self.password =password
        ##save users
    def save_user(self):
        User.user_list.append(self)
   #delete user
    def delete_user(self):
        User.user_list.remove(self)
    @classmethod
    def find_user(cls, username):
        '''
        find username using search terms
        '''
        for user in cls.user_list:
            if user.username == username:
                return  user