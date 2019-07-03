import random
import time
while (True):
	yeni_oyun = input("Yeni Oyun [E/H] :")
	if (yeni_oyun == "E"):
		print("OYUN PLATFORMU OLUŞTURULUYOR...")
		time.sleep(2)
		print("""
===========================

    ADAM ASMACA OYUNU
  >Tahmin için 1
  >Çıkmak için 2
===========================
		""")
		kelime_listesi = ["backdoor","keylogger","klavye","merhaba"]
		gizli_kelime = random.choice(kelime_listesi)
		can = len(gizli_kelime)+1
		liste = list()
		kelime_şifreleri = "_" * len(gizli_kelime)
		liste.extend(kelime_şifreleri)
		print(liste)
		bilinen_karakterler = 0
		harfler = ""
		while (can > 0):
			analiz = True
			tahmin = input("Tahmin:")
			if (tahmin == "1"):
				k_tahmin = input("Tahmininiz nedir :")
				if (k_tahmin == gizli_kelime):
					liste.clear()
					liste.extend(gizli_kelime)
					print(liste)
					print(">>> KAZANDINIZ <<<")
					break
				else:
					print("> Yanlış tahmin")
					can -= 1
					print(f"Can:",can)
					print(liste)
					continue
			elif (tahmin == "2"):
				print("Çıkış yapılıyor...")
				time.sleep(2)
				print("Çıkış Yapıldı ✓")
				break
			elif not(tahmin):
				print("> Lütfen tahmin giriniz...")
			else:
				if tahmin in harfler:
					print("> Bu karakter girildi")
					print(liste)
					continue
				else:
					harfler += tahmin
					for i in enumerate(gizli_kelime):
						if tahmin in i[1]:
							liste.insert(i[0],i[1])
							liste.pop(i[0]+1)
							bilinen_karakterler+=1
							analiz = False
					print(liste)
					if (bilinen_karakterler == len(gizli_kelime)):
						print(">>> KAZANDINIZ! <<<")
						break
					if (analiz):
						print("> Yanlış tahmin")
						can-=1
						print(f"Can:",can)
						if (can == 0):
							print(">>> KAYBETTİNİZ <<<")
	elif (yeni_oyun == "H"):
		print("Yine bekleriz...")
		break
	else:
		print("Lütfen [E/H] seçiniz")