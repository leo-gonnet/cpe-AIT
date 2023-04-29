def syracuse(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n] + syracuse(n // 2)
    else:
        return [n] + syracuse(3 * n + 1)

def syracuse_2(n):
    syr = syracuse(n)
    res = []
    res.append(syr)
    res.append(len(syr))
    res.append(max(syr))
    return res

if __name__ == "__main__":
    print(syracuse(13))
    print(syracuse_2(13))