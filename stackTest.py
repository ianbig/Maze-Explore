import p2stack
# test default stack
st = Stack()
# test push / pop
for i in range(0, 3):
    st.push(i)
    print(st)
    pass
for i in range(0,3):
    ele = st.pop()
    print(st)
    print(f'(ele is {ele})')
    pass

st = Stack(0)
for i in range(0, 12):
    st.push(i)
    print(st)
    pass
for i in range(0, 12):
    st.pop()
    print(st)
    print(f'(ele is {ele})')
    pass

for i in range(0, 4):
    st.push(i)
    print(st)
    pass

for i in range(0,4):
    st.pop(i)
    print(st)
    print(f'(ele is {ele})')
# test resize
# test isFull/isEmpty

# test abirtary stack
