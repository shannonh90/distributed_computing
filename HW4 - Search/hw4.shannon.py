#!/usr/bin/env python3

import urllib.request as re;
import urllib.error as er;
import string
import pprint
import operator
from collections import defaultdict


def ReadCatalog(filename):
#reads the catalog file, creates the dictionary Books and list Titles
    try:
        with open(filename, 'rU') as f:
            Books = {}      #initiate the dictionary
            Titles = []     #initiate the list
            count = 0
            for line in f:
                data = line.split(',')
                if len(data) != 2:
                    print("The line in file, '{}' does not lead to a functional URL. \n That file will not be included in the search.".format(line))
                if len(data) > 1:
                    Books[data[0]] = [count, data[1].rstrip()]   #create keys/values for dict
                    count += 1
                    Titles.append(data[0]) 
                else:
                    pass
    except:
        print("The file is not of an expected format.")
        quit(0)
    return Books, Titles


def ReadBook(url):
    try: 
        #Open url
        response = re.urlopen(url)
        #get data, content is a string
        content = response.read()
        #close connection
        response.close()
    except(er.URLError):
        content = [ ]
        print("### NOTE: There is a non-functional URL in your file: " + url)
        print("### While the URL's contents will not be included in the search, the URL's associated book title will still be included in the <catalog>.")
    try:
        content = content.decode('utf-8')  #convert the txt at the URL from bits to strings
    except:
        # print("Could not decode the URL.")
        return [ ]
    else:
        list_of_words = content.split()
        #remove non alpha characters
        list_of_words = [''.join([char for char in word if char in string.ascii_letters]).lower() for word in list_of_words]
        #remove empty spaces
        list_of_words = [word for word in list_of_words if word.isalpha()]
        return list_of_words


def add_to_dict(Words, list_of_words, index, total_books):
    for word in list_of_words:
        if word not in Words:   #if word NOT in Dict, Words, add the word
            Words[word] = [0]*total_books   #initialize counts
        Words[word][index] += 1
    return Words


#Phase3
#Run a loop asking for search qords until it receives "terminate" 
#Report books sorted in the order of how many times a word appears
#Impement <catalog> = prints out the contents of dictioanry Books
#Implement <titles> = printso ut contents of the list Titles
#Make sure time/times matches output
#prints the count, handles the terminate, catalog
def Search(Words, Books, Titles):
    while True:
        search_word = input('Search term? ').lower()
        if not search_word:
            print('No search term entered (type "<terminate>" if you wish to quit the program)')
        elif search_word == "<terminate>":
            exit(0)
        elif search_word == "<catalog>":
            # pprint.pprint(Books)
            for k, v in Books.items():
                print("Title: {} \n Index: {} \n URL: {} \n".format(k, v[0], v[1]))    
        elif search_word == "<titles>":
            print("\n".join(Titles))
        elif search_word not in Words:
            print("The word {} does not appear in any books in the library.".format(search_word))
        else:
            word_counts_list = Words[search_word]
            word_counts_list = [pair for pair in enumerate(word_counts_list)]
            word_counts_list = sorted(word_counts_list, key=operator.itemgetter(1), reverse=True)
            # print(word_counts_list)
            list_count = 1
            for i, word_count in word_counts_list: 
            	if word_count > 0:
	                print("{a}. The word {b} appears {c} {d} in {e}\n\t(link: {f})".format(
	                	a = list_count, b = search_word, c = word_count,
	                	d = ("time" if word_count == 1 else "times"),
	                	e = Titles[i], f = Books[Titles[i]][1]) )
	                list_count += 1


def main():
    while True:
        print("Enter the file name to read:")
        filename = input('> ')
        # filename = 'hw4simplecatalog.txt'
        try:
            Books, Titles = ReadCatalog(filename)
            break
        except IOError:
            if filename == "<terminate>":
                quit(0)
            print("Unable to find and read file: {} ".format(filename))
    
    Words = {}
    for title in Books:
        dict_values = Books[title]   #initiate variables
        url = dict_values[1]        
        index = dict_values[0]
        total_books = len(Books)
        list_of_words = ReadBook(url)   #run ReadBooks for each title in Books to read each URL, create a list of words
        Words = add_to_dict(Words, list_of_words, index, total_books)  #run add_to_dict for each list of words, create a dict of all words with word counts

    # Now that the dictionary has been populated, perform any search at user's request.
    Search(Words, Books, Titles)


if __name__ == "__main__":
    main()
