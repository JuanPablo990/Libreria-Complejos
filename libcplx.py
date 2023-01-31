import math
# Suma
def sumacplx(c1,c2):
    real = c1[0] + c2[0]
    img = c1[1] + c2[1]
    resultado = (real,img)
    return resultado

# Resta
def restacplx(c1,c2):
    real = c1[0] - c2[0]
    img = c1[1] - c2[1]
    resultado = (real, img)
    return resultado

# Division
def divcplx(c1, c2):
    num = multcplx(c1, conjugadocplx(c2))
    denomi = multcplx(c2, conjugadocplx(c2))
    real = num[0] / denomi[0]
    img = num[1] / denomi[0]
    resultado = (real, img)
    return resultado

# Salida Escritura
def prettyPcplx(c):
    print("{} + {}i".format(c[0],c[1]))

# Multiplicacion
def multcplx(c1,c2):
    real = ((c1[0]*c2[0])-(c1[1]*c2[1]))
    img = (c1[0]*c2[1])+(c1[1]*c2[0])  
    resultado = (real,img)
    return resultado

# Módulo
def modulocplx(c):
    modu = math.sqrt(c[0]**2+c[1]**2)
    return modu

# Conjugado
def conjugadocplx(c):
    return (c[0], -c[1])  

# convercion de crtesiano a polar
def cart_polcplx(c1):
    r = math.sqrt(c1[0]**2 + c1[1]**2)
    angulo = math.degrees(math.atan2(c1[1], c1[0]))
    resultado = (r, angulo)
    return resultado

# Conversion de polar a cartesiano
def pol_cartcplx(c1):
    r, angulo = c1[0], math.radians(c1[1])
    real = r * math.cos(angulo)
    img = r * math.sin(angulo)
    resultado = (real, img)
    return resultado

# Fase
def fasecplx(c1):
    resultado = math.degrees(math.atan2(c1[1], c1[0]))
    return resultado

if __name__ == '__main__':
    prettyPcplx((7,-4))
    prettyPcplx(sumacplx((3,-8),(4,6)))
    prettyPcplx(multcplx((3,-8),(4,6)))
    prettyPcplx(restacplx((3,-8),(4,6)))
    prettyPcplx(divcplx((3,-8),(4,6)))
    print(modulocplx((3,-8)))
    prettyPcplx(conjugadocplx((3,-8)))
    print(cart_polcplx((3,-8))[0],"<",cart_polcplx((3,-8))[1],"°")
    prettyPcplx(pol_cartcplx((3,-8)))
    print(fasecplx((3,-8)))


