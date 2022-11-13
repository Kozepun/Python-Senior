def int_inp(message):
    try:
        inp = int(input(message))
    except ValueError:
        print("Please Enter Number")
        return int_inp(message)
    except Exception as error:
        print(f"Error: {error}")
        return int_inp(message)
    else:
        return inp
a = int_inp("1")
b = int_inp("2")

print(a + b)