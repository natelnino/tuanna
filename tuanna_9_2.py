list_input = ['nhung', 'bong', 'hoa', 'nho']
iteration = iter(list_input)
while True:
    try:
        print iteration.next()
    except StopIteration:
        pass