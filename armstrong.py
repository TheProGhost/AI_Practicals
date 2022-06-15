# armstrong number

in_num = int(input("Entyer the number: "))

digits = len(str(in_num))
src = in_num
num = 0
for i in range(digits):
    tmp = in_num % 10
    num+=tmp**digits
    in_num = in_num // 10

if num == src:
    print("Armstrong number")
else:
    print("Not armstrong")