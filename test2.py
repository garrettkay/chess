boardRawInput = "0,1.2/3;4'5[6]7\8!@@#@!#!$(!&@3"
print(boardRawInput)
i = 0
while i < len(boardRawInput):
	if not boardRawInput[i].isdecimal():
		boardRawInput = boardRawInput[:i] + boardRawInput[i + 1:]
		i -= 1
	i += 1
print(boardRawInput)