# Kurallar ve kaynakları

> Bu dosya `Bilgi Bankası/Girişim & Pazarlama/00 Girişim & Pazarlama.md` ve `Bilgi Bankası/E-ticaret/00 E-ticaret.md` içindeki playbook'lardan üretilir (2026-11-13; Girişim & Pazarlama 43 not, E-ticaret 14 not; skill v0.5). Elle düzenleme; playbook'u güncelle, sonra bu dosyayı yenile.
> ★ = en az 2 bağımsız kaynak. ★★ = 4 ve üstü. Kaynak id'leri X yer işareti id'leridir. Gn = Girişim & Pazarlama playbook'undaki kural n, En = E-ticaret playbook'undaki kural n. Kurallar playbook'taki bölümlerinde durur; bu yüzden bazı bölümlerde numara sırası atlar (G33, G34, G35, G36).
> Klasör işaretleri: (G) Girişim & Pazarlama, (E) E-ticaret, (M) Mobil Geliştirme, (R) kullanıcının başka bir yer işareti klasörü.
> Kanıt düzeyi kaynağın kendisi içindir: iddia · görüş · vaka · veri. Henüz "denendi" olan kural yok.
> Tanıtım kaynakları ★ sayımında ayrılmaz ama bağımsız kanıt gibi okunmaz; bütün kaynakları tanıtım olan kural Kanıt sütununda "tanıtım" diye işaretlenir. Alıntılanan kişi ancak notta kuralı kendisi söylüyorsa kaynak sayılır.
> Tek kaynak sayılanlar:
> - aynı yazarın birden fazla notu: natiakourdadze (4) ve seonatia (muhtemelen aynı kişi), coreprompt (4), cambudakburak (2), levelsio (2), illyism (Girişim ve SEO notları), Ruesandora0 (E-ticaret ve SEO notları)
> - alıntı zincirleri: sab8a + alıntılayan tibo_maker (G23), marckohlbrugge + alıntılayan ozi_dev (G22). G35'te tibo_maker, G33'te ozi_dev kendi gözlemiyle kaynak.
> - ChatSEO ailesi: VengeonsP, NicholasDulait, iziatask
> - aynı birincil veriyi aktaranlar: Etsy'nin 22 Ekim e-postası (bdurangg, berkayalinkilic, e_onbasioglu)
> - destekleyici, sayılmayan: wjsidiss'in etsyotomasyon aracı (E1, E2, E13); berkayalinkilic'in hattını izliyor, bağımsızlığı belirsiz
>
> Tanıtım (2026-11-13 turu): illyism (bülten), natiakourdadze (100 müşteri notu: kendi skill ve aracı), shiri_shh (RentMyHeader), 1tunademir (E16: göç hizmeti), wjsidiss (kendi aracı).
>
> **Denetim (2026-10-26):** G2 ve G21'in Kanıt sütunu düzeltildi ve playbook'a (`00 Girişim & Pazarlama.md`, kural 2 ve 21) taşındı.
> **Güncelleme (2026-11-01):** G8'e kaynak eklendi (★ aynı); G11'e Meta ayarı eklendi (tek kaynak kaldı); G15'in metni düzeltildi ve Kanıt sütunu bölündü; G22-G32 yeni. E1, E2 ve E6'ya kaynak eklendi, E6'nın Kanıt sütunu yeniden yazıldı; E11 ve E12 yeni.
> **Güncelleme (2026-11-13):** G11'e başa baş ROAS eklendi (tek kaynak kaldı); G22'ye illyism eklendi (registry ve dizin kısmı ★, iki kaynak da tanıtım); G33-G36 yeni. E1 ve E2'ye wjsidiss destekleyici olarak eklendi (★ değişmedi); E11 düzeltildi (herkese açık ilan verisi resmî API'den de okunabiliyor, kullanım amacı kısıtlı olabilir); E13-E17 yeni, hepsi tek kaynak.

## Kanal seçimi ve sıralama

| # | Kural | Kanıt | Kaynaklar |
|---|---|---|---|
| G1 | Kanallar birbirinin yerine geçmez, üst üste biner: çalışan kanalı bırakmadan bir sonrakini ekle. | ★ (vaka) | pierreeliottlal (2109787937684566357, Gojiberry), natiakourdadze (2113228918492692870, Postiz: Reddit changelog'u ve affiliate lansmandan sonra da sürdü) |
| G2 | Aynı anda beş kanal kovalama; birini çalışana kadar zorla, sonra sıradakine geç. | tek kaynak (vaka; B2B SaaS, aşama eşikleri o vakanın) | pierreeliottlal (2109787937684566357) |
| G3 | Ücretli reklam en son katman: önce outbound, topluluk, içerik ve SEO; ücretli kanal birim ekonomi oturunca. | ★ (vaka + veri) | pierreeliottlal (2109787937684566357, ücretli 1.500+ müşteride), aashrungautam (2112986890840551640, kârlı yazılım işletmelerinde PPC %4, ağızdan ağıza %46, SEO %38) |
| G4 | Reddit erken dönemde ucuz ve güçlü kanal; ama sadece değer paylaş: eğitici analiz, gerçek özellik changelog'u, niyetli soruya cevap. Hata düzeltmesi tek başına duyurulmaz. | ★ | pierreeliottlal (2109787937684566357), natiakourdadze (2113228918492692870, Postiz), chaitanya_one (2113050937740992626) |
| G5 | Uzun soluklu affiliate güçlü kaldıraç: tekrarlayan/ömür boyu komisyon ve uzun çerez; affiliate yazıları backlink de getirir. | ★ (vaka) | natiakourdadze (2113228918492692870, Postiz, %30 ömür boyu), pierreeliottlal (2109787937684566357, ömür boyu affiliate "büyük kaldıraç") |
| G6 | Lansman günü: üye olduğun topluluklara duyur, lansmanları (açık kaynak + Product Hunt) aynı güne yığ, lansman gibi görünmeyen tek bir video. | tek kaynak (vaka) | natiakourdadze (2113228918492692870, Postiz) |
| G34 | Lansman dizinleri ve awesome-list'ler ucuz bir backlink ve dizine alma katmanıdır, gelir kanalı değil. Listeyi önce canlılık için test et (park sayfası 200 döner, gövdeye bak); ürün bilgisini tek manifestte tut; girişli ve CAPTCHA'lı formları insan göndersin; "ücretsiz" görünüp ödeme isteyeni bırak. Sonucu yayına giren link, yeni referans alan adı ve ödemeyle ölç. | ★ (tanıtım; iki kaynak da kendi ürününe yönlendiriyor). "Gelir getirmez" kısmı tek kaynak (illyism, vaka) | illyism (2118261278137573417, 439 gönderim: 97 kayıt, 15 PR; SEO'daki ölçümü: 98 dizin → 64 ziyaretçi, 0 $), natiakourdadze (2120044213496840671, "20 ücretsiz startup dizini") |

## Müşterinin dili ve niyeti

| # | Kural | Kanıt | Kaynaklar |
|---|---|---|---|
| G7 | Müşteriyi listeden değil niyet sinyalinden bul: şikâyet, öneri isteme, "nasıl yaparım" gönderileri. Toplu şablon hacim yaratır, niyet yaratmaz. | ★ | chaitanya_one (2113050937740992626), sakevoid (2083960811878297860, leafer, tanıtım), pierreeliottlal (2109787937684566357, "niyet gösteren kişilere" outbound) |
| G8 | Müşterinin kendi kelimeleriyle çalış: yanıtta onların cümlesine atıf yap; içerik ve teklifi yayından önce müşteri diliyle beslenmiş bir "ICP ajanına" okut. | ★ (görüş) | EXM7777 (2113269645365174525, ICP ajanı), chaitanya_one (2113050937740992626), coreprompt (2114000699176493376, reklamın ilk cümlesi rakibin 1-2 yıldızlı yorumlarından) |
| G9 | Günde bir yüksek niyetli yanıt, 20 öfke gönderisine yanıttan iyidir; tarama otomatik olabilir, yanıtı insan yazar ve göndermeden önce onaylar. | ★ (görüş, biri tanıtım) | chaitanya_one (2113050937740992626), sakevoid (2083960811878297860, onaysız göndermiyor) |

## Teklif, reklam ve ölçüm

| # | Kural | Kanıt | Kaynaklar |
|---|---|---|---|
| G10 | Bütçeden önce teklif: "neden senden, neden şimdi, rakipten farkın ne" cevaplanmadan bütçe artırılmaz; para kaçıran yerler (fiyat, teklif, dönüşüm) kapanmadan reklamla büyütülmez. | ★ | cambudakburak (2113371571670888689, vaka), errenozgur (2062223900885254593, Hormozi videosu özeti) |
| G11 | Reklamın değerini yeni müşteriyle ölç; mevcut müşterileri bir sette hariç tutup karşılaştır. Tekrar satış ayrı kampanya, ayrı ölçüm. Meta'da bu ayrım kampanya ayarıyla da yapılabiliyor ("Customer Lifecycle Strategy": yeni / mevcut / ikisi). ROAS'ı tek başına değil başa baş ROAS'la (≈ 1 / reklam öncesi brüt marj) karşılaştır; sipariş başı reklam maliyetinin sepetin yüzde kaçı olduğuna bak, düşük sepetli üründe aynı ROAS zarar olabilir. | tek kaynak (görüş + vaka; ayarın adı ve yeri doğrulanmadı) | coreprompt (2112967188701184232; 2115120446169325666, Meta ayarı; 2119909549347880974, başa baş ROAS) |
| G12 | Hacimli içerik/UGC'de tek videonun tepesine değil günlük tabana bak. | tek kaynak (vaka) | sannticas_ (2112977888114831515) |

## PR ve dağıtım

| # | Kural | Kanıt | Kaynaklar |
|---|---|---|---|
| G13 | Basına lansman değil kendi verinden hikâye götür: kişisel ilk satır, tek şaşırtıcı sayı, tek müşteri hikâyesi, 100 kelime altı, istek yok. | tek kaynak (görüş; aynı yazarın SEO'daki istatistik sayfası notu destekliyor ama bağımsız değil) | natiakourdadze (2113193059995238617) |
| G14 | Edinimi başka platformun algoritmasına bağlama: lead magnet'leri sitede ücretsiz ver, e-postayı kendi kanalında topla. | tek kaynak (vaka) | Timseo_ (2112872778433249673) |
| G15 | X'te aynı metni gün içinde birçok yere yapıştırma (spam'e düşer); uzun okunan içerik öne çıkar. ("İzlenen içerik, video" kısmı kodla çelişiyor; bkz. playbook'taki Çelişkiler.) | ★ sadece okunma süresi kısmı (veri: tıkladıktan sonra okuma 0,4, kalma süresi 0,006). Spam kısmı tek kaynak (iddia). Video kısmı çelişkili: kodda video izleme 0, açma 0,02 | MrAente (2113208381456454016), vibeeval (2115738642459054251, okunma süresi kısmı, açık kaynak kod) |
| G35 | Lansman videosu gerçek ürünü vaat ettiği tek işi yaparken göstersin; basit bir ekran kaydı yeter, jargon yok, kitlenin diliyle. Kitlenin zaten olduğu yerde paylaş; ürün kapalıysa tek çağrı bekleme listesi. Çekmeden önce kendi kategorindeki lansmanların ilk 5 saniyesine bak (tutanlarla batanlar orada ayrılıyor). | İki yarı ayrı ayrı tek kaynak: gerçek ürün, sade ekran kaydı, kitlenin yeri tibo_maker (görüş); ilk 5 saniye shiri_shh (iddia, tanıtım). "Kitlenin olduğu yerde paylaş" G6 ile aynı yönde. Video bekleme listesini doldurur, büyümeyi tek başına taşımaz (Dropbox'ta referans programı; playbook'taki Çelişkiler) | tibo_maker (2118289869428380138, Dropbox demosu analizi), shiri_shh (2117256023975383484, 600 lansman videosu kütüphanesi; ilk 5 saniye iddiası; tanıtım) |

## AI ile iş modeli

| # | Kural | Kanıt | Kaynaklar |
|---|---|---|---|
| G16 | Özellik değil sonuç sat: "bu süreç şu kadar kısalır, şöyle" cümlesi; zaman, maliyet ve hata azalması. | ★ (görüş) | AIHighlight (2112940270597599505), EXM7777 (2112967402992570452, AI danışmanı) |
| G17 | Ajan her şeyi değil tek bir değerli işi uçtan uca yapsın; kritik adımda insan onayı. | ★ | AIHighlight (2112940270597599505), berkayalinkilic (E) (2097403472177938912) |
| G18 | Talebi iltifatla değil ücretli pilotla doğrula; işin maliyetini, sıklığını ve nerede bozulduğunu sektörden insanlara sor. | tek kaynak (görüş) | AIHighlight (2112940270597599505) |
| G19 | Ajan işini brief'le ver: hedef, teslim formatı (PDF/CSV/HTML), roller, doğrulama ölçütü. Planlama ve sentez güçlü modelde, bağımsız birimler paralel. | tek kaynak (iddia) | karankendre (2063668275641565429, X makalesi) |
| G20 | İki taraflı platformda arzı otomasyonla kendin üretirsen soğuk başlangıç sorunu küçülür. | tek kaynak (vaka) | Alican_Selcuk (2112948934544912559; aynı konuşmadaki kendi yanıtı 2112956283833790910 aynı notta) |

## Türkiye: vergi (bilgi, tavsiye değil)

| # | Kural | Kanıt | Kaynaklar |
|---|---|---|---|
| G21 | 20/B: belge → özel banka hesabı → bütün tahsilat bu hesaba → %15 stopaj nihai vergi. Başka yerde SGK'lı değilsen ilk ödemeyle Bağ-Kur başlar; gelir Bağ-Kur'u karşılamadan belge açma. Sınır tavandır, hedef değil. Mali müşavirle teyit. | ★ sadece işleyiş kısmı (fatihiosdev kendi tweet'inde anlatıyor). Bağ-Kur, sınır ve zamanlama tek kaynak (Tunimba). İddia, 2026 rakamları | Tunimba (2063997316864864374), fatihiosdev (2063218601897709729, Tunimba'nın alıntıladığı tweet; ayrı notu yok) |
| G36 | Yurt dışı yazılım ya da AI aboneliğini vergi numarasıyla kurumsal alırsan fatura KDV'siz gelir ama KDV kalkmaz: 2 No.lu KDV beyannamesiyle sorumlu sıfatıyla beyan edip ödersin, KDV mükellefiysen 1 No.lu'da indirirsin. Toplam maliyet değişmez; avantaj indirim hakkı. Mükellef değilsen avantaj yok, beyan yükü var. Beyan etmemek vergi ziyaı cezası riski. Mali müşavirle teyit. | tek kaynak (görüş; mevzuat okunmadı, uzmana doğrulat) | surucudev (2118056137958330856; ilk tweet'i yanıltıcıydı, kendi düzeltmesi 2118083793768624264 ve paylaştığı açıklama görseli aynı notta) |

## Ajanlar ve yeni dağıtım kanalları

| # | Kural | Kanıt | Kaynaklar |
|---|---|---|---|
| G22 | Ürünü ajanlara aç: arayüzdeki işler MCP/API'de de olsun (özellik eşitliği); kullanıcı verisine dokunan işlemlerde OAuth. Önce resmi MCP Registry'ye yayınla (birçok dizin oradan kopyalıyor), sonra trafiğe göre dizinlere gönder. | ★ (vaka + görüş). Registry ve dizin kısmı ★ (marckohlbrugge, illyism; ikisi de tanıtım). Kullanıcı ya da trafik etkisini hiçbir kaynak ölçmemiş | levelsio (2115586985888825445, nomads.com), marckohlbrugge (2115106902841397750, dizin listesi, tanıtım; alıntılayan ozi_dev aynı zincir), sab8a (2115830400178139506, "ürünü ajanların kullanmasını kolaylaştır"), illyism (2118261278137573417, tek açık repoda `server.json`, `glama.json`, `SKILL.md`, `gemini-extension.json` gibi dosyalarla 15+ AI/MCP kaydına form doldurmadan girmek; tanıtım) |
| G23 | Organik aramadan gelen tık düşüyorsa önce hangi ziyaretlerin kaybolduğunu ve gelirin değişip değişmediğini ayır; AI'da anılmayı ziyaret ve müşteriyle ölç; talebi marka araması ve ağızdan ağıza yayılmayla güçlendir. | ★ sadece ağızdan ağıza kısmı (veri). Teşhis ve ölçüm kısmı tek kaynak (görüş + VEED vakası) | sab8a (2115830400178139506, VEED; alıntılayan tibo_maker aynı zincir), aashrungautam (2112986890840551640, ağızdan ağıza %46, sadece bu kısım) |

## Creator, UGC ve clipping

| # | Kural | Kanıt | Kaynaklar |
|---|---|---|---|
| G24 | Creator/UGC programını portföy gibi yönet: çok sayıda creator ve klip; tek bir çıkış birçok başarısızın masrafını öder. Hacim tek başına yetmez, izleyici şüphelenince tutmaz. | ★ hacim kısmı (görüş + vaka). "Tek çıkış başarısızları öder" kısmı tek kaynak (sab8a) | sab8a (2115830400178139506), natiakourdadze (2113964209507631535, Whop, 4 haftada 8.000 clipper) |
| G25 | Creator'a ya da izlenmeye ödemeden önce kitleyi doğrula, sonra sonuca öde: takipçinin ülkesi, sadece doğrulanmış izlenme, klip başı tavan, klip başına kayıt; dönüştürene daha fazla öde. | ★ (vaka) | lukecarry_ (2114255053552791726, 3M izlenmeli İngilizce videonun kitlesinin %65'i Filipinler), natiakourdadze (2113964209507631535, bot çiftlikleri, klip başı kayıt) |

## Reklam: metin, hedefleme ve işletme

| # | Kural | Kanıt | Kaynaklar |
|---|---|---|---|
| G26 | Reklam metni alıcının tek şüphesini kanıtla gidersin: ilk cümleyi rakibin 1-2 yıldızlı yorumlarındaki şikâyetten çıkar; sıfat yerine belge (analiz raporu, menşe, fiyat geçmişi). | ★ (görüş + vaka; biri tanıtım). İlk cümle (rakibin 1-2 yıldızlı yorumları) tek kaynak: coreprompt | coreprompt (2114000699176493376), cambudakburak (2116508705051079137, doğal gıda), devindirim (2116025257903706253, fiyat geçmişi kartı, tanıtım) |
| G27 | Arama reklamında kategori kelimesi değil ürün + özellik kelimesi; bilgi kalıplarını (fayda, tarif, nasıl yapılır, zararlı mı) negatif kelimeyle ele. Kural 7'nin ücretli aramadaki karşılığı. | tek kaynak (vaka; 3,36 milyon TL Google'ın dönüşüm değeri, harcama yok) | cambudakburak (2116508705051079137) |
| G28 | Çalışan reklamı kopyalayıp daraltma ya da ilk günlerde değiştirme; kazananı koru, bütçeyi kademeli artır. | ★ (vaka). Artış hızı kaynağa göre değişiyor (Çelişkiler) | wickedguro (2116103272759021592, Meta), optimalfocus (M) (2114544390870118574, "1-3. gün dokunma, kazananları tut"), maubaron (M) (2113025482392314181, sadece kademeli artırma, TikTok) |
| G29 | Sosyal reklam ya da bio linki veriyorsan kayıt akışını reklamın açıldığı uygulamanın içinden test et: uygulama içi tarayıcı Google girişini engeller; algıla ve dış tarayıcıya geçiş ekranı göster. | tek kaynak (vaka) | VengeonsP (2114419469640782252, ChatSEO, 10 ay fark edilmemiş) |
| G33 | Reklamda tek formata bağlanma: videonun yanında statik reklamı da test et (hızlı üretilir, bir bakışta okunur). Tek kreatife güvenme; her hafta yeni açılar dene, kazananı rakam seçsin. | ★ (vaka + görüş). Drama ve espri reklamı kısmı tek kaynak (coreprompt). ozi_dev, itsnotmyai'yi Mobil'de alıntılamış; burada kendi gözlemi | coreprompt (2119909549347880974, 9 günlük vaka: statik, drama ve espri reklamları), ozi_dev (2120108648214974620, "statik çalışmaz sanıyordum"; quickdesign kütüphanesi), itsnotmyai (M) (2119169959896986096, Andromeda: format bir konsept ekseni, haftalık yeni konsept grubu) |

## X algoritması

| # | Kural | Kanıt | Kaynaklar |
|---|---|---|---|
| G30 | X'te kodla doğrulanan sinyallere göre yaz: özgün post (yanıt/RT değil), ilk 2 saatte beğeni (50 bin altı hesaplarda yeni post itişi), paylaşılmaya (link kopyalama 20, DM 5) ve yanıta (5; karşılıklı takipte 20) değer içerik, tıklandıktan sonra okutan uzunluk. "İlgilenmiyorum" dedirtecek hedefsiz posttan kaçın (-52); video izleme ve yer işareti skora girmiyor. | tek kaynak (veri). Canlı deneyler ve sunucu ayarları kodda yok | vibeeval (2115738642459054251, xai-org/x-algorithm; param.rs'i biz de kontrol ettik) |

## Rakip analizi ve farklılaşma

| # | Kural | Kanıt | Kaynaklar |
|---|---|---|---|
| G31 | Rakibin büyümesini zaman çizelgesiyle çöz: trafik kırılma noktasını bul, öncesindeki hamleleri (lansman, reklam başlangıcı, creator videosu, ürün döngüsü) eşleştir; her bulguyu GÖRÜLDÜ / ÇIKARIM diye etiketle. 60 günden uzun yayındaki reklam muhtemel kazanandır. | tek kaynak (tanıtım) | jasonzhou1993 (2116122945605222637, REA-growth) |
| G32 | Karşılaştırma ürününde kaynakların şişirilmiş puanını ya da indirimini olduğu gibi gösterme; kendi dağılımına ya da geçmişine göre düzelt, ham ve düzeltilmiş değeri yan yana göster. | ★ (vaka; biri tanıtım). Türkiye'de indirim öncesi fiyat olarak son 10 günün en düşüğü esas alınıyor (E12, tek kaynak; uzmana doğrulat) | levelsio (2115771822499049773, Hotelist puan normalizasyonu), devindirim (2116025257903706253, indirim "son 90 günde genelde" fiyata göre, tanıtım) |

## E-ticaret ve pazar yeri

| # | Kural | Kanıt | Kaynaklar |
|---|---|---|---|
| E1 | Aylık kiralanan araçların işini (toplu düzenleme, analiz, ürün yükleme) platform API'si/CLI'ı + AI ile kendi kurallarınla yaz. | ★ (vaka) | berkayalinkilic (2097403472177938912, Etsy API), becqir (2042381767517024385, Shopify CLI + AI Toolkit), e_onbasioglu (2115536494152851922, Etsy API anahtarı + Claude: rapor, listing önerisi, toplu fiyat/stok); destekleyici: wjsidiss (2119900269211427091, ücretli Etsy araçlarının yerine resmî API'yle çalışan açık kaynak araç; AI ile yazıldığı doğrulanmadı) |
| E2 | Mağazaya dokunan toplu işlemde akış "hazırla → göster → kontrol et → onaylarsa uygula"; tam otomatik bot yok. | ★ (wjsidiss sayılmadı: aracı berkayalinkilic'in hattını izliyor, bağımsızlığı belirsiz) | berkayalinkilic (2097403472177938912), AIHighlight (G) (2112940270597599505), e_onbasioglu (2115536494152851922, "yazsın, öneri getirsin, son onayı sen ver"); destekleyici: wjsidiss (2119900269211427091, README: varsayılan taslak; yayın, canlı düzenleme, SEO düzeltmesi, takip numarası ve pin önce sorulur; silme izni bile istenmez) |
| E3 | Modele API yazdırırken "endpoint veya alan uydurma, güncel resmi dokümantasyonu kullan" şartını koy; izinleri işe göre seç. | tek kaynak (vaka) | berkayalinkilic (2097403472177938912) |
| E4 | Listing'leri kendi kural dokümanınla 100 üzerinden puanlat: puanın nereden kırıldığı, en büyük sorunlar, ne değişmeli. | tek kaynak (vaka) | berkayalinkilic (2097403472177938912) |
| E5 | Bir modelle yaz, başka modelle denetle. | ★ (görüş) | becqir (2042381767517024385, Claude Opus yazar, Codex denetler), EXM7777 (2113631026140643582, Claude Code kategorisi: başka modelle alt ajan incelemesi) |
| E6 | Pazar yerinde AI araç olarak serbest ama beyan edilir ve satıcının rolü görünür; botla tek tıkla listing yok; her listing'de en az bir düzenlenmemiş gerçek fotoğraf (istisnalar var). | tek kaynak, iddia (üçü de Etsy'nin aynı e-postasını aktarıyor; resmi metin açılmadı) | bdurangg (2113303171154272365), berkayalinkilic (2114638568295395405, 22 Ekim alıntısı), e_onbasioglu (2115536494152851922) |
| E7 | Rakiplerin çalışan reklamlarından öğren: hook, format, teklif ve farkındalık aşamasını çıkar; formatı kendi ürününle yeniden üret. | ★ (ikisi de tanıtım) | 1tunademir (2113020445998141887, remix), TheMattBerman (R) (2100654891756589230, 724 reklamı etiketleme) |
| E8 | Baskı ve kesim ürünlerinde PNG değil vektör (SVG). | tek kaynak (tanıtım) | wjsidiss (2113301020826624420) |
| E9 | Tedarikçi ararken başarılı markanın üreticisini gümrük kayıtlarından bul (ABD ithalatıyla sınırlı). | tek kaynak (görüş) | canceylandigi (2073718386647871556) |
| E10 | AI arama (GEO) e-ticarette küçük ama hızlı sipariş kaynağı olabilir; AI kaynaklı trafiği ayrı ölç. | tek kaynak | Ruesandora0 (2112914594565869632, vaka; aynı yazarın SEO'daki 100 site verisi bağımsız sayılmadı) |
| E11 | Mağaza yönetimi API'si kendi verine yazar. Rakip mağaza ve arama sırası incelemesini ajana tarayıcıdan (ör. eRank) yaptır. Düzeltme (2026-11-13): herkese açık ilan verisi (arama sonucu, etiket, fiyat, favori) resmî API'den de okunabiliyor, wjsidiss'in aracı rakip araştırmasını böyle yapıyor. Ama API koşullarının bu veriyi analitik için kullanmayı yazılı izne bağladığı söyleniyor (E14); amacı önce koşullardan doğrula. | tek kaynak, çelişkili | e_onbasioglu (2115536494152851922, görüş); karşı örnek: wjsidiss (2119900269211427091, README) |
| E12 | İndirim iddiasında karşılaştırılan eski fiyat yasal pencerenin en düşüğü olmalı ve reklamda görünmeli (Türkiye: indirimden önceki 10 günün en düşüğü); gerçeğe aykırı aciliyet dili ("son ürün", "son saat") kullanılmaz. Yaptırım bu yıl 108.370 TL ile 39,9 milyon TL arasında. | tek kaynak (veri, ikinci el; resmi metin açılmadı) | gkntan (2115127200038932955) |
| E13 | Etsy API'yi satış yapan mağazada Developer Mode'a alarak deneme: ilanlar aramada keşfedilemez olur, trafik kesilir. Çıkmak için önce aktif test ilanlarını kaldır, developer@etsy.com'a yaz (bir vakada ~4-5 saat). | tek kaynak (veri: Etsy'nin kendi metni). wjsidiss sayılmadı, bağımsızlığı belirsiz | berkayalinkilic (2118258299359445470, Etsy'nin kendi geliştirici sayfasının ekran görüntüsü); destekleyici: wjsidiss (2119900269211427091, README: "Developer Mode'u açmayın") |
| E14 | Etsy'den alınan içeriği (rakibin başlığı, etiketi, açıklaması) izinsiz AI'a verip türev üretme; 16 Aralık'tan itibaren elle kopyalanması da yasak (madde 6.E). API verisini Etsy'nin yazılı izni olmadan analitik, makine öğrenmesi ya da AI eğitimi için kullanma. İlham serbest, kopya değil. | tek kaynak (iddia; Etsy'nin koşul metinleri açılmadı) | e_onbasioglu (2118713496032383071) |
| E15 | Etsy API'de erişimi varsayma, uygulamanın kendi satırından doğrula. Kişisel erişim README'ye göre 5 QPS ve günde 5.000 istek. Ticari erişim onaylı bir kişisel uygulama ve uzun bir inceleme istiyor; bir ticari uygulamanın satırında 150 QPS / günde 100 bin görünüyor. Alıcı adresi ayrı izin. Yeni anahtarlarla takip numarası Türkiye'de kısıtlı. Uygulama adında "Etsy" geçmesin. | tek kaynak (her madde ayrı kaynaktan); ortak çekirdek "ticari erişim her şeyi açmaz" e_onbasioglu ve wjsidiss'te | wjsidiss (2119900269211427091, README, CLI.md), e_onbasioglu (2118713496032383071, kendi ticari başvurusu), berkayalinkilic (2118258299359445470, ekran görüntüsü) |
| E16 | Platform göçünde: eski URL'leri tek tek 301'le eşle, SEO alanlarını koru, ürün → müşteri → sipariş sırasıyla aktar, ödeme, kargo ve vergiyi gerçek sepetlerle dene, reklam olaylarının çift sayılmadığını doğrula. DNS'te MX, SPF ve DKIM'i koru. İlk günlerde 404, Search Console, dönüşüm ve ödeme hatalarını izle; doğrulama bitmeden eski sistemi silme. | tek kaynak (görüş; tanıtım: göç hizmeti satıyor) | 1tunademir (2117887542649368741) |
| E17 | Toplu yazan satıcı aracında: metni deterministik üret (aynı girdi aynı çıktı, böylece örneklem kontrolü anlamlı olur), platform sınırlarını üretim anında zorla. İdempotency anahtarı olmayan yazma isteğini körlemesine tekrar deneme: 429 tekrar denenir, ama gitmiş olabilecek bir yazma (taslak, alıcıya e-posta) belirsiz diye raporlanır. Yarım kalan toplu yüklemeyi kayıt tutarak sürdür, mükerrer oluşturma. | tek kaynak (iddia; kod okunmadı, sadece belge ve modül açıklaması) | wjsidiss (2119900269211427091, README, CLI.md) |
