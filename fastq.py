import timeit
from collections import Counter

#Ion P1 Adapter
'''
5'–CCACTACGCCTCCGCTTTCCTCTCTATGGGCAGTCGGTGAT–3'
3'–T*T*GGTGATGCGGAGGCGAAAGGAGAGATACCCGTCAGCCACTA–5'
'''

#FASTQ quality ASCII
'''
!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHI
'''

q_score_dict = {'!': 0, '"': 1, '#': 2, '$': 3, '%': 4, '&': 5, "'": 6, '(': 7, ')': 8, '*': 9, '+': 10,
                 ',': 11, '-': 12, '.': 13, '/': 14, '0': 15, '1': 16, '2': 17, '3': 18, '4': 19, '5': 20,
                   '6': 21, '7': 22, '8': 23, '9': 24, ':': 25, ';': 26, '<': 27, '=': 28, '>': 29, '?': 30,
                     '@': 31, 'A': 32, 'B': 33, 'C': 34, 'D': 35, 'E': 36, 'F': 37, 'G': 38, 'H': 39, 'I': 40}

q_scores = Counter() #empty dict to be populated with q-score counts

def main():
    #fastq_path = r"C:\Users\32313\Desktop\Scripts\FASTQ\example.fastq"
    fastq_path = input('Enter fastq file path: ').strip('"')
    #fastq_path = fastq_path.strip('"')
    sequences_lenght = []

    with open(fastq_path) as f:
        while True:
            header = f.readline() #1st line
            if header.strip() == '':
                break
            sequence = f.readline() #2nd line
            plus_sign = f.readline() #3rd line
            quality = f.readline() #4th line

            sequences_lenght.append(len(sequence.strip())) #Append lenght of sequence to a list
            q_scores.update(quality.strip()) #Updates the counter. Chars are added to the dict as they appear. New appearances of the same char adds to the count

    #Get total bases and calculate mean read lenght
    total_bases = sum(sequences_lenght)
    mean_bp = round((total_bases)/len(sequences_lenght))
    print(f'Mean read lenght: {mean_bp}bp')
    
    #Get quality scores and output % of Q30 and Q20 bases
    Q30 = 0
    Q20 = 0

    for char in q_scores:
        if q_score_dict[char] >= 30:
            Q30 += q_scores[char]
        if q_score_dict[char] >= 20:
            Q20 += q_scores[char]     
        #print (char, q_scores[char])
    
    Q30_percent = round(((Q30 / total_bases)*100), 3)
    Q20_percent = round(((Q20 / total_bases)*100), 3)

    print(f'Q30 bases = {Q30} ({Q30_percent}%)')
    print(f'Q20 bases = {Q20} ({Q20_percent}%)')

main()
#print('\nTime taken:', round(timeit.timeit(main, number=1), 3), 'seconds')
