# Konversi Suhu Tempratur(Celcius)
print('\n PROGAM KONVERSI SUHU TEMPRATUR');

# Celcius
celcius = float(input('Masukan suhu dalam celcius: '));
print('Suhu adalah: ', celcius, 'C');

# Reamur
reamur = (4 / 5) * celcius;
print('Suhu Reamur adalah: ', reamur, 'R');

# Fahrenheit
fahrenheit = ((9 / 5) * celcius) + 32;
print('Suhu Fahrenheit adalah: ', fahrenheit, 'F');

# Kelvin
kelvin = celcius + 273;
print('Suhu Kelvin adalah: ', kelvin, 'K');

# Fahrenheit to Kelvin
fahrenheits = float(input('Masukan Suhu Fahrenheit: '));
print('Suhu Fahrenheit adalah:', fahrenheit, 'F');

Kelvins = 5 / 9 * (fahrenheits - 32) + 273;
print('Suhu Kelvin adalah: ', Kelvins, 'K');

# Kelvin to Fahrenheit
suhu_Kelvin = float(input('Masukan suhu kelvins: '));
print('Suhu Kelvin adalah: ', suhu_Kelvin, 'K');

Convert_Fahrenheit = 9 / 5 * (suhu_Kelvin - 273) + 32;
print('Subu Fahrenheit adalah: ', Convert_Fahrenheit, 'F');

