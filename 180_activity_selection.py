def max_activities(n, s, f):
  a = list(zip(s, f))
  a.sort(key=lambda x: x[1])
  count = 0
  last_ft = -1
  for st, ft in a:
    if st >= last_ft:
      count += 1
      last_ft = ft
  return count

t = int(input())
for _ in range(t):
  n = int(input())
  s = list(map(int, input().split()))
  f = list(map(int, input().split()))
  print(max_activities(n, s, f))