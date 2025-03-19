#================>>>>>>> COLUTION HANDLING
#approch : 1 chaning
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Create a list of empty lists (buckets)

    def hash_function(self, key):
        # Simple hash function: sum of ASCII values of characters modulo size
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        # Check if the key already exists in the bucket
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Update the value if key exists
                return
        # If key doesn't exist, add the new key-value pair
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        # Search for the key in the bucket
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]  # Return the value if key is found
        return None  # Return None if key is not found

    def delete(self, key):
        index = self.hash_function(key)
        # Search for the key in the bucket
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]  # Delete the key-value pair
                return True
        return False  # Return False if key is not found

# Example usage
ht = HashTable(5)
ht.insert("John", 25)
ht.insert("Jane", 30)
ht.insert("Tom", 35)

print(ht.search("Tom"))  # Output: 35
ht.delete("Jane")
print(ht.search("Jane"))  # Output: None




#================>>>>>>> COLUTION HANDLING
#approch : 2 open addressing

class HashTableOpenAddressing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Initialize table with None

    def hash_function(self, key):
        # Simple hash function: sum of ASCII values of characters modulo size
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        start_index = index
        while self.table[index] is not None:
            # If the key already exists, update the value
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            # Linear probing: move to the next slot
            index = (index + 1) % self.size
            # If we've checked all slots and haven't found an empty one, the table is full
            if index == start_index:
                raise Exception("Hash table is full!")
        # Insert the new key-value pair
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        start_index = index
        while self.table[index] is not None:
            # If the key is found, return the value
            if self.table[index][0] == key:
                return self.table[index][1]
            # Linear probing: move to the next slot
            index = (index + 1) % self.size
            # If we've checked all slots and haven't found the key, it doesn't exist
            if index == start_index:
                break
        return None  # Key not found

    def delete(self, key):
        index = self.hash_function(key)
        start_index = index
        while self.table[index] is not None:
            # If the key is found, mark the slot as deleted (use a special marker like "DELETED")
            if self.table[index][0] == key:
                self.table[index] = "DELETED"
                return True
            # Linear probing: move to the next slot
            index = (index + 1) % self.size
            # If we've checked all slots and haven't found the key, it doesn't exist
            if index == start_index:
                break
        return False  # Key not found

# Example usage
ht = HashTableOpenAddressing(5)
ht.insert("John", 25)
ht.insert("Jane", 30)
ht.insert("Tom", 35)

print(ht.search("Tom"))  # Output: 35
ht.delete("Jane")
print(ht.search("Jane"))  # Output: None
