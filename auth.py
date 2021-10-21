import os
import json

__users_folder__ = 'db/users/'
__user_id_path__ = 'db/ids/user_id'
__session_file__ = 'db/session'


def user_view():
    sessionFile = open(__session_file__, 'r')
    userId = sessionFile.read()
    if userId == '':
        print('No user is signed in')
    else:
        usersFolderFile = open(__users_folder__+userId+'.json')
        user = json.load(usersFolderFile)
        print(user)

def user_signin(username, password):
    
    files = os.listdir(__users_folder__)
    users = []


    
    for file in files:
        usersFolderFile = open(__users_folder__+file, 'r')
        users.append(json.load(usersFolderFile))
        
    userId = -1

    for index, val in enumerate(users):
        if val['username'] == username and val['password'] == password:
            userId = val['id']
    

    if(userId == -1):
        print('Invalid credentials')
    else:
        sessionFile = open(__session_file__, 'w')
        sessionFile.write(str(userId))
        print('Successfully signed in')


def user_signup(username, password):
    
    dirs = os.listdir(__users_folder__)
    users = []

    for dir in dirs:
        file = open(__users_folder__+dir, 'r')
        users.append(json.load(file))
    
    username_taken = False

    for user in users:
        if user['username'] == username:
            username_taken = True
    
    if username_taken:
        print('Username already taken')
    else:
        userIdFile = open(__user_id_path__, 'r')
        userId = userIdFile.read()
        if userId == '':
            userId = '1'
        userFolderFile = open(__users_folder__+userId+'.json', 'w')
        data = {
            "id": userId,
            "username": username,
            "password": password
        }
        json.dump(data, userFolderFile)
        userIdFile = open(__user_id_path__, 'w')
        userIdFile.write(str(int(userId)+1))
            
