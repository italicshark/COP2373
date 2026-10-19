import re

def find_sentences(paragraph):
    pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'
    sentences = re.findall(pattern, paragraph, flags=re.DOTALL | re.MULTILINE)
    return sentences


def main():
    paragraph = input("Enter a paragraph: ")

    sentences = find_sentences(paragraph)

    for i, sentence in enumerate(sentences, 1):
        print(f"Sentence {i}: {sentence.strip()}")

    print(f"\nTotal sentences: {len(sentences)}")


main()
