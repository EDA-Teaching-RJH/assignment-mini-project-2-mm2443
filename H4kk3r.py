import re
import cowsay

class Villains:

    class User:

        def __init__(self, name, skill_level):
            self.name = name
            self.skill_level = skill_level
    user = User("BigBaddie99", 2)
    
    class Boss:
        def __innit__(self, name, skill_level):
            self.name = name
            self.skill_level = skill_level
    boss = Boss("DarthBalrog", 999)

rules = {
    "Password must start with 'p'": r"^p.*|^P",
    "Password must end with 'd'": r"[dD]$",
    "Password must contain at least one digit": r"\d",
    "Password must include an uppercase letter": r"[A-Z]"
}

def validate_password(password):
    feedback = []
    for hint, rule_pattern in rules.items():
        if not re.search(rule_pattern, password):
            feedback.append(hint)
    return feedback

def main():
    print("Welcome agent, today's mission is a simple one, no exploding cars or airplane dogfights unlike yesterday.")
    print("You will not even have to leave your house. We need you to infiltrate 'the database'")
    print("A super-secret organization with TOP security. No worries for you though,")
    print("I don't even need to tell you how to get in! I believe in you agent!")
    print("-----------------------------------------------------------------------------------------------------------")

    while True:
        password = input("Enter password: ")
        feedback = validate_password(password)

        if not feedback:  # No feedback means the password is valid
            print("Access granted!")
            break
        else:
            print("Access denied. Here are some hints:")
            for message in feedback:
                print(f"- {message}")
    print(f"welcome to the super secret database, current user: {user.name}, clearance level: {user.skill_level}")
    print ("What would you like to acess?")
    import Deets
    
if __name__ == "__main__":
    main()