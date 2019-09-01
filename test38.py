def countAndSay(n: int):
    seq = "1"
    for i in range(n-1):
        j, next_seq = 0, ""
        print("loop i is:", i)
        while j < len(seq):
            print("seq:", seq, "\nindex:", j)
            count = 1
            while j < len(seq) -1 and seq[j] == seq[j + 1]:
                count += 1
                print("count:", count)
                j += 1
                print("the twice while index:", j)
            j += 1
            next_seq += str(count) + seq[j-1]
            print("next_seq:", next_seq)
        seq = next_seq
    return next_seq

print("return:", countAndSay(5))
print("----------------------")
