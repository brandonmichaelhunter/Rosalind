def convertLettersListToString(lst):
    str1 = ""
    return (str1.join(lst))
def NumberListToStringWithSpaces(Numbers):
    retString = ""
    for number in Numbers:
        retString += " {}".format(number)
    return retString

s = "TCCTATGAACTATGAAGCTATGAACGTCTATGAACCATGCTATGAAAATATATCCCCGGCGACACTATGAAGTCCTATGAATTACTGTCATTGGCTTTTAGGGCTATGAACTATGAATAAGACTATGAACTCTATGAAGCTTACTTGTCTATGAACACTATGAAGCTATGAACTATGAAATTTTCTATGAAGCTATGAACTATGAATGTGCTATGAAACTATGAAAGCTATGAAGGTGACTATGAAGCACTATGAACTATGAAGTGCTATGAACACTCTATGAAACTATGAAATACTATGAATCTATGAATCACCTATGAATCTATGAAGCTATGAAACTATGAAGCTATGAACATAACCCTATGAACTATGAACTTACGGGCACCTATGAACTATGAACTATGAAGCTATGAAACTATGAAGCACTCTATGAAATCTATGAACTATGAACCCTATGAACTATGAATATCTATGAACTATGAACTATGAACCTATGAATAAGGCTATGAAGTTAAGTTACAGTTCTTCCGAATGACTATGAAAGCTATGAAGCTATGAAGGTACTATGAATCCTATGAACACCCTATGAAGTTGCCCTATGAAGCTATGAACTATGAAACCTATGAACTATGAACTATGAACTATGAACTATGAATTTGCCTATGAACTATGAAGGTCTATGAATCTCTATGAAGTCCCTATGAACTATGAAAACTATGAACTATGAAACTATGAAGCTATGAACTATGAACAAGCTATGAATGGCGAAGTACTATGAACTTACACTATGAAGTCTATGAAAAACTATGAATCTATGAACTCTATGAATTCGCTTGCAACTATGAACTATGAACTATGAACCTATGAAATATTAAC"
t = "CTATGAACT"

# Enable debugging
DEBUG_ENABLED = False
# turn s into a list.
sList = list(s)

# get the length of t
tLength = len(t)

# turn t into a list
tList = list(t)

# store the location of where t is found in s.
positions = []
# loop through s list.
countIndex = 0
for letter in sList:
    
    if(letter == tList[0]): 
       startIndex = countIndex
       endIndex = startIndex + tLength
       # find the substring within the DNA string using the start and end index values.
       substringDNA = convertLettersListToString(sList[startIndex:endIndex]) 
       
       if(substringDNA == t):
          if(DEBUG_ENABLED == True):
             print(letter == tList[0])
             print("Current Index: {}".format(countIndex))
             print("Letter {} - compare with {}".format(letter, tList[0]))
             print("Length: {}".format(tLength))
             print("Start Index: {}".format(startIndex))
             print("End Index: {}".format(endIndex))
             print("Search DNA: {} == t {}".format(substringDNA, t))
             print("---------------------")
          position = countIndex + 1
          positions.append(position)
    countIndex += 1
answer = NumberListToStringWithSpaces(positions)
print("The answer is: {}".format(answer))

       