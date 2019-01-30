from shared import use_case as uc
from shared import response_object as res

from arangodb.User import User

class DeltaCalculator(uc.UseCase):

    # get all first degree from db
    # get all first degree from sc
    # 
    # Check differences
    # add missing first degree
    # 
    # for each first degree calculate delta
    # 
    # print deltas
    # 
  
    def __init__(self, userRepo, sCuserDao):
        self.userRepo=userRepo
        self.sCuserDao=sCuserDao

    def calculate_delta_on_first_degree(self, userId):
       #userDbList = user.followings_count
       userScList = self.sCuserDao.get_all_followings_from_user(userId=userId, limit=0)
       user=self.userRepo.get_by_id(userId)

       print(str(user.followings_count)+ " - " +str(len(userScList)))
