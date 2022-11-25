from grammar_converter import readGrammarFile
from grammar_converter import mapGrammar
from grammar_converter import convertGrammar
from lexAnalysis import lexicalAnalysis
from cyk import cyk
import re
import os
import sys
import argparse
from rules import lex_rule
import time

def main():
  # Argparse, mengambil argument dari CLI
  parser = argparse.ArgumentParser()
  parser.add_argument(" File ",type = argparse.FileType('r'))
  args = parser.parse_args()

  # Parsing script JavaScript
  print()
  print("JavaScript Parser")
  print("_________________________")
  time.sleep(2)
  print()
  
  # Konversi code dalam file script menjadi token 
  token = lexicalAnalysis(args.file.name,lex_rule)
  print(token)

  # Buat CNF berdasarkan grammar CFG
  CNFgrammar = mapGrammar(convertGrammar((readGrammarFile("cfg.txt"))))
  print("Result : ", end ="")
  cyk(token, CNFgrammar)
  print("_______________________________________________________________")

if __name__ == "__main__":
  main()