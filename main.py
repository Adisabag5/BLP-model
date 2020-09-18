from User import User
from State import State

classification = {
    "1": "Top-secret",
    "2": "Secret",
    "3": "Confidential",
    "4": "Unclassified"
}

Worlds = {
    "1": "Mars",
    "2": "Jupiter",
    "3": "Saturn",
    "4": "Neptune"
}

currentUser = User("Admin", "123456", "true", 0,0,0,0)
currentState = State(currentUser.userName, "Admin", 0, "Mars")

def create_user(user):
    user.create_user()
    return user

def delete_user(user):
    userName = input("Please enter a user's name to be deleted.")
    user.delete_user(userName)
    return user

def create_file(user):
    user.create_file(currentState)
    return user

def find_file(user):
    fileName = input("enter the name of the file:")
    user.findFile(fileName, currentState.world)
    return user

def read_file(user, currentState):
    user.read_file(currentState)
    return user

def write_to_file(user, currentState):
    user.write_to_file(currentState)
    return user

def change_world(user):
    userChoice = "Invalid"
    print("Which world you want to visit now?")
    while userChoice == "Invalid":

        userChoice = input( "1. Mars 2. Jupiter 3. Saturn 4. Neptune")
        newWorld = Worlds.get(userChoice, "Invalid")

        if newWorld == currentState.world:
            print("You are already in this world, pick again")
            userChoice = "Invalid"
        else:
            userClassification = ""
            if newWorld == "Mars": userClassification = user.marsClass
            if newWorld == "Jupiter": userClassification = user.jupiterClass
            if newWorld == "Saturn": userClassification = user.saturnClass
            if newWorld == "Neptune": userClassification = user.neptuneClass
            currentState.world = newWorld
            if user.isAdmin == "false":
                currentState.classification = userClassification
    print("***********************************************************")
    print("                 Welcome to " + currentState.world                     )
    print("        Your class in this world is - " + currentState.classification)
    print("***********************************************************")
    return user

def change_password(user):
    user.change_password()
    return user

def worldToValue(world, user):
    if world == "Mars": return user.marsClass
    if world == "Jupiter": return user.jupiterClass
    if world == "Saturn": return user.saturnClass
    if world == "Neptune": return user.neptuneClass

def logout(user):
    global currentUser
    global currentState
    userName = 'Invalid'
    counter = 0
    while user.userName != userName and counter < 3:
        userName = input("Username:")
        password = input("Password:")
        user = user.check_user(userName, password)
        if user.userName != userName:
            print("Wrong username or password, try again")

    if user.userName == userName:
        print("***********************************************************")
        print("                 Welcome " + userName)
        print("***********************************************************")
        #currentState.userName = userName
        #currentState.classification = worldToValue(currentState.world, user)
        #currentUser = (user.userName, user.password, user.isAdmin, user.marsClass, user.jupiterClass, user.saturnClass,user.neptuneClass)
    return user

def convertToInt(classification):
        value = 4
        if classification == "Top-secret":
            value = 1
        else:
            if classification == "Secret":
                value = 2
            else:
                if classification == "Confidential":
                    value = 3
                else:
                    if classification == "Unclassified":
                        value = 4
        return value

def main():

    #Original Admin
    world_A = "Mars"
    world_B = "Jupiter"

    currentUser = User("Admin", "123456", "true", 0,0,0,0)
    currentState = State(currentUser.userName, "Admin", 0, world_A)

    adminMenu = {
        '1': create_user,
        '2': delete_user,
        '3': create_file,
        '4': read_file,
        '5': write_to_file,
        '6': change_world,
        '7': change_password,
        '8': logout
    }

    userMenu = {
        '1': create_file,
        '2': read_file,
        '3': write_to_file,
        '4': change_password,
        '5': change_world,
        '6': logout
    }

    userChoice = 0
    print("WELCOM!!")

    while userChoice != "9":
        if userChoice == "Invalid choice":
            print("Invalid choice, try again")

        print("Choos what you want to do from the following options: ")
        print("1. Create new user. ")
        print("2. Delete user. ")
        print("3. Create new file. ")
        print("4. Read a file.")
        print("5. Write to an existing file. ")
        print("6. Enter a new world. ")
        print("7. Change your password. ")
        print("8. Logout. ")
        print("9. Exit. ")

        userChoice = input("Enter your choice")

        func = adminMenu.get(userChoice, "Invalid choice")
        if userChoice == "4" or userChoice == "5":
            currentUser = func(currentUser, currentState)
        else:
            currentUser = func(currentUser)
        if currentUser.isAdmin == 'false':
            userChoice = "9"
    x = convertToInt(worldToValue(currentState.world, currentUser))
    currentState = State(currentUser.userName, worldToValue(currentState.world, currentUser), x, currentState.world)
    print(currentState.userName, currentState.world, currentState.classification)

    userChoice = "0"
    while userChoice != "7":
        if userChoice == "Invalid choice":
            print("Invalid choice, try again")
        if currentUser.isAdmin == 'true':
            break

        print("Choos what you want to do from the following options: ")
        print("1. Create new file. ")
        print("2. Read file. ")
        print("3. Write to file. ")
        print("4. Change your password. ")
        print("5. Enter a new world. ")
        print("6. Logout. ")
        print("7. Exit. ")

        userChoice = input("Enter your choice")
        func = userMenu.get(userChoice, "Invalid choice")
        if userChoice == "3" or userChoice == "2":
            currentUser = func(currentUser, currentState)
        else:
            currentUser = func(currentUser)

    print("Bye")

main()

