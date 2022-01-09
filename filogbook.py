#Author: Natalie Niemeir
#Date: 1/6/2021
#FiLogbook
#Simple financial logbook to keep track of money earned/spent fairly conveniently 
import os
from os.path import exists
from datetime import datetime
while True:
  log_choice = input("1. New Logbook\n2. Add/Subtract From Existing Logbook\n3. Delete Existing Logbook\n4. View Existing Logbook\n")
  file_exists = exists("CB.txt")
  if log_choice == "1":
    file_exists = exists("CB.txt")
    if file_exists == True:
        print("Logbook already exists")
    else:
      #CB.txt is opened in write mode and user input is written to it
      #Same input is written in a more readable format to the log
      log_file = open("CB.txt", "x")
      initial_balance = input("Enter Balance:\n")
      log_file.write(initial_balance)
      first_entry = open("LOG.txt", "a")
      first_entry.write(f"\n Initial Balance Set to ${initial_balance}")
      first_entry.close()
      print("Logbook Created")
    quit()
  elif log_choice == "2":
    file_exists = exists("CB.txt")
    if file_exists == True:
        print("")
    else:
        print("Logbook Does Not Exist")
        quit()
  elif log_choice == "3":
    #If balance file exists, it is deleted along with the log file
    if file_exists == True:
      os.remove("CB.txt")
      os.remove("LOG.txt")
      print("Logbook Deleted")
      quit()
    else:
      print("Logbook Does Not Exist")
      quit()
  elif log_choice == "4":
    if file_exists == True:
      logdisplay = open("LOG.txt", "r")
      s = logdisplay.read()
      print(s)
      logdisplay.close()
      quit()
    else:
      print("Logbook Does Not Exist")
      quit()
  else:
    print("Invalid Choice")
    quit()
  #CB.txt is read into variable c
  with open ("CB.txt", "r") as myfile:
    current_balance_file=myfile.readlines()
    line_number = 1
    empty_file = 0
    balance = ''
    #If CB.txt is empty, nothing happens
    for new_lines in current_balance_file:
      if empty_file > line_number:
        break
      else:
        #The first line is written into the balance variable
        if empty_file == line_number-1 and new_lines != '\n':
          balance += new_lines
        elif new_lines == '\n':
          empty_file += 1
  print(f"Current Balance is ${balance}")
  balance_change = input("Enter amount to change balance by\n")
  #Variables are converted to floats for calculation
  new_balance = float(balance) + float(balance_change)
  description = input("Reason for change?\n")
  print(f"Your new balance is ${new_balance}")
  #New balance replaces the old one in the balance file
  balance_replacement = open("CB.txt", "rt")
  change = balance_replacement.read()
  change = change.replace(str(balance), str(new_balance))
  balance_replacement.close()
  balance_replacement = open("CB.txt", "wt")
  balance_replacement.write(change)
  balance_replacement.close()
  #Date and time written to regional_time using Datetime module
  now = datetime.now()
  regional_time = now.strftime("%m/%d/%Y %H:%M:%S")
  #New line containing details of balance change added to log file
  log = open("LOG.txt", "a")
  log.write(f"\n {regional_time} | Balance changed by ${balance_change} | Description: {description} | New Balance: ${new_balance}")
  log.close()
  quit()