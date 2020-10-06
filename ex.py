import functools 

def isPrime(n): 
    if n <= 1: 
        return False
    if n <= 3: 
        return True
  
    if n % 2 == 0 or n % 3 == 0: 
        return False
  
    i = 5
    while i * i <= n: 
        if n % i == 0 or n % (i + 2) == 0: 
            return False
        i = i + 6
  
    return True

def ex1(arr):
  return functools.reduce(lambda a,b : a+b,[n for n in arr if isPrime(n)]) if len(arr) > 0 else None

print(ex1([1,2,3,4,5]))

morse_dict = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

def ex2(str):
  return "".join(map(lambda x : morse_dict[x.capitalize()], str))

print(ex2("LoL kek"))

vowels = ["a", "e", "i", "o", "u", "y"]
vowels_dict = {v: i for i, v in enumerate(vowels)}

def ex3(string):
  return "".join(map(lambda x : str(vowels_dict[x]) if x in vowels else x , string[::-1])) + "aca"

print(ex3("apple"))
