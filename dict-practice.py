shoppingList = {
    "butcher": ["Chicken legs", "Chicken wings"],
    "food store": ["Cabbage", "Rice", "Bananas", "Oranges"],
    "Other": 'Spices'
}

#print(shoppingList["butcher"][1])

#print(shoppingList["Other"])

shoppingList["snacks"] = ['Chocolate', 'Walkers Crisps']

#print(shoppingList)

practice_dict = { 
    "London": "England", 
    "Edinburgh": "Scotland", 
    "Cardiff": "Wales", 
    "Belfast": "Northern Ireland" 
}

passwords = {
  'acebook' : {
    'password' : 'password123',
    'added_on' : '22/03/22',
  },
  'makersbnb' : {
    'password' : 'qwerty789',
    'added_on' : '22/03/22',
  }
}

passwords2 = [
  {'service' : 'acebook', 'password' : 'password123', 'added_on' : '22/03/22'},
  {'service' : 'makersbnb', 'password' : 'qwerty789', 'added_on' : '22/03/22'}
]

print(passwords2[0]['added_on'])

#print(practice_dict.keys())
#print(practice_dict.values())
#print(practice_dict.get('London'))
#print(practice_dict.items())
#print(practice_dict.pop('Belfast'))
#print(practice_dict.clear())
#print(practice_dict.setdefault('Edinburgh', 'Manchester'))
