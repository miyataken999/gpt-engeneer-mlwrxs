import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def extract_proper_nouns(text):
    """
    Extract proper nouns from a given text.

    Args:
        text (str): The input text.

    Returns:
        list: A list of extracted proper nouns.
    """
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    proper_nouns = [word for word, pos in tagged if pos in ['NNP', 'NNPS']]
    return proper_nouns

def main():
    text = "Please provide the text you want to extract proper nouns from."
    proper_nouns = extract_proper_nouns(text)
    print("Extracted proper nouns:", proper_nouns)

if __name__ == "__main__":
    main()