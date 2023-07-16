A, B, C = map(int, input().split())
I, J, K = map(int, input().split())

min_num= min(A / I, B / J, C / K)

calc_A = A-I*min_num
calc_B = B-J*min_num
calc_C = C-K*min_num

print(f"{calc_A:.6f} {calc_B:.6f} {calc_C:.6f}")