
import re

# This is the main file of the project, here the interpretation for the language is done. 
# This program takes an specific file, so if you want to try it with another you must change the path in the reader function.



def reader (file_path):
    
    """
    This function reads a file with an specific language and separates it into "words" and send it 
    to the interpreter to be tokenized.
    
    Args:
        file_path (str): The path to the file to be read.
        
    Returns:
    
    List: A list with the words of the file.
    in case it does not match a word by tthe interpreter it will return a "NO" message.
      
    """
    pattern = r'([ \/\(\)\{\}])'
    final_list_of_lines = []
    
    with open(file_path, 'r') as file:
        for line in file:
            split_result = re.split(pattern, line)
            split_result = [s for s in split_result if s.strip()]
            for word in split_result:
                final_list_of_lines.append(word)
            
    
    print(final_list_of_lines)    


def interpreter (word):
    """
    This function receives a word and checks if it belongs to the language.
    
    Args:
        word (str): The word to be checked.
        
    Returns:
        str: The token of the word.
        str: A message saying that the word does not belong to the language.
    """
    
reader('LYM\pruebasOK.txt')