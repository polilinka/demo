calls = 0
def count_calls():
    global calls
    calls += 1
    return calls
def string_info(string):
    count_calls()
    i = len(string)
    a = (i, string.upper(), string.lower())
    return a
def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [s.lower() for s in list_to_search]
    if string in list_to_search:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)