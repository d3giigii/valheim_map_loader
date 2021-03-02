#!/usr/bin/env python

"""Simple map loading script for valheim dedicated servers.
"""

map_dict = {1: "equinox", 2:"torchlight"}
batch_file_content = """@echo off
set SteamAppId=892970

echo "Starting server PRESS CTRL-C to exit"

REM Tip: Make a local copy of this script to avoid it being overwritten by steam.
REM NOTE: Minimum password length is 5 characters & Password cant be in the server name.
REM NOTE: You need to make sure the ports 2456-2458 is being forwarded to your server through your local router & firewall.

valheim_server -nographics -batchmode -name {} -port {} -world {} -password {}
"""

num_maps = map_dict.__len__() + 1

print("Valheim Map Loader")
while(True):
    print("\nSelect from the following menu.")
    for i in range(1, num_maps):
        print("\t{}. Load {}.".format(i, map_dict[i]))
    print("\t0. Exit application")

    try:
        choice_int = int(input("Selection: "))
        print("You selected {}.".format(choice_int))
    except ValueError:
        print("Invalid input. Please try again")
        continue

    if choice_int == 0:
        print("Thanks for using this application!")
        break

    if choice_int in map_dict.keys():
        world_name = map_dict[choice_int]
        file = open("server_start.bat", "w")

        server_name = "Dedicated"
        port = 2456
        password = "secret"

        file.write(batch_file_content.format(server_name, port, world_name, password))
        file.close()