# Below was written in class but doesn't seem to work. It might be a white space/indenting error.

"""
def flatten_and_sort(list):
    out = []
    for item in list:
        if type(item) == list:
            for i in item:
                out.append(i)
        else:
            out.append(item)

    return sorted(out)

nested = [0, 2, 5, 4, [5, 344, 4, 19], [215, 8585965]]

out = flatten_and_sort(nested)
print(out)

print(nested)
"""

# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)