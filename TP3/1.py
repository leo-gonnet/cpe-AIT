def rec_dec(n):
    print(n)
    if n == 0:
        return 0
    else:
        return rec_dec(n - 1)
    
def rec_inc(n, i=0):
    print(i)
    if i >= n:
        return 0
    else:
        return rec_inc(n, i+1)
    
if __name__ == "__main__":
    rec_dec(5)
    rec_inc(5)
