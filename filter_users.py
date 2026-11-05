import json

"""defining Parameter """
repeat_user_request = True


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)
    
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    
    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user.get("age") == age]

    for user in filtered_users:
        print(user)

def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user.get("email", "").lower() == email.lower()]

    for user in filtered_users:
        print(user)



if __name__ == "__main__":


    while repeat_user_request == True:
        filter_option = input("What would you like to filter by? (name, email, age): ").strip().lower()
        if filter_option == "name":
            name_to_search = input("Enter a name to filter users: ").strip()
            filter_users_by_name(name_to_search)
            break
        elif filter_option == "email":
            email_to_search = input("Enter a email to filter users: ").strip()
            filter_users_by_email(email_to_search)
            break
        elif filter_option == "age":
            age_to_search = int(input("Enter a age to filter users: "))
            filter_users_by_age(age_to_search)
            break
        else:
            print("Filtering by that option is not yet supported.")
            repeat_filter = input ("would like to filter again? (yes or y).").strip().lower()
            if repeat_filter != "yes" and repeat_filter != "y":
                repeat_user_request = False
