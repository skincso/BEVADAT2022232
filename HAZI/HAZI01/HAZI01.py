
#Create a function that returns with a subset of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index

def subset(input_list, start_index, end_index):
    output_list = []
    for i in range(start_index, end_index):
        output_list.append(input_list[i])

    return output_list


#ilist = [11, 15, 0, 4, 6, 54]
#subset(ilist, 2, 6)



#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size

def every_nth(input_list, step_size):
    output_list = []
    for i in range(0, len(input_list), step_size):
        output_list.append(input_list[i])
    return output_list


#ilist = [11, 15, 0, 4, 6, 54, 12, 3, 8, 12, 19]
#every_nth(ilist, 7)



#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list

def unique(input_list):
    for i in range(len(input_list) - 1):
        for j in range(i + 1, len(input_list)):
            if input_list[i] == input_list[j]:
                return False
    return True


#ilist = []
#print(unique(ilist))



#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#fucntion name must be: flatten
#input parameters: input_list

def flatten(input_list):
    output_list = []
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            output_list.append(input_list[i][j])
    return output_list


#ilist = []
#flatten(ilist)



#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args

def merge_lists(*args):

    output_list = []
    
    for arg in args:
        for i in range(len(arg)):
            output_list.append(arg[i])

    return output_list


#lista_1 = [1,2,3, 0, 0, 0]
#lista_2 = [4,5,6]
#lista_3 = [7,8,9]
#merge_lists(lista_1, lista_2, lista_3)



#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#fucntion name must be: reverse_tuples
#input parameters: input_list

def reverse_tuples(input_list):
    
    output_list = []
    
    for t in input_list:
        output_list.append((t[1], t[0]))
    
    return output_list


#ilist = []
#reverse_tuples(ilist)



#Create a function that removes duplicates from a list
#return type: list
#fucntion name must be: remove_tuplicates
#input parameters: input_list

def remove_duplicates(input_list):

    output_list = []

    for i in range(len(input_list)):
        
        j = 0

        while j < len(output_list):
            if input_list[i] == output_list[j]:
                break
            j += 1

        if j == len(output_list):
            output_list.append(input_list[i])

    return output_list


#ilist = [0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0]
#remove_duplicates(ilist)
        


#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list

def transpose(input_list):
    
    output_list = []

    for i in range(len(input_list)):
        output_list.append([])

    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            if i == j:
                output_list[i].append(input_list[i][j])
            else:
                output_list[i].append(input_list[j][i])

    return output_list


#ilist = [[1, 2],
#         [3, 4]]

#print(transpose(ilist))



#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size

def split_into_chunks(input_list, chunk_size):

    output_list = []

    for i in range(0, len(input_list), chunk_size):
        output_list.append([])
        for j in range(i, i + chunk_size):
            if j < len(input_list):
                output_list[i // chunk_size].append(input_list[j])
    return output_list


#ilist = []
#print(split_into_chunks(ilist, 2))



#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict



#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list



#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict



#If all the functions are created convert this notebook into a .py file and push to your repo


