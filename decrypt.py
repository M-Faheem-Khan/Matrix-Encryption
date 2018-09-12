class create(object):
    # convert to original array
    def original_key(self, key, msg):
        temp = []
        for i in range(len(msg)):
            temp.append(msg[i]/key[i])
        return temp

# converts ascii values to string
class convert_from(object):
    def string_to_int(self, array):
        converted_array = []
        array = array.split(", ")
        for i in range(len(array)):
            converted_array.append(int(array[i]))
        return converted_array
    
    def ascii_to_string(self, msg1, msg2):
        converted_string = ""
        for i in msg1:
            converted_string+= str(chr(int(i)))

        for i in msg2:
            converted_string+= str(chr(int(i))) 
        
        return converted_string


def main():
    # seed = int(input("Seed:"))
    key = input("Key: ")
    msg1 = input("Message: ")
    msg2 = input("Message: ")

    key = convert_from().string_to_int(key)
    msg1 = convert_from().string_to_int(msg1)
    msg2 = convert_from().string_to_int(msg2)
 

    # c = create()
    msg1 = create().original_key(key, msg1)
    msg2 = create().original_key(key, msg2)

    m = convert_from()
    print(m.ascii_to_string(msg1,msg2))

main()
