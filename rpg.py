##Exc1.

inventory = {
    "gold" : 500,
    "pouch" : ["flint", "twine", "gemstone"],
    "backpack" : ["xylophone", "dagger", "bedroll", "bread loaf"]
}

inventory["pocket"] = ["seashell", "strange berry", "lint"]
print (inventory)

inventory["backpack"].sort()
print (inventory["backpack"])

inventory["backpack"].remove("dagger")
print (inventory["backpack"])

inventory["gold"] += 50
print (inventory)

fruitshop = {
    "banana":{
        "price":4,
        "stock": 6},
    "apple":{
        "price": 2,
        "stock": 0},
    "orange":{
        "price": 1.5,
        "stock": 32},
    "pear":{
        "price": 3,
        "stock": 15}
    }

for key,value in fruitshop.items():
    print ("{}:".format(key), value)

##Exc2
total = 0
for value in fruitshop.values():
    total += value["price"]*value["stock"]

fruitshop = {
    "banana":{
        "price":4,
        "stock": 6},
    "apple":{
        "price": 2,
        "stock": 0},
    "orange":{
        "price": 1.5,
        "stock": 32},
    "pear":{
        "price": 3,
        "stock": 15}
    }
print (total)

##Exc3
food_list = ["banana", "orange", "apple"]

def compute_bill(foodlist):
    total = 0

    for food in foodlist:

        if fruitshop[food]["stock"] > 0:

            total += fruitshop[food]["price"]

            fruitshop[food]["stock"] -= 1

    return total, fruitshop

print (compute_bill(food_list))

