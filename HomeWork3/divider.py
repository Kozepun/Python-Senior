result = []
def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b
data = {10: 2, 2: 5, "123": 4, 18: 0, 489: 15, 8 : 4}
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ValueError:
        print("1 number must be bigger then 2 number")
    except IndexError:
        print("2 number can't be bigger than 100")
    except TypeError:
        print("you can't input str")
    except ZeroDivisionError:
        print("can't divide by 0")
    except Exception as error:
        print(f"error{error}")

print(result)