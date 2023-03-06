def subset(input_list, start, end):
    output_list = []
    for i in range(start, end):
        output_list.append(input_list[i])

    return output_list


def every_nth(input_list, step_size):
    output_list = []
    for i in range(0, len(input_list), step_size):
        output_list.append(input_list[i])
    return output_list


def unique(input_list):
    for i in range(len(input_list) - 1):
        for j in range(i + 1, len(input_list)):
            if input_list[i] == input_list[j]:
                return False
    return True


def flatten(input_list):
    output_list = []
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            output_list.append(input_list[i][j])
    return output_list


def merge_lists(*args):

    output_list = []
    
    for arg in args:
        for i in range(len(arg)):
            output_list.append(arg[i])

    return output_list


def reverse_tuples(input_list):
    
    output_list = []
    
    for t in input_list:
        output_list.append((t[1], t[0]))
    
    return output_list


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


def split_into_chunks(input_list, chunk_size):

    output_list = []

    for i in range(0, len(input_list), chunk_size):
        output_list.append([])
        for j in range(i, i + chunk_size):
            if j < len(input_list):
                output_list[i // chunk_size].append(input_list[j])
    return output_list


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


