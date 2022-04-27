while True:
    servos.P0.set_angle(0)
    basic.show_leds("""
    . . . . .
    . . . . .
    . . # # #
    . . . . .
    . . . . .
    """)
    basic.pause(1000)

    servos.P0.set_angle(45)
    basic.show_leds("""
    . . . . #
    . . . # .
    . . # . .
    . . . . .
    . . . . .
    """)
    basic.pause(1000)
    
    servos.P0.set_angle(180)
    basic.pause(1000)
    servos.P0.set_angle(90)
    basic.pause(1000)
