import numpy as np


def calculate_probabilities(text, level='char'):
    """
    Calculate probability distribution of characters or words in text.
    Parameters:
        text (str): Input text for analysis.
        level (str): 'char' for character level, 'word' for word level.
    Returns:
        np.array: Probability distribution of characters or words.
    """
    items = list(text) if level == 'char' else text.split()
    _, counts = np.unique(items, return_counts=True)
    return counts / counts.sum()

def calculate_entropy(probabilities, base=np.e):
    return -np.sum(probabilities * np.log(probabilities) / np.log(base))

def calculate_perplexity(entropy, base=np.e):
    return base ** entropy

def calculate_normalized_entropy(entropy, num_unique_items, base=np.e):
    if num_unique_items == 0 or num_unique_items == 1:
        return 0
    normalized_entropy = entropy / np.log(num_unique_items)
    return normalized_entropy

def calculate_surprisal(probabilities, base=np.e):
    return -np.log(probabilities) / np.log(base)

# Metrics calculation functions
def char_entropy(text, base=np.e):
    probabilities = calculate_probabilities(text, level='char')
    return calculate_entropy(probabilities, base)

def word_entropy(text, base=np.e):
    probabilities = calculate_probabilities(text, level='word')
    return calculate_entropy(probabilities, base)

def char_perplexity(text, base=np.e):
    entropy = char_entropy(text, base)
    return calculate_perplexity(entropy, base)

def word_perplexity(text, base=np.e):
    entropy = word_entropy(text, base)
    return calculate_perplexity(entropy, base)

def normalized_entropy(text, base=np.e):
    probabilities = calculate_probabilities(text, level='char')
    entropy = calculate_entropy(probabilities, base)
    return calculate_normalized_entropy(entropy, len(set(text)), base)

def surprisal(text, level='char', base=np.e):
    probabilities = calculate_probabilities(text, level=level)
    if probabilities.size == 0:
        return 0
    surprisal_values = -np.log(probabilities) / np.log(base)
    return surprisal_values.mean() 

def comparison(input_file1, input_file2, input_file3, output_file):
    # Placeholder implementation
    text1 = input_file1.read()
    text2 = input_file2.read()
    text3 = input_file3.read()
        
    # Example comparison logic
    output_file.write(f"{'Metric':<30}{'File 1 (elementaryschool)':<20}{'File 2 (middleschool)':<20}{'File 3(highschool)':<20}\n")
    output_file.write("="*90 + "\n")
        
    output_file.write(f"{'Length':<30}{len(text1):<20}{len(text2):<20}{len(text3):<20}\n")
        
    char_entropy1 = char_entropy(text1)
    char_entropy2 = char_entropy(text2)
    char_entropy3 = char_entropy(text3)
    output_file.write(f"{'Character Entropy':<30}{char_entropy1:<20}{char_entropy2:<20}{char_entropy3:<20}\n")
        
    word_entropy1 = word_entropy(text1)
    word_entropy2 = word_entropy(text2)
    word_entropy3 = word_entropy(text3)
    output_file.write(f"{'Word Entropy':<30}{word_entropy1:<20}{word_entropy2:<20}{word_entropy3:<20}\n")
        
    char_perplexity1 = char_perplexity(text1)
    char_perplexity2 = char_perplexity(text2)
    char_perplexity3 = char_perplexity(text3)
    output_file.write(f"{'Character Perplexity':<30}{char_perplexity1:<20}{char_perplexity2:<20}{char_perplexity3:<20}\n")
        
    word_perplexity1 = word_perplexity(text1)
    word_perplexity2 = word_perplexity(text2)
    word_perplexity3 = word_perplexity(text3)
    output_file.write(f"{'Word Perplexity':<30}{word_perplexity1:<20}{word_perplexity2:<20}{word_perplexity3:<20}\n")
    
    normalized_entropy1 = normalized_entropy(text1)
    normalized_entropy2 = normalized_entropy(text2)
    normalized_entropy3 = normalized_entropy(text3)
    output_file.write(f"{'Normalized Entropy':<30}{normalized_entropy1:<20}{normalized_entropy2:<20}{normalized_entropy3:<20}\n")
        
    surprisal1 = surprisal(text1)
    surprisal2 = surprisal(text2)
    surprisal3 = surprisal(text3)
    output_file.write(f"{'Surprisal':<30}{surprisal1:<20}{surprisal2:<20}{surprisal3:<20}\n")
   
    output_file.write("="*90 + "\n")
    output_file.write("Metrics Comparison for Language Complexity and Bias\n")   
    output_file.write("The following metrics measure different aspects of linguistic complexity and usage:\n")
    output_file.write(" - Character Entropy: Measures the variety of characters, indicating vocabulary richness and complexity.\n")
    output_file.write(" - Word Entropy: Reflects the diversity of words, providing insight into the vocabulary range.\n")
    output_file.write(" - Perplexity: Indicates how predictable the language is, with higher values suggesting more complex language.\n")
    output_file.write(" - Normalized Entropy: Adjusts entropy for text length, allowing fair comparison across varying text lengths.\n")
    output_file.write(" - Surprisal: Measures how unexpected the words or characters are based on frequency, highlighting reader difficulty.\n")
    
    
    input_file1.close()
    input_file2.close()
    input_file3.close()
    output_file.close()


def main():
     input_file1_path = "wiki_elem.txt" #randomly selected a wikipedia article, asked chat gpt to summarize it for different age levels using the same prompt
     input_file2_path = "wiki_college.txt"
     input_file3_path = "wiki_og.txt"
     #input_file1_path = "comparison_file1.txt" //asked chat gpt to write an essay on the same topic and lenght for different age levels
     #input_file2_path = "comparison_file2.txt"
     #input_file3_path = "comparison_file3.txt"
     output_file_path = "comparison.txt"
        
     input_file1 = open(input_file1_path, "r")
     input_file2 = open(input_file2_path, "r")
     input_file3 = open(input_file3_path, "r")
     output_file = open(output_file_path, "w")
     
     
    
     comparison(input_file1, input_file2, input_file3, output_file)
   
    # text = "This is a sample text for calculating entropy and perplexity."
    # print("Character entropy of the text:", char_entropy(text))
    # print("Word entropy of the text:", word_entropy(text))
    # print("Character perplexity of the text:", char_perplexity(text))
    # print("Word perplexity of the text:", word_perplexity(text))
    # print("Normalized entropy of the text:", normalized_entropy(text))
    # print("Surprisal of the text:", surprisal(text))


main()

  