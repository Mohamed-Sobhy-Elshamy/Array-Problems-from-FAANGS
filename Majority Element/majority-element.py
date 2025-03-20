arr = [3, 1, 3, 3, 2]

def majorityElement(arr): 
    count_map = {}
    
    for num in arr:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1
    
    n = len(arr) 
    for key, value in count_map.items():
        if value > n // 2: 
            return key 
    return -1 

print(majorityElement(arr))