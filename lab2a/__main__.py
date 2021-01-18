    print("Lab2", False)
    print("Lab2", True)
    print("Lab2", None)

    a=2
    print(abs(-12.5), f"є рівним {abs(12.5)}")
    print(abs(a), f"+ {abs(a)}", "= 4")
    print(abs(a), f"+ {abs(a)}", f"={abs(a*2)}")



    documents = ["Лапи", "вуса","хвіст"]
    for oficer in documents:
        if oficer == "Лапи":
            print("Показую лапи")

        elif oficer == "вуса":
            print("Показую вуса")
    else:
            print("Показую хвіст")
    print("ось мої документи")

    n = input("Введіть ціле число: ")
    try:
        n = int(n)
        print("Ваууууу")
    except:
        print("Це не ціле число -_-")

    try:
        x = float(input("Введіть ділене: "))
        b = float(input("Введіть дільник: "))
        c = a / b
        print("Приватне: %.2f" % c)
    except ValueError:
        print("Не можна вводити рядки")

    except Exception as e:
        print(e)
    finally:
        print("Понятно")



    with open('One_to_divide_by_N.txt', 'wt', ) as inFile:
        num = int(input())
        line = str('1 / ' + str(num) + ' = ' + str(1 / num))
        print(line)
        inFile.write (line)


    u = [1, 2, 10]
    u= list(map(lambda y: y * 2, u))
    print(u)
