# Latihan konversi satuan temperature

# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukkan Suhu dalam celsius: '))
print("suhu adalah", celcius, "Celcius")

# reamur 
reamur = (4/5) * celcius
print("suhu dalam remaur adalah ", reamur, "Reamur")

# fahrenheit
fahrenhait = ((9/5) * celcius) +32
print("suhu dalam fahrenhait adalah ", fahrenhait, "fahrenheit")


# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah", "kelvin")

# fahrenheit ke kelvin
fahrenheit = float(input("Masukkan Suhu Fahrenheit:"))
celcius = (5/9) * (fahrenheit - 32)
kelvin = (celcius + 273)
print("suhu dalam kelvin :", kelvin)

# kelvin ke farenheit
kelvin = float(input("masukkan suhu dalam kelvin:"))
celcius = kelvin - 273
fahrenheit = ((9/5)*celcius) + 32
print(" suhu dalam fahrenheit:" fahrenheit)