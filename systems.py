import random

def play_game():
    year = 1
    population = 100
    bushels = 2800
    acres = 1000
    price = 20
    dead_total = 0
    
    # A small introduction to the setting of the game before it begins
    print("Welcome to Gildegar. You are the ruler of a small but growing city of Gildegarans.")
    print("Your task is to manage the city's resources wisely over the next several years.")
    print("You will need to buy and sell land, feed your people, and plant crops to ensure the prosperity of your kingdom. And I, your trusted Advisor Revalto will provide guidance and counsel throughout your reign.")
    
    while year <= 10:
        print(f"\n--- Year {year} ---")
        print(f"Population: {population}")
        print(f"Bushels in storage: {bushels}")
        print(f"Acres owned: {acres}")
        print(f"Land price: {price} bushels/acre")

        try:
            land_action = int(input("How many acres to buy/sell (+/-)? "))
            if land_action * price > bushels:
                print("Not enough grain!")
                continue
            acres += land_action
            bushels -= (land_action * price)
        except ValueError:
            print("Invalid input.")
            continue

        try:
            feed = int(input("Bushels to feed people? "))
            if feed > bushels:
                print("Not enough grain!")
                continue
            bushels -= feed
        except ValueError:
            print("I'm... not sure what you mean sire?")
            continue

        try:
            planted = int(input("Acres to plant with seed? "))
            if planted > acres:
                print("You lack the proper amount of Acres to do this!")
                continue
            if planted > bushels:
                print("Sire, we need more grain to plant!")
                continue
            bushels -= planted
        except ValueError:
            print("I'm... not sure what you mean sire?")
            continue


        if starved > 0:
            print("Sire, your people are hungry. Think more for them rather than yourself!")
        elif harvest < planted * 2:
            print("Pah! Such a measly yield! Surely you aren't trying to sabotage your own farms...")
        else:
            print("Magnificent! I daresay no-one in the kingdom will doubt your qualifications to lead!")

        rats = random.randint(0, 500)
        bushels = max(0, bushels - rats)
        
        harvest = planted * random.randint(1, 5) 
        bushels += harvest
    
        fed = feed // 20 
        starved = max(0, population - fed)
        dead_total += starved
        population = max(0, population - starved)
        
        if starved > 0:
            print(f"{starved} people starved. Keep it up and you'll witness revolution...")
        else:
            population += random.randint(1, 10)
        
        price = random.randint(17, 26)
        
        if starved > population * 0.45:
            print("Your people had too much of your lax leadership and have overthrown you!")
            return
            
        year += 1

    print(f"\nGame Over. You managed your city for 10 years!")
    print(f"Final population: {population}")
    print(f"Total dead: {dead_total}")
    print(f"Bushels in storage: {bushels}")
    print(f"Acres owned: {acres}")

if __name__ == "__main__":
    play_game()
