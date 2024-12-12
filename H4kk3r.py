import re
import cowsay

class Villains: #this is my example of the class system, with a superclass of vilains and subclasses showcasing the users and thair 'supervisors'

    class User:

        def __init__(self, name, skill_level):
            self.name = name
            self.skill_level = skill_level
    user = User("BigBaddie99", 2)
    
    class Boss:
        def __init__(self, name, skill_level):
            self.name = name
            self.skill_level = skill_level
    boss = Boss("DarthBalrog", 999)

rules = { #here is the rules for my example of using regex, it should prompt the user to imput sometheing like P4ssw0rd but can be easily bypassed (hacker style) using P1d 
    "Password must start with 'p'": r"^p.*|^P",
    "Password must end with 'd'": r"[dD]$",
    "Password must contain at least one digit": r"\d",
    "Password must include an uppercase letter": r"[A-Z]"
}

def validate_password(password): #here is my function to validate the password, it is crucial to have this for testing later on 
    feedback = []
    for hint, rule_pattern in rules.items():
        if not re.search(rule_pattern, password):
            feedback.append(hint)
    return feedback

def main(): #this is the main section of code that introduces the user to the task and the theme for this program, a hacker spy expirience.
    print("Welcome agent, today's mission is a simple one, no exploding cars or airplane dogfights unlike yesterday.")
    print("You will not even have to leave your house. We need you to infiltrate 'the database'")
    print("A super-secret organization with TOP security. No worries for you though,")
    print("I don't even need to tell you how to get in! I believe in you agent!")
    print("-----------------------------------------------------------------------------------------------------------")

    while True: # here is an example of a simple loop that allows the user to put in incorrect answers and try again without the need to restart the program again 
        password = input("Enter password: ")
        feedback = validate_password(password)

        if not feedback:  
            print("Access granted!")
            break
        else:
            print("Access denied. Here are some hints:")
            for message in feedback:
                print(f"- {message}")
    # after the user passes the password puzzle it continues to the next lines of story and launches the deets 'library' that i have created to continue the story seamlessly
    print(f"welcome to the super secret database, current user: {Villains.user.name}, clearance level: {Villains.user.skill_level}")
    print(f"your current supervisor is {Villains.boss.name}, clearence level:{Villains.boss.skill_level}")
    print ("What would you like to acess?")
    import Deets
    
if __name__ == "__main__":
    main()