
# Cibinizdə Analitik - İdarəçi Sİ Biznes İnformasiyası

**Cibinizdə həmişə mövcud olan etibarlı Sİ biznes məsləhətçiniz.**

Bank direktorları və icraçılar üçün Telegram vasitəsilə real vaxt strateji fikirlər çatdıran premium B2B SaaS həlli. Google Gemini tərəfindən dəstəklənən Sİ məsləhətçi ilə güclü analitik panelləri birləşdirir - hamısına sadə danışıqlar vasitəsilə daxil olmaq mümkündür.

## Xüsusiyyətlər

### 💼 İdarəetmə Paneli

- **Portfel İcmalı** - Bütün hesablarda real vaxt idarə olunan aktivlər
- **Əməliyyat İnformasiyası** - Nümunə analizi və əməliyyat axını haqqında fikirlər
- **Xərc Analizi** - Faizlərlə strateji xərc bölgüsü
- **Biznes Performansı** - Gəlir, xərc və xalis mövqe izləməsi
- **Yüksək Dəyərli Monitorinq** - Ən böyük əməliyyatları dərhal izləyin
- **İnteraktiv Vizuallaşdırmalar** - Tələb əsasında yaradılan peşəkar qrafiklər

### 🤖 Sİ Biznes Məsləhətçi

- **Strateji Danışıqlar** - Bankınızın performansı haqqında təbii dildə hər şeyi soruşun
- **Məlumata Əsaslanan Fikirlər** - Sİ sizin real əməliyyat məlumatlarınızı təhlil edir
- **İdarəçi Səviyyəsində Ünsiyyət** - Cavablar texniki detallar deyil, biznes təsirinə fokuslanır
- **Kontekstdən Xəbərdar İnformasiya** - Daha dərin təhlil üçün danışıq tarixini xatırlayır
- **24/7 Əlçatanlıq** - Etibarlı məsləhətçiniz həmişə cibinizdədir
- **Qrup Dəstəyi** - Birdən çox icraçı komanda kanallarında fikirlərə daxil ola bilər

### 🎯 İcraçılar üçün Qurulmuş

- Texniki jarqon yox - təmiz biznes informasiyası
- Məlumat analitiki asılılığı olmadan ani fikirlər
- Yoldakı icraçılar üçün mobil-ilk dizayn
- Hər icraçı üçün təhlükəsiz, şəxsi danışıqlar
- Real vaxt əməliyyat göstəriciləri

## Docker ilə Sürətli Başlanğıc (Tövsiyə olunur)

### Ön Şərtlər

- Docker və Docker Compose quraşdırılmış
- Telegram Bot Tokeni
- Google Gemini API Açarı
- `demo_bank` sxemi ilə PostgreSQL məlumat bazası

### Quraşdırma

1. **Mühit dəyişənlərini konfiqurasiya edin**

`.env` faylını redaktə edin:

```env
DATABASE_URL="postgresql://user:password@host:port/database"
TELEGRAM_BOT_TOKEN="sizin_bot_tokeniniz"
GEMINI_API_KEY="sizin_gemini_api_açarınız"
ADMIN_USER_IDS=""
```

2. **Botu yerləşdirin**

```bash
# Deploy skriptini icra edilə bilən edin (yalnız ilk dəfə)
chmod +x deploy.sh

# Yerləşdirin
./deploy.sh
```

3. **Bot indi işləyir!** Telegram-ı açın və botunuza `/start` göndərin.

## Necə İstifadə Etmək Olar

### 🚀 Başlanğıc

1. **Botu başladın** - Telegram-da botunuza `/start` göndərin
2. **Panelə daxil olun** - İnteraktiv göstəricilər üçün `/analytics` istifadə edin
3. **Sual verin** - Strateji suallarınızla sadəcə bota təbii şəkildə mesaj göndərin

### 💬 Sİ Biznes Məsləhətçidən İstifadə

#### Şəxsi Söhbətlərdə

Sadəcə istənilən strateji sual ilə bota mesaj göndərin:

**Nümunə Danışıqlar:**

```
İcraçı: Bizim böyümə imkanlarımız nələrdir?
Bot: Cari 5 aktiv hesabda $487K portfeliniz və bu ay $11.2K müsbət
xalis mövqeyinizlə, mən üç əsas böyümə imkanı müəyyən edirəm:

1. Müştəri əldə etmə potensialı
2. Kredit portfeli genişlənməsi
3. Rüsum optimallaşdırması

Tövsiyə: İlk növbədə əməliyyat həcmini maksimuma çatdırmaq üçün
müştəri əldə etməyə fokuslanın.
```

#### Qrup Söhbətlərində (İcraçı Komandaları)

Bot onu qeyd etdiyiniz və ya mesajlarına cavab verdiyiniz zaman cavab verir:

**Üsul 1: Botu qeyd edin**

```
@sizin_bot_username Əməliyyat həcmi trendi necədir?
```

**Qeyd:** `@sizin_bot_username` əvəzinə öz botunuzun istifadəçi adını yazın (böyük-kiçik hərf ayrımı yoxdur)

**Üsul 2: Botun mesajına cavab verin**

```
Bot: [Biznes xülasəsini göstərir]
İcraçı: [Cavab verir] Gəlir mənbələrini detalizə et
Bot: [Ətraflı gəlir təhlili təqdim edir]
```

**Üsul 3: /ask əmrindən istifadə edin**

```
/ask Hansı müştəri seqmentləri ən gəlirlidir?
```

### 📊 İdarəetmə Panelindən İstifadə

#### Panelə Daxil Olun

```
/analytics
```

Bu, bu informasiya variantları ilə interaktiv menyu açır:

1. **📊 Biznes Xülasəsi** - Aylıq performans icmalı
2. **💼 Portfel İcmalı** - İdarə olunan aktivlər
3. **💸 Xərc Analizi** - Pul harada xərclənir
4. **📈 Əməliyyat Nümunələri** - 90 günlük əməliyyat axını
5. **🎯 Yüksək Dəyərli Əməliyyatlar** - Məbləğə görə ilk 10
6. **📉 Portfel Trendi** - 90 günlük aktiv trayektoriyası

#### Sürətli Əmrlər

Menyunu keç və birbaşa fikirlər əldə et:

```
/summary   - Ani biznes performans xülasəsi
/balance   - Portfel icmalı
/spending  - Qrafiklərlə xərc analizi
/trends    - Əməliyyat nümunə analizi
/top       - Yüksək dəyərli əməliyyat nəzərdən keçirilməsi
```

### 💡 Strateji Sual Nümunələri

**Böyümə və Gəlir:**

- "Cari məlumatlarımızda hansı gəlir imkanları mövcuddur?"
- "Gəlirlilik necə artırıla bilər?"
- "Hansı müştəri seqmentlərinə fokuslanmalıyıq?"

**Risk İdarəetməsi:**

- "Portfel risk məruzumuz necədir?"
- "Defolt göstəricilərimiz nələrdir?"
- "Kredit portfeli sağlamlığını qiymətləndir"

**Əməliyyat Səmərəliliyi:**

- "Xidmətə təsir etmədən xərcləri haradan azalda bilərik?"
- "Əməliyyat səmərəlilik trendimiz necədir?"

### 🔄 Danışıqların İdarəsi

**Danışıq tarixini təmizləyin:**

```
/clear
```

**İcraçi ID-nizi əldə edin:**

```
/myid
```

**Bütün imkanları görün:**

```
/help
```

## Bot Əmrlər Arayışı

### 🎯 İcraçı Əmrləri

- `/start` - Xoş gəlmisiniz brifinqi və bot təqdimatı
- `/help` - Tam əmr arayışı və imkanlar
- `/myid` - Sistem girişi üçün İcraçi ID-nizi göstərin

### 📊 Strateji İnformasiya Əmrləri

- `/analytics` - Bütün göstəricilərlə interaktiv idarəetmə paneli
- `/summary` - Ani biznes performans xülasəsi
- `/balance` - Portfel icmalı (idarə olunan aktivlər, hesab bölgüsü)
- `/spending` - Vizual qrafik və faizlərlə xərc analizi
- `/trends` - Əməliyyat nümunə analizi (90 günlük axın)
- `/top` - Yüksək dəyərli əməliyyat nəzərdən keçirilməsi (məbləğə görə ilk 10)

### 💼 Sİ Məsləhətçi Əmrləri

- `/chat` - Sİ biznes məsləhətçi rejimini aktivləşdirin
- `/ask [sual]` - Birbaşa strateji sorğu (məs: `/ask Bizim böyümə imkanlarımız nələrdir?`)
- `/clear` - Danışıq kontekstini sıfırlayın

## Real Həyat İstifadə Halları

### 📱 Yoldakı Direktor

**Ssenari:** Direktor idarə heyəti iclasına gedərkən sürətli portfel yeniləməsi lazımdır

```
Direktor: /summary
Bot: [30 saniyədə biznes xülasəsi çatdırır]

Direktor: İdarə heyətinə nə vurğulamalıyam?
Bot: Üç əsas güclü tərəfə fokuslanın:
1. $11.2K güclü xalis mövqe (əvvəlki dövrdən 15% artım)
2. Diversifikasiya olunmuş hesablarda $487K portfel artımı
3. Kredit portfelində sıfır defolt göstəriciləri

Ünvanlama imkanı: Yalnız 25% tutumda kredit portfeli
istifadə olunmamış kredit gəlir potensialını göstərir.
```

### 👥 İcraçı Komanda Strategiya Sessiyası

**Ssenari:** Rəhbərlik komandası qrup söhbətində 4-cü rüb strategiyasını müzakirə edir

```
Maliyyə direktoru: @sizin_bot_username Xərc bölgüsünü göstər
Bot: [87.7% kredit xidmətində qrafik və təhlil göndərir]

Direktor: [Bota cavab verir] Bu gəlirlə necə müqayisə olunur?
Bot: Cari gəlir əməliyyatlar üçün 35% marja ilə kredit xidmətini
əhatə edir. Bu sağlamdır, lakin sənaye standartı olan 45-50%-dən
aşağıdır. Nəzərdən keçirin...

Əməliyyat direktoru: @sizin_bot_username Marjları hansı əməliyyat
səmərəliliyiləri artıra bilər?
Bot: [Ətraflı səmərəlilik təhlili təqdim edir]
```

## API Açarları Əldə Etmək

### Telegram Bot Tokeni

1. Telegram-da `@BotFather` axtarın
2. `/newbot` göndərin və təlimatlara əməl edin
3. Verilən tokeni kopyalayın

### Gemini API Açarı

1. https://makersuite.google.com/app/apikey ünvanına daxil olun
2. Yeni API açarı yaradın
3. Açarı kopyalayın

## Problemlərin Həlli

### Məlumat Bazası Bağlantı Problemləri

```bash
# Bağlantını əl ilə test edin
python -c "from database import get_session; print('Bağlandı!' if get_session() else 'Uğursuz')"
```

### Bot Başlamır

- `.env` faylının mövcudluğunu və bütün tələb olunan dəyişənlərin olduğunu yoxlayın
- Telegram tokeninin düzgün olduğunu yoxlayın
- Məlumat bazasının əlçatan olduğunu yoxlayın
- Problemləri diaqnoz etmək üçün `python test_bot.py` işə salın

### Gemini API Xətaları

- API açarının etibarlı olduğunu yoxlayın
- https://makersuite.google.com ünvanında kvota limitlərini yoxlayın
- İnternet bağlantısını təmin edin

## Docker Əmrləri

```bash
# Logları görün
docker-compose logs -f

# Botu dayandırın
docker-compose down

# Botu yenidən başladın
docker-compose restart

# Yenidən qur və başlat
docker-compose up -d --build
```

## Layihə Strukturu

```
analyst_in_pocket/
├── bot.py                   # Əsas bot tətbiqi
├── config.py                # Konfiqurasiya idarəetməsi
├── requirements.txt         # Python asılılıqları
├── deploy.sh               # Docker yerləşdirmə skripti
├── Dockerfile              # Docker image təyini
├── docker-compose.yml      # Docker Compose konfiqurasiyası
│
├── database/               # Məlumat bazası layı
│   ├── connection.py       # Məlumat bazası bağlantı idarəedici
│   ├── models.py           # SQLAlchemy modelləri
│   └── DEMO_BANK_DOCUMENTATION.md
│
├── analytics/              # Analitik mühərrik
│   ├── insights.py         # Analitik fikirlər yaradıcısı
│   └── charts.py           # Qrafik yaradıcı
│
└── chatbot/                # Sİ çatbot
    └── gemini_client.py    # Gemini API inteqrasiyası
```

## Nə Üçün Cibinizdə Analitik?

### 💎 Dəyər Təklifi

**Bank Direktorları Üçün:**

- **Ani İnformasiya** - Saatlar əvəzinə saniyələrdə strateji fikirlər
- **Həmişə Əlçatan** - Sİ məsləhətçiniz 24/7 işləyir, harada olursunuzsa olun
- **Texniki Maneə Yox** - Biznes dili, İT jarqonu yox
- **Məlumata Əsaslanan Etibarlılıq** - Real məlumatlarla dəstəklənən qərarlar verin
- **Xərc Səmərəli** - Tam zamanlı analitik işə götürməyin xərcinin bir hissəsi

**Biznes Təsiri:**

- ⏱️ **Həftədə 10+ saat qənaət edin** məlumat təhlili və hesabatda
- 📊 **Daha sürətli qərarlar verin** fikirlərə ani girişlə
- 💰 **Gəlir imkanlarını müəyyən edin** məlumatlarınızda gizlənmiş
- 🎯 **Riski azaldın** davamlı portfel monitorinqi ilə
- 📈 **Marjları artırın** məlumata əsaslanan optimallaşdırma vasitəsilə

## Lisenziya

Bu layihə təhsil və şəxsi istifadə üçün olduğu kimi təqdim olunur.

## Dəstək

Problemlər üçün:

1. Diaqnoz etmək üçün `python test_bot.py` işə salın
2. Xəta mesajları üçün logları yoxlayın
3. Bütün mühit dəyişənlərinin təyin edildiyini yoxlayın
