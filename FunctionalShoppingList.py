#!/usr/bin/env python3
"""evelandy/W.G.
Aug. 15 2018 4:32pm
ShoppingList
Python36-32
appends data into a list 
"""
import os

shop_list = []

def clear_scrn():
  os.system('cls' if os.name == 'nt' else 'clear')
  

def help():
    clear_scrn()
    print("To add to the list just type each item... ")
    print("""
Enter help to get help at any time
Enter rem to delete an item from the list
Enter show to show list
Enter q to quit
""")


def add_list(item):
    show_list()
    if len(shop_list):
      position = input("Where should I add {}?\n"
                       "Press enter to add to end of the list\n"
                       "> ".format(item))
    else:
      position = 0
      
    try:
      position = abs(int(position))
    except ValueError:
      position = None
    if position is not None:
      shop_list.insert(position-1,item)
    else:
      shop_list.append(item)

    show_list()

    
def show_list():
    clear_scrn()
    print("List items: ")
    
##    index=1
##    for item in shop_list:
##        print("{}. {}".format(index,item))
##        index += 1
    for index, item in enumerate(shop_list, start=1):
      print("{}. {}".format(index, item))

    print("-"*16)


def rem_list():
    show_list()
    rem_what = input("What item would you like to delete?\n> ")
    try:
      shop_list.remove(rem_what)
    except ValueError:
      pass
    
    
help()
while True:
    item = input("> ")

    if item.lower() == "q":
        break
    elif item.lower() == 'help':
        help()
        continue
    elif item.lower() == 'show':
        show_list()
        continue
    elif item.lower() == 'rem':
        rem_list()
    else:
        add_list(item)

show_list()
