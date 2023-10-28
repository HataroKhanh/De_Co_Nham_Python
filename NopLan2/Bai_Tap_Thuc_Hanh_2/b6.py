N = int(input())
if N%400==0 or (N%4==0 and N%100!=0):
    print('366')
else:
    print('365')