import string
import random

characters = string.digits + string.punctuation + string.ascii_letters # the combination of characters that will be used to make the password
length = 12 #number of letters
password = ""
for i in range(length):
  random_character = random.choice(characters) #randomly choosing one character from the combination we made
  password = password + random_character #adding chosen random character to password
print("Your random password is:", password)#printing the 12-digit password after the loop iterates 12 times and adds something to password each time
