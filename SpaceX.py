print('SpaceX	Odyssey')

#Prompt user to load BTC and save the value in integer
wallet = int(input("Load Wallet with BTC: "))

#Display available locations for user
print('Available locations are: abuja,spook,iss,moon,')

#Prompt user to input current location
location1 = input("Enter your current location: ")

#Display available destinations for user
print('Available destinations are: abuja,spook,iss,moon,')

#Prompt user to input destination
location2 = input("Enter your destination: ")

#Display available destinations for user
print('falcon1, falcon9')
#Prompt user to input desired spacecraft
spacecraft = input("Enter your desired spacecraft e.g falcon1 or falcon9") 
royalty = 200
fare1 = 250
fare9 = fare1 * 2

#Function to run if user takes Falcon 1
def falcon1(location1, location2):
    if (location1 == 'abuja' and location2 == 'spook') or (location1 == 'spook' and location2 == 'abuja'):
        charge = wallet - fare1
    if (location1 == 'abuja' and location2 == 'iss') or (location1 == 'iss' and location2 == 'abuja'):
        if location2 == 'iss':
            charge = wallet - (fare1 + royalty)
        else:
            charge = wallet - fare1
    if (location1 == 'abuja' and location2 == 'moon') or (location1 == 'moon' and location2 == 'abuja'):
        charge = wallet - fare1
    if (location1 == 'spook' and location2 == 'iss') or (location1 == 'iss' and location2 == 'spook'):
        if location2 == 'iss':
            charge = wallet - (fare1 + royalty)
        else:
            charge = wallet - fare1
    if (location1 == 'moon' and location2 == 'spook') or (location1 == 'spook' and location2 == 'moon'):
        charge = wallet - fare1
    if (location1 == 'iss' and location2 == 'moon') or (location1 == 'moon' and location2 == 'iss'):
        if location2 == 'iss':
            charge = wallet - (fare1 + royalty)
        else:
            charge = wallet - fare1
    return charge

def falcon9(location1, location2):
    if (location1 == 'abuja' and location2 == 'spook') or (location1 == 'spook' and location2 == 'abuja'):
        charge = wallet - fare9
    if (location1 == 'abuja' and location2 == 'iss') or (location1 == 'iss' and location2 == 'abuja'):
        if location2 == 'iss':
            charge = wallet - (fare9 + royalty)
        else:
            charge = wallet - fare9
    if (location1 == 'abuja' and location2 == 'moon') or (location1 == 'moon' and location2 == 'abuja'):
        charge = wallet - fare9
    if (location1 == 'spook' and location2 == 'iss') or (location1 == 'iss' and location2 == 'spook'):
        if location2 == 'iss':
            charge = wallet - (fare9 + royalty)
        else:
            charge = wallet - fare9
    if (location1 == 'moon' and location2 == 'spook') or (location1 == 'spook' and location2 == 'moon'):
        charge = wallet - fare9
    if (location1 == 'iss' and location2 == 'moon') or (location1 == 'moon' and location2 == 'iss'):
        if location2 == 'iss':
            charge = wallet - (fare9 + royalty)
        else:
            charge = wallet - fare9
    return charge

if spacecraft == 'falcon1':
    falcon1(location1, location2)
elif spacecraft == 'falcon9':
    falcon9(location1, location2)