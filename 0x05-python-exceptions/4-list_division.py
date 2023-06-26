#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length
    for i in range(list_length):
        try:
            result[i] = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result[i] = 0
        except IndexError:
            print("out of range")
            result[i] = 0
        except ZeroDivisionError:
            print("division by 0")
            result[i] = 0
        finally:
            pass
    return result
    """we can use result.append in finally"""
