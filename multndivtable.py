print ("DO you want to do multiplication or Division")

number = int(input("Enter number whose multiplication table you want to see: "))
limit = int(input("\nEnter the last number of the multiplication tale you need: "))

print("Multiplication table from 0 to", limit)
for i in range(0, limit+1):
    answer = number * i
    print(number, "x", i, "=", answer)

print("\n Division Table from 1 to", limit) 
for i in range(1, limit+1):
    answer = number/i
    print(number, "÷", i, "=", answer)
