from collections import defaultdict

# def letterCount( file, letter ):
#     count = 0
#
#     inFile = open( file, 'r' )
#     contents = inFile.read()
#
#     for character in contents:
#         if character == letter:
#             count += 1
#     inFile.close()
#     print( "Number of occurrences: " + str(count) )

def largestWord( file ):
    inFile = open( file )
    contents = inFile.read()
    dict = defaultdict()

    for word in contents.split():
        dict[word] = len(word)
    for word in sorted(dict, key=dict.get, reverse=True):
        print word, dict[word]
    inFile.close()
    
# def locator(file, word):
#     line_num = 0
#     inFile = open(file)
#     for line in inFile.readlines():
#         line_num += 1
#         if line.find(word) >= 0:
#             print("line number: " + str(line_num))
#     inFile.close()

# def textFileReverse(file):
#     inFile = open(file)
#     contents = inFile.readlines()
#     for line in reversed(contents):
#         print(line.rstrip())
#     inFile.close()

if __name__ == "__main__":

    # textFileReverse("textFile.txt")
    # letterCount("textFile.txt", "a")
    largestWord("textFile.txt")
    # locator('textFile.txt', "Writing")



