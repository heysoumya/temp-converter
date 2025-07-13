def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

if __name__ == "__main__":
    print("32°C =", celsius_to_fahrenheit(32), "°F")
    print("89.6°F =", fahrenheit_to_celsius(89.6), "°C")