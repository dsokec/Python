#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# This was an error
# word_per_page == int(input("Number of words per page: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)