from Bio.Seq import Seq
fileReader = open("mRNA.txt", "r")
mRNAData = fileReader.read()
messenger_rna = Seq(mRNAData)
print("The protein string encoded: ")
print(messenger_rna.translate())