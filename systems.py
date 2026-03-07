# Systems module for Hammurabi game
import random


class Hammurabi:
    
    def __init__(self):
        self.year = 1
        self.population = 100
        self.acres = 1000
        self.bushels = 2800
        self.harvest = 0
        self.land_price = 20

    def next_year(self):
        self.year += 1
        self.land_price = 20 + (self.year % 10) * 2
        self.harvest = self.acres * 2
        self.bushels += self.harvest
        pass

    def display_status(self):
        print(f"Year: {self.year}")
        print(f"Population: {self.population}")
        print(f"Acres: {self.acres}")
        print(f"Bushels: {self.bushels}")
        print(f"Harvest: {self.harvest}")
        print(f"Land Price: {self.land_price}")

        # Build the advisor character who offers guidance to the player and slowly becomes snarkier or begins to respect you more the better the kingdom is doing
        self.advisor_mood = "neutral"

    def update_advisor_mood(self):
        if self.bushels > 5000 and self.population > 200:
            self.advisor_mood = "respectful"
        elif self.bushels < 1000 or self.population < 50:
            self.advisor_mood = "snarky"
        else:
            self.advisor_mood = "neutral"

    def give_advice(self):
        self.update_advisor_mood()
        if self.advisor_mood == "respectful":
            print("Advisor: Your leadership is commendable, my lord. The kingdom prospers under your rule.")
        elif self.advisor_mood == "snarky":
            print("Advisor: Perhaps you should reconsider your decisions, my lord. The kingdom is suffering.")
        else:
            print("Advisor: The kingdom is stable, my lord. Continue your wise governance.")
        #Build another set of code for handling random events in the kingdom and ways to counteract it
        
        def handle_random_events(self):
            event_chance = random.randint(1, 100)
            if event_chance <= 10:
                print("Random Event: A plague has struck the kingdom, reducing the population by 10%.")
                self.population = int(self.population * 0.9)
            elif event_chance <= 20:
                print("Random Event: A bountiful harvest! The kingdom gains an extra 500 bushels.")
                self.bushels += 500
            elif event_chance <= 30:
                print("Random Event: Bandits have raided the kingdom, stealing 200 bushels.")
                self.bushels = max(0, self.bushels - 200)
