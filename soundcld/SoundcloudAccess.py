from flask import g, current_app
class SoundcloudAccess():
 

    def __init__(self):
        print("constructor")
        client_sc=getattr(g, 'client_sc', None)
        print(client_sc)

    def get_client_sc(self):
        return self.client_sc
        