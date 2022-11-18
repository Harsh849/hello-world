def gaussquad(func, rnge, x_vals, w_vals):

    sum = 0
    a = rnge[0]
    b = rnge[1]

    for i in range(len(x_vals)):
        x = (a + b)/2 + (b-a)*x_vals[i]/2
        sum += func(x)*w_vals[i]
    
    return sum*(b-a)/2

def by_parts(n, rnge, func, x_vals, w_vals):

    a = rnge[0]
    b = rnge[1]
    h = (b-a)/n

    sum = 0

    for i in range(n):
        x0 = a + i*(h)
        x1 = x0 + h

        sum += gaussquad(func, [x0, x1], x_vals, w_vals)
    
    return sum
