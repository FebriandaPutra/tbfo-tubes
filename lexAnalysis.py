import os
import sys 
import re
import rules as rule

def lexicalAnalysis(file, lex_rule):
    file = open(file, encoding="utf8")
    characters = file.read()
    file.close()

    column = 1
    line = 1

    tokens = []
    idx = 0
    while (idx < len(characters)):
        if characters[idx] == '\n':
            line += 1
            column = 1
            
        cocok = None
        for rule in lex_rule:
            identifier, keyword = rule    
            cocok = re.compile(identifier).match(characters, idx)
            if cocok:
                if keyword: #biar None (blank space) ga masuk
                    tokens.append(keyword)
                break
        if not cocok:
            print("SYNTAX ERROR")
            print(f"Unindentified character '{characters[idx]}' at line {line} and column {column}")
            sys.exit(1)
        else:
            idx = cocok.end(0)
        column += 1
   
    tokenResult = []
    for token in tokens:
        tokenResult.append(token)

    gabung = " ".join(tokenResult)
    output_file=open("tokenResult.txt","w")
    output_file.write(gabung)
    output_file.close
    
    return tokenResult