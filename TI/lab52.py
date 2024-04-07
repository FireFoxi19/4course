#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random
import math

def delete_spaces(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i.replace(' ', ''))
    return new_lst

def read_file(file_name, len_str):
    f = open(file_name, 'r')

    file_text = f.read()

    code_text = []

    string = ""
    for i in range(len(file_text)):

        if (len(string) == len_str):
            code_text.append(string)
            string = ""
        string = string + file_text[i]

    code_text.append(string)
 
    f.close()

    code_text = delete_spaces(code_text)

    return code_text

def write_file(file_name, code_text):
    f = open(file_name, 'w')
    for string in code_text:
        f.write(f"{string} ")

    f.close()

def write_file_with_errors(file_name, code_text, p):
    f = open(file_name, 'w')
    p_error = int(p*10000)
    for string in code_text:
        for j in string:

            if random.randint(1, 10000) <= p_error:
                symbol = (int(j) + 1) % 2
                # print("Помеха! Символ заменен!")
            else:
                symbol = j

            f.write(f"{symbol}")
        f.write(f" ")

    f.close()

def string_element_change(string, element, i1):

    new_string = list(string)
    new_string[i1] = str(int(element))
    string = ""
    for j in new_string:
        string += f"{j}"

    return string


def Hamming_encode(file_text):

    code_text = []

    for string in file_text:

        k_control_bit = 0
        while True:
            position = pow(2, k_control_bit)
            if position > len(string):
                break
            string = string[:(position-1)] + '0' + string[(position-1):]
            k_control_bit += 1
        

        control_bit = []
        for i in range(k_control_bit):
            control_bit.append(0)


        for i in range(k_control_bit):
            
            position = pow(2, i)
            j = position - 1

            while True:

                if j > len(string) - 1:
                    break
                
                for k in range(position):
                    if (j+k) < len(string):
                        control_bit[i] = (control_bit[i] + int(string[j+k])) % 2

                j += 2*position
                

        for i in range(k_control_bit):

            position = pow(2, i)
            
            string = string_element_change(string, control_bit[i], position-1)

        code_text.append(string)


    return code_text


def Hamming_decode(file_text):

    k_control_bit = math.ceil((math.sqrt(len(file_text[0]))))

    check_file = []
    decode_text = []
    iterator = 0

    for string in file_text:
        
        for i in range(k_control_bit):

            position = pow(2, i)
            
            string = string_element_change(string, 0, position-1)

        check_file.append(string)


    errors_count = 0
        
    for string in check_file:

        control_bit = []
        for i in range(k_control_bit):
            control_bit.append(0)


        for i in range(k_control_bit):
            
            position = pow(2, i)
            j = position - 1

            while True:

                if j > len(string) - 1:
                    break
                
                for k in range(position):
                    if (j+k) < len(string):
                        control_bit[i] = (control_bit[i] + int(string[j+k])) % 2

                j += 2*position
                

        for i in range(k_control_bit):

            position = pow(2, i)
            string = string_element_change(string, control_bit[i], position-1)

        if file_text[iterator] != string:
            # print ("Найдена ошибка!")
            errors_count += 1
            position_error = 0
            for i in range(k_control_bit):
                position = pow(2, i) - 1   
                if string[position] != file_text[iterator][position]:
                    position_error += (position+1)
            
            try:
                new_element = (int(file_text[iterator][position_error-1]) + 1) % 2
                string = string_element_change(file_text[iterator], new_element, position_error-1)
            except:
                string = file_text[iterator]

        
        decode_text.append(string)
            
        iterator += 1

    return decode_text, errors_count
            



def main():
    file_text = read_file("coded_shannon.txt", 16)

    code_text = Hamming_encode(file_text)
    write_file("encode_text.txt", code_text)
    
    write_file_with_errors("errors_text.txt", code_text, 0.1)

    error_file = read_file("errors_text.txt", 22)

    decode_text, error_count = Hamming_decode(error_file)

    errors = 0
    for i in range(len(code_text)):
        if code_text[i] != decode_text[i]:
            errors += 1
    
    print("Всего ошибок")
    print(error_count)
    print("Исправленных ошибок")
    print(error_count - errors) 
    print("Не исправленных ошибок")
    print(errors)   

if __name__ == "__main__":
    main()





