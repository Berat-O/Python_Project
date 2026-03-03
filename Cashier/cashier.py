#COUNTER
print("***WELCOME TO RAFEEQ DAIRY FARM***")
print()
print("ITEMS    PRICES\na.milk          100\nb.curd(sweet)   80\nc.curd(sour)    60\nd.khowa         320 \ne.ghee          560\nf.cream         200")
print()
def shop():
 item=input("enter the code of item you want: ")
 hm=float(input("enter the number of litres or kgs you want: "))
 print()
 if item=="a":
   m=hm*100
 elif item=="b":
   m=hm*80
 elif item=="c":
   m=hm*60
 elif item=="d":
   m=hm*3200
 elif item=="e":
   m=hm*560
 elif item=="f":
   m=hm*200
 else:
   print("invalid code")
 return m
n=int(input("how many items do you need: "))
lst=[]
print()
for i in range(n):
  lst.append(shop())
print(f"the total amount for {n} items is {sum(lst)} rupees")
print()
print("thanks for shopping with RDF!")
