#A4 Word Spinner
#Participant: Jiho Im (solo)
#GitHub repo link:

def main():
    # read the text file
        with open("short_text.txt") as file:
            original_text = file.read()
    #make all letters lower case and remove punctuations
    original_text_cleaned = original_text.lower().translate(str.maketrans("", "", string.punctuation))