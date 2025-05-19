x = input("what is the answer to the greatest question of life, the universe and everything? ")
match(x):
    case "42" | "forty two" | "forty-two":
        print("yes")
    case _:
        print("no")    

   
