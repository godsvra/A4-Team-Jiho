#A4 Word Spinner
#Participant: Jiho Im (solo)

#class Spinner
import random

class Spinner:
    def __init__(self, file):
        self.synonym_dict = {}
        with open(file) as file:
            for line in file:
                #remove blank lines (and extra spaces) at the beginning and end of a string
                line = line.strip()
                #first split it by ':'
                key_and_values = line.split(':')
                #store the first one as key
                key = key_and_values[0]
                #store the rest as synonyms
                synonyms = key_and_values[1].split(',')
                #store the key and value in the dictionary
                self.synonym_dict[key] = synonyms



