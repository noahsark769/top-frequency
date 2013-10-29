from collections import defaultdict

def most_frequent_words(corpus, n):
    """Given a large string representing a text document,
    return a list of the n most frequent words in the string.

    Args:
        corpus - a string
        n - an integer representing the number of most frequent words
            to return, in order of frequency, with ties broken
            arbitrarily.

    Returns:
        a list of the n most frequent words

    Raises:
        ValueError if either of the arguments are improperly formatted
    """
    word_to_frequency = defaultdict(lambda: 0) # a dict mapping words to their frequencies
    frequency_to_words = defaultdict(set) # a dict mapping a frequency to a set of words with that frequency
    non_empty_frequencies = set() # a set of all the frequencies for which there are words with that frequency
    max_frequency = 0 # the maximum frequency of any word
    words = corpus.strip().split(" ")

    # iterate through all the words in the corpus.
    # for each word, increment its frequency. remove the word
    # from the old frequency entry, and add it to the new one.
    # update the max if needed.
    for word in words:
        # the current frequency of the word that we've noted so far:
        curr_word_frequency = word_to_frequency[word]

        # say a word currently has frequency 4, but we've seen it again, so
        # we want to increment it to 5. we have to remove the word from the frequency 4
        # set and add it to the frequency 5 set. additionally, if frequency 4 no longer
        # has any words, we'll remove it from the set of non empty frequencies.
        if curr_word_frequency > 1:
            frequency_to_words[curr_word_frequency].remove(word)
            if len(frequency_to_words[curr_word_frequency]) == 0:
                non_empty_frequencies.remove(curr_word_frequency)

        # now, actually increment the frequency
        word_to_frequency[word] += 1
        new_frequency = word_to_frequency[word]

        # update the maximum frequency we've seen so far
        if new_frequency > max_frequency:
            max_frequency = new_frequency

        # if frequency 5 is still believed to be empty, then we say it's not anymore
        if new_frequency not in non_empty_frequencies:
            non_empty_frequencies.add(new_frequency)

        # and add the current word to the set of words with frequency 5
        frequency_to_words[new_frequency].add(word)

    # now, start with the maximum frequency, and take words in
    # decreasing order of frequency and print them.
    result = []
    frequency = max_frequency
    num_printed = 0
    while frequency != 0 and num_printed < n:
        if frequency in non_empty_frequencies:
            words_with_this_frequency = frequency_to_words[frequency]
            while len(words_with_this_frequency) != 0 and num_printed <= n:
                result.append(words_with_this_frequency.pop())
                num_printed += 1
        frequency -= 1
    return result

def print_most_frequent_words(corpus, n):
    """Given a large text document as a string, print the n most frequent words."""
    for word in most_frequent_words(corpus, n):
        print word
