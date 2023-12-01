# Write a function called merge that merges two sorted lists of integers into a single sorted list.

# The function should perform the following tasks:

# Accept two parameters, list1 and list2, which represent the two sorted lists of integers.
# Initialize an empty list called combined, and two index variables, i and j, both initialized to 0.
# While both i and j are within the bounds of their respective lists, perform the following steps:
# Compare the elements at position i in list1 and position j in list2.
# If the element in list1 is smaller, append it to combined and increment i.
# Otherwise, append the element from list2 to combined and increment j.
# After one of the lists has been fully traversed, append any remaining elements from list1 and list2 to combined.
# Return the merged list combined.


def merge(list1, list2): # the two lists being passed in need to be SORTED for this to work
    combined = []
    i = 0  # make our own pointers since we dont know what the lengths of each list will be when this function is called
    j = 0

    while i < len(list1) and j < len(list2): # this while loop will conclude once either list1 is empty OR list2 is empty
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    # since the lists were already sorted, and we dont know which list was emptied from the first loop, we can simply append the remaining values from both lists
    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
        combined.append(list2[j])
        j += 1

    print("COMBINED ---> ", combined)
    print('\n')
    return combined  # since these loops arent nested, this function is O(n)


if __name__ == "__main__":
    # code here will only run if the script is executed directly, not when imported
    print("RESULT OF MERGE ---", merge([1,2,7,8], [3,4,5,6]))  # note that these lists are sorted upon entry
