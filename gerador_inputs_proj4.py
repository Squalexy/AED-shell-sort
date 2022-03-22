import random


def seq_aleatoria(n_inputs, N):
	for i in range(n_inputs):
		with open("inputs2/seq_aleatoria" + str(i).zfill(2) + ".txt", "w") as escrever:
			escrever.write(str(N) + "\n")
			num_list = []
			for j in range(N):
				num_list += [j]
			random.shuffle(num_list)
			for j in range(N):
				escrever.write(str(num_list[j]) + "\n")

		if i == 0:
			N += 49_000
		else:
			N += 50_000


def seq_decrescente(n_inputs, N):
	for i in range(n_inputs):
		with open("inputs2/seq_decrescente" + str(i).zfill(2) + ".txt", "w") as escrever:
			escrever.write(str(N) + "\n")
			num_list = []
			for j in range(N):
				num_list += [j]
			reversed_list = sorted(num_list, reverse=True)
			for j in range(N):
				escrever.write(str(reversed_list[j]) + "\n")

		if i == 0:
			N += 49_000
		else:
			N += 50_000


def seq_1percent(n_inputs, N):
	for i in range(n_inputs):
		with open("inputs2/seq_1percent" + str(i).zfill(2) + ".txt", "w") as escrever:
			percent1 = int(N * 0.01)
			escrever.write(str(N) + "\n")
			num_list = []

			for j in range(N):
				num_list += [j]

			numbers_to_shuffle = []
			indexes = []

			for j in range(percent1):
				shuffled_num = random.randint(0, len(num_list) - 1)
				numbers_to_shuffle += [num_list[shuffled_num]]
				indexes += [shuffled_num]

			random.shuffle(numbers_to_shuffle)

			for j in range(len(indexes)):
				# acede ao array original, o elemento do index original é substituído pelo elemento shuffled
				num_list[indexes[j]] = numbers_to_shuffle[j]

			for j in range(N):
				escrever.write(str(num_list[j]) + "\n")

		if i == 0:
			N += 49_000
		else:
			N += 50_000


def seq_5percent(n_inputs, N):
	for i in range(n_inputs):
		with open("inputs2/seq_5percent" + str(i).zfill(2) + ".txt", "w") as escrever:
			percent5 = int(N * 0.05)
			escrever.write(str(N) + "\n")
			num_list = []

			for j in range(N):
				num_list += [j]

			numbers_to_shuffle = []
			indexes = []

			for j in range(percent5):
				shuffled_num = random.randint(0, len(num_list) - 1)
				numbers_to_shuffle += [num_list[shuffled_num]]
				indexes += [shuffled_num]

			random.shuffle(numbers_to_shuffle)

			for j in range(len(indexes)):
				# acede ao array original, o elemento do index original é substituído pelo elemento shuffled
				num_list[indexes[j]] = numbers_to_shuffle[j]

			for j in range(N):
				escrever.write(str(num_list[j]) + "\n")

		if i == 0:
			N += 49_000
		else:
			N += 50_000


def main():
	n_inputs = 21
	N = 1000
	seq_aleatoria(n_inputs, N)
	seq_decrescente(n_inputs, N)
	seq_1percent(n_inputs, N)
	seq_5percent(n_inputs, N)


if __name__ == "__main__":
	main()
