import nltk

def download_nltk_resources():
    """
    Download required NLTK resources.
    """
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')

download_nltk_resources()