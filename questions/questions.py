import itertools
import nltk
import sys
import string
import os
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """

    # Introduce empty dictionary
    load = dict()
    # List of the all file in the path
    for i in os.listdir(os.path.join(os.getcwd(), directory)):
        # Open and read text in latin format
        with open(os.path.join(os.getcwd(), directory, i), encoding="utf8") as f:
            load.update({i: f.read()})
    
    return load


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """

    s =  [word.lower() for word in nltk.tokenize.word_tokenize(document)]
    s_new = []
    for i in s:
        if i not in nltk.corpus.stopwords.words("english") and i not in string.punctuation:
            s_new.append(i)
    return s_new


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """

    # Empty dictionary to compute idfs
    idf = dict()
    for d in documents.keys():
        for word in documents[d]:
            i = 0
            for d in documents.keys():
                if word in documents[d]:
                    i += 1
            idf.update({word: math.log(len(documents.keys())/i)})
    
    return idf


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    
    # Empty dictionary for selected files
    
    top = []
    for f in files:
        i = 0
        for word in query:     
            i += idfs[word] * files[f].count(word)
        top.append((f, i))
    
    # Sorting in descending order 
    top.sort(key=lambda item: item[1], reverse= True)
    # Select n file from files
    best = []
    for j in range(n):
        best.append(top[j][0])
    return best


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    
    # Empty dictionary for selected sentences
    sen = {}
    for f in sentences:
        i = 0
        j = 0
        for word in query:
            if word in sentences[f]:
                i += idfs[word]
                j += 1
        sen.update({f:[i, float(j/len(sentences[f]))]})
    # Sorting in descending order with idf
    sen = dict(sorted(sen.items(), key=lambda item: (item[1][0], item[1][1]) ,reverse= True))
    sen = dict(itertools.islice(sen.items(), n))
    return sen


if __name__ == "__main__":
    main()

