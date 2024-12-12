import cowsay
# this part moves the story along with a simple if statement user input 
print ("Nuclear codes | Homework | Dastardly Plans | Destruct-Inator")
while True:
    Deets = input("")
    if Deets == "Nuclear codes":
        print("098462789103628933647")
    elif Deets == "Homework":
        print("Saucy content: sriracha, Barbecue, Mustard.")
    elif Deets == "Dastardly Plans":
        print("Evil cow")
        cowsay.cow('Mooooahahaha')
    elif Deets == "Destruct-Inator": # Phineas and Ferb reference
        print("A local evil mastermind with a very large nose and a hatred for semi aquatic egg laying mammals of action")
        print("has come up with a new invention that may be of interest to us, the Destruct-Inator, we will investigate")
        print("further once the device is fully operational, until that point we hope he will go far.")
    break
else:
    print("Unrecognized evil commands")

print("------------------------------------------------------------------------------------------------------")
print("Agent? Are you there, you must be in by now, remember once you have found incriminating evidence")
print("prepare to export with the command 'EXPORT'")
print("are you ready agent?")
export = input("Type 'yes' to export: ").strip().lower()
# this part shows that i can take a separate file from outside the program, read and write to this file, as a 'spy' you'd need this to escape with the info on a separate file
if export == "yes":
    with open('Extraction.txt', 'w') as file:
        file.write('Incriminating evidence')
        print("Incriminating evidence written to Extraction.txt!")

    with open('Extraction.txt', 'r') as file:
        content = file.read()
        print("Written info:")
        print(content)
else:
    print("Mission aborted!")