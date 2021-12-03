from array import *

a = array('i' , [12 ,21 ,1 ,11])
def check_prime_number(a, c=int):
    c = 0 
    #flag = 0 => không phải số nguyên tố
    #flag = 1 => số nguyên tố
    for n in range(0, 3):
        flag = 1 
        if (a[n] <2):
           flag = 0
           return flag  #Số nhỏ hơn 2 không phải số nguyên tố => trả về 0
    
    #Sử dụng vòng lặp while để kiểm tra có tồn tại ước số nào khác không
        for p in range(2, a[n]):
            if n % p == 0:
              flag = 0
              break #Chỉ cần tìm thấy 1 ước số là đủ và thoát vòng lặp
              return flag    
        if flag == 1:
            c = c + 1
        else:
            c = c
def check(c=int):
    if c >= 2:
        print("True")
    else:
        print("False")         