english = int(input("masukan nilai english "))
matematika = int(input("masukan nilai mtk "))
indonesia = int(input("masukan nilai indonesia "))
ipa = int(input("masukan nilai ipa "))
ips = int(input("masukan nilai ips "))

rata_rata = (english + matematika + indonesia) / 3 
rata_rata2 = (english + matematika + indonesia + ipa + ips) / 5
nilai = english > 90 and matematika > 90
if rata_rata >=75:
    print("lulus", rata_rata)

elif rata_rata2  >=70:
    print("lulus",rata_rata2)

elif nilai:
    print("lulus" )

else:
    print("tidak lulus")