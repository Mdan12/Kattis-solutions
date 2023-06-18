text = input()
midpoint = len(text) // 2
first_part = text[:midpoint]
second_part = text[midpoint:]

first_sum = sum(ord(i) - 65 for i in first_part)
second_sum = sum(ord(k) - 65 for k in second_part)

first_div_sum = first_sum % 26
second_div_sum = second_sum % 26

first_new_string = ''.join(
    chr((ord(j) - 65 + first_div_sum) % 26 + 65) for j in first_part)
second_new_string = ''.join(
    chr((ord(l) - 65 + second_div_sum) % 26 + 65) for l in second_part)

last_string = ''.join(chr((ord(first_new_string[m]) + ord(
    second_new_string[m]) - 2 * 65) % 26 + 65) for m in range(len(second_new_string)))

print(last_string)
