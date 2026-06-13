charDict = {
    "A" : ".-", "B" : "-...",
    "C" : "-.-.", "D" : "-..",
    "E" : ".", "F" : "..-.",
    "G" : "--.", "H" : "....",
    "I" : "..", "J" : ".---",
    "K" : "-.-,", "L" : ".-..",
    "M" : "--", "N" : "-.",
    "O" : "---", "P" : ".--.",
    "Q" : "--.-", "R" : ".-.",
    "S" : "...", "T" : "-",
    "U" : "..-", "V" : "...-",
    "W" : ".--", "X" : "-..-",
    "Y" : "-.--", "Z" : "--..",
    
    " " : "/"
}

def txttomorse(str1):
    morse = ""
    for i in str1.upper():
        morse += charDict.get(i, "NOT FOUND")
        morse += ' '
    
    return morse



str1 = input("Enter your text : ")
print(f"Morse code for your input is : {txttomorse(str1)}")