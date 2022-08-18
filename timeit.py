import timeit

l = [26.7, 34.23, 67.45]

echo_one = "label test"

testcode = '''
def my_funct():
    print ("list = ", l)
    l.sort(reverse=True)
    print("sorted liist = ", l)
    return l
    '''

print(timeit.timeit(setup = echo_one, stmt = testcode, number=l))
