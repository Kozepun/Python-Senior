def int_inp(message):
    while True:
        try:
            inp = int(input(message))
        except ValueError:
            print("Please Enter Number")
        except Exception as error:
            print(f"Error: {error}")
        else:
            return inp
a = int_inp("1")
b = int_inp("2")

print(a + b)