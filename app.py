from utils.general_utils import GeneralUtils

_gen_utils = GeneralUtils()

user_answer = ''

while user_answer != '3':
    print("1. Save new data\n2.Find Data\n3.Quit")
    user_answer = input("What do you want to do?\n")
    if user_answer == "1":
        url = input("Enter the URL: \n")
        username = input("Enter your username: \n")
        password = input("Enter your password: \n")

        input_data = dict({
            "url": url,
            "username": username,
            "password": password
        })
        _gen_utils.saveToJson(input_data)
        print("New data has been saved!\n")
        
    elif user_answer == "2":
        input_url = input("What is the website you are looking for?\n")
        _gen_utils.find_and_copy(input_url)
    else:
        print("Goodbye!")
        break





