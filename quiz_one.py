#Declaring variables using array
Svelt = ["Vinico Sumbad", "Jeremie Dela Cruz", "Princess Daquing"]
Age = ["20","22","20"]
WeekAllo = [1000.00,500.00,1000.00]

#Printing
print("Svelt:", Svelt[0], ",his age is", Age[0], ", allowance per week is", WeekAllo[0])
print("Svelt:", Svelt[1], ",his age is", Age[1], ", allowance per week is", WeekAllo[1])
print("Svelt:", Svelt[2], ",her age is", Age[2], ", allowance per week is", WeekAllo[2])

#Getting the length of the name
NameLength = [len(Svelt[0]),len(Svelt[1]),len(Svelt[2])]

#Printing
#Subracting 1s and 2s to eliminate the spaces on the names
print("Member 1 consist of ", (NameLength[0]-1), "characters")
print("Member 2 consist of ", (NameLength[0]-2), "characters")
print("Member 3 consist of ", (NameLength[0]-1), "characters")

