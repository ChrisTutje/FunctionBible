def alphabetToNumber(s: str) -> int:
    s = s.lower()
    cipher = {
	' ' : 0,
	'a' : 1,
	'b' : 2,
	'c' : 3,
	'd' : 4,
	'e' : 5,
	'f' : 6,
	'g' : 7,
	'h' : 8,
	'i' : 9,
	'j' : 10,
	'k' : 11,
	'l' : 12,
	'm' : 13,
	'n' : 14,
	'o' : 15,
	'p' : 16,
	'q' : 17,
	'r' : 18,
	's' : 19,
	't' : 20,
	'u' : 21,
	'v' : 22,
	'w' : 23,
	'x' : 24,
	'y' : 25,
	'z' : 26
    }
    result = 0
    for i in s:
        result += cipher[i]
    return result

def numberToAlphabet():
	pass

def arabicToRoman(arabicNumeral: int) -> str:
    arabicNumerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    result = ''
    for value, symbol in arabicNumerals.items():
        while arabicNumeral >= value:
            result += symbol
            arabicNumeral -= value
    return result

def romanToArabic(romanNumeral: str) -> int:
	valid_characters = 'IVXLCDM'
	if any(char not in valid_characters for char in romanNumeral):
		raise ValueError("Invalid Roman numeral: '{}'".format(romanNumeral))

	romanNumerals = {
		'M': 1000,
		'CM': 900,
		'D': 500,
		'CD': 400,
		'C': 100,
		'XC': 90,
		'L': 50,
		'XL': 40,
		'X': 10,
		'IX': 9,
		'V': 5,
		'IV': 4,
		'I': 1
	}
	result = 0
	i = 0
	while i < len(romanNumeral):
		if i + 1 < len(romanNumeral) and romanNumeral[i:i + 2] in romanNumerals:
			result += romanNumerals[romanNumeral[i:i + 2]]
			i += 2
		else:
			result += romanNumerals[romanNumeral[i]]
			i += 1

	return result

def camelcaseToSnakecase(camel: str) -> str:
    camel = ''.join(['_' + i.lower() if i.isupper() else i for i in camel])
    if camel[0] == '_':
        camel = camel[1:]
    return camel

def snakecaseToCamelcase():
	pass

def capitalizeFirst():
	pass
def capitalizeAll(s: str) -> str:
	return s.upper()

toUpper = capitalizeAll

def lowercaseFirst():
	pass

def lowercaseAll():
	pass
