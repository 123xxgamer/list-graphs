import random
def rand_list(n, limit):
    g = []
    i=0
    while i<n:
        g.append(random.randrange(limit))
        i+=1
    return g

print(('=' * 10) + "Example 0" + ('=' * 10))
a = rand_list(10, 10)
b = rand_list(10, 10)
print("list a: ", len(a), a)
print("list b: ", len(b), b)



def bar_graph(g):
    s = ''
    i=0
    for cur in g:
        s+=str(i)+': '+('='*cur)+'''
'''
        i+=1
    return s

print(('=' * 10) + "Example 1" + ('=' * 10))
test = [9, 5, 5, 3, 1, 5, 9, 5, 7, 8]
print("test list:")
print(bar_graph(test))

print("list a:")
print(bar_graph(a))
print("list b:")
print(bar_graph(b))


def list_avg( g ):
    avg = 0
    for cur in g:
        avg+=cur
    avg/=len(g)
    return avg

print(('=' * 10) + "Example 2" + ('=' * 10))
print('test list (5.7):', list_avg(test) )

print( 'list a:', list_avg(a) )
print( 'list b', list_avg(b) )

def count(n, g):
    c = 0
    for cur in g:
        if n==cur:
            c+=1
    return c

print(('=' * 10) + "Example 3" + ('=' * 10))
print( 'test list (4):', count(5, test) )

def find_mode(g):
    guess = 0
    curc=0
    for e in g:
        if count(e,g)>curc:
            guess=e
            curc=count(e,g)
    return guess

print(('=' * 10) + "Example 4" + ('=' * 10))
print( 'test list (5):', find_mode(test) )

print( 'list a:', find_mode(a) )
print( 'list b:', find_mode(b) )

def list_counts(g, max_value):
    counts = [0] * max_value
    return counts

print(('=' * 10) + "Example 5" + ('=' * 10))
test_counts = list_counts( test, 10 )
print( 'test list ([0, 1, 0, 1, 0, 4, 0, 1, 1, 2]):', test_counts )

print( 'list a:', list_counts(a, 10) )
print( 'list b:', list_counts(b, 10) )
c = rand_list(10,5)
print('list c (values [0, 5) ):', c)

c_counts=[]
c_counts = list_counts(c,5)
i=0
while i<5:
    c_counts[i]=count(i,c)
    i+=1
print('list c counts:', c_counts)

def bar_graph_scaled(g, scale_factor):
    s = ''
    i=0
    while i<len(g):
        g[i]//=scale_factor
        i+=1
    s=bar_graph(g)
    return s

print(('=' * 10) + "Example 6" + ('=' * 10))
scale_test = [500, 670, 125]
print(bar_graph_scaled(scale_test, 100))

big_list = rand_list(10, 1000)
print( bar_graph_scaled(big_list, 25))

print(('=' * 10) + "Example 7" + ('=' * 10))
ls=rand_list(1000000,5)
ls_counts = list_counts(c,5)
i=0
while i<5:
    ls_counts[i]=count(i,ls)
    i+=1
print('list ls counts:', ls_counts)
print('ls_counts graphed:')
graph=bar_graph_scaled(ls_counts,(1000000//100))
print(graph)
