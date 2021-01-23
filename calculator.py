prodolzhit = 'y'
while prodolzhit == 'y':
    f_num = float(input("Виберіть перше число: "))
    oper = input("Виберіть дію: ")
    s_num = float(input("Виберіть друге число: "))
    if oper == '+':
        print(f_num + s_num)
    elif oper == '-':
        print(f_num - s_num)
    elif oper == '*':
        print(f_num * s_num)
    elif oper == '/':
        print(f_num / s_num)
    else:
        print("Error")
    prodolzhit = input("Ввдіть 'y', щоб продовжити, або любу кнопку, щоб звершити: ")