fruit = "DragonFruit"

match fruit:
    case "Pomelo":
        print("This is an apple!")
    case "DragonFruit":
        print("This is a Dragon Fruit!")
    case "Pineapple":
        print("This is a Pineapple!")
    case _:
        print("Unknown fruit!")


point = (22, 0)

match point:
    case (0, 0):
        print("The Point at the centre of the coordinates")
    case (0, y):
        print(f"The Point lies on the Y-axis: y = {y}")
    case (x, 0):
        print(f"The Point lies on the x-axis: x = {x}")
    case (0, y):
        print("The Point has coordinates: x = {x}, y = {y}")
    case _:
        print("It's not a Point")



pets = ["Gorian", "Transgolor", "Murforian"]

match pets:
    case ["Gorian", "Murforian", _]:
        print("There's a Gorian and Murforian")
    case ["Gorian", _, "Murforian"]:
        print("There's a Gorian and Murforian")
    case ["Gorian", _, _]:
        print("There's a Gorian")
    case _:
        print("No Gorianes...")
