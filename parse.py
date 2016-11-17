def letterCount( file, letter ):
    count = 0

    inFile = open( file, 'r' )
    contents = inFile.read()

    for character in contents:
        if character == "a":
            count += 1
    inFile.close()
    print( "Number of occurrences: " + str(count) )

letterCount( "textFile.txt", "a" )

def largestWord( file ):
    inFile = open( file )
    contents = inFile.read()

    maxLength = 0
    biggestWord = ""
    count = 0

    for word in contents.split():
        lengthOfWord = len( word )
        bigWord = word

        if lengthOfWord > maxLength:
            maxLength = lengthOfWord
            biggestWord = bigWord

            if word == biggestWord:
                count += 1

    inFile.close()

    print( "Length of the largest word: " + str(maxLength) )
    print( "Largest word: " + biggestWord )
    print("Occurrences: " + str(count) )
largestWord( "textFile.txt" )

def locator(file, word):
    line_num = 0
    inFile = open(file)
    for line in inFile.readlines():
        line_num += 1
        if line.find(word) >= 0:
            print("line number: " + str(line_num))

locator('textFile.txt', "Writing")








