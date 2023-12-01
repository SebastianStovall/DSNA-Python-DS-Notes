class HashTable:
    def __init__(self, size = 7):   # size is 7 ... you want a PRIME number of buckets in your hash table to reduce collisions
        self.data_map = [None] * size # create a list with size number of buckets

    def __hash(self, key):  # hash function used to return an address/index to store our KVP
        my_hash = 0
        for letter in key:
            my_hash = ( my_hash + ord(letter) * 23 % len(self.data_map) ) # this particular hash gets the ascii value for each letter and multiplies it by a prime number and moduluo's by the length of the hashmap list to determine what index to place at
        return my_hash                                                         # works cause when doing   ( randInt % 7 ) ---> always will return an index between 0 - 6 (WHICH ARE THE INDICIES AVAILABLE IN OUR HASH MAP LIST)

    def print_table(self):  # this method not needed but is useful for debugging and such
        for i, val in enumerate(self.data_map):
            print(i, ': ', val)


# create the hash table and print out its values
my_hash_table = HashTable()

my_hash_table.print_table()
