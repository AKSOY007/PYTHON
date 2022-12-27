import random
sayi = random.randrange(1,100)
tadet = 10
for i in range(10):
    tadet -=1
    tahmin = int(input('1 ile 100 arasında bir tahminde bulun:'))
    if tahmin > sayi: print(f'tahmininiz yanlış daha küçük bir sayı tahmin etmeyi dene, {tadet} adet tahmin hakkın kaldı')
    elif tahmin < sayi: print(f'tahmininiz yanlış daha büyük bir sayı tahmin etmeyi dene, {tadet} adet tahmin hakkın kaldı')
    elif tahmin == sayi:
        print(f'Tebrikler doğru sayıyı {10-tadet}. denemede buldun')
        break

else:
    print(f'Tüm tahmin haklarını kullandın ancak doğru sayıyı bulamadın. Doğru sayı:{sayi}')
