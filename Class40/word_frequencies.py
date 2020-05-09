

def main():

    filename = input("Enter a filename: ")

    file_to_read = open(filename, "r")

    file_contents = file_to_read.read()
    words = file_contents.split()

    word_frequencies = {} # word - frequency pairs

    for word in words:
        prev_freq = word_frequencies.get(word, 0)
        word_frequencies[word] = prev_freq + 1

    print(word_frequencies)

    for key in word_frequencies:
        print(word_frequencies[key], " = ", key)




if __name__ == "__main__":
    main()
