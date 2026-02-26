""" count = 1

while count <= 5:
    print("This is loop number", count)
    count = count + 1 """

""" order = ""

while order != "done":
    order = input("What would you like to order? (type 'done' to finish): ")

print("Thanks for your order!") """

""" count = 10
while count >= 1:
    print("this is number", count)
    count = count - 1 """
""" 
color =""
while color != "stop":
    color = input("What is your favorite color? (type stop to finish)")
print("Cool Color!") """

import random
randomnumber = random.randint(1,10)
def game():
    gtn = 0
    while gtn != randomnumber:
        list = []
        for i in range (gtn):
            gtn = int(input("Enter Number:"))
            list.append(gtn)
            print ("Wrong guesses:", list)
            if gtn > randomnumber:
                print ("Too High")
            elif gtn < randomnumber:
                print ("Too Low")
            elif gtn == randomnumber:
                print ("You Win!!!") 
game()











