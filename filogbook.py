#Author: Natalie Niemeir
#Date: 1/6/2021
#Simple financial logbook to keep track of money earned/spent fairly conveniently 
import os
from os.path import exists
from datetime import datetime
while True:
  WALLET_CHOICE = input("1. New Wallet\n2. Add/Subtract From Existing Wallet\n3. Delete Existing Wallet\n4. View Existing Wallet Log\n")
  cwd = os.getcwd()
  file_exists = exists("CB.txt")
  if WALLET_CHOICE == "1":
    file_exists = exists("CB.txt")
    if file_exists == True:
        print("Wallet already exists")
    else:
      #CB.txt is opened in write mode and user input is written to it
      #Same input is written in a more readable format to the log
      WALLET_FILE = open("CB.txt", "x")
      INITIAL_BALANCE = input("Enter Balance:\n")
      WALLET_FILE.write(INITIAL_BALANCE)
      FIRSTENTRY = open("LOG.txt", "a")
      FIRSTENTRY.write("\n Initial Balance Set to $" + INITIAL_BALANCE)
      FIRSTENTRY.close()
      print("Wallet Created")
    quit()
  elif WALLET_CHOICE == "2":
    file_exists = exists("CB.txt")
    if file_exists == True:
        print("")
    else:
        print("Wallet Does Not Exist")
        quit()
  elif WALLET_CHOICE == "3":
    #If balance file exists, it is deleted along with the log file
    if file_exists == True:
      os.remove("CB.txt")
      os.remove("LOG.txt")
      print("Wallet Deleted")
      quit()
    else:
      print("Wallet Does Not Exist")
      quit()
  elif WALLET_CHOICE == "4":
    if file_exists == True:
      logdisplay = open("LOG.txt", "r")
      s = logdisplay.read()
      print(s)
      logdisplay.close()
      quit()
    else:
      print("Wallet Does Not Exist")
      quit()
  else:
    print("Invalid Choice")
    quit()
  #CB.txt is read into variable c
  with open ("CB.txt", "r") as myfile:
    c=myfile.readlines()
    line_number = 1
    a = 0
    BALANCE = ''
    #If CB.txt is empty, nothing happens
    for b in c:
      if a > line_number:
        break
      else:
        #The first line is written into the BALANCE variable
        if a == line_number-1 and b != '\n':
          BALANCE += b
        elif b == '\n':
          a += 1
  print("Current Balance is $" + BALANCE)
  BALANCE_CHANGE = input("Enter amount to change balance by\n")
  #Variables are converted to floats for calculation
  NEW_BALANCE = float(BALANCE) + float(BALANCE_CHANGE)
  DESCRIPTION = input("Reason for change?\n")
  print("Your new balance is $" + str(NEW_BALANCE))
  #New balance replaces the old one in the balance file
  BC = open("CB.txt", "rt")
  change = BC.read()
  change = change.replace(str(BALANCE), str(NEW_BALANCE))
  BC.close()
  BC = open("CB.txt", "wt")
  BC.write(change)
  BC.close()
  #Date and time written to REGIONAL_TIME using Datetime module
  now = datetime.now()
  REGIONAL_TIME = now.strftime("%m/%d/%Y %H:%M:%S")
  #New line containing details of balance change added to log file
  log = open("LOG.txt", "a")
  log.write("\n " + REGIONAL_TIME +  " | Balance changed by $" + BALANCE_CHANGE + " | Description: " + DESCRIPTION + " | New Balance: $" + str(NEW_BALANCE))
  log.close()
  quit()
