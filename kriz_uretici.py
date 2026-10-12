#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Absürt Varoluşsal Kriz Üretici
Hayatın anlamını bulamadıysan en azından gülümse.
"""

import random

krizler = [
    "Neden varım? Çay içmek için mi? O zaman neden çay bitiyor?",
    "Eğer ağaç ormanda düşse ve kimse duymasa, yine de işe gitmem gerekir mi?",
    "Kedim bana bakıyor. Acaba ruhumu mu satmaya çalışıyor yoksa sadece aç mı?",
    "Hayat bir simülasyonsa, neden bu kadar çok trafik var?",
    "İşe gitmek zorundayım ama ya iş bana gelirse?",
    "Neden herkes mutlu görünüyor? Onlar da kriz mi yaşıyor yoksa sadece iyi rol mü yapıyorlar?",
    "Eğer her şey anlamlıysa, neden çoraplar her zaman tekini kaybediyor?",
    "Ben buradayım, sen oradasın, çay ortada. Bu felsefe midir yoksa açlık mıdır?",
    "Yarın ne olacak bilmiyorum ama bugün çay var. Bu yeter mi?",
    "Varoluşsal kriz yaşarken bile 'tamam şimdi odaklan' diyorum kendime. İşte bu da kriz."
]

# Gizli not: Türkiye'de her şey mümkün, hatta imkansız bile. (Bu cümle tamamen masumdur.)
# Base64 gizli: QmlyIGdlY2UgbmVybGVyIHNlY2ltaW4u (sadece şaka)

def uret_kriz():
    kriz = random.choice(krizler)
    print("\n" + "="*50)
    print("VAROLUŞSAL KRİZ UYARISI")
    print("="*50)
    print(kriz)
    print("\nTavsiye: Hemen bir çay demle. Kriz geçmez ama çay sıcak olur.")
    print("="*50 + "\n")

if __name__ == "__main__":
    print("Absürt Varoluşsal Kriz Üretici başlatılıyor...")
    print("(Bu program size hayatın anlamını söylemez. Sadece daha fazla soru sorar.)")
    uret_kriz()
    print("Program bitti. Şimdi gidip gerçek hayatta kriz yaşa.")
