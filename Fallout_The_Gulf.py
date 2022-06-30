# Main function: Calls all files and turns them into dictionaries that can then be called when necessaary
def main():
    #Makes initial empty dictionaries
    weapons_dict = {}
    armor_dict = {}
    equipement_dict = {}
    aid_dict = {}
    ammo_dict = {}
    inventory_dict = {}
    #Paths are kinda messed up for me, so cut it down for putting this on github, wont work on my computer though
    with open(r"\FalloutWeapons.csv", "r", encoding="utf-8") as weapons_csv:
        data = weapons_csv.read()
    #turn string into lists based on each new line
    rows = data.split("\n")
    for row in rows:
        value = row.split(",")
        #sets values to their name to keep code orderly and readable, but ,aybe think of better way to do this
        try:
            weap_name = value[0]
        except: weap_name = -1
        try:
            weap_damage = float(value[1])
        except: weap_damage = -1
        try:
            weap_accuracy = float(value[2])
        except: weap_accuracy = -1
        try:
            weap_range = float(value[3])
        except: weap_range = -1
        try:
            weap_ap = float(value[4])
        except: weap_ap = -1
        try:
            weap_weight = float(value[5])
        except: weap_weight = -1
        try:
            weap_mag_size = int(value[6])
        except: weap_mag_size = -1
        try:
            weap_ammo_type = value[7]
        except: weap_ammo_type = -1
        try:
            weap_durability = int(value[8])
        except: weap_durability = -1
        try:
            weap_crit_multiplier = float(value[9])
        except: weap_crit_multiplier = -1
        try:
            weap_crit_chance = float(value[10])
        except: weap_crit_chance = -1
        try:
            weap_attachement_1 = bool(value[11])
        except: weap_attachement_1 = -1
        try:
            weap_attachement_2 = bool(value[12])
        except: weap_attachement_2 = -1
        try:
            weap_type = value[13]
        except: weap_type = -1
        #adds weapon to weapon dictionary
        weapons_dict[weap_name] = [weap_damage, weap_accuracy, weap_range, weap_ap, weap_weight, weap_mag_size, weap_ammo_type, weap_durability, weap_crit_multiplier, weap_crit_chance, weap_attachement_1, weap_attachement_2, weap_type]

    #debug for main CURRENTLY CANT HAVE 2 OF THE SAME ITEM might make it so you can pick up new weapons to increase the durability of yours
    add_to_inventory(weapons_dict, inventory_dict, "10mm revolver")
    add_to_inventory(weapons_dict, inventory_dict, "10mm revolver")
    add_to_inventory(weapons_dict, inventory_dict, "10mm auto pistol")
    print(inventory_dict)
#    print_inventory(inventory_dict, weapons_dict)
# Dialogue function: contains a system to connect dialogue to different npcs and encounters, and order dialogue trees. find a way to order
# dialogue trees and maybe put all dialugue saved in another function


# Inventory functions: adds and takes away gear from inventory, might call all dictionaries, calling for now, might change dictionaries to 
# global values later. If youre gonna keep calling dictionaries ADD NEW ONES
def add_to_inventory(weapons_dict, inventory_dict, added_item):
#    for item in weapons_dict:
    if added_item in weapons_dict:
        #should make script to fill up a weapons durability a certain percent every time you picl up a duplicate. also need to make a script 
        # to randomize durability of weapons found
        inventory_dict[added_item] = weapons_dict[added_item]

#Function to print out all items currently in inventory and some data for each one in a table, for example the name, ammo, damage, ap.
#find function you used to make orderly lists and use that here.
def print_inventory(inventory_dict, weapons_dict):
    stop_weap_print = 0 
    #should put all printouts at end eventually. if there is any of an item prints this header for each type, then the different items of this
    #type.
    for item in inventory_dict:
        printout_list = []
        if item in weapons_dict:
            # moves dictionary to list so each variable can be printed out, also adds headings to each shown section of a weapons stats, 
            # change this to use a for statement
            if stop_weap_print == 0:
                WEAP_PRINTOUT = ["Weapon:", "Damage:", "Accuracy:", "Range:", "AP:", "Weight:", "Magazine:", "Ammo:", "Condition:"]
                print(WEAP_PRINTOUT)
                stop_weap_print += 1
            printout_list.append(item)
            printout_list.extend(inventory_dict[item]) 
            for attribute in range(5):
                printout_list.pop()
            print(printout_list)
# Debug thing to see what all is working.
#            print(item, printout_list[1], printout_list[2], printout_list[3], printout_list[4], printout_list[5], printout_list[6], printout_list[7])


# Equip gear function: equips gear and updates combat and other functions based on that. Should search for whether an item is a weapon, armor, 
# etc then add the key/name of that items dictionary to the coresponding "item"_equipped variable.


# Combat system: takes equipped item varibles and searches inventory for those items, and takes away durability when used, updates damage etc


# Save system: saves progress to another file (location, inventory, equipped gear, XP, perks, stats, etc)


# Roll Stats: S.P.E.C.I.A.L selection


# Select name and stuff


# Travel function: updates coordinate matrix and allows character to travel to different locations based on coordinates. any time plaer moves 
# rolls for encounter, or has set encounter depending on location moving to.


# Base UI function: Shows SPECIAL stats, AP, carry weight, armor, weapon, DT, etc and what commands can be entered


# Call to main
#main()


#notes, potential program implementations, etc:
    #list function to turn lists of data into dictionaries
#list1 = [4, 3, 2]
#list2 = [6, 7, 8]
#lists = { }
#for i in range(len(list1)):
#	lists[list1[i]] = list2[i]