def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

print(greet("DevOps Beginner"))
print("Sum:", add(5, 3))

def greet(name):
    return f"Hello, {name}!!!"

def welcome(name):
    return f"Welcome, {name}"

def main():
    print("Welcome App")

    name = input("Enter your name: ")
    message = welcome(name)

    print(message)

if __name__ == "__main__":
    main()
