def count_words_and_chars(text):
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    return word_count, char_count


def main():
    user_input = input("Enter a sentence or paragraph: ").strip()
    if not user_input:
        print("Please enter some text.")
        return

    words, chars = count_words_and_chars(user_input)
    print(f"Total words: {words}")
    print(f"Total characters (with spaces): {chars}")


if __name__ == "__main__":
    main()
  
