#Question_16_B_HL
#Enter your name here: Daniel O'Mahony

import random
from random import randint
print("Welcome to my shop")
total = 0
item_list = []
item_prices = []
#(i) creating a string input then appending it to item_list
#if the item is "Stop" it will break the loop and tally everything up and present it to the user
#otherwise it will continue the loop and show the current full price of the items
while True:
    userItem = input("Please enter the item: ")
    if userItem == "Stop":
        print("Your items are: ", item_list)
        print("The prices are: ", item_prices)
        print("Grand total £",sum(item_prices))
        break
    else:
        item_list.append(userItem)
        userPrice = float(input("Please enter the price of the item: "))
        item_prices.append(userPrice)
        print("The current total is ",sum(item_prices))
#(ii) using randint to get a random index of an item in the list
print("Your random item to be checked is: ", item_list[randint(0, len(item_list)-1)])

#(iii)sorting the list to find the highest and lowest value, then finding where that value was indexed in the original list.
#then im using that index to find the item in the orignal list correlated with that price
sortPrices = sorted(item_prices)
highestItemInd = item_prices.index(sortPrices[-1])
expItem = item_list[highestItemInd]
lowestItemInd = item_prices.index(sortPrices[0])
cheItem = item_list[lowestItemInd]
print("The most expensive item is:", expItem)
print("The cheapest item is: ", cheItem)



    
