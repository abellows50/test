import stock
import os
import datetime

class User:
    def __init__(self,user):
        created = False
        try:
            # with open(f"{os.getcwd()}/programFiles/{user}.logf","r") as userFile:
            with open(f"{os.getcwd()}\\programFiles\\{user}.logf","r") as userFile:
                userData = userFile.readlines()

        except:
            # with open(f"{os.getcwd()}/programFiles/template.logf","r") as template:
            with open(f"{os.getcwd()}\\programFiles\\template.logf","r") as template:
                with open(f"{os.getcwd()}/programFiles/{user}.logf","w") as userFile:
                    templateData = template.read()
                    userFile.write(templateData)
                    userData = templateData.split("\n")
                    created = True

        bank = userData[0][:-1].split(",")[:2] #contains the users total money
        dates = userData[0][:-1].split(",")[2:-1] #gets the dates of last use

        stocks = [stockrow.split(",")[:2] for stockrow in userData[1:]] #extracts the stocks (this is number,stock)
        
        for mystock in range(len(stocks)): #Convert all str's to int
            stocks[mystock][0] = int(stocks[mystock][0])

        self.money = int(bank[1])
        self.worth = self.money
        self.stocks = {}
        if not created:
            for mystock in stocks:
                stockSearch = stock.makeSearch(mystock[1])
                if stockSearch[1] != 'USD':
                    stockPrice = int(input(f"Your stock {mystock[1]} has its price in {stockSearch[1]} please convert {stockSearch[0]} {stockSearch[1]} to USD"))
                else:
                    stockPrice = stockSearch[0]
                self.worth += stockPrice * mystock[0]
                self.stocks[mystock[1]] = [stockPrice,mystock[0]]
        self.printToUser()
        self.userInteractive()
                
    def printToUser(self):                
        print(f"Your Net Worth: {self.worth}")
        print(f"Your Free Money: {self.money}")
        print(f"Your Stock Holdings:")
        print("stock:[shares,price]")
        for key in self.stocks.keys():
            print(f"{key}:{self.stocks[key]}")

    def exit(self):
        pass

    def buy(self):
        purchase = input("stock to buy>> ")
        try:
            purchaseData = stock.makeSearch(purchase)
            if purchaseData[1] != 'USD':
                stockPrice = int(input(f"Your stock {purchase} has its price in {purchaseData[1]} please convert {purchaseData[0]} {purchaseData[1]} to USD"))
            else:
                stockPrice = int(purchaseData[0])
            
            if input(f"{purchase} costs {stockPrice} USD. continue? [y/n]>> ") == "y":
                shares = int(input("how many shares do you want to buy>> "))
                if self.worth - stockPrice *shares < 0:
                    print("ERR: not enough money to procede")
                else:
                    if input(f"buy {shares} [y/n]>> ") == "y":
                            self.worth -= stockPrice
                            self.stocks[purchase] = [shares,stockPrice]
                            print(f"bought {shares} shares of {purchase} at {stockPrice}. net worth is now {self.worth}")
                            print(self.stocks)
        except:
            print("ERR: stock not found")
        

    def sell(self):
        pass

    def graph(self):
        pass

    def userInteractive(self):
        print("MAIN LOOP NOW RUNNING. To exit type \"exit\", to buy stock type \"buy\", to sell stock type \"sell\", to show graph type \"graph\"")
        while True:
            userDesire = input(">>")
            if userDesire == "exit":
                self.exit()
                break
            elif userDesire == "buy":
                self.buy()
            elif userDesire == "sell":
                self.sell()
            elif userDesire == "graph":
                self.graph()
        
        

# with open("programFiles/users.csv") as users:
#     myUsers = user.readlines()
#     myUsers = [u.split(",") for u in myUsers]
#     file = False
#     for auser in myUsers:
#         if auser[0] == user:
#             myPass = input("Password")
#             if myPass == auser[1]:
#                 file = auser[2]
#                 break
#     if not file:
#         myUsers.append("")     
     

theuser = User("Abel")

