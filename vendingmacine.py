product = {
    "Chips": 1.5, "Soda": 1.25, "Candy": 0.75, "Water": 1.0, "Chocolate": 1.75, "Gum": 0.5,
    "Lemonade": 1.0, "Juice": 1.25, "Tea": 1.0, "Coffee": 1.5, "Peanuts": 1.25, "Granola Bar": 1.0,
    "Cookies": 1.25, "Muffin": 1.5, "Popcorn": 1.0, "Energy Drink": 2.0, "Ice Cream": 2.5,
    "Milk": 1.25, "Watermelon": 1.5, "Apple": 1.0, "Orange": 1.0, "Banana": 1.0, "Pineapple": 2.0,
    "Carrot Sticks": 1.0, "Celery": 1.0, "Yogurt": 1.5
}

def displayproduct():
    counter=1
    for name,price in product.items():
        if(len(name)<6):
            print(f"{counter}. name:{name} \t\t\t price:{price}")
        elif(len(name)<15):
            print(f"{counter}. name:{name} \t\t price:{price}")
        else:
            print(f"{counter}. name:{name} \t price:{price}")
        counter+=1
def totalz(selectedproducts):
    total=0
    for price in selectedproducts:
        total+=price 
    return total
    
selectedproduct=[]

def startvendingmachine():
   print("welcome to z.vend machine ⊹")
   displayproduct()
   productprices=list(product.values())
#    print(productprices)
   select=int(input(f"picka produkt 1-{len(product)}: "))
   selectedproduct.append(productprices[select-1])
   
   buymoreyorn=input("wanna buy more?y/n: ")

   if buymoreyorn=="y":
        startvendingmachine()
   else:
        print(f"list of what u buy:{selectedproduct}")
        print(f"total:{totalz(selectedproduct)}")
        exit
        

startvendingmachine()   


   
