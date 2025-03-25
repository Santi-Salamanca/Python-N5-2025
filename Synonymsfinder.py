from spellchecker import SpellChecker
from colorama import Fore #adds function to change  text colour
import nltk
from nltk.corpus import wordnet
nltk.download('wordnet') # downloads wordnet

#synonyms finding function
def synonymsfind(i, limit=10): #limit changes the amount of synonyms that will be shown to the user
    synsets = wordnet.synsets(i) #find the dictionary like set thingy for the word
    synonyms = [] # creats list for synonyms to go to
    for i in synsets: # loops through each synset
        for lemma in i.lemmas(): # Get all lemmas (synonyms) for the synset
            synonyms.append(lemma.name())
    return list(set(synonyms))[:limit] # Remove duplicates and limit the number of synonyms

print(Fore.YELLOW + "Welcome to the Synonyms Finder!")
print(Fore.GREEN + "To use this programme, all you have to do is input your word you want to find a synonym for. And voila!")


spell = SpellChecker() #spellchecker function
while True:
    word = str(input(Fore.LIGHTBLACK_EX + "Enter the word: ")).strip().lower()
    corrected_word = spell.correction(word)
    synonyms = synonymsfind(corrected_word)
    if synonyms:
        print(Fore.CYAN + "synonyms for the word" + "", corrected_word,"are:", Fore.LIGHTWHITE_EX + "",synonyms)
    else:
        print(Fore.RED + "word has no snyonyms")



