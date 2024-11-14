
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']


first_result=(len(x[0])-len(x[1]) for x in zip(first,second) if len(x[0])!=len(x[1]))

second_result=(False if len(first[i])!=len(second[i]) else True for i in range(0,3))

print(list(first_result))
print(list(second_result))