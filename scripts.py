import os
import re
import socket
from collections import Counter
import os.path

def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        # Split text into words, removing punctuation and converting to lowercase
        words = re.findall(r'\b\w+\b', text.lower())
        return len(words), words

def handle_contractions(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        # Replace common contractions with full forms
        text = re.sub(r"n't", " not", text)
        text = re.sub(r"'re", " are", text)
        text = re.sub(r"'m", " am", text)
        text = re.sub(r"'ve", " have", text)
        text = re.sub(r"'ll", " will", text)
        text = re.sub(r"'d", " would", text)
        text = re.sub(r"'s", " is", text)
        
        # Split text into words
        words = re.findall(r'\b\w+\b', text.lower())
        return len(words), words

def get_ip_address():
    try:
        # Get the hostname first
        hostname = socket.gethostname()
        # Get the IP address
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except:
        return "Could not determine IP address"

def main():
    # Create output directory if it doesn't exist
    os.makedirs('/home/data/output', exist_ok=True)
    
    # Define file paths
    if_file = '/home/data/IF-1.txt'
    always_file = '/home/data/AlwaysRememberUsThisWay-1.txt'
    output_file = '/home/data/output/result.txt'
    
    # Process IF-1.txt
    if_word_count, if_words = count_words(if_file)
    
    # Process AlwaysRememberUsThisWay-1.txt with contraction handling
    always_word_count, always_words = handle_contractions(always_file)
    
    # Calculate total word count
    total_word_count = if_word_count + always_word_count
    
    # Find top 3 most frequent words in IF-1.txt
    if_counter = Counter(if_words)
    if_most_common = if_counter.most_common(3)
    
    # Find top 3 most frequent words in AlwaysRememberUsThisWay-1.txt
    always_counter = Counter(always_words)
    always_most_common = always_counter.most_common(3)
    
    # Get IP address
    ip_address = get_ip_address()
    
    # Write results to output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("Word Count Analysis\n")
        file.write("===================\n\n")
        
        file.write(f"1. Word count in IF-1.txt: {if_word_count}\n")
        file.write(f"2. Word count in AlwaysRememberUsThisWay-1.txt: {always_word_count}\n")
        file.write(f"3. Total word count: {total_word_count}\n\n")
        
        file.write("4. Top 3 most frequent words in IF-1.txt:\n")
        for word, count in if_most_common:
            file.write(f"   - '{word}': {count} occurrences\n")
        
        file.write("\n5. Top 3 most frequent words in AlwaysRememberUsThisWay-1.txt (with contractions handled):\n")
        for word, count in always_most_common:
            file.write(f"   - '{word}': {count} occurrences\n")
        
        file.write(f"\n6. IP Address of the container: {ip_address}\n")
    
    # Print the results to console
    with open(output_file, 'r', encoding='utf-8') as file:
        print(file.read())

if _name_ == "_main_":
    main()
