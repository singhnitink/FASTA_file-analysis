###Python Code for the analysis of Fasta files for the chemical analysis data
filename=input("Enter the name of FASTA file: ")
data = open(filename, 'r')
count_residues =open('Analysis_data.dat','w')
aa=['K','R','H','E','D','G','A','V','C','I','L','M','F','Y','W','P','S','T','N','Q']
aa_list=[]
for line in data:
    if line.startswith('>')!=True:
        #print(line)
        for alphabet in line:
            #print(alphabet)
            if alphabet.upper() in aa:
                entry=alphabet.upper()
                aa_list.append(entry)
#print(aa_list)
total_aa=len(aa_list)     ##total number of amino acids
namex=['K','R','H','E','D']
namep=['K','R','H']
namen=['E','D']
namenonpolar=['G','A','V','C','I','L','M','F','Y','W','P']
namepolar=['S','T','N','Q']
positive=0
negative=0
polar=0
nonpolar=0
count=0
while count<total_aa:
    if aa_list[count] in namep:
        positive+=1
    elif aa_list[count] in namen:
        negative+=1
    elif aa_list[count] in namenonpolar:
        nonpolar+=1
    elif aa_list[count] in namepolar:
        polar+=1
    count+=1

total_charge=positive-negative
fr_charged=(positive+negative)/total_aa
fr_polar=polar/total_aa
fr_nonpolar=nonpolar/total_aa
#print(positive,negative,nonpolar,polar,total_charge,fr_charged,fr_polar,fr_nonpolar)
count_residues.write(' Total-aa \t %d \n Positive-aa \t %d \n Negative-aa \t %d \n Charged-aa \t %d \n Nonpolar-aa \t %d \n Polar-aa  \t %d \n Total-Charge \t %d \n Fr-charged \t %2.2f \n Fr-polar  \t %2.2f \n Fr-nonpolar \t %2.2f \n'%(total_aa,positive,negative,(positive+negative),nonpolar,polar, total_charge,fr_charged,fr_polar,fr_nonpolar))
data.close()
count_residues.close()
