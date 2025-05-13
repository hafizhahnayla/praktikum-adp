x = [i for i in range (-7,7+1)]
n = len(x)

f_x = []
for i in x:
    if i > 0:
        fx = i**3 - i
    elif i < 0:
        fx = 1/(i**2)
    else:
        fx = 1
    f_x.append(fx)
print('')
print('tabel fungsi f(x)')
print('')
print('--------------------')
print('|  x  |     f(x)   |')
print('--------------------')
for i in range (n):
    print(f'| {x[i]:>3} | {f_x[i]:>10.5f} |')  
print('--------------------') 
print('')