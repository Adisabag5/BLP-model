from File import File
import csv
import random
import string
import hashlib, binascii, os

class User(File):
    def __init__(self, userName, password, isAdmin, marsClass, jupiterClass, saturnClass, neptuneClass):
        self.userName = userName
        self.password = password
        self.isAdmin = isAdmin
        self.marsClass = marsClass
        self.jupiterClass = jupiterClass
        self.saturnClass = saturnClass
        self.neptuneClass = neptuneClass


    def create_user(self):
        Worlds = {
            "1": "Mars",
            "2": "Jupiter",
            "3": "Saturn",
            "4": "Neptune"
        }

        classification = {
            "1": "Top-secret",
            "2": "Secret",
            "3": "Confidential",
            "4": "Unclassified"
        }

        newUserName = input("Enter the new username:")
        newPassword = self.first_password()

        print("Which type of user you want to create?")
        print("1. Admin")
        print("2. Regular")
        print("3. Cancel")
        userType = input("Enter your choice")

        # if Admin
        if userType == "1":
            newUser = User(newUserName,newPassword,"true",0,0,0,0)

        # if Regular
        if userType == "2":

            worldsClassification = list()
            print("Choose clasification of the user for each world:")
            print("1. Top-secret 2. Secret 3. Confidential 4. Unclassified")
            userChoice = input("Enter your choice")
            marsClass = classification.get(userChoice, "Invalid choice")
            print("1. Top-secret 2. Secret 3. Confidential 4. Unclassified")
            userChoice = input("Enter your choice")
            jupiterClass = classification.get(userChoice, "Invalid choice")
            print("1. Top-secret 2. Secret 3. Confidential 4. Unclassified")
            userChoice = input("Enter your choice")
            saturnClass = classification.get(userChoice, "Invalid choice")
            print("1. Top-secret 2. Secret 3. Confidential 4. Unclassified")
            userChoice = input("Enter your choice")
            neptuneClass = classification.get(userChoice, "Invalid choice")


            hash_pass = self.hash_password(newPassword)
            newUser = User(newUserName,hash_pass,"false",marsClass, jupiterClass, saturnClass, neptuneClass)
        newUser.insert_user_to_list()
        print("The new user was created with user name - " + newUserName + "and password - " + newPassword)


    def insert_user_to_list(self):
        with open('users.csv', mode='a', newline='') as users_file:
            user_writer = csv.writer(users_file, delimiter=',')
            user_writer.writerow([self.userName, self.password, self.isAdmin, self.marsClass, self.jupiterClass, self.saturnClass, self.neptuneClass])

        users_file.close()

    def check_user(self,userName, password):
        with open('users.csv', mode='r') as users_file:
            csv_reader = csv.reader(users_file)
            tempUser = User(userName, password, "false", 0,0,0,0)
            for line in csv_reader:
                if line != []:
                    if line[0] == userName:
                        if self.verify_password( line[1], password):
                            users_file.close()
                            tempUser = User(line[0],line[1],line[2],line[3],line[4],line[5],line[6] )
                            return tempUser
                        else:
                            users_file.close()
                            return self



    def first_password(self):
        sample_str = ''.join((random.choice(string.ascii_letters) for i in range(4)))
        sample_str += ''.join((random.choice(string.digits) for i in range(4)))

        sample_list = list(sample_str)
        random.shuffle(sample_list)
        final_string = ''.join(sample_list)
        return final_string


    def hash_password(self, password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                      salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')


    def verify_password(self, stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    def change_password(self):
        newPassword = input("Enter your new password:")
        newHashPassword = self.hash_password(newPassword)
        self.delete_user(self.userName)
        insert_user_to_list(self)


    def delete_user(self, userName):
        lines = list()
        with open('users.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == userName:
                        lines.remove(row)
                        print("The user - " + userName + "was deleted from the list")
        with open('users.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)