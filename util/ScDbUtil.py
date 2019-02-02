from ardb.User import User
from datetime import datetime

class ScDbUtil:

    @staticmethod
    def create_user_to_db(scUser):
        u = User()
        u.convert(soundcloudUser=scUser)
        u.dt_bd_action=datetime.today()
        return u

    @staticmethod
    def scUsersToJsonDbUsers(usersList):
        dbUsers = []
        for user in usersList :
           dbUsers.append(ScDbUtil.create_user_to_db(user).to_dict())
        return dbUsers
       