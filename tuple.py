fruits=("apple","banana","cherry")
(green,yellow,red)=fruits
print(green)
print(yellow)
print(red)
#using asterisk
fruits=("apple","banana","cherry","strawberry","raspberry")
(green,yellow,*red,)=fruits
print(green)
print(yellow)
print(red)
print("/n")
print("/n")


#join list
tuple1=("apple","banana","cherry")
tuple2=(1,2,3)
tuple3=tuple1+tuple2
print(tuple3)