def add(a, b):
  return a + b
  
def subtract(a, b):
  return a - b
  
def multiply(a, b):
  return a * b
  
def divide(a, b):
  return a / b

def main():
  while True:
     print("Pick an operation 1-4")
     print("1. Add")
     print("2. Subtract")
     print("3. Multiply")
     print("4. Divide")

def main():
    while True:
        print("Pick an operation 1-4")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter choice: ")
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print(add(a, b))
        elif choice == "2":
            print(subtract(a, b))
        elif choice == "3":
            print(multiply(a, b))
        elif choice == "4":
            if b == 0:
                print("Error: can't divide by zero")
            else:
                print(divide(a, b))
        else:
            print("Invalid choice, try again")

if __name__ == "__main__":
    main()