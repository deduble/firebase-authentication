
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class FirebaseCustomAuthentication:
    def __init__(self, admin_sdk_private_key, app_id):
        self.cred = credentials.Certificate("admin-sdk-key.json")
        self.app = firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()
        self.collection = self.db.collection(app_id)

    def save_user(self, uid, access_token):
        user = self.collection.document(uid).create({'access_token': access_token})
        return user

    def get_user(self, uid):
        user = self.collection.document(uid).get()
        return user

    def get_access_token(self, uid):
        try:
            return self.collection(uid).document('uid').get().to_dict()['access_token']
        except TypeError:
            return None
