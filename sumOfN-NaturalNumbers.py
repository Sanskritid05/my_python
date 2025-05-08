    
# sum of n natural numbers 

start = int(input("Enter the start value of range : "))

end = int(input("Enter the end value of range : "))

sum_ = 0

if start == end :
    sum_ += start

if start < end :
    for i in range(start , end+1 ):
        sum_ = sum_ + i 

elif start > end :
    for j in range(start+1):
        sum_ += j
        j -= 1
print(sum_)     
