"""
Question 1: Getting Max Over Kernel 
- Idea: [Sliding window: Apply in sound detection]
1) Create a kernel (sub-list) => In the sub-list we find a large result by max() [create_sub_list()]
2) Append the max result into the result list [find_max_value(list)]
"""

""" Solution 1: """
k = 3  # kernel size
manual_list = [50, 12, 28, 25, 33, 42, 47, 56, 63, 71]

def create_sub_list():
    collection_sub_list = []
    sub_list = []

    # Get kernels (sub-lists) and print them out
    for element in manual_list:
        sub_list.append(element)    
        
        if len(sub_list) == k:
            collection_sub_list.append(sub_list.copy())  # Append a copy of sub_list
            print(sub_list)
            del sub_list[0]  

    return collection_sub_list


def find_max_value(list):
    list_of_max_value = []

    for sub_list in list:
        list_of_max_value.append(max(sub_list))

    return print(list_of_max_value)

# total_sub_list = create_sub_list()
# find_max_value(total_sub_list)

""" Solution 2: iterate by index and zip the couple index in zip()"""
def max_kernel(num_list, k):
    start_indexs = list(range(0, len(num_list)-k+1))
    end_indexs = list(range(k, len(num_list)+1))

    result = []

    for start_index, end_index in zip(start_indexs, end_indexs):
        sub_list = num_list[start_index: end_index]
        result.append(max(sub_list))

    return result

assert max_kernel([3 , 4 , 5 , 1 , -44], 3) == [5, 5, 5]
print(max_kernel(manual_list, k))




