def turn_right():
    turn_left()
    turn_left()
    turn_left()

def preskoci_zid():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# ovo je jednako kao:
# for korak in range(0, 6)
for korak in range(6):
    preskoci_zid()