def withFreeInfiniteTransaction(arr, n, fee):
    bsp = 0
    ssp = 0
    for k in range(n):
        if k == 0:
            bsp, ssp = -1 * arr[k], 0
        else:
            bsp, ssp = max(bsp, ssp - (1*arr[k])), max(ssp, bsp + arr[k] - fee)
    print(ssp)

def main():
    n = int(input())
    array = []
    for i in range(n) :
        array.append(int(input()))

    fee = int(input())
    withFreeInfiniteTransaction(array, n, fee)

if __name__ == '__main__':
    main()