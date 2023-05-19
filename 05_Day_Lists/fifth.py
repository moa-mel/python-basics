empty_list = list()
print(len(empty_list))

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
animal_products = ['milk', 'meat', 'butter', 'yoghut']
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:', animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]
print(first_fruit)
second_fruit =fruits[1]
print(second_fruit)
last_fruit =fruits[3]
print(last_fruit)
last_index = len(fruits)-1
last_fruit = fruits[last_index]

fruits = ['banana', 'orange', 'mango', 'lemon']
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)
print(second_last)

#slicing items
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]
print(all_fruits)
all_fruits = fruits[0:]
print(all_fruits)
some_fruits = fruits[:3]
print(some_fruits)
orange_and_mango = fruits[1:3]
print(orange_and_mango)
orange_mango_lemon = fruits[-3:]
print(orange_mango_lemon)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'Avocado'
print(fruits)
fruits[1] = 'apple'
print(fruits)
last_index = len(fruits) -1 
fruits[last_index] = 'lime'
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)
does_exist = 'lime' in fruits
print(does_exist)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')
print(fruits)
fruits.insert(3, 'lime')
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
fruits.remove('lemon')
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]
print(fruits)
#clear
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)
