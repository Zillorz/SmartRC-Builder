import SMRCBuilder

def on_press(key):
    print("{0}".format(key))

keyboard = SMRCBuilder.Input.input_()
keyboard.setgroup("Keyboard")
keyboard.keyboard.start(on_press=on_press)