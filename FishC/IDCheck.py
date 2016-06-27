# coding='utf-8'
__author__ = 'RandyGuo'


def login(user):
    user_dicts = {'user1':'Password1','user2':'Password2'}
# Check the user whether or not in the user lists
    while True:
        if user_dicts.get(user,'none') == 'none':
            print('There is no this user %s: ' % user)
            user = input("Please input a valid user:")
            continue
        else :
            break

    password = input("Please input your password.")
    if '*' in password :
        enter_temp = 3
        first_flag = True
    else :
        enter_temp = 2
        first_flag = False

    while enter_temp > 0 :
        if user_dicts[user] == password:
            print("Welcome to you , %s" % user)
            break
        else :
            if '*' in password :
                password = input("Incorrect Password!! Please enter a correct password without include '*'!!!\n")
                print('enter_temp contain "*" :',enter_temp)
            else :
                enter_temp -= 1
                print("Incorrect Password !!\nYou have only %d chance to try" % enter_temp)
                if (enter_temp <= 0)and first_flag:
                    break
                password = input("Incorrect Password!! Please enter a correct password!!!\n")
                print()
                if (enter_temp < 0) and (not first_flag) :
                    break

    if enter_temp <= 0:
        print('You have tried 3 times. Bye Bye!!!')

if __name__ == '__main__' :
    user = input("Welcome to FishC!!\nPlease enter your user: ")
    login(user)