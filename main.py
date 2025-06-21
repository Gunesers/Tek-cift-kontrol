try:
    sayi = int(input("Bir sayı girin: "))
    if sayi < 0:
        print("Sayınız negatif. (Your number is negative.)")
    if sayi % 2 == 0:
        print("Sayınız çift. (Your number is even.)")
    else:
        print("Sayınız tek. (Your number is odd.)")
except ValueError:
    print("Lütfen geçerli bir sayı girin. (Please enter a valid number.)")
  #İlk python algoritmam: Tek/Çift kontrolü
