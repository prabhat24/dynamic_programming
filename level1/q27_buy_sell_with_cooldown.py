def cooldownInfiniteTransaction(arr, n):
    bsp = 0
    ssp = 0
    cdp = 0
    for k in range(n):
        if k == 0:
            bsp, ssp, cdp = -1 * arr[k], 0, 0
        else:
            bsp, ssp, cdp = max(bsp, cdp - (1*arr[k])), max(ssp, bsp + arr[k]), max(cdp, ssp)
    print(ssp)

def main():
    n = int(input())
    array = []
    for i in range(n) :
        array.append(int(input()))
    cooldownInfiniteTransaction(array, n)

if __name__ == '__main__':
    main()