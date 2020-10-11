def maximum_number(array):
    #high stands for highest number(maximum)
    largest = array[0]
    for i in array:
        if largest < i:
            largest = i
    return(largest)

print(maximum_number([1,5,2,7,12,14]))

