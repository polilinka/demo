def print_params(a=1, b='строка', c=True):
    print(a,b,c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])


values_list = [1, 'Hello', True]
values_dict = {'a': 1, 'b': 9, 'c': 2}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Polina', 58]
print_params(*values_list_2, 42)