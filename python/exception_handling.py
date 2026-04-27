a = 2
b = 0

try:
    result = a/b
    print(result)
except Exception as error:
    print(error)
    print(f"We can't perform {a} / {b}")
finally:
    print("This will execute every time")    
