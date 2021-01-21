# Count up
# Bart Massey 2021

count = int(input("count up to? "))
# current_count will be set to 0, 1, … count - 1.  Each time
# it is set, the body will be executed.
for current_count in range(count):
	print(current_count + 1)
# When current_count reaches count, execution will pick up
# here.
print("we're out")
