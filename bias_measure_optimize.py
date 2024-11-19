import numpy as np
import os, psutil, time

start_time = time.time()

def calculate_probabilities(text, level='char'):
    if not text:  # Empty string check
        return np.array([])  # Return empty array if text is empty
    items = list(text) if level == 'char' else text.split()
    _, counts = np.unique(items, return_counts=True)
    return counts / counts.sum() if counts.size > 0 else np.array([])  # Handle empty counts


def calculate_entropy(probabilities, base=np.e, epsilon=1e-10):
    probabilities = np.clip(probabilities, epsilon, 1)  # Avoid log(0)
    return -np.sum(probabilities * np.log(probabilities) / np.log(base))

def calculate_perplexity(entropy, base=np.e):
    return base ** entropy

def calculate_normalized_entropy(entropy, num_unique_items, base=np.e):
    if num_unique_items <= 1:  
        return 0
    return entropy / np.log(num_unique_items)

def calculate_surprisal(probabilities, base=np.e, epsilon=1e-10):
    if probabilities.size == 0:
        return 0
    return -np.log(probabilities) / np.log(base)


def calculate_metrics_for_text(text):
    char_probs = calculate_probabilities(text, level='char')
    word_probs = calculate_probabilities(text, level='word')
    entropy_char = calculate_entropy(char_probs)
    entropy_word = calculate_entropy(word_probs)
    perplexity_char = calculate_perplexity(entropy_char)
    perplexity_word = calculate_perplexity(entropy_word)
    normalized_entropy_char = calculate_normalized_entropy(entropy_char, len(set(text)))
    surprisal_char = np.mean(calculate_surprisal(char_probs))
    
    surprisal_word = np.mean(calculate_surprisal(word_probs))

    return {
        'Length': len(text),
        'Character Entropy': entropy_char,
        'Word Entropy': entropy_word,
        'Character Perplexity': perplexity_char,
        'Word Perplexity': perplexity_word,
        'Normalized Entropy': normalized_entropy_char,
        'Word Surprisal': surprisal_char,
        'Char Surprisal': surprisal_word
    }

def write_metrics_to_file(output_file, metrics, texts):
    output_file.write(f"{'Metric':<30}")
    for i in range(len(texts)):
        output_file.write(f"{f'File {i+1}':<20}")
    output_file.write("\n" + "=" * (30 + 20 * len(texts)) + "\n")

    # Write each metric row by row
    for metric, values in metrics.items():
        output_file.write(f"{metric:<30}")
        for value in values:
            output_file.write(f"{value:<20}")
        output_file.write("\n")
    
def compile_data(input_files, output_file_path):
    # Read all lines from each input file and flatten them into a single list
    texts = []
    for file_path in input_files:
        with open(file_path, "r") as f:
            texts.extend(f.read().splitlines())

    # Calculate metrics for each text
    metrics = {metric: [] for metric in ['Length', 'Character Entropy', 'Word Entropy', 'Character Perplexity', 'Word Perplexity', 'Normalized Entropy', 'Char Surprisal', 'Word Surprisal']}
    
    for text in texts:
        text_metrics = calculate_metrics_for_text(text)
        for metric in text_metrics:
            metrics[metric].append(text_metrics[metric])

    # Write metrics to output file
    with open(output_file_path, "w") as output_file:
        write_metrics_to_file(output_file, metrics, texts)
        output_file.write("=" * (30 + 20 * len(texts)) + "\n")
        output_file.write("Metrics Comparison for Language Complexity and Bias\n")
        output_file.write("=" * (30 + 20 * len(texts)) + "\n")
        output_file.write("The following metrics measure different aspects of linguistic complexity and usage:\n")
        output_file.write(" - Character Entropy: Measures the variety of characters, indicating vocabulary richness and complexity.\n")
        output_file.write(" - Word Entropy: Reflects the diversity of words, providing insight into the vocabulary range.\n")
        output_file.write(" - Perplexity: Indicates how predictable the language is, with higher values suggesting more complex language.\n")
        output_file.write(" - Normalized Entropy: Adjusts entropy for text length, allowing fair comparison across varying text lengths.\n")
        output_file.write(" - Surprisal: Measures how unexpected the words or characters are based on frequency, highlighting reader difficulty.\n")
        output_file.write("=" * (30 + 20 * len(texts)) + "\n\n")

def compare_data(input_files, output_file_path):
    # Read all lines from each input file and flatten them into a single list
    texts = []
    for file_path in input_files:
        with open(file_path, "r") as f:
            texts.extend(f.read().splitlines())

    # Calculate metrics for each text
    metrics = {metric: [] for metric in ['Length', 'Character Entropy', 'Word Entropy', 'Character Perplexity', 'Word Perplexity', 'Normalized Entropy', 'Char Surprisal', 'Word Surprisal']}
    
    for text in texts:
        text_metrics = calculate_metrics_for_text(text)
        for metric in text_metrics:
            metrics[metric].append(text_metrics[metric])

    # Write average of each metric to output file
    with open(output_file_path, "w") as output_file:
        output_file.write(f"{'Metric':<30}")
        output_file.write("\n")
        
        for metric, values in metrics.items():
            average_value = sum(values) / len(values)
            output_file.write(f"{metric:<30}{average_value:<20}\n")

def main():
    input_file_paths = ["pubmed_2020_sample.txt", "pubmed_2024_sample.txt"]
    output_file_path = "comparison.txt"
    output_comparison_file_path = "avg_data.txt"

    compile_data(input_file_paths, output_file_path)  # For full metric comparison
    compare_data(input_file_paths, output_comparison_file_path)  # For average comparison

    # Execution time and memory usage
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")
    process = psutil.Process(os.getpid())
    print('Memory usage in Mega Bytes: ', process.memory_info().rss / (1024 ** 2))

if __name__ == "__main__":
    main()
import numpy as np
import os, psutil, time

start_time = time.time()

