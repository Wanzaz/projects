from cryptography.fernet import Fernet

#pass does nothing it is there because of errors
'''  b'hello' = byte string
    'hello' = string
'''

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()'''

def load_key():
    file = open("key.key", "rb") # rb = read bits
    key = file.read()
    file.close()
    return key

# master_pwd = input('What is the master password? ')
key = load_key() # + master_pwd
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f: # it will automatically close the file
        # w = overwrite (already exist), r = read only, a = add something to file, it does not have exist 
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print('User:', user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input('Acount Name: ')
    pwd = input('Password: ')

    with open('password.txt', 'a') as f: # it will automatically close the file
        # w = overwrite (already exist), r = read only, a = add something to file, it does not have exist 
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input('Would you like to add a new password or view existing ones (view, add), press q to quit? ').lower()
    if mode == 'q':
        break
    
    if mode == 'view':
        view()
    elif mode == "add":
        add()
    else:
        print('Invalid mode.')
        continue

