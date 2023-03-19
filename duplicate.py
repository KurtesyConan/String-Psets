L1 =[1,2,3,4]
L2 =[4,1,6,7]
L3 =[5,8,7,1]

L4 =[]
for i in L3:
     print(f'i = {i}')
     if i not in L1 :  #parent block
                 if i not in L2:
                       L4.append(i)
                       print(f'{L4} is not inside L1 and L2')
                 else:
                       print((i), f'is a half duplicate')
     else:
         print((i), f'is a complete duplicate')
         
            
                            

#L3 = [i for i in tuple(L1) if i in tuple(L2)]
#print("duplicates", L3)



