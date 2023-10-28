bookls=['toan10','ly 11','hoa 12','tin 10','tin 12']
print(bookls) #['toan10', 'ly 11', 'hoa 12', 'tin 10', 'tin 12']
print(len(bookls))#5
print(bookls[3])#tin 10
print(bookls[3:5])#['tin 10', 'tin 12']
print('tin 11' in bookls)#False
bookls.insert(4,'tin 11')
print('tin 11' in bookls)#True
bookls.sort()
print(bookls)#['hoa 12', 'ly 11', 'tin 10', 'tin 11', 'tin 12', 'toan10']