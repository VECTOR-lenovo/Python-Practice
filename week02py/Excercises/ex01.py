def list_remo(lst):
    return list(set(lst))
sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
unique_list = list_remo(sample_list)
print(unique_list)