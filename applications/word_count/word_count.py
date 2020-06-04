def word_count(s):
    # Your code here
    # Convert string to lowercase and remove bad characters
    # Split the string into a list
    # Loop through the list
    # If the list item is in the dictionary, add to its count
    # If it's not, initialize it
    # Return the dictionary
    wordCounts = {}
    s = s.lower().translate(str.maketrans("", "", '":;,.-+=/\\|[]{}()*^&'))
    words = s.split()

    for w in words:
        if w in wordCounts:
            wordCounts[w] +=1
        else:
            wordCounts[w] = 1
    return wordCounts



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))