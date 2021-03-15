import SMRCBuilder

def on_move(x,y):
    print("{0}".format((x,y)))

mouse = SMRCBuilder.Input.input_()
mouse.setgroup("Mouse")
mouse.mouse.start(on_move=on_move)