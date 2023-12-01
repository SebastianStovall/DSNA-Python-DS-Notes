# Implement the set_item method for the HashTable class that inserts a key-value pair into the hash table.

# The method should perform the following tasks:

# Calculate the hash value of the given key by calling the private __hash method (to be implemented separately) and store the result in a variable named index.
# Check if the data_map list at the calculated index is None:
# If it is, create an empty list at that index in data_map.
# Append the key-value pair as a list containing two elements [key, value] to the list at the calculated index in data_map.



class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):  # this method adds a KVP to our hash table
        index = self.__hash(key)   # get the bucket index to place the KVP into by hashing the key
        if self.data_map[index] is None: # if this bucket is empty, first initialize before adding (could also make it a LinkedList instead of a matrix)
            self.data_map[index] = []
        for KVP in self.data_map[index]: # this loop is checking if the KEY already exists
                if key == KVP[0]:  # if the current KVP's key equals the key passed in, UPDATE ITS VALUE AND RETURN
                    KVP[1] = value
                    return
        self.data_map[index].append([key, value])  # if the key was NOT found, add the KVP to the bucket



my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)    # initial value of lumber
my_hash_table.print_table()


"""
    EXPECTED OUTPUT:
    ----------------
    0 :  None
    1 :  None
    2 :  None
    3 :  None
    4 :  [['bolts', 1400], ['washers', 50]]
    5 :  None
    6 :  [['lumber', 70]]

"""


my_hash_table.set_item('lumber', 600)    # UPDATE value of lumber to be 600
print('--------------------------------------')
my_hash_table.print_table()



"""
    EXPECTED OUTPUT:
    ----------------
    0 :  None
    1 :  None
    2 :  None
    3 :  None
    4 :  [['bolts', 1400], ['washers', 50]]
    5 :  None
    6 :  [['lumber', 600]]    <----- ** UPDATED value**

"""
