# -*- coding: utf-8 -*-

import math as m

def f(x):
    return x**3 - x - 1 #object function

a = 1.
b = 2.

x = (a + b) * 0.5

e1 = 1e-12

#exact root
alpha = 1.324717957244746

#error estimate
err = m.fabs(alpha - x)

#creating empty list to populate
xl = []
pl = []
errl = []

i = 0

while e1 < m.fabs(f(x)) or e1 < err:
    
    if f(x) * f(a) < 0.:
        b = x
    
    else:
        a = x
    
    x = (a + b) * 0.5
    xl.append(x); err = m.fabs(alpha-x); errl.append(err); i += 1
    
    if len(errl) > 2:
        p = m.log(m.fabs(errl[-1]/errl[-2])) / m.log(m.fabs(errl[-2]/errl[-3]))
        pl.append(p)

print('x̄=', x)
print('f(x̄)=', f(x))
print('error=', err)
print('Number of Iterations =', i)
print('Order of Convergence =', round(pl[-1], 2))
print('Series of Convergence:', *pl, sep = "\n")

'''
Output:

= 1.3247179572449568
f(x̄)= 8.988365607365267e-13
error= 2.107203300738547e-13
Number of Iterations = 40
Order of Convergence = -1.15
Series of Convergence:
3.571925429658261
-0.3132850258921622
-3.8813456662029227
-0.1493939750008764
-8.47308701995477
-0.49091043355784847
-1.0418713970899518
3.391331518616553
-0.81035749040353
-0.24213479673340002
1.07488026784045
1.1788520594576648
1.606731204972337
0.18114073742247558
6.770371026382475
-0.533026850170738
-1.1758898957566273
2.0319738286275295
-0.6636670186002689
-0.5932730471731334
1.5590471205009804
0.32535257785259153
2.5539707559471143
-0.12604684405677039
-17.521515798129872
-0.6497052200253091
-0.5156045363967379
1.4185782061462293
1.0506700424232611
-0.2441787311161161
-6.112868420986828
-0.3789046568347028
-1.7777046174262685
0.6955297192487017
0.2912028900947023
6.907916028836713
-0.537999124074767
-1.1462774424094857
'''
