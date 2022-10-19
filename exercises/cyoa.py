"""My choose your own adventure. Inspired by a mobile game that I played like 10 years ago called 'A Dark Room'."""

__author__ = "730622383"

from random import randint
player: str = ""
points: int = 0
items: int = 0
GREEN_BOX: str = "\U0001F7E9"
PURPLE_BOX: str = "\U0001F7EA"
RED_BOX: str = "\U0001F7E5"
BLACK_BOX: str = "\U00002B1B"


def greet() -> None:
    """Greet message, explains the game and gets the players name."""
    print("Hello Adventurer, you are a wanderer in a post apocalyptic earth, post colonization of the solar system. You awaken in a house with no memory, with a basic set of tools and supplies.")
    print("At the start of each turn, you can either type 'Exit' to quit, or type in 'Up','Down','Left', or 'Right', to move. Your home base is at the center of the board, and there are different events scattered around the map. Those events will also prompt you for an input.")
    print("The player is at the green box, the start point (home base) is at the purple box, and all events are at red boxes.")
    global player
    player = input("What is your name?")


def generate() -> list:
    """Generates the location of all of the random events on the map."""
    dimensions: int = 9
    returner: list(list) = []
    holder: list(int)
    i: int = 0
    while i < dimensions:
        """Generates a random event on every row of the map."""
        x: int = randint(0, (dimensions - 1))
        while x == 4 and i == 4:
            """Checks to make sure that there is no location at the home base."""
            x = randint(0, (dimensions - 1))
        holder = [x, i, 0]
        returner.append(holder)
        i += 1
    return (returner)


def collision(locations: list[list], player: list[int]) -> bool:
    """Detects if the player is currently standing on a location."""
    i: int = 0
    while i < len(locations):
        holder: list[int] = locations[i]
        if holder[0] == player[0] and holder[1] == player[1]:
            return (True)
        i += 1
    return (False)


def screen_write(locations: list[list], player: list[int]) -> None:
    """Prints the map."""
    dimensions: int = len(locations)
    i: int = 0
    while i < dimensions:
        """Prints each row, using black for nothing, green for player, purple for home, and red for locations"""
        j: int = 0
        holder: list[int] = locations[i]
        while j < dimensions:
            """Iterates through each column and actually does the printing."""
            if j == player[0] and i == player[1]:
                print(GREEN_BOX, end="") 
            elif j == (dimensions // 2) and i == (dimensions // 2):
                print(PURPLE_BOX, end="") 
            elif j == holder[0] and i == holder[1]:
                print(RED_BOX, end="") 
            else:
                print(BLACK_BOX, end=" ") 
            j += 1
        print("")
        i += 1


def event(locations: list[list], player: list[int], score: int) -> int:
    """If the player is on a location this function executes the interaction."""
    global items
    j: int = 0
    while j < len(locations):
        holder: list[int] = locations[j]
        if holder[1] == 0 and holder[1] == player[1] and holder[0] == player[0]:
            if items > 0 and items < (len(locations) - 1):
                print("You have found an alien spacecraft. The weird items you have collected so far feel as though they are pulling toward it. Upon entering the craft, you realize there are more pieces missing than you are currently carrying. There is nothing else you can do here at this time.")
                return (score)
            elif items > 0 and items == (len(locations) - 1):
                print("You have found an alien spacecraft. Upon entering you realize all the relics you have been carrying slot into the ship in various places. Upon placing the last relic into its place, the ship powers up. You now have the ability to leave this desolate world.")
                return (score + 5000)
            else:
                print("You stumble upon an alien craft, after searching it, you find nothing useful")
                return (score)
        j += 1
    i: int = 0
    while i < len(locations):
        holder: list[int] = locations[i]
        if holder[2] == 1 and holder[1] == player[1] and holder[0] == player[0]:
            print("You have already been here, move on.")
            return (score)
        i += 1
    event: int = randint(0, 2)
    given: str = ""
    if event == 0:
        print("You stumble onto the remains of a run down, overgrown city. There appears to be a small camp set up in the city center. Would you like to Approach? (Y/N)")
        given = input()
        while given != "Y" and given != "N":
            print("Please enter 'Y' or 'N'")
            given = input()
        if given == "Y":
            print("You approach the camp to see a group of settlers being held up by a crew of bandits. Would you like to help the settlers or move on (H/M)")
            given = input()
            while given != "H" and given != "M":
                print("Please enter 'H' or 'M'")
            if given == 'H':
                print("You quickly take cover and shoot down  the group of bandits. They panic and scatter. Once the scene is safe, you venture down into camp.")
                print("The settlers, incredibly grateful for being saved, gift you an ancient artifact. You rest for awile, and the continue on your way.")
                items += 1
                return (score + 100)
            else:
                print("You skirt the edge of the settlement, grabbing a bag from nearby.")
                print("You open it up to find a strange object. After moving across the city you decide to move on.")
                items += 1
                return (score + 10)
        else:
            print("You stay on the edge of the city, trying to stay away from the camp.")
            print("Crossing through an abandoned building, you hear some footsteps shuffling around.")
            print("A lone scavenger comes around the corner, sees you, drops his bag, and runs off.")
            print("You take his bag and add its contents to your suplies and move on.")
            items += 1
            return (score + 50)
    elif event == 1:
        print("You stumble across an ancient battlefield. After searching around you find some useful things, including some things that appear to be war relics")
        print("While scavenging, a pack of wild animals starts to approach you. Would you like to stand your ground or run? (S/R)")
        given = input()
        while given != "S" and given != "R":
            input("Please input either 'S' or 'R'")
        if given == "S":
            print("After taking a shot at the animals, they retreat to a safe distance to keep an eye on you. You then leave.")
            return (points + 50)
        else:
            print("Your attempt to run was successful.")
            return (points + 50)
    elif event == 2:
        print("You make your way into a small town, in the saloon, you overhear a small group of people bantering. One person is talking about how he needs hands for some small jobs, and another is bragging about how he found some debris that crashed down from the heavens.")
        print("Would you like to offer to help the man in need, or attempt to steal the heaven debris?(H/S)")
        given = input()
        while given != "H" and given != "S":
            input("Please input either 'H' or 'S'")
        if given == "S":
            print("After dusk, you sneak into his barn in search of the debris. You hearing some scuttering, only for a rat to pop out and scare you. You find the debris uneventfully from there.")
            print("You then sneak out of the town and move on.")
            return (points + 20)
        else:
            print("The man has you doing odd jobs for two whole days, but in the end rewards you with an object that looks suspiciously like the debris that the other man was bragging about. You dont want to be around when the other man realizes, so you leave.")
            return (points + 100)


def has_seen(locations: list[list], player: list[int]) -> list[list]:
    """Sets the location third variable to 1, basically telling the program the player has been to that location before."""
    i: int = 0
    while i < len(locations):
        holder: list[int] = locations[i]
        if holder[0] == player[0] and holder[1] == player[1]:
            locations.pop(i)
            holder.pop(2)
            holder.append(1)
            locations.insert(i, holder)
        i += 1
    return (locations)


def main() -> None:
    """The main loop of the game, handles other function calls."""
    global points
    greet()
    locations: list = generate()
    player_location = [len(locations) // 2, len(locations) // 2]
    holder: int

    while True is True:
        print(f"{player}, you currently have {points} points.")
        print("What would you like to do?")
        screen_write(locations, player_location)
        collide: bool = collision(locations, player_location)
        if collide is True:
            points = event(locations, player_location, points)
            locations = has_seen(locations, player_location)
            if points > 5000:
                print("You have successfully escaped the ruined planet. Congratulations")
                print(f"Thank you for playing! You accumulated {points} Points!")
                break
            print(f"{player}, you currently have {points} points.")
            print("What would you like to do?")
        movement: str = input()
        while movement != "Exit" and movement != "Up" and movement != "Down" and movement != "Left" and movement != "Right":
            print("Invalid Input, please input 'Exit' or 'Up' or 'Down' or 'Right' or 'Left'")
            movement = input()
        if movement == "Exit":
            print(f"Thank you for playing! You accumulated {points} Points!")
            break
        elif movement == "Up":
            if player_location[1] == 0:
                print("You tried to move off the edge of the map, you have not moved.")
            else:
                holder = player_location[1]
                player_location.pop(1)
                player_location.insert(1, holder - 1)
                points += 1
        elif movement == "Down":
            if player_location[1] == len(locations) - 1:
                print("You tried to move off the edge of the map, you have not moved.")
            else:
                holder = player_location[1]
                player_location.pop(1)
                player_location.insert(1, holder + 1)
                points += 1
        elif movement == "Left":
            if player_location[0] == 0:
                print("You tried to move off the edge of the map, you have not moved.")
            else:
                holder = player_location[0]
                player_location.pop(0)
                player_location.insert(0, holder - 1)
                points += 1
        elif movement == "Right":
            if player_location[0] == len(locations) - 1:
                print("You tried to move off the edge of the map, you have not moved.")
            else:
                holder = player_location[0]
                player_location.pop(0)
                player_location.insert(0, holder + 1)
                points += 1

           
if __name__ == "__main__":
    main()