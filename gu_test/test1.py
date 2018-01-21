
# 1.) Write a method, reverseShortestFirst, that takes two parameters, both simple arrays of doubles, and returns an array of strings.
# The method should:
# • convert each array of doubles to strings
# • reverse the order of each array
# • and return a concatenation of the two arrays, the shortest of the which occurs first in the returned array
# For example:
# double [] arr1 = {23.4, 51.89, 2.34, 5.69};
# double [] arr2 = {3.45, 672.45, 37.8};
# Should result in a String array with the following content:
#       {"37.8", 672.45", "3.45", "5.69", "2.34", "51.89", "23.4"};
# A call to the method could look like:
# resultingString = reverseShortestFirst(arr1, arr2);


def reverseShortestFirst(arr1, arr2):
    new_arr1 = []
    new_arr2 = []
    for val in arr1:
        new_arr1.append(str(val))
    new_arr1.reverse()
    for val in arr2:
        new_arr2.append(str(val))
    new_arr2.reverse()
    if len(new_arr1) > len(new_arr2):
        new_arr = new_arr2 + new_arr1
    else:
        new_arr = new_arr1 + new_arr2
    print(new_arr)



def reverseShortestFirst2(arr1,arr2):
    arr1_new = []
    for i in reversed(arr1):
        arr1_new.append(str(i))
    arr2_new = []
    for i in reversed(arr2):
        arr2_new.append(str(i))

    if len(arr1_new) > len(arr2_new):
        new_arr = arr2_new + arr1_new
    else:
        new_arr = arr1_new + arr2_new
    print(new_arr)

reverseShortestFirst2([23.4, 51.89, 2.34, 5.69],[3.45, 672.45, 37.8])