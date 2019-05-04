import pyrebase

config = {
    "apiKey": "AIzaSyAyEpR_SUexgv7Zbo0KOGWLx5LWsaCpfoQ",
    "authDomain": "testinglab-a2a6b.firebaseapp.com",
    "databaseURL": "https://testinglab-a2a6b.firebaseio.com",
    "projectId": "testinglab-a2a6b",
    "storageBucket": "testinglab-a2a6b.appspot.com",
    "messagingSenderId": "1054922607107"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("chirag@labsearch.com","123456")

def insert(bname,link,tag1,tag2,tag3):
    data = {"link":link, "tag1":tag1, "tag2":tag2, "tag3":tag3}
    try:
        db.child("bookmarks").child("{}".format(bname)).set(data, user['idToken'])
        print("Created")
        return "Successful"

    except:
        return "0"

def fetch():
    users = db.child("bookmarks").get(user['idToken'])
    vals = users.val()
    print(dict(vals))
    return dict(vals)
    
    
