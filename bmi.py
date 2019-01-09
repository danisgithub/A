h = input('身高（M）：')
w = input('体重（KG)：')

hh = float(h)
ww = float(w)

bmi = ww/(hh*hh)

if float(bmi) > 32:
    print('严重肥胖')
elif 28 < float(bmi) <= 32:
    print('肥胖')
elif 25 < float(bmi) <=28:
    print('过重')
elif 18.5 < float(bmi) <= 25:
    print('正常')
else:
    print('过轻')
