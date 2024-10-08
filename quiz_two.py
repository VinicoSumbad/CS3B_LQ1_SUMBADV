#Declaring variables using array
Svelt = ["Vinico Sumbad", "Jeremie Dela Cruz", "Princess Daquing"]
Age = ["20","22","20"]
WeekAllo = [1000.00,500.00,1000.00]

#Converting String (Age) to Integer
AgeConverted = [int(Age[0]),int(Age[1]),int(Age[2])]

#Sum of overall age
SumofAge = AgeConverted[0] + AgeConverted[1] + AgeConverted[2]
print("The sum of their age is",SumofAge)

#Difference of overall age
DiffofAge = AgeConverted[0] - (AgeConverted[1] - AgeConverted[2])
print("The Difference of their age is",DiffofAge)


#Product of overall age
ProductofAge = AgeConverted[0] * AgeConverted[1] * AgeConverted[2]
print("The Product of their age is",ProductofAge)

#Product of overall allowance
ProductofAllo = WeekAllo[0] * WeekAllo[1] * WeekAllo[2]
print("The Product of their Allowance is",ProductofAllo)

#Space
print("")

#Comparing age from Age 1 to Age 3
CompareAge = [AgeConverted[0] == AgeConverted[1], AgeConverted[1] == AgeConverted[2],AgeConverted[0]==AgeConverted[2]]

#Printing the Comparison of Age
print("Comparison of Age 1 and Age 2:",CompareAge[0])
print("Comparison of Age 2 and Age 3:",CompareAge[1])
print("Comparison of Age 1 and Age 3:",CompareAge[2])

#Getting the length of the name
NameLength = [len(Svelt[0]),len(Svelt[1]),len(Svelt[2])]

#Space
print("")

#Comparing the length of Names
CompareLen = [(NameLength[0]-1)==(NameLength[1]-2),(NameLength[1]-2)==(NameLength[2]-1), (NameLength[0]-1)==(NameLength[2]-2)]

#Printing the Comparison of Name Length
print("Comparison of Name Length 1 and Name Length 2:",CompareLen[0])
print("Comparison of Name Length 2 and Name Length 3:",CompareLen[1])
print("Comparison of Name Length 1 and Name Length 3:",CompareLen[2])






