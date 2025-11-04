import sys
from collections import Counter

def count_vowels(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read().lower()
            vowels = [c for c in text if c in "aeiou"]
            counts = Counter(vowels)
            print("Vowel frequency result:")
            for v in "aeiou":
                print(f"{v}: {counts.get(v, 0)}")
    except FileNotFoundError:
        print("File not found:", file_path)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python frequency.py <file_path>")
        sys.exit(1)
    count_vowels(sys.argv[1])
