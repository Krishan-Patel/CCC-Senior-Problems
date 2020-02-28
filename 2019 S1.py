
numbers= [1,2,3,4]
flip_sequence = input()


#flip_sequence1= flip_sequence.replace("VV","")
#flip_sequence2 = flip_sequence1.replace("HH","")
#flip_sequence3 = flip_sequence2.replace("HVHV","")
#flip_sequence4 = flip_sequence3.replace("VHVH","")
#flip_sequence5 = flip_sequence4.replace("VHHV","")
#flip_sequence6 = flip_sequence5.replace("HVVH","")

def number_flip(flip_seuqence):

    for character in flip_sequence:
        if character == "H":
            num1 = numbers[0]
            numbers[0] = numbers[2]
            numbers[2] = num1 
            num2 = numbers[1]
            numbers[1] = numbers[3]
            numbers[3] = num2
        else: 
            num3 = numbers[0]
            numbers[0] = numbers[1]
            numbers[1] = num3
            num4 = numbers[2]
            numbers[2] = numbers[3]
            numbers[3] = num4 

number_flip(flip_sequence)
print(str(numbers[0]) + "   "  + str(numbers[1]))
print(str(numbers[2]) + "   " + str(numbers[3]))


