#1.converting the altered DNA to protein
import  importlib
modName = input ('DNAFile.txt')
importlib.import_module(modName)

inputfile = "DNAFile.txt"
f =open(inputfile, "r")
seq = f.read()#reading the textfile

seq = seq.replace("\n"," ")#replace all instances of new lines
seq = seq. replace("\r", " ")#replace all carriage return that is stored in the seq var

#2.Creating function called translate that 
def translate(seq):
    table = {'ATA':'I','ATC':'I','ATT':'I'
            ,'ATG':'M','ACG':'T','ACU':'T',
            'UUA':'L','CUU':'L','CUA':'L'}
    protein =" "
    if not len(seq)%3==0:
        for i in range(0,len(seq),3):
            codon = seq [i:i+3]
            table[codon]
            return protein
        else:
            return 'X'
            
#3.Write a function that will mutate
def mutate(inputfile):
    with open(inputfile,"r")as f:
        seq = f.read()
        seq = seq.replace("\n"," ")
        seq = seq.replace("\r", " ")
        return seq
    prt= mutate("normalDNA.txt")
    dna = mutate ("mutatedDNA.txt")
    
    p=translate(dna[20:935])
    p ==prt


