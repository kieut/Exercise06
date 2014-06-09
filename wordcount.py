from sys import argv

script, filename = argv

def main():
    my_file = open(filename)

    word_count = {}

    for line in my_file:
        line = line.rstrip().lower()
        words = line.rsplit(' ')
        

        for word in words:
            if ord(word[-1]) < 97:
                word = word[0:-1] 
            #dict.setdefault will set dict[key] = default if key is not in dictionary
            # it will insert the key into the dictionary if not there
                word_count[word] = word_count.setdefault(word, 0) + 1
            #elif ord(word[-1]) > 122:
                #word = word[0:-1]
                #word_count[word] = word_count.setdefault(word, 0) + 1 
            else: 
                word_count[word] = word_count.setdefault(word, 0) + 1

    # In Python, you don't have to define variables before using them. key, value
    for key, value in sorted(word_count.items()):
        print key, value


if __name__ == '__main__':
     main() 

