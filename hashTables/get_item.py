# Implement the get_item method for the HashTable class that retrieves the value associated with a given key from the hash table.

# The method should perform the following tasks:

# Calculate the hash value of the given key by calling the private __hash method and store the result in a variable named index.
# Check if the data_map list at the calculated index is not None:
# If it is not, iterate through the key-value pairs stored in the list at the calculated index in data_map:
# For each key-value pair, compare the stored key (located at position 0) with the given key.
# If a match is found, return the corresponding value (located at position 1) of the key-value pair.
# If he given key is not found in the hash table, return None.


class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):    # <--- this function returns the value of the key provided in the hash table, if one exists
        index = self.__hash(key)  # find the bucket that the item is in
        if self.data_map[index] is not None:  # if the bucket has items inside of it, look for our item, else return None
            for KVP in self.data_map[index]: # this loop is checking the bucket for the item
                if key == KVP[0]:  # if the current KVP's key equals the key passed in, return its value
                    return KVP[1]
        return None    # this indicates that the key you gave was not in the hash table




my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)

print('Bolts:', my_hash_table.get_item('bolts'))
print('Washers:', my_hash_table.get_item('washers'))
print('Lumber:', my_hash_table.get_item('lumber'))



"""
    EXPECTED OUTPUT:
    ----------------
    Bolts: 1400
    Washers: 50
    Lumber: None

"""
