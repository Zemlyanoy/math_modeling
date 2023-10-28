a,b=map(int,input().split())
if b!=0 and a%b==0:
 print("делится, ответ",int(a/b))
elif b == 0:
 print("некорректный ввод")
else:
 print("цeлочисленно не делится, ответ",int(a//b), "остаток",int(a%b))