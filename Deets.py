import cowsay

print ("Nuclear codes | Homework | Darstardly Plans | Destruct-Inator")
while True:
    Deets = input("")
    if Deets == "Nuclear codes":
        print("098462789103628933647")
    elif Deets == "Homework":
        print("Saucy content: sriracha, Barbaque, Mustard.")
    elif Deets == "Darstardly Plans":
        print("Evil cow")
        cowsay.cow('Mooooahahaha')
    elif Deets == "Destruct-Inator":
        print("A local evil mastermind with a very large nose and a hatred for semi aquatic egg laying mamals of action")
        print("has come up with a new invention that may be of interest to us, the Destruct-Inator, we will investigate")
        print("further once the device is fully operational, untill that point we hope he will go far.")
    break
else:
    print("Unrecognised evil commands")

print("------------------------------------------------------------------------------------------------------")
print("Agent? Are you there, you must be in by now, remember once you have found incriminating evidence")
print("prepare to export with the command 'EXPORT'")
print("are you ready agent?")
export = input("Type 'yes' to export: ").strip().lower()

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