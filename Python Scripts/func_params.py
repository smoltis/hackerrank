# zip and print accept arbitrary number of parameters
# to pass a collection of collections
# collection unpacking should be used f(*col_of_col)
my_list_of_lists = [[1,2],
                    [3,4],
                    [5,6]]

print(my_list_of_lists)
print(*my_list_of_lists)
print(list(zip(my_list_of_lists)))
print(list(zip(*my_list_of_lists))) # transpose operation

