import os
import json
from cake_model import Cake


database = "bakery.json"

cakes = []
paresedData = []


def read_data():
    if not os.path.exists(database):
        return{}
    with open(database, 'r') as file:
        return json.load(file)
    

def write_data(cakes):
    with open(database, 'w') as file:
        for cake in cakes:
            paresedData.append(Cake.to_json(cake))
        json.dump(cakes, file, indent=4)

def add_cake():
    print("Enter which cake you want to add: ")
    name = input()
    print("Enter which flavour you want: ")
    flavour = input()
    print("Enter the size: ")
    size = int(input())
    print("Enter the shape: ")
    shape = input()
    storage = [name, shape, flavour, size]
    write_data(storage)

    cakes.append(Cake(name=name,shape=shape,flavour=flavour,size=size))


def view_detail():
    print("__Details of Bakery__")
    for index, cake in cakes:
        print(f"{index + 1}.{cake.name}\t{cake.flavour}\t{cake.shape}\t{cake.size}")

def main():
    print("-__BAKERY SYSTEM__")
    print("Choose options:\n1.Add Cake\n2.View Details")
    user_select = int(input())

    if user_select == 1:
        add_cake()
    elif user_select == 2:
        view_detail()


main()