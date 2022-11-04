
# 1'den kullanıcının girdiği sayıya kadar
# olan sayıların eğer tek ise karesini , çift ise küpünün
# toplamını ayrı ayrı hesaplayan kod parçacığı

sayi = input('Bir Sayı Girin : ')
tekToplam=0
ciftToplam=0

for i in range(1,int(sayi)):
  if(i%2==0):
        ciftToplam+=i**3

  else:
        tekToplam+=i**2
print("Tek Sayıların Toplamı : {0}".format(tekToplam))

print("Çift Sayıların Toplamı : {0}".format(ciftToplam))