n = int(input())
dane = input().split()
ilep = 0
maxskok = 0
for i in dane:
    if i == '0':
        if maxskok < ilep:
            maxskok = ilep
            ilep = 0

    else:
        ilep += 1
    print(ilep, maxskok)

if maxskok<ilep:
    maxskok=ilep
    ilep=0

print(maxskok)

# a = int(input())
# dane = input('podaj liczby').split()
# ilep = 0
# maxskok = 0
# for i in dane:
#     if i == '1':
#         ilep += 1
#         if maxskok<ilep:
#             maxskok=ilep
        
    