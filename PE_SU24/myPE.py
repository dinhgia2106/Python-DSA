import csv


class Player:
    def __init__(self, id, name, position, rating, age, country):
        self.id = int(id)
        self.name = name
        self.position = position
        self.rating = float(rating)
        self.age = int(age)
        self.country = country

    def __lt__(self, other):
        """Compare players based on their name."""
        return self.name < other.name

    def __str__(self):
        return (f"Player ID: {self.id}, Name: {self.name}, Position: {self.position}, "
                f"Rating: {self.rating}, Age: {self.age}, Country: {self.country}")


class HashMap:
    def __init__(self, size=20):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        """Hash function using the player's name."""
        hash_value = sum(ord(c) for c in key) % self.size
        return hash_value

    def insert(self, player):
        """Insert a player into the HashMap."""
        key = player.name
        index = self._hash(key)
        i = 1
        initial_index = index
        while self.table[index] is not None and self.table[index].name != key:
            # Quadratic probing
            index = (initial_index + i * i) % self.size
            i += 1
            if i == self.size:
                raise Exception("HashMap is full, cannot insert")
        self.table[index] = player

    def delete(self, key):
        """Delete a player by name from the HashMap."""
        index = self._hash(key)
        i = 1
        initial_index = index
        while self.table[index] is not None:
            if self.table[index].name == key:
                self.table[index] = None
                print(f"Player '{key}' deleted from the HashMap.")
                return
            index = (initial_index + i * i) % self.size
            i += 1
            if i == self.size:
                break
        print(f"Player '{key}' not found in the HashMap.")

    def search(self, key):
        """Search for a player by name in the HashMap."""
        index = self._hash(key)
        i = 1
        initial_index = index
        while self.table[index] is not None:
            if self.table[index].name == key:
                return self.table[index]
            index = (initial_index + i * i) % self.size
            i += 1
            if i == self.size:
                break
        return None

    def display(self):
        """Display the contents of the HashMap."""
        for i, player in enumerate(self.table):
            if player is not None:
                print(f"Index {i}: {player.name}")
            else:
                print(f"Index {i}: Empty")


def bubble_sort_players(players):
    n = len(players)
    for i in range(n):
        for j in range(0, n - i - 1):
            if players[j].rating > players[j + 1].rating:
                players[j], players[j + 1] = players[j + 1], players[j]


def main():
    # Read players from data.csv file.
    players = []
    try:
        with open('PE_SU24/data.csv', mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player = Player(row['Player ID'], row['Name'], row['Position'],
                                row['Rating'], row['Age'], row['Country'])
                players.append(player)
    except FileNotFoundError:
        print("The file 'data.csv' was not found.")
        return
    except Exception as e:
        print("An error occurred while reading the file:", e)
        return

    # Initialize the HashMap and insert players.
    hashmap = HashMap()
    for player in players:
        hashmap.insert(player)

    # Display the HashMap contents.
    print("HashMap Contents:")
    hashmap.display()

    # Demo for delete operation.
    print("\nDeleting player 'Scott McTominay'...")
    hashmap.delete("Scott McTominay")

    # Try to delete a non-existent player.
    print("\nDeleting player 'Lionel Messi'...")
    hashmap.delete("Lionel Messi")

    # Demo for search operation.
    print("\nSearching for player 'Luka Modric'...")
    player = hashmap.search("Luka Modric")
    if player:
        print("Player found:", player)

    print("\nSearching for player 'Lionel Messi'...")
    player = hashmap.search("Lionel Messi")
    if player:
        print("Player found:", player)
    else:
        print("Player 'Lionel Messi' not found.")

    # Sort the players array by rating using Bubble Sort.
    print("\nSorting players by rating using Bubble Sort...")
    bubble_sort_players(players)
    print("Players sorted by rating (ascending):")
    for player in players:
        print(player)

    # Display the highest rated player.
    highest_rated_player = players[-1]
    print("\nThe highest rated player is:")
    print(highest_rated_player)


if __name__ == "__main__":
    main()
