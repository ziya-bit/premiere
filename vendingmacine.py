product = {
    "Chips": 1.5, "Soda": 1.25, "Candy": 0.75, "Water": 1.0, "Chocolate": 1.75, "Gum": 0.5
    }
def displayproduct():
    counter=1
    for name,price in product.items():
        if(len(name)<8):
            print(f"{counter}. name:{name} \t\t price:{price}")
        else:
            print(f"{counter}. name:{name} \t price:{price}")
        counter+=1
def total(selectedproducts):
    total=0
    for price in selectedproducts:
        total+=price
    return total
def startvendingmachine():
   print("welcome to z.vend machine ⊹")
   displayproduct()
   selectedproduct=[]
   productprices=list(product.values())
#    print(productprices)
   select=int(input("picka produkt 1-6: "))
   selectedproduct.append(productprices[select-1])
   
   print(selectedproduct)
startvendingmachine()
   
