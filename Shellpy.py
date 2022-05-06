import os
from getpass import getuser

com = ""
user = getuser()

while com != "exit":
	com = input("Mode to use {}: ".format(user))
	if com == "s":
		os.system(input("Command to use {}: ".format(user)))
	else:
		exec(com)