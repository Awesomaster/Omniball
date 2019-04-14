import math
pi = math.pi

import turtle
turtle.speed(0)

d30 = 0
d90 = 0
d150 = 0
d210 = 0
d270 = 0
d330 = 0

reciprical = 0

h = int(input('H: '))
v = int(input('V: '))

def setup():
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    turtle.left(90)
    turtle.circle(100)
    turtle.right(90)
    turtle.penup()
    turtle.backward(100)
    turtle.left(90)
    turtle.pendown()
    for i in range(3):
        turtle.forward(100)
        turtle.backward(100)
        turtle.right(120)

    
    turtle.color('red')
    turtle.right(30)
    for i in range(3):
        turtle.color('red')
        turtle.forward(100)
        turtle.backward(100)
        turtle.right(180)
        turtle.color('purple')
        turtle.forward(100)
        turtle.backward(100)
        turtle.left(180)
        turtle.right(120)
        turtle.color('red')
    turtle.left(30)
    turtle.color('black')

r = math.sqrt(h*h + v*v)/10

if h > 0 and v > 0:
    feta = math.atan(h/v)
    print('Top Left')
elif h > 0 and v < 0:
    feta = math.atan(math.fabs(v/h)) + pi/2
    print('Bottom Right')
elif h < 0 and v < 0:
    feta = math.atan(h/v) + pi
    print('Bottom Left')
elif h < 0 and v > 0:
    feta = math.atan(math.fabs(v/h)) + (3/2)*pi
    print('Top Right')
else:
    move = False

setup()
feta = math.degrees(feta)

if r > 100:
    r = 100

turtle.color('blue')
turtle.right(feta)
turtle.forward(r)
turtle.backward(r)
turtle.left(feta)

print('r = ' + str(r))
print('feta = ' + str(feta))

angle = min([math.fabs(feta - 30), math.fabs(feta - 90), math.fabs(feta - 150), math.fabs(feta - 210), math.fabs(feta - 270), math.fabs(feta - 330)])

if feta == 0:
    print('GG')



'''
90 and 270
'''




if angle == math.fabs(feta - 90) or angle == math.fabs(feta - 270):
    # This is using the wheel at 0 degrees going forward or back
    
    if angle == math.fabs(feta - 90):
        # Forward (Purple)
        feta = feta - 90
        if (feta) > 0:
            C = feta
            
            # Blue is a
            a = r
            print('a = ' + str(a))
            # Purple/Red is b
            b = 100
            print('b = ' + str(b))
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))
            print('c = ' + str(c))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            print('A = ' + str(A))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            print('B = ' + str(B))
            # Angle C = C
            print('C = ' + str(C))

            print('A+B+C = ' + str(A+B+C))

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))
            
            turtle.right(C + 90)
            turtle.forward(r)
            turtle.color('green')
            turtle.left(180-B)
            turtle.forward(c)
            turtle.backward(c)
            turtle.left(120-A)
            turtle.forward(x)
            turtle.right(60)
            turtle.forward(y)

            # b = 90 deg forward motor
            d90 = b
            
            if x < 0:
                d330 = math.fabs(x)
                print('d330 (Forwards on w240)', str(d330))
            elif x > 0:
                d150 = math.fabs(x)
                print('d150 (Backwards on w240)', str(d150))

            if y > 0:
                d210 = math.fabs(y)
                print('d210 (Forwards on w120)', str(d210))
            elif y < 0:
                d30 = math.fabs(y)
                print('d30 (Backwards on w120)', str(d30))


                
            print('x =', str(x))
            print('y =', str(y))
            
            
        elif (feta) < 0:
            C = feta
            
            # Blue is a
            a = r
            print('a = ' + str(a))
            # Purple/Red is b
            b = 100
            print('b = ' + str(b))
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))
            print('c = ' + str(c))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            print('A = ' + str(A))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            print('B = ' + str(B))
            # Angle C = C
            print('C = ' + str(C))

            print('A+B+C = ' + str(A+B+C))

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))
            print('x =', str(x))
            print('y =', str(y))


            if y > 0:
                d330 = math.fabs(y)
                print('d330 (Forwards on w240)', str(d330))
            elif y < 0:
                d150 = math.fabs(y)
                print('d150 (Backwards on w240)', str(d150))

            if x < 0:
                d210 = math.fabs(x)
                print('d210 (Forwards on w120)', str(d210))
            elif x > 0:
                d30 = math.fabs(x)
                print('d30 (Backwards on w120)', str(d30))

                
            turtle.right(C + 90)
            turtle.forward(r)
            turtle.color('green')
            turtle.right(180-B)
            turtle.forward(c)
            turtle.backward(c)
            turtle.right(120-A)
            turtle.forward(x)
            turtle.left(60)
            turtle.forward(y)

            # b = 90 deg forward motor
            d90 = b

    else:
        # Back (Red)
        d270 = 100
        feta = feta - 270
        if (feta) > 0:
            C = feta
            print('Aids', str(feta))
            # Blue is a
            a = r
            print('a = ' + str(a))
            # Purple/Red is b
            b = 100
            print('b = ' + str(b))
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))
            print('c = ' + str(c))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            print('A = ' + str(A))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            print('B = ' + str(B))
            # Angle C = C
            print('C = ' + str(C))

            print('A+B+C = ' + str(A+B+C))

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))
            
            turtle.right(C + 270)
            turtle.forward(r)
            turtle.color('green')
            turtle.left(180-B)
            turtle.forward(c)
            turtle.backward(c)
            turtle.left(120-A)
            turtle.forward(x)
            turtle.right(60)
            turtle.forward(y)

            # b = 270 deg forward motor
            d270 = b
            
            if y < 0:
                d210 = math.fabs(y)
                print('d210 (Forwards on w120)', str(d210))
            elif y > 0:
                d30 = math.fabs(y)
                print('d30 (Backwards on w120)', str(d30))
            
            if x > 0:
                d330 = math.fabs(x)
                print('d330 (Forwards on w240)', str(d330))
            elif x < 0:
                d150 = math.fabs(x)
                print('d150 (Backwards on w240)', str(d150))


                
            print('x =', str(x))
            print('y =', str(y))
            
            
        elif (feta) < 0:
            C = feta
            
            # Blue is a
            a = r
            print('a = ' + str(a))
            # Purple/Red is b
            b = 100
            print('b = ' + str(b))
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))
            print('c = ' + str(c))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            print('A = ' + str(A))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            print('B = ' + str(B))
            # Angle C = C
            print('C = ' + str(C))

            print('A+B+C = ' + str(A+B+C))

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))
            print('x =', str(x))
            print('y =', str(y))

            
            if x > 0:
                d210 = math.fabs(x)
                print('d210 (Forwards on w120)', str(d210))
            elif x < 0:
                d30 = math.fabs(x)
                print('d30 (Backwards on w120)', str(d30))
            
            if y < 0:
                d330 = math.fabs(y)
                print('d330 (Forwards on w240)', str(d330))
            elif y > 0:
                d150 = math.fabs(y)
                print('d150 (Backwards on w240)', str(d150))

            

                
            turtle.right(C + 270)
            turtle.forward(r)
            turtle.color('green')
            turtle.right(180-B)
            turtle.forward(c)
            turtle.backward(c)
            turtle.right(120-A)
            turtle.forward(x)
            turtle.left(60)
            turtle.forward(y)

            # b = 270 deg forward motor
            d270 = b
        
    turtle.color('black')



'''
30 and 210
'''



# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------  30 AND 210  ----------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------



if angle == math.fabs(feta - 30) or angle == math.fabs(feta - 210):
    One20 = 100
    # If it comes for the 120 LEG
    
    if angle == math.fabs(feta - 30):
        # Forward (Purple)
        feta = feta - 30
        if (feta) > 0:
            C = feta
            
            # Blue is a
            a = r
            print('a = ' + str(a))
            # Purple/Red is b
            b = 100
            print('b = ' + str(b))
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))
            print('c = ' + str(c))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            print('A = ' + str(A))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            print('B = ' + str(B))
            # Angle C = C
            print('C = ' + str(C))

            print('A+B+C = ' + str(A+B+C))

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))
            
            turtle.right(C + 30)
            turtle.forward(r)
            turtle.color('green')
            turtle.left(180-B)
            turtle.forward(c)
            turtle.backward(c)
            turtle.left(120-A)
            turtle.forward(x)
            turtle.right(60)
            turtle.forward(y)

            # b = 90 deg forward motor
            d30 = b
            
            if y < 0:
                d330 = math.fabs(y)
                print('d330 (Forwards on w240)', str(d330))
            elif y > 0:
                d150 = math.fabs(y)
                print('d150 (Backwards on w240)', str(d150))

            if x < 0:
                d270 = math.fabs(x)
                print('d270 (Backwards on w0)', str(d270))
            elif x > 0:
                d90 = math.fabs(x)
                print('d90 (Forwards on w0)', str(d90))


                
            print('x =', str(x))
            print('y =', str(y))
            
            
        elif (feta) < 0:
            C = feta
            
            # Blue is a
            a = r
            print('a = ' + str(a))
            # Purple/Red is b
            b = 100
            print('b = ' + str(b))
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))
            print('c = ' + str(c))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            print('A = ' + str(A))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            print('B = ' + str(B))
            # Angle C = C
            print('C = ' + str(C))

            print('A+B+C = ' + str(A+B+C))

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))
            print('x =', str(x))
            print('y =', str(y))


            if y > 0:
                d270 = math.fabs(y)
                print('d270 (Backwards on w0)', str(d270))
            elif y < 0:
                d90 = math.fabs(y)
                print('d90 (Forwards on w0)', str(d90))

            if x > 0:
                d330 = math.fabs(x)
                print('d330 (Forwards on w240)', str(d330))
            elif x < 0:
                d150 = math.fabs(x)
                print('d150 (Backwards on w240)', str(d150))

                
            turtle.right(C + 30)
            turtle.forward(r)
            turtle.color('green')
            turtle.right(180-B)
            turtle.forward(c)
            turtle.backward(c)
            turtle.right(120-A)
            turtle.forward(x)
            turtle.left(60)
            turtle.forward(y)

            # b = 30 deg forward motor
            d30 = b

    else:
        # Back (Red)
        #turtle.right(210)
        d210 = 100
        feta = feta - 210
        
        if (feta) > 0:
            C = feta
            print('Aids', str(feta))
            # Blue is a
            a = r
            print('a = ' + str(a))
            # Purple/Red is b
            b = 100
            print('b = ' + str(b))
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))
            print('c = ' + str(c))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            print('A = ' + str(A))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            print('B = ' + str(B))
            # Angle C = C
            print('C = ' + str(C))

            print('A+B+C = ' + str(A+B+C))

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))
            
            turtle.right(C + 210)
            turtle.forward(r)
            turtle.color('green')
            turtle.left(180-B)
            turtle.forward(c)
            turtle.backward(c)
            turtle.left(120-A)
            turtle.forward(x)
            turtle.right(60)
            turtle.forward(y)

            # b = 210 deg forward motor
            d210 = b
            
            if x > 0:
                d270 = math.fabs(x)
                print('d270 (Backwards on w120)', str(d270))
            elif x < 0:
                d90 = math.fabs(x)
                print('d90 (Forwards on w120)', str(d90))
            
            if y > 0:
                d330 = math.fabs(y)
                print('d330 (Forwards on w240)', str(d330))
            elif y < 0:
                d150 = math.fabs(y)
                print('d150 (Backwards on w240)', str(d150))


                
            print('x =', str(x))
            print('y =', str(y))
            
            
        elif (feta) < 0:
            C = feta
            
            # Blue is a
            a = r
            print('a = ' + str(a))
            # Purple/Red is b
            b = 100
            print('b = ' + str(b))
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))
            print('c = ' + str(c))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            print('A = ' + str(A))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            print('B = ' + str(B))
            # Angle C = C
            print('C = ' + str(C))

            print('A+B+C = ' + str(A+B+C))

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))
            print('x =', str(x))
            print('y =', str(y))

            
            if y < 0:
                d270 = math.fabs(y)
                print('d270 (Backwards on w0)', str(d270))
            elif y > 0:
                d90 = math.fabs(y)
                print('d90 (Forwards on w0)', str(d90))
            
            if x > 0:
                d330 = math.fabs(x)
                print('d330 (Forwards on w240)', str(d330))
            elif x < 0:
                d150 = math.fabs(x)
                print('d150 (Backwards on w240)', str(d150))

            

                
            turtle.right(C+210)
            turtle.forward(r)
            turtle.color('green')
            turtle.right(180-B)
            turtle.forward(c)
            turtle.backward(c)
            turtle.right(120-A)
            turtle.forward(x)
            turtle.left(60)
            turtle.forward(y)

            # b = 270 deg forward motor
            d270 = b
        
    turtle.color('black')


'''
150 and 330
'''


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------  150 AND 330  ---------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------




if angle == math.fabs(feta - 150) or angle == math.fabs(feta - 330):
    Two40 = 100

    turtle.color('green')
    
    turtle.forward(50)
    turtle.backward(50)
    turtle.color('black')



if angle == math.fabs(feta - 150) or angle == math.fabs(feta - 330):
    Two40 = 100
    # If it comes for the 240 LEG
    
    if angle == math.fabs(feta - 150):
        # Forward (Purple)
        feta = feta - 150
        if (feta) > 0:
            C = feta
            
            # Blue is a
            a = r
            print('a = ' + str(a))
            # Purple/Red is b
            b = 100
            print('b = ' + str(b))
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))
            print('c = ' + str(c))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            print('A = ' + str(A))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            print('B = ' + str(B))
            # Angle C = C
            print('C = ' + str(C))

            print('A+B+C = ' + str(A+B+C))

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))
            
            turtle.right(C+150)
            turtle.forward(r)
            turtle.color('green')
            turtle.left(180-B)
            turtle.forward(c)
            turtle.backward(c)
            turtle.left(120-A)
            turtle.forward(x)
            turtle.right(60)
            turtle.forward(y)

            # b = 150 deg forward motor
            d150 = b
            
            if y > 0:
                d270 = math.fabs(y)
                print('d270 (Backwards on w0)', str(d270))
            elif y < 0:
                d90 = math.fabs(y)
                print('d90 (Forwards on w0)', str(d90))

            if x > 0:
                d210 = math.fabs(x)
                print('d210 (Forwards on w120)', str(d210))
            elif x < 0:
                d30 = math.fabs(x)
                print('d30 (Backwards on w120)', str(d30))


                
            print('x =', str(x))
            print('y =', str(y))
            
            
        elif (feta) < 0:
            C = feta
            
            # Blue is a
            a = r
            print('a = ' + str(a))
            # Purple/Red is b
            b = 100
            print('b = ' + str(b))
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))
            print('c = ' + str(c))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            print('A = ' + str(A))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            print('B = ' + str(B))
            # Angle C = C
            print('C = ' + str(C))

            print('A+B+C = ' + str(A+B+C))

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))
            print('x =', str(x))
            print('y =', str(y))


            if x < 0:
                d270 = math.fabs(x)
                print('d270 (Backwards on w0)', str(d270))
            elif x > 0:
                d90 = math.fabs(x)
                print('d90 (Forwards on w0)', str(d90))

            if y < 0:
                d210 = math.fabs(y)
                print('d210 (Forwards on w120)', str(d210))
            elif y > 0:
                d30 = math.fabs(y)
                print('d30 (Backwards on w120)', str(d30))

                
            turtle.right(C+150)
            turtle.forward(r)
            turtle.color('green')
            turtle.right(180-B)
            turtle.forward(c)
            turtle.backward(c)
            turtle.right(120-A)
            turtle.forward(x)
            turtle.left(60)
            turtle.forward(y)

            # b = 150 deg forward motor
            d150 = b

    else:
        # Back (Red)
        d330 = 100
        feta = feta - 330
        
        if (feta) > 0:
            C = feta
            print('Aids', str(feta))
            # Blue is a
            a = r
            print('a = ' + str(a))
            # Purple/Red is b
            b = 100
            print('b = ' + str(b))
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))
            print('c = ' + str(c))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            print('A = ' + str(A))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            print('B = ' + str(B))
            # Angle C = C
            print('C = ' + str(C))

            print('A+B+C = ' + str(A+B+C))

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))
            
            turtle.right(C+330)
            turtle.forward(r)
            turtle.color('green')
            turtle.left(180-B)
            turtle.forward(c)
            turtle.backward(c)
            turtle.left(120-A)
            turtle.forward(x)
            turtle.right(60)
            turtle.forward(y)

            # b = 330 deg forward motor
            d330 = b
            
            if y > 0:
                d270 = math.fabs(y)
                print('d270 (Backwards on w0)', str(d270))
            elif y < 0:
                d90 = math.fabs(y)
                print('d90 (Forwards on w0)', str(d90))

            if x < 0:
                d210 = math.fabs(x)
                print('d210 (Forwards on w120)', str(d210))
            elif x > 0:
                d30 = math.fabs(x)
                print('d30 (Backwards on w120)', str(d30))


                
            print('x =', str(x))
            print('y =', str(y))
            
            
        elif (feta) < 0:
            C = feta
            
            # Blue is a
            a = r
            print('a = ' + str(a))
            # Purple/Red is b
            b = 100
            print('b = ' + str(b))
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))
            print('c = ' + str(c))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            print('A = ' + str(A))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            print('B = ' + str(B))
            # Angle C = C
            print('C = ' + str(C))

            print('A+B+C = ' + str(A+B+C))

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))
            print('x =', str(x))
            print('y =', str(y))

            
            if x > 0:
                d270 = math.fabs(x)
                print('d270 (Backwards on w0)', str(d270))
            elif x < 0:
                d90 = math.fabs(x)
                print('d90 (Forwards on w0)', str(d90))

            if y > 0:
                d210 = math.fabs(y)
                print('d210 (Forwards on w120)', str(d210))
            elif y < 0:
                d30 = math.fabs(y)
                print('d30 (Backwards on w120)', str(d30))

            

                
            turtle.right(C+330)
            turtle.forward(r)
            turtle.color('green')
            turtle.right(180-B)
            turtle.forward(c)
            turtle.backward(c)
            turtle.right(120-A)
            turtle.forward(x)
            turtle.left(60)
            turtle.forward(y)

            # b = 330 deg forward motor
            d330 = b
        
    turtle.color('black')
    

