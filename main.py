######https://github.com/Flexen21#####
######https://github.com/Flexen21#####
######https://github.com/Flexen21#####
######https://github.com/Flexen21#####
######https://github.com/Flexen21#####
######https://github.com/Flexen21#####
######https://github.com/Flexen21#####
######https://github.com/Flexen21#####
######https://github.com/Flexen21#####
######https://github.com/Flexen21#####
######https://github.com/Flexen21#####
######https://github.com/Flexen21#####
######https://github.com/Flexen21#####
######https://github.com/Flexen21#####
######https://github.com/Flexen21#####
######https://github.com/Flexen21#####
######https://github.com/Flexen21#####
######https://github.com/Flexen21#####
######https://github.com/Flexen21#####
######https://github.com/Flexen21#####
######https://github.com/Flexen21#####
import json
import time
import requests
import os
import colorama

from colorama import Back, Fore, Style

os.system("title PyTracker V1.0 https://github.com/Flexen21")


print(Fore.YELLOW + "██████╗░██╗░░░██╗████████╗██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░")
print(Fore.YELLOW + "██╔══██╗╚██╗░██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗")
print(Fore.YELLOW + "██████╔╝░╚████╔╝░░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝")
print(Fore.YELLOW + "██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗")
print(Fore.YELLOW + "██║░░░░░░░░██║░░░░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║")
print(Fore.YELLOW + "╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝")
print(Fore.WHITE + ".")                                           
 



target_ip = input("Whats The Target Ip:" )
api = "http://ip-api.com/json/" 


res = requests.get(api + target_ip)

data = res.json()

print(Fore.RED + "Ip country is: ", data["country"])
print(Fore.GREEN + "City is: ", data["city"])
print(Fore.YELLOW + "CountryCode: ", data["countryCode"])
print(Fore.BLUE + "Zip", data["zip"])
print(Fore.MAGENTA + "Org", data["org"])
print(Fore.RED + "Lat", data["lat"])
print(Fore.GREEN + "As", data["as"])
print(Fore.YELLOW + "Isp", data["isp"])
print(Fore.BLUE + "RegionName", data["regionName"])
print(Fore.MAGENTA + "Region", data["region"])
print(Fore.GREEN + "Status", data["status"])
print(Fore.WHITE + ".")

print(Fore.MAGENTA + "https://github.com/Flexen21")

print(Fore.RED + "press Ctrl+c to stop run")
time.sleep(100000)
