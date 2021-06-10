print(f" ** Welcome to Relaince Fresh **\n ")
print(f" the Availbale items ")
rfset = {"oil","soap","cookies","vegetables","friuts"}
print("\n 1.oil\n 2.soap\n 3.cookies\n 4.vegetables\n 5.fruits")

def rf(n):
    if(n=="oil"):
        print(f' Thank you purchasing Oil')
        rfset.remove("oil")
        print("the updated available items: \n",rfset)
    elif(n=="soap"):
        print(f' Thank you purchasing Soap')
        rfset.remove("soap")
        print("the updated available items: \n",rfset)
    elif(n=="cookies"):
        print(f' Thank you purchasing Cookies')
        rfset.remove("cookies")
        print("the updated available items: \n",rfset)
    elif(n=="vegetables"):
        print(f' Thank you purchasing Vegetables')
        rfset.remove("vegetables")
        print("the updated available items: \n",rfset)
    elif(n=="fruits"):
        print(f' Thank you purchasing Fruits')
        rfset.remove("fruits")
        print("the updated available items: \n",rfset) 
    else:
        print('the item you entered is not available currently')
    
print(f"\n Enter the items to purchase: ")
k=input()
rf(k)
    