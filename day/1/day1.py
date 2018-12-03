with open('input') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
#content = [x.strip() for x in content]

sum = 0
for line in content:
	num = int(line.strip())
	sum += num

print("sum: {}".format(sum))
