# ls = []
# print("Nhập 1 dãy số nguyên, mình sẽ tìm các cặp số có tích bằng 128 và vị trí của nó!")
# m = int(input("Nhập số phần tử của dãy số:"))
# for i in range(1,m+1):
#     n = int(input("Nhập số thứ "+str(i)+" : "))
#     ls.append(n)

ls = [1,4,1,64,2,128,5,4,7,31]

print("Trong dãy số:")
print(*ls, sep=" ")
print("")
print("Có những cặp số sau có tích bằng 128:")
for i in range(len(ls)):
    for j in range(i+1,len(ls)):
        if ls[i]*ls[j]==128:
            print("{0} và {1} tại vị trí {2} và {3}".format(ls[i],ls[j],i+1,j+1))
