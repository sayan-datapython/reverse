# 1. Ask user for name, print reverse of name
# a=name[::-1]

# index -> 0 ; a[i-1]


reverse = ''
name = input("your name?")
i = len(name)
for index in range(0, i):
  reverse = reverse + name[i-index-1]

print(reverse)
