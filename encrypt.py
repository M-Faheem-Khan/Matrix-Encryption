import numpy as np


class create(object):
    '''
    Creates a matrix of n by 2 of the ascii string 
    '''
    def matrix(self,test_array):
        array_len = len(test_array)
        mod_val = array_len % 2
        half_val = round(array_len/2)
        if (mod_val == 0):
            temp = [test_array[:half_val], test_array[half_val:]]
            return temp
        else:
            test_array.append(ord(" "))
            half_val = round(len(test_array)/2)        
            temp = [test_array[:half_val], test_array[half_val:]]
            return temp
    
    # generates a random sorted
    # generates a multiplication matrix
    # returns the multiplication matrix
    def key_matrix(self, rows, cols):
        seed = np.random.randint(1, 99999999)
        np.random.seed(seed)
        key_matrix = np.random.randint(10, size=(rows ,cols))
        return (seed, key_matrix)
    
    def multiplied_matrix(self, seed, goal_array, key_array):
        temp = [] # the multiplied matrix
        for i in range(len(goal_array)):
            k = []
            for j in range(len(goal_array[0])):
                z = goal_array[i][j]*key_array[j]
                k.append(z)
            temp.append(k)

        return [seed, key_array, temp]

    
class convert_this_to(object):
    '''
    Converts passed string to ascii
    '''
    def ascii(self, goal):
        return [ord(goal[i]) for i in range(len(goal))]

    def numpy_array(self, array):
        return np.asarray(array)

def main():
    '''
    Gets a goal from the user
    Converts it to ascii
    Creates a matrix out of the values
    Generates a random seed value (for reproduciblity)
    Creates another array of the size (len_of_array ) 
    '''
    goal = input("GOAL: ")
    goal_ascii = convert_this_to().ascii(goal)
    m = create()
    goal_array = m.matrix(goal_ascii)
    key_array = m.key_matrix(len(goal_array), len(goal_array[0]))
    seed = key_array[0]
    key_array = key_array[1]
    final_matrix = m.multiplied_matrix(seed, goal_array, key_array[1])
    for i in final_matrix:
        print(i)

main()
