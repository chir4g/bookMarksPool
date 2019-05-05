import pyrebase

"""Once you are done pasting your info here please change the file name to pyre.py """
config = {
    "apiKey": "YOUR API KEYS HERE",
    "authDomain": "SOMETHING DOMAINY",
    "databaseURL": "DATABASE URL",
    "projectId": "ID OF THE PROJECT",
    "storageBucket": "WHATEVER IT MEANS",
    "messagingSenderId": "YEAH MESSAGE"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()
#make sure user already exists before sigining in otherwise it fails
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
    
    
