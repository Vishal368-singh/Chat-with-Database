import tiktoken

def test_tokenization(text):
    
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(text)
    decoded_text = encoding.decode(tokens)
    print("Split tokens:", tokens)
    print("Decoded text:", decoded_text)
    
def main():
    Sentence = input("Enter a sentence to tokenize: ")
    test_tokenization(Sentence)

if __name__ == "__main__":
    main()
    