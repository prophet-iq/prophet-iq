# -*- coding: utf-8 -*-
"""
Created on Fri May 12 11:07:25 2023

@author: Matt
"""
# Create the Account class
class Account:
        def __init__(self):
            self.balance=0
            print("Hello! Please make a deposit or withdraw")
 
        def deposit(self):
            amount=float(input("Enter amount to be Deposited: "))
            self.balance += amount
            print("\n Amount Deposited:",amount)
 
        def withdraw(self):
           amount = float(input("Enter amount to be Withdrawn: "))
           if self.balance>=amount:
              self.balance-=amount
              print("\n You withdrew: $",amount)
           else:
              print("\n Insufficient funds for withdraw!")
        
        def display(self):
            print("\n Available Balance=",self.balance)
            
# User Code -- placeholder "u"
u = Account()

u.deposit()
u.withdraw()
u.display()

# How would you maintain the balance between multiple runs?
# How would you prompt additional deposits or withdraws?
# In welcome, add user.name for more personable approach
