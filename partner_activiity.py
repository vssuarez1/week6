#Partner activity.. Names: Malik Hreish, Vanessa Suarez
school = {
    "class": {
        "name": "Math 101",
        "students": {"student1": "A", "student2": "B", "student3": "C"}
    }
}


# Update the grade of student2
school["class"]["students"]["student2"] = "A+"


#Find the student who is making an A and upgrade it to an A +
print(school["class"]["students"]["student1"]) 

 #Define the dictionary
product_inventory = {
    "warehouse1": {
        "products": ["apples", "oranges", "bananas"],
        "quantities": [50, 30, 20]
    },
    "warehouse2": {
        "products": ["grapes", "pears", "peaches"],
        "quantities": [60, 40, 30]
    }
}


# Find the total number of oranges in warehouse1
print(product_inventory["warehouse1"]["quantities"][1])

#Sum up all the quantities in the warehouse
apples = product_inventory["warehouse1"]["quantities"][0]
oranges = product_inventory["warehouse1"]["quantities"][1]
bananas = product_inventory["warehouse1"]['quantities'][2]
grapes = product_inventory["warehouse2"]["quantities"][0]
pears = product_inventory["warehouse2"]["quantities"][1]
peaches = product_inventory["warehouse2"]["quantities"][2]
sum = apples + oranges + bananas + grapes + pears + peaches
print(sum)
