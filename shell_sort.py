from time import perf_counter
import glob
import os


def shell_sort(sequence, gap, algorithm):
	flag = 0
	while gap > 0:
		tik = perf_counter()
		for i in range(gap, len(sequence)):
			temp = sequence[i]  # valor "da direita" vai ser armazenado numa variável temporária
			j = i
			# 1ª condição: garante que tem gap suficiente para fazer troca com o valor da esquerda
			#              ex: 1 2 3 4 5, gap=3, trocar 1 e 3 não ia dar, mas 1 e 5 sim
			# 2ª condição: o valor da esquerda é maior que o valor da direita; se sim, vai fazer uma troca
			while j >= gap and sequence[j - gap] > temp:
				sequence[j] = sequence[j - gap]  # o da direita passa a ter o valor do da esquerda
				j -= gap
			sequence[j] = temp  # o da esquerda passa a ter o valor do da direita
		tok = perf_counter()
		time_improved3 = tok - tik
		if flag == 1:
			break
		if algorithm == "base":
			gap = gap // 2
		elif algorithm == "imp1":
			gap = int(gap // 2.2)
		elif algorithm == "imp2":
			sum_numbers, total_digits, max_number, max_min_diff = sum_digits(gap)
			if max_number == 1:
				gap = int(gap // 2.2)
			else:
				gap = int(gap // max_number)
		elif algorithm == "imp3":
			if time_improved3 < 0.5:
				time_improved3 += 4
			elif 0.5 <= time_improved3 < 2:
				time_improved3 += 2
			gap = int(gap // time_improved3)
		elif algorithm == "imp4":
			sum_numbers, total_digits, max_number, max_min_diff = sum_digits(gap)
			if total_digits == 1:
				gap = int(gap / gap)
			else:
				gap = int(gap // total_digits)
		if gap == 1:
			flag = 1


def shell(sequence, gap, algorithm):
	flag = 0
	time_improved3 = 0
	right_index = gap
	left_index = 0

	tik = perf_counter()
	while gap > 0:
		if sequence[left_index] > sequence[right_index]:
			temp = sequence[right_index]
			sequence[right_index] = sequence[left_index]
			sequence[left_index] = temp
			if left_index - 1 >= 0:
				left_index -= 1
				right_index -= 1
				continue

		left_index += 1
		right_index += 1
		tok = perf_counter()
		time_improved3 += tok - tik

		if right_index == len(sequence):
			if flag == 1:
				break
			if algorithm == "base":
				gap = gap // 2
			elif algorithm == "imp1":
				gap = int(gap // 2.2)
			elif algorithm == "imp2":
				sum_numbers, total_digits, max_number, max_min_diff = sum_digits(gap)
				if max_number == 1:
					gap = int(gap // 2.2)
				else:
					gap = int(gap // max_number)
			elif algorithm == "imp3":
				if time_improved3 < 0.5:
					time_improved3 += 4
				elif 0.5 <= time_improved3 < 2:
					time_improved3 += 2
				gap = int(gap // time_improved3)
			elif algorithm == "imp4":
				sum_numbers, total_digits, max_number, max_min_diff = sum_digits(gap)
				if total_digits == 1:
					gap = int(gap / gap)
				else:
					gap = int(gap // total_digits)
			if gap == 1:
				flag = 1
			left_index = 0
			right_index = gap


def sum_digits(gap):
	total_sum = 0
	total_digits = 0
	number = gap
	numbers = []
	while number > 0:
		total_sum += number % 10
		numbers += [number % 10]
		number = number // 10
		total_digits += 1
	return total_sum, total_digits, max(numbers), max(numbers) - min(numbers)


def main():
	sequence = []
	N = int(input())
	for i in range(N):
		sequence += [int(input())]

	# gap: potência de 2 mais perto de N, sem ultrapassar o seu valor
	initial_gap = 2
	while initial_gap < N:
		initial_gap *= 2
		if initial_gap > N:
			initial_gap = initial_gap // 2
			break

	# ------------------------------- BASE SHELL SHORT ------------------------------- #
	# BASE SHELL -> gap = gap // 2
	total_time = 0
	sequence_base = sequence.copy()
	base_gap = initial_gap
	tik = perf_counter()
	shell_sort(sequence_base, base_gap, "base")
	tok = perf_counter()
	total_time += tok - tik
	print(f"BASE SHELL SORT -- Time: {total_time}")
	with open("times/base" + ".txt", "a") as writing:
		writing.write(str(total_time)+"\n")

	# ------------------------------- IMPROVED 1 ------------------------------- #
	# BASE SHELL -> gap = gap // 2.2
	total_time = 0
	sequence_imp1 = sequence.copy()
	gap_imp1 = initial_gap
	tik = perf_counter()
	shell_sort(sequence_imp1, gap_imp1, "imp1")
	tok = perf_counter()
	total_time += tok - tik
	print(f"IMPROVED 1 -- Time: {total_time}")
	with open("times/imp1" + ".txt", "a") as writing:
		writing.write(str(total_time)+"\n")

	# ------------------------------- IMPROVED 2 ------------------------------- #
	# NÚMERO MÁXIMO: divide pelo digito máximo do gap. Se máximo for 1, divide por 2.2
	total_time = 0
	sequence_imp2 = sequence.copy()
	gap_imp2 = initial_gap
	tik = perf_counter()
	shell_sort(sequence_imp2, gap_imp2, "imp2")
	tok = perf_counter()
	total_time += tok - tik
	print(f"IMPROVED 2 -- Time: {total_time}")
	with open("times/imp2" + ".txt", "a") as writing:
		writing.write(str(total_time)+"\n")

	# ------------------------------- IMPROVED 3 ------------------------------- #
	# TEMPO DE EXECUÇÃO: divide pelo tempo que demorou a fazer as comparações com aquele valor de gap
	total_time = 0
	sequence_imp3 = sequence.copy()
	gap_imp3 = initial_gap
	tik = perf_counter()
	shell_sort(sequence_imp3, gap_imp3, "imp3")
	tok = perf_counter()
	total_time += tok - tik
	print(f"IMPROVED 3 -- Time: {total_time}")
	with open("times/imp3" + ".txt", "a") as writing:
		writing.write(str(total_time)+"\n")

	# ------------------------------- IMPROVED 4 ------------------------------- #
	# Nº DE DIGITOS: divide pelo número de digitos existentes naquele gap
	total_time = 0
	sequence_imp4 = sequence.copy()
	gap_imp4 = initial_gap
	tik = perf_counter()
	shell_sort(sequence_imp4, gap_imp4, "imp4")
	tok = perf_counter()
	total_time += tok - tik
	print(f"IMPROVED 4 -- Time: {total_time}")
	with open("times/imp4" + ".txt", "a") as writing:
		writing.write(str(total_time)+"\n")


if __name__ == "__main__":
	main()
