import evdev
gamepads = []
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
count = False
controller_list = ['Logitech Gamepad F710', 'Logitech Cordless RumblePad 2', 'Logitech Logitech Dual Action']
for c in controller_list:
    for device in devices:
        if device.name == c:
            gamepad = device
            count = True

try:
    print(gamepad)
except NameError:
    print('controller not found')

#from controller import *
for event in gamepad.read_loop():
    x = event.code
    y = event.value
    z = event.type
    if x == 1:
        if y >= 127:
            v = y-127
            v = (v/128)*100
        elif y < 127:
            v = (y/127)*100
            v = 100-v
    if x == 0:
        if y != 0:
            if y >= 128:
                h = y-128
                h = (h/128)*100
            elif y < 128:
                h = (y/127)*100
                h = 100-h

# _-____--_-------__-____---____

import math
pi = math.pi


d30 = 0
d90 = 0
d150 = 0
d210 = 0
d270 = 0
d330 = 0

r = math.sqrt(h*h + v*v)/10

if h > 0 and v > 0:feta = math.atan(h/v)
elif h > 0 and v < 0:feta = math.atan(math.fabs(v/h)) + pi/2
elif h < 0 and v < 0:feta = math.atan(h/v) + pi
elif h < 0 and v > 0:feta = math.atan(math.fabs(v/h)) + (3/2)*pi
else:move = False

feta = math.degrees(feta)

if r > 100:
    r = 100

angle = min([math.fabs(feta - 30), math.fabs(feta - 90), math.fabs(feta - 150), math.fabs(feta - 210), math.fabs(feta - 270), math.fabs(feta - 330)])

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------  90 AND 270  ----------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


if angle == math.fabs(feta - 90) or angle == math.fabs(feta - 270):
    # This is using the wheel at 0 degrees going forward or back
    
    if angle == math.fabs(feta - 90):
        # Forward (Purple)
        feta = feta - 90
        if (feta) > 0:
            C = feta
            
            # Blue is a
            a = r

            # Purple/Red is b
            b = 100

            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))

            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))

            # Angle C = C

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))
 
            # b = 90 deg forward motor
            d90 = b
            
            if x < 0:
                d330 = math.fabs(x)
            elif x > 0:
                d150 = math.fabs(x)

            if y > 0:
                d210 = math.fabs(y)
            elif y < 0:
                d30 = math.fabs(y)
            
            
        elif (feta) < 0:
            C = feta
            
            # Blue is a
            a = r
            # Purple/Red is b
            b = 100
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            # Angle C = C

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))

            if y > 0:
                d330 = math.fabs(y)
            elif y < 0:
                d150 = math.fabs(y)

            if x < 0:
                d210 = math.fabs(x)
            elif x > 0:
                d30 = math.fabs(x)

            # b = 90 deg forward motor
            d90 = b

    else:
        # Back (Red)
        d270 = 100
        feta = feta - 270
        if (feta) > 0:
            C = feta
            
            # Blue is a
            a = r
            # Purple/Red is b
            b = 100
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            # Angle C = C

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))

            # b = 270 deg forward motor
            d270 = b
            
            if y < 0:
                d210 = math.fabs(y)
            elif y > 0:
                d30 = math.fabs(y)
            
            if x > 0:
                d330 = math.fabs(x)
            elif x < 0:
                d150 = math.fabs(x)

            
        elif (feta) < 0:
            C = feta
            
            # Blue is a
            a = r
            # Purple/Red is b
            b = 100
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            # Angle C = C

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))

            
            if x > 0:
                d210 = math.fabs(x)
            elif x < 0:
                d30 = math.fabs(x)
            
            if y < 0:
                d330 = math.fabs(y)
            elif y > 0:
                d150 = math.fabs(y)


            # b = 270 deg forward motor
            d270 = b


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
            # Purple/Red is b
            b = 100
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            # Angle C = C


            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))

            # b = 90 deg forward motor
            d30 = b
            
            if y < 0:
                d330 = math.fabs(y)
            elif y > 0:
                d150 = math.fabs(y)

            if x < 0:
                d270 = math.fabs(x)
            elif x > 0:
                d90 = math.fabs(x)
            
        elif (feta) < 0:
            C = feta
            
            # Blue is a
            a = r
            # Purple/Red is b
            b = 100
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            # Angle C = C

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))

            if y > 0:
                d270 = math.fabs(y)
            elif y < 0:
                d90 = math.fabs(y)

            if x > 0:
                d330 = math.fabs(x)
            elif x < 0:
                d150 = math.fabs(x)

            # b = 30 deg forward motor
            d30 = b

    else:
        # Back (Red)
        d210 = 100
        feta = feta - 210
        
        if (feta) > 0:
            C = feta
            
            # Blue is a
            a = r
            # Purple/Red is b
            b = 100
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            # Angle C = C

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))

            # b = 210 deg forward motor
            d210 = b
            
            if x > 0:
                d270 = math.fabs(x)
            elif x < 0:
                d90 = math.fabs(x)
            
            if y > 0:
                d330 = math.fabs(y)
            elif y < 0:
                d150 = math.fabs(y)

            
        elif (feta) < 0:
            C = feta
            
            # Blue is a
            a = r
            # Purple/Red is b
            b = 100
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            # Angle C = C

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))

            
            if y < 0:
                d270 = math.fabs(y)
            elif y > 0:
                d90 = math.fabs(y)
            
            if x > 0:
                d330 = math.fabs(x)
            elif x < 0:
                d150 = math.fabs(x)


            # b = 270 deg forward motor
            d270 = b

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
    # If it comes for the 240 LEG
    
    if angle == math.fabs(feta - 150):
        # Forward (Purple)
        feta = feta - 150
        if (feta) > 0:
            C = feta
            
            # Blue is a
            a = r
            # Purple/Red is b
            b = 100
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            # Angle C = C

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))
            
            # b = 150 deg forward motor
            d150 = b
            
            if y > 0:
                d270 = math.fabs(y)
            elif y < 0:
                d90 = math.fabs(y)
            if x > 0:
                d210 = math.fabs(x)
            elif x < 0:
                d30 = math.fabs(x)
            
        elif (feta) < 0:
            C = feta
            
            # Blue is a
            a = r
            # Purple/Red is b
            b = 100
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            # Angle C = C

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))

            if x < 0:
                d270 = math.fabs(x)
            elif x > 0:
                d90 = math.fabs(x)

            if y < 0:
                d210 = math.fabs(y)
            elif y > 0:
                d30 = math.fabs(y)

            # b = 150 deg forward motor
            d150 = b

    else:
        # Back (Red)
        d330 = 100
        feta = feta - 330
        
        if (feta) > 0:
            C = feta
            
            # Blue is a
            a = r
            # Purple/Red is b
            b = 100
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            # Angle C = C

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))

            # b = 330 deg forward motor
            d330 = b
            
            if y > 0:
                d270 = math.fabs(y)
            elif y < 0:
                d90 = math.fabs(y)

            if x < 0:
                d210 = math.fabs(x)
            elif x > 0:
                d30 = math.fabs(x)
            
        elif (feta) < 0:
            C = feta
            
            # Blue is a
            a = r
            # Purple/Red is b
            b = 100
            # Orange is c
            c = math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(C)))

            # Angle A = A = opposite to blue
            A = math.degrees(math.acos( (b*b + c*c - a*a)/(2*b*c) ))
            # Angle B = B = opposite to purple/red
            B = math.degrees(math.acos( (a*a + c*c - b*b)/(2*a*c) ))
            # Angle C = C

            x = (c/math.sin(math.radians(120))*math.sin(math.radians(A-60)))
            y = (c/math.sin(math.radians(120))*math.sin(math.radians(120-A)))

            if x > 0:
                d270 = math.fabs(x)
            elif x < 0:
                d90 = math.fabs(x)

            if y > 0:
                d210 = math.fabs(y)
            elif y < 0:
                d30 = math.fabs(y)

            # b = 330 deg forward motor
            d330 = b

# Wheel 120
if d30 > 0:print('d30', str(d30))
if d210 > 0:print('d210', str(d210))

# Wheel 0
if d90 > 0:print('d90', str(d90))
if d270 > 0:print('d270', str(d270))

# Wheel 240
if d150 > 0:print('d150', str(d150))
if d330 > 0:print('d330', str(d330))
