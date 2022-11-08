import board

print("List of available pins on Raspberry Pi Pico W:")
print(dir(board))
print()

print("Built-in modules in CircuitPython:")
print(help("modules"))