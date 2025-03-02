import pyrebase
import time
import re, uuid
import pyautogui
import socket

config={
    "apiKey": "AIzaSyDj7KWAyQbKRNKf52raGiHrDWphmCzFSHY",
    "authDomain": "fir-422e2.firebaseapp.com",
    "databaseURL": "https://fir-422e2.firebaseio.com",
    "projectId": "fir-422e2",
    "storageBucket": "fir-422e2.appspot.com",
    "messagingSenderId": "345766133818",
    "appId": "1:345766133818:web:092cf367b8b45d945ab503",
    "measurementId": "G-LGXJBKL3J9"
}
# intial variable for mac and Ip address
macadd= str(':'.join(re.findall('..', '%012x' % uuid.getnode())))
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

# initial fire base app config to a object
firebase =pyrebase.initialize_app(config)
# login authincate
auth = firebase.auth()
email = input("please Enter your mail: \n")
password = input("please Enter your password: \n")
# username split from email
rm_add=email.split("@", maxsplit=1)[0]
username = rm_add.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
# if authincate then function execute
if auth.sign_in_with_email_and_password(email,password):
    print("sign in sucessfully")
    def screenshot():
        date = time.strftime("%Y-%m-%d")
        current_time = time.strftime("%H:%M:%S")
        name = int(round(time.time() * 1000))
        name = './Screenshots/{}.png'.format(name)
        time.sleep(5)
        img = pyautogui.screenshot(name)
        storage = firebase.storage()
        path_on_cloud = time.strftime("%Y-%m-%d")+ "/" +username.lower() +"/" + time.strftime("%H:%M:%S")
        path_local = name
        storage.child(path_on_cloud).put(path_local)
        image = storage.child(path_on_cloud).get_url(None)
        a_dict = {}
        for variable in ["username","date","current_time","IPAddr","macadd", "image" ]:
            a_dict[variable] = eval(variable)
        print(a_dict)
        db = firebase.database()
        db.child("Monitor").child(username).push(a_dict)
    while True:
        screenshot()
        time.sleep(60)