a = float(input())
b = float(input())
c = float(input())

D = lambda x,y,z:y**2 -4*x*z

find_x = lambda x,y,z:[(-b + D(x,y,z) ** 0.5) / 2 / a,(-b - D(x,y,z) ** 0.5) / 2 / a]


result_D = D(a,b,c)
result_find_x = find_x(a,b,c)

if result_D < 0:
    print("근이 없음")
else:
    print(result_find_x)