# Code copied from https://github.com/Jac21/GistsCollection/blob/master/Python/Rosalind/11%20-%20Mendel's%20First%20Law.py
import itertools

def dominant_probability(num_homozygous_dominant, num_heterozygous, num_homozygous_recessive):
	total = num_homozygous_dominant + num_heterozygous + num_homozygous_recessive

	recessive_probability = (num_homozygous_recessive / total) * ((num_homozygous_recessive - 1) / (total - 1))
	heterozygous_probability = (num_heterozygous / total) * ((num_heterozygous - 1) / (total - 1))
	hetero_recessive_probability = (num_heterozygous / total) * (num_homozygous_recessive / (total - 1)) + (num_homozygous_recessive / total) * (num_heterozygous / (total - 1))

	recessive_total = recessive_probability + heterozygous_probability * (.25) + hetero_recessive_probability * (.5)
	return (1 - recessive_total)

result = round(dominant_probability(16.0, 17.0, 26.0), 5)
print(result)