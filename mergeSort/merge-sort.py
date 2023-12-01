from merge import merge

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list

    mid = int(len(my_list) / 2)  # same thing as Math.floor()

    left = merge_sort(my_list[:mid]) # same thing as using slice()      (sort left side until list is sorted with length of 1)  ...this call eventually returns full sorted left half
    right = merge_sort(my_list[mid:]) # saming thing as using slice()   (sort right side until list is sorted with length of 1) ...this call eventually returns full sorted right half

    print("MERGING", left, right)
    return merge(left, right)  # combine left and right sides into a sorted list, this builds up recursively from returns made on lines 9 and 10



original_list = [3,1,4,2]

sorted_list = merge_sort(original_list)

print("original list:", original_list)
print('sorted list:', sorted_list)




# Initial Call: merge_sort([3, 1, 4, 2])

# merge_sort([3, 1]) is called.
# merge_sort([3]) returns [3].
# merge_sort([1]) returns [1].
# Merging [3] and [1] results in [1, 3].

# merge_sort([4, 2]) is called.
# merge_sort([4]) returns [4].
# merge_sort([2]) returns [2].
# Merging [4] and [2] results in [2, 4].

# Merging [1, 3] and [2, 4] results in [1, 2, 3, 4].
# The final result is [1, 2, 3, 4].
