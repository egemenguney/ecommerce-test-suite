# 📦 Proje Taşıma Rehberi

## 🎯 Durum

Şu anki yapı:
```
C:\Users\egeme\Desktop\egemenguney.net\
  └── ecommerce-test-suite\  ← Burada (YANLIŞ)
```

İstenen yapı:
```
C:\Users\egeme\Desktop\
  ├── egemenguney.net\        ← Portfolio repo
  └── ecommerce-test-suite\   ← Ayrı repo (DOĞRU)
```

## 🚀 Adım Adım Taşıma

### 1. Yeni Klasör Oluştur

```bash
# Desktop'a git
cd C:\Users\egeme\Desktop

# Yeni klasör oluştur
mkdir ecommerce-test-suite
```

### 2. Dosyaları Kopyala

**Seçenek A: Git ile (Önerilen - Git history korunur)**

```bash
# Mevcut konumdan
cd C:\Users\egeme\Desktop\egemenguney.net\ecommerce-test-suite

# Git remote'u kontrol et
git remote -v

# Yeni konuma taşı
cd C:\Users\egeme\Desktop
xcopy /E /I /H /Y "egemenguney.net\ecommerce-test-suite" "ecommerce-test-suite"

# Ya da PowerShell ile
Copy-Item -Path "egemenguney.net\ecommerce-test-suite\*" -Destination "ecommerce-test-suite\" -Recurse -Force
```

**Seçenek B: Manuel Kopyala**

1. `C:\Users\egeme\Desktop\egemenguney.net\ecommerce-test-suite` klasörünü seç
2. Tüm dosyaları kopyala (Ctrl+C)
3. `C:\Users\egeme\Desktop\ecommerce-test-suite` klasörüne yapıştır (Ctrl+V)

### 3. Git Repository'yi Kontrol Et

```bash
# Yeni konuma git
cd C:\Users\egeme\Desktop\ecommerce-test-suite

# Git durumunu kontrol et
git status

# Remote'u kontrol et
git remote -v
# Şunu görmeli: origin https://github.com/egemenguney/ecommerce-test-suite.git

# Eğer remote yoksa ekle
git remote add origin https://github.com/egemenguney/ecommerce-test-suite.git
```

### 4. Eski Klasörü Temizle

```bash
# egemenguney.net repo'sundan ecommerce-test-suite'i sil
cd C:\Users\egeme\Desktop\egemenguney.net

# .gitignore'a ekle (eğer yoksa)
echo "ecommerce-test-suite/" >> .gitignore

# Git'ten kaldır (eğer eklenmişse)
git rm -r --cached ecommerce-test-suite/

# Commit et
git commit -m "Remove ecommerce-test-suite (moved to separate repo)"
git push
```

### 5. Yeni Konumda Test Et

```bash
cd C:\Users\egeme\Desktop\ecommerce-test-suite

# Test çalıştır
pytest tests/test_login.py -v

# Git push test
git status
git add .
git commit -m "Update: Project moved to separate directory"
git push
```

## ✅ Sonuç

Artık yapı şöyle olacak:

```
C:\Users\egeme\Desktop\
├── egemenguney.net\           ← Portfolio repo (sadece website)
│   ├── index.html
│   ├── projects\
│   │   └── ecommerce-test-suite.html (link verir)
│   └── .git\
│
└── ecommerce-test-suite\      ← Ayrı repo (test projesi)
    ├── tests\
    ├── pages\
    ├── .git\
    └── README.md
```

## 🎯 Avantajlar

✅ **Temiz Yapı**
- Her proje kendi klasöründe
- Nested git repo sorunu yok
- Daha organize

✅ **Kolay Yönetim**
- Portfolio sitesi sadece link verir
- Test projesi bağımsız
- Her biri kendi git repo'su

✅ **Profesyonel Görünüm**
- Ayrı repository'ler
- Daha iyi GitHub organizasyonu
- Kolay paylaşım

## ⚠️ Önemli Notlar

1. **Git History Korunur**: Dosyaları kopyalarken `.git` klasörü de kopyalanmalı
2. **Remote Kontrol**: Yeni konumda remote'un doğru olduğunu kontrol et
3. **Portfolio Güncelle**: `egemenguney.net` sitesinde sadece link olduğundan emin ol

## 🔄 Hızlı Komutlar (PowerShell)

```powershell
# 1. Yeni klasör oluştur
New-Item -ItemType Directory -Path "C:\Users\egeme\Desktop\ecommerce-test-suite" -Force

# 2. Dosyaları kopyala (git history dahil)
Copy-Item -Path "C:\Users\egeme\Desktop\egemenguney.net\ecommerce-test-suite\*" `
          -Destination "C:\Users\egeme\Desktop\ecommerce-test-suite\" `
          -Recurse -Force

# 3. Yeni konuma git
cd C:\Users\egeme\Desktop\ecommerce-test-suite

# 4. Git durumunu kontrol et
git status
git remote -v
```

## ✅ Kontrol Listesi

- [ ] Yeni klasör oluşturuldu
- [ ] Dosyalar kopyalandı
- [ ] Git remote doğru
- [ ] Test çalıştırıldı
- [ ] Eski klasör temizlendi
- [ ] Portfolio sitesi güncellendi (sadece link)
