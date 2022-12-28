import math
def tinh_BMI(can_nang,chieu_cao):
#tinh chi so BMI cua mot nguoi dua tren can nang va chieu cao
 BMI = can_nang/math.pow(chieu_cao,2)
 return BMI
a = float(input("cho biet so can(kg):"))
b = float(input("cho biet so do chieu cao(m):"))
print("chi so BMI cua ban la: %0.2f"%(tinh_BMI(a,b)))