from p2stack import *
# test default stack
st = Stack()
# test push / pop
'''
for i in range(0, 3):
    st.push(i)
    print(st)
    pass
for i in range(0,3):
    ele = st.pop()
    print(st)
    print(f'(ele is {ele})')
    pass
'''
'''
st = Stack(0)
# import pdb; pdb.set_trace()
print(f'+++++++Begin pushing++++++++')
for i in range(0, 6):
    st.push(i)
    print(st)
    pass

print(f'+++++++Begin pop++++++++')
for i in range(0, 7):
    ele = st.pop()
    print(st)
    print(f'element is {ele}')
    pass

print(f'+++++++Begin pushing++++++++')
for i in range(0, 4):
    st.push(i * 2)
    print(st)
    pass

print(f'+++++++Begin pop++++++++')
for i in range(0,4):
    ele  = st.pop()
    print(st)
    print(f'(ele is {ele})')
'''
# test resize
# test isFull/isEmpty
st = Stack(0)
print(f'st empty: {st.isEmpty()}')
print(f'st empty: {st.isFull()}')
# test abirtary stack
