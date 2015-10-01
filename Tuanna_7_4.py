#Dung thuat toan De Quy
def hanoi(n, source, helper, target):
    # print "hanoi( ", n, source, helper, target, " called"
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        # move disk from source peg to target peg
        if source[0]:
            disk = source[0].pop()
            print "moving " + str(disk) + " from " + source[1] + " to " + target[1]
            target[0].append(disk)
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)


source = ([3, 2, 1], "source")
target = ([], "target")
helper = ([], "helper")
hanoi(len(source[0]), source, helper, target)
#Output
# print source, helper, target
# moving 1 from source to target
# moving 2 from source to helper
# moving 1 from target to helper
# moving 3 from source to target
# moving 1 from helper to source
# moving 2 from helper to target
# moving 1 from source to target
# ([], 'source') ([], 'helper') ([3, 2, 1], 'target')