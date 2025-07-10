import sys
import time

print("Welcome to band name generator!")
play_or_nah = input("Play or Nah?: ")

if play_or_nah == "y" or play_or_nah == "Y":
    print("Sick!")
    time.sleep(1)
else:
    print("Bye!")
    time.sleep(2)
    sys.exit(0)

favorite_location = input("Enter favorite location: ")
city_born = input("Enter the city you were born in: ")

time.sleep(1)
print(f"your band name is {favorite_location}{city_born}")
time.sleep(1)
sys.exit(0)

