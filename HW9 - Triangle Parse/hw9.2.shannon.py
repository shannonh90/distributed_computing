

result = [(a*b, a, b) for a in range (1,1000) for b in range(1,1000) if str(a*b) == str((a*b))[::-1]]
highest_result = max(result)
print("{} x {} = {}".format(highest_result[1], highest_result[2], highest_result[0]))