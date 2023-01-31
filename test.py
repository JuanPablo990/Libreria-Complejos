import libcplx as cplx

passed =0
failed =0

# c1 = (3,-8) ; c2 = (4,6)
resp = cplx.sumacplx((3,-8),(4,6))
resp1 = cplx.multcplx((3,-8),(4,6))
resp2 = cplx.restacplx((3,-8),(4,6))
resp3 = cplx.divcplx((3,-8),(4,6))
resp4 = cplx.modulocplx((3,-8))
resp5 = cplx.conjugadocplx((3,-8))
resp6 = cplx.cart_polcplx((3,-8))
resp7 = cplx.pol_cartcplx((3,-8))
resp8 = cplx.fasecplx((3,-8))

#c1 = (1,2); c2 = (3,4)
resp9 = cplx.sumacplx((1,2),(3,4))
resp10 = cplx.multcplx((1,2),(3,4))
resp11 = cplx.restacplx((1,2),(3,4))
resp12 = cplx.divcplx((1,2),(3,4))
resp13 = cplx.modulocplx((1,2))
resp14 = cplx.conjugadocplx((1,2))
resp15 = cplx.cart_polcplx((1,2))
resp16 = cplx.pol_cartcplx((1,2))
resp17 = cplx.fasecplx((1,2))

# suma
if resp[0] == 7 and resp[1] == -2:
    passed += 1
else:
    failed += 1

if resp9[0] == 4 and resp9[1] == 6:
    passed += 1
else:
    failed += 1


# multiplicasion
if resp1[0] == 60 and resp1[1] == -14:
    passed += 1
else:
    failed += 1

if resp10[0] == -5 and resp10[1] == 10:
    passed += 1
else:
    failed += 1

#resta
if resp2[0] == -1 and resp2[1] == -14:
    passed += 1
else:
    failed += 1

if resp11[0] == -2 and resp11[1] == -2:
    passed += 1
else:
    failed += 1

#divicion
if resp3[0] == -0.6923076923076923 and resp3[1] == -0.9615384615384616:
    passed += 1
else:
    failed += 1

if resp12[0] == 0.44 and resp12[1] == 0.08:
    passed += 1
else:
    failed += 1

#modulo
if resp4 == 8.54400374531753:
    passed += 1
else:
    failed += 1

if resp13 == 2.23606797749979:
    passed += 1
else:
    failed += 1

#conjugado
if resp5[0] == 3 and resp5[1] == 8:
    passed += 1
else:
    failed += 1

if resp14[0] == 1 and resp14[1] == -2:
    passed += 1
else:
    failed += 1

# conversion cartesiano a polar
if resp6[0] == 8.54400374531753 and resp6[1] == -69.44395478041653:
    passed += 1
else:
    failed += 1

if resp15[0] == 2.23606797749979 and resp15[1] == 63.43494882292201:
    passed += 1
else:
    failed += 1

# conversion de polar a cartesiano
if resp7[0] == 2.9708042062247113 and resp7[1] == -0.41751930288019634:
    passed += 1
else:
    failed += 1

if resp16[0] == 0.9993908270190958  and resp16[1] == 0.03489949670250097:
    passed += 1
else:
    failed += 1

# fase
if resp8 == -69.44395478041653 :
    passed += 1
else:
    failed += 1

if resp17 == 63.43494882292201 :
    passed += 1
else:
    failed += 1

print("passed:",passed,"failed:",failed)