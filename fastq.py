
fastq_path = input('Enter fastq file path')

sequences = []
max_reads = 10000000
current_read = 1

with open(fastq_path) as f:
    while current_read <= max_reads:
        header = f.readline() #1st line
        sequence = f.readline() #2nd line
        plus_sign = f.readline() #3rd line
        quality = f.readline() #4th line

        sequences.append(len(sequence)) #Append lenght of sequence to a list
        current_read += 1

mean_bp = int((sum(sequences))/len(sequences))
print(mean_bp)


