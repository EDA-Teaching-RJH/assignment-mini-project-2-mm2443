def main():

    import re

    print("Welcome agent, today's mission is a simple one, no exploding cars or airplane dogfights unlike yesterday.")
    print("You will not even have to leave your house. We need you to infiltrate 'the database'")
    print("A super-secret organization with TOP security. No worries for you though,")
    print("I don't even need to tell you how to get in! I believe in you agent!")
    print("-----------------------------------------------------------------------------------------------------------")

    rules = {
        "Password must start with 'p'": r"^p.*[A-Z]|^P",
        "Password must end with 'd'": r"[dD]$",
        "Password must contain at least one digit": r"\d",
        "Password must include an uppercase letter": r"[A-Z]"
    }

    while True:
        password = input("Enter password: ")

        pattern = r"(^p.*[A-Z\d].*[dD]$)|(^P.*\d.*[dD]$)"
        if re.match(pattern, password):
            print("Access granted!")
            break
        else:
            feedback = []
            for hint, rule_pattern in rules.items():
                if not re.search(rule_pattern, password):
                    feedback.append(hint)

            print("Access denied. Here are some hints:")
            for message in feedback:
                print(f"- {message}")

if __name__ == "__main__":
    main()