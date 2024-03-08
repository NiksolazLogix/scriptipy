def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")

def my_count(n):
    return lambda a,b : (a * n) / b


count_1 = my_count(3)(10, 2)
print(count_1)


def get_list(arr):
    for x in arr:
        print(x)

my_list = ['a', 'b', 'c', 'd', 'e', 'f']

my_list.remove('d')
print(my_list)
my_list.append('g')
print(my_list)
my_list.pop(3)
print(my_list)

get_list(my_list)
