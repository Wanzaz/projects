import os

#this code renames all the files in the specific directory

def main():
    i = 0
    path = "C:/Users/Uzivatel/Desktop/testing/" #you have to change the backslash to frontslash
    for filename in os.listdir(path):
        my_dest = "img" + str(i) + ".jpg"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == '__main__':
    main()

