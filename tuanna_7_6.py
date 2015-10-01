# input: abbbccccdddd output: abb3cc4dd4
# input: xxyyyxyyx output: xx2yy3xyy2x
def convert(string):
    result = ''
    count = 1
    for i in range(1, len(string) + 1):
        if i + 1 == len(string):
            if count > 1:
                return result + string[i] * 2 + str(count)
                count = 1
            elif count == 1:
                return result + string[i] + str(count)
        elif string[i] == string[i + 1]:
            count += 1
        elif string[i] != string[i + 1]:
            if count > 1:
                result = result + string[i] * 2 + str(count)
                count = 1
            elif count == 1:
                result = result + string[i] + str(count)
    return result


print convert('xxyyyxyyxxx')
# x1yy3x1yy2xx3