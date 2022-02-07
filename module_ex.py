import fah_converter

if __name__ == "__main__":
    print("Enter a celsius value: ")
    celsius = float(input())
    fahrenheit = fah_converter.convert_c_to_f(celsius)
    print("That's ", fahrenheit, "Jegrees Fahrenheit")

# __pycache : 기계어로 코딩해논 상태
