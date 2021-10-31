from p2queue import *

# test default stack
'''
st = Queue()
# test push / pop
print(f'+++++++Begin pushing++++++++')
for i in range(0, 3):
    st.push(i)
    print(st)
    pass

print(f'+++++++Begin pop++++++++')
for i in range(0,4):
    ele = st.pop()
    print(st)
    print(f'(ele is {ele})')
    pass
'''

st = Queue(0)
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
for i in range(0, 9):
    st.push(i * 2)
    print(st)
    pass


print(f'+++++++Begin pop++++++++')
for i in range(0,10):
    ele  = st.pop()
    print(st)
    print(f'(ele is {ele})')
st.push(100)
print(st)



