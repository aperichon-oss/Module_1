# Exercice 1
age = 23
height = 1.69
name = 'Aurélie'
is_student = True
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Name: {name}, Type: {type(name)}")
print(f"Student: {is_student}, Type: {type(is_student)}")

# Exercice 2
a = 3
b = 2
print(f"Addition : {a+b}")
print(f"Subtraction :{a-b}")
Multiplication = a*b
Division = a/b
print(Multiplication)
print(Division)
modulo = b % a
print(modulo)
exponentiation = a ** b
print(exponentiation)

# Exercice 3
first_name = "Aurélie"
last_name = "Perichon"
full_name = first_name + " " + last_name
uppercase_name = full_name.upper()
print(uppercase_name)
name_length = len(full_name)
print(name_length)
sentence = "Ceci est une phrase de test"
word_list = sentence.split()
print(word_list)

# Exercice 4
string = "123"
Convert_int = int(string)
Float = 12.3
Float_to_int = int(Float)
Integer = 123
Int_to_float = float(Integer)
Float_to_str = str(Float)
print(f"{string} string --> {Convert_int} interger, type : {type(Convert_int)}")
print(f"{Float} float --> {Float_to_int} interger, type : {type(Float_to_int)}")
print(f"{Integer} integer --> {Int_to_float} float, type : {type(Int_to_float)}")
print(f"{Float} float --> {Float_to_str} string, type : {type(Float_to_str)}")

# Exercice 5
Morning = True
Rain = False
result_and = Morning and Rain
result_or = Morning or Rain
result_not_1 = not Morning
result_not_2 = not Rain
print(f"AND: {Morning} and {Rain} est {result_and}")
print(f"OR: {Morning} or {Rain} est {result_or}")
print(f"NOT: not {Morning} est {result_not_1}")
print(f"NOT: not {Rain} est {result_not_2}")
weather = 25.5
hot = 30
print(f"{weather} > {hot} est : {weather > hot}")
print(f"{weather} < {hot} est : {weather < hot}")
print(f"{weather} >= {hot} est : {weather >= hot}")
print(f"{weather} <= {hot} est : {weather <= hot}")
number_a = 10
number_b = 10.0
print(f"{number_a} == {number_b} est : {number_a == number_b}")
print(f"{weather} != {hot} est : {weather != hot}")
