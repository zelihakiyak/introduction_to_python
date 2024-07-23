# #global scope
# x= 'global scope'
# def function():
#     #local scope
#     x= 'local x'

# function()
# print(x)
###########################
name='zeliha'
def changeName(new_name):
    name=new_name
    print(name)

changeName('nihal')
print(name)
##############
name='glabal string'
def greeting():
    name='zeliha'
    def hello():
        print('hello'+ name)
    hello()
greeting()
#####################

x=30
def test(x):
    global x 
    print('x'+ x)
    x=100
    print(f'change x to {x}')

test(x)
print(x)