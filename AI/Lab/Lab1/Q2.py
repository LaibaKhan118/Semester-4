count = 0
n = int(input("Enter a number: "))

print("Even numbers: ", end='')
for i in range(1, n+1):
    if i%2==0:
        print(i, end=' ')
        count = count + 1

print("\nTotal even numbers: ", count)
