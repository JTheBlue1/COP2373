##Using the code in Section 7.4, write a program that will allow me to have any number of
##sentences, including sentences which begin with numbers.
##Display the sentences and the count of sentences.

import re

def sentences_s(text):
    # create the regular expression pattern to identify sentences
    reg_pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'

    #locate the sentences in the text
    final_sentences = re.findall(reg_pattern, text, flags=re.DOTALL | re.MULTILINE)

    # exclude empty strings and spaces
    return [sentence.strip() for sentence in final_sentences if sentence.strip()]


def main():
    # prompt user for input
    text = input("Please enter the text: ")

    # split text into sentences
    final_sentences = sentences_s(text)

    # display each sentence with number
    for int, final_sentence in enumerate(final_sentences, start=1):
        print(f"Sentence {int}: {final_sentence}")

    # display the total amount of sentences shown
    print(f"\nTotal sentences: {len(final_sentences)}")


if __name__ == "__main__":
    main()