c1=input('Enter color list 1 seperated by commas').split(',')
c2=input('Enter color list 2 seperated by commas').split(',')
print('Colors not in list 2 that are in list 1 are ',set(c1)-set(c2))
