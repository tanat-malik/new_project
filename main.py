user_choice = ''
while True:
    user_choice = input('Ты кто такой? ')
    if user_choice == '' or user_choice == ' ':
        print('Напиши че нить')
    else:
        print(user_choice)
        break
