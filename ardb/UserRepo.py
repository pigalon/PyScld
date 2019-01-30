from arango_orm import Database
from ardb.User import User

class UserRepo():

    def __init__(self, db):
        self.db = db
        
    def get_by_id(self, userId):
        return self.db.query(User).by_key(str(userId))

    def get_by_username(self, username):
        return self.db.query(User).filter("username==@username", username=username).first()

    def get_all_first_degree(self):
        return self.db.query(User).filter("degree==@degree", degree=1).all()

    def get_all_second_degree(self):
        return self.db.query(User).filter("degree==@degree", degree=2).all()
    
    def sc_to_db(self, user):
        u= User()
        u.convert(soundcloudUser=user)
        self.db.add(u)

    def write(self, user):
        try :
            self.db.add(user)
            return True
        except Exception as e:
            print('Already stored! : ' + str(e))
            return False


    def change_degree_for_a_list(self, users, degree):
        for user in users :
            user.degree=degree


    def write_user_list(self, users):
        cpt_added = 0
        cpt_canceled = 0
        
        for user in users :
            print(str(user._key) + " - " + user.username)
            if (self.write(user=user)) : 
                cpt_added = cpt_added + 1
                print("added cpt : " + str(cpt_added))
            else :
                cpt_canceled = cpt_canceled + 1
                print("canceled cpt : " + str(cpt_canceled))

    

    

