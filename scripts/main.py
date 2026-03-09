#variables
gen = 500
q = 0.06
#main
file = open('results/csv.Sickle_cell_freq_het', 'w')
file.write("Generation\tFreq_HbS\tFreq_HbA\tFreq_Dominant\tFreq_Hetero\tFreq_Recessive\n")

for i in range(1, gen+1): 
    p = 1 - q
    freq_HbS = q
    freq_HbA = p
    freq_Dominant = p**2
    freq_Hetero = 2 * p * q
    freq_Recessive = q**2
    file.write(f'{i}\t{freq_HbS:.10f}\t{freq_HbA:.10f}\t{freq_Dominant:.10f}\t{freq_Hetero:.10f}\t{freq_Recessive:.10f}\n')
    q = q / (0.98*p+2*q) # Update q for the next generation
file.close()