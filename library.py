import os

DOSYA_ADI = "books.txt"

def kitaplari_yukle():
    if not os.path.exists(DOSYA_ADI):
        return []
    with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
        kitaplar = []
        for satir in dosya:
            isim, yazar, yil = satir.strip().split(" | ")
            kitaplar.append({"isim": isim, "yazar": yazar, "yil": yil})
        return kitaplar

def kitaplari_kaydet(kitaplar):
    with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
        for kitap in kitaplar:
            dosya.write(f"{kitap['isim']} | {kitap['yazar']} | {kitap['yil']}\n")

def listele(kitaplar):
    if not kitaplar:
        print("Kütüphane boş.")
        return
    print("\nKütüphanedeki Kitaplar:")
    for i, kitap in enumerate(kitaplar, 1):
        print(f"{i}. {kitap['isim']} - {kitap['yazar']} ({kitap['yil']})")

def kitap_ekle(kitaplar):
    isim = input("Kitap ismi: ").strip()
    yazar = input("Yazar: ").strip()
    yil = input("Yayın yılı: ").strip()
    if isim and yazar and yil:
        kitaplar.append({"isim": isim, "yazar": yazar, "yil": yil})
        print(f"'{isim}' kitaplığına eklendi.")
    else:
        print("Tüm alanlar doldurulmalı.")

def kitap_sil(kitaplar):
    listele(kitaplar)
    if not kitaplar:
        return
    try:
        secim = int(input("Silmek istediğiniz kitabın numarası: "))
        if 1 <= secim <= len(kitaplar):
            silinen = kitaplar.pop(secim - 1)
            print(f"'{silinen['isim']}' kütüphaneden silindi.")
        else:
            print("Geçersiz numara.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

def kitap_ara(kitaplar):
    if not kitaplar:
        print("Kütüphane boş.")
        return
    terim = input("Arama terimi (isim veya yazar): ").strip().lower()
    bulunanlar = [k for k in kitaplar if terim in k['isim'].lower() or terim in k['yazar'].lower()]
    if bulunanlar:
        print("\nBulunan Kitaplar:")
        for kitap in bulunanlar:
            print(f"- {kitap['isim']} - {kitap['yazar']} ({kitap['yil']})")
    else:
        print("Eşleşen kitap bulunamadı.")

def main():
    kitaplar = kitaplari_yukle()

    while True:
        print("\n--- Kişisel Kitaplık ---")
        print("1. Kitapları Listele")
        print("2. Kitap Ekle")
        print("3. Kitap Sil")
        print("4. Kitap Ara")
        print("5. Çıkış")

        secim = input("Seçiminiz (1-5): ")

        if secim == "1":
            listele(kitaplar)
        elif secim == "2":
            kitap_ekle(kitaplar)
        elif secim == "3":
            kitap_sil(kitaplar)
        elif secim == "4":
            kitap_ara(kitaplar)
        elif secim == "5":
            kitaplari_kaydet(kitaplar)
            print("Değişiklikler kaydedildi. Hoşça kal!")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    main()
