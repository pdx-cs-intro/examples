# Convert degrees Fahrenheit to Celsius
# Bart Massey 2021

# Ask the user to type a temperature in degrees Fahrenheit.
# Turn it into a number.
degrees_f = float(input("°F? "))
# Convert Fahrenheit to Celsius. Algorithm from
# https://www.google.com/search?
#  q=convert+fahrenheit+to+celsius
degrees_c = (5 / 9) * (degrees_f - 32)
# Show the user the Celsius temperature.
print(degrees_c, "°C")
