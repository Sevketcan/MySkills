# Kurallar ve kaynakları

> Bu dosya `Bilgi Bankası/Mobil Geliştirme/00 Mobil Geliştirme.md` içindeki playbook'tan üretilir. Elle düzenleme; playbook'u güncelle, sonra bu dosyayı yenile.
> ★ = en az 2 bağımsız kaynak. ★★ = 4 ve üstü. Kaynak id'leri X yer işareti id'leridir.
> Kanıt düzeyi kaynağın kendisi içindir: iddia · görüş · vaka · veri. Henüz "denendi" olan kural yok.
> Aynı raporun özeti ayrı kaynak sayılmaz (david_attisaas 2112895931062636617 → Adapty).
> **Tanıtım (`tanitim: true`):** Adapty (2112499213796003976), RevenueCat (2113016096139997583, 2113661600603443282), statistics1012 (2112848115753451897), jacobrodri_ (2113623373335122152), thousif_maker (2112877677245874506). ★ sayımı tanıtımı ayırmıyor.
> **Denetim (2026-10-26):** K5, K18-K21, K23 ve K25'in Kanıt sütunu düzeltildi ve playbook'a (`00 Mobil Geliştirme.md`) taşındı.

## Yayın öncesi ve App Review

| # | Kural | Kanıt | Kaynaklar |
|---|---|---|---|
| K1 | Sunucuda uid'ye bağlı veri varsa (Firebase anonymous auth dahil) Ayarlar'da tek akışta çalışan "Hesabı sil" olsun. "Mail at" ya da "forma git" yetmez (5.1.1(v)). | tek kaynak, iddia | istifadilkcesi (2113184141768310935) |
| K2 | Sign in with Apple kullanılıyorsa silme anında Apple token'ı Apple sunucularında iptal (revoke) edilsin. | tek kaynak, iddia | istifadilkcesi (2113184141768310935) |
| K3 | Reviewer notlarına silme akışının adımlarını tek tek ve ekran kaydı linkini yaz; reviewer bulamazsa 2.1 reddi gelir. | tek kaynak, iddia | istifadilkcesi (2113184141768310935) |
| K4 | Mağaza açıklamasının sonuna Privacy Policy, EULA, Terms ve Support linkleri; otomatik yenileme ve iptal bilgisi. | tek kaynak, vaka | samlecan (2112965084762771807) |
| K5 | İlk gönderimde haftalık 9,99$ fiyat koyma; onaydan sonra yükselt ya da paket ekle. | tek kaynak, vaka (yazarın deneyimi; Apple'ın yazılı kuralı değil) | samlecan (2112965084762771807) |
| K6 | Paywall'da faturalanan tutar en belirgin rakam olsun; yıllık plan "haftalık" fiyatla satılmasın (3.1.2). Gerçek indirim yoksa geri sayım ya da "sınırlı teklif" yok (5.6). İndirim gerçekse sunumu yaratıcı olabilir. | ★ | AppStorePolice (2112652373520679305, vaka), appstoretracker (2112981500727873882, vaka) |
| K7 | Nişe girmeden son 30 günde o nişten kalkan uygulamalara bak. Şu an en riskli: AI foto/video editörleri, AI companion, görüntülü sohbet/flört. | ★ | Siron93 (2111529179598434577, veri), itsnotmyai (2113501027487862907, görüş) |
| K8 | Tanınmış bir uygulamanın ikonunu ya da adını taklit etme; klon/spam görünümlü build'ler otomatik taramaya (4.3, 2.5.19) takılır. Çok hızlı gelen red bunun işareti olabilir. | ★ | Siron93 (2111529179598434577, veri: klon authenticator'lar), istifadilkcesi (2113184141768310935 thread'inin yanıtı, iddia) |
| K9 | Doz hesaplayan sağlık uygulamaları kurum güvencesi olmadan kaldırılıyor; sağlık, fitness ve finansta uzman ya da kurum görünür olsun. | tek kaynak, iddia, tanıtım | thousif_maker (2112877677245874506) |
| K10 | Red döngüsünde Meet with Apple → "App Review appointment" (30 dk Webex) iste. Talepte uygulamanın Apple ID'si ve somut konu; aktif Developer Program üyeliği gerekli. | tek kaynak, vaka + Apple sayfası | yigitech (2112075095363514465) |
| K11 | Hesap 3.2(f) ile kapandıysa Apple Support'a itiraz et; geri açılma e-posta ile bildirilmeyebilir. | tek kaynak, vaka | meyusufdemirci (2112838807800177074) |
| K12 | Mağaza ekran görüntüsü gerçek ekrandan çok farklı olmasın; az yazı, tek değer önerisi, içerikle uyumlu buton. | tek kaynak, görüş | meyusufdemirci (2112911761170977084) |

## iPhone Duo ve ekran uyumu

| # | Kural | Kanıt | Kaynaklar |
|---|---|---|---|
| K13 | iPhone Duo'nun kapalı (dar, kısa) ve açık (geniş) ekranı için ayrıca hazırlan; kapalı, açık ve yan çevrilmiş halde test et. iPad düzeni hazırsa iş kısa. | ★ | twostraws (2113580570634600776, görüş), Kerem_Erkan (2113168278977720399, vaka), RevenueCat (2113661600603443282, rehber) |
| K14 | Kendi tab bar'ını çizme; sistemin gezinme bileşenini ya da genişliğe uyarlanan bir düzen kullan. | tek kaynak, görüş | twostraws (2113587082816000064) |
| K15 | Paywall: içerik en fazla ~600pt, satın alma butonu ~400pt, ortada; kapalı ekranda fiyat ve buton görünür; kapat butonu sistem kontrolü. RevenueCat Paywalls'ta min/max için iOS SDK 5.93.0+, çok adımlı paywall için 5.83.0+. | tek kaynak, tanıtım | RevenueCat (2113661600603443282) |

## Paywall ve monetizasyon

| # | Kural | Kanıt | Kaynaklar |
|---|---|---|---|
| K16 | Paywall onboarding'in sonunda olsun (onboarding paywall'u %0,85, sonrakiler %0,23; ilk satın almaların %93'ü kurulum günü), ama sonraki paywall'ları kaldırma (gelirin %38'i). | ★ | Adapty (2112499213796003976, veri), statistics1012 (2112848115753451897, vaka), appstoretracker (2112981500727873882, vaka) |
| K17 | Onboarding'de kısa anket ya da sorularla kişiselleştir, sorunu ve sosyal kanıtı göster, yükleme ekranını boş bırakma. | ★ | statistics1012 (2112848115753451897), appstoretracker (2112981500727873882), Adapty (2112499213796003976: kişiselleştiren üst %10) |
| K18 | Önce teklifi test et (yerelleştirme %62, deneme %60, plan süresi %59 oranında LTV artırdı), sonra görsel ve metni (%35). | tek kaynak, veri, tanıtım | Adapty (2112499213796003976) |
| K19 | Deneme süresi plana göre: haftalıkta 3 gün, aylık ve yıllıkta 7 gün. | tek kaynak, veri, tanıtım | Adapty (2112499213796003976) |
| K20 | Fiyat çapası: haftalık ~6,99$, aylık ~9,99$, yıllık ~39,99$. Haftalık 9,99$ ilk gönderimde riskli. | ★ (rakamlar Adapty'nin tipik fiyatları: referans, kural değil) | Adapty (2112499213796003976, veri), samlecan (2112965084762771807, vaka), mmdincerdev (2112959602014691668, vaka) |
| K21 | Az plan göster (çoğunlukla 2), birini önceden seçili getir; az kullanılan planı "tüm planlar" arkasına al. | ★ (zayıf: Adapty yaygınlığı ölçüyor, etkiyi değil; diğeri tek vaka) | Adapty (2112499213796003976, veri), appstoretracker (2112981500727873882, vaka) |
| K22 | Web funnel / web checkout mağaza komisyonunu düşürür ama arkasında yoğun ücretli trafik var. RevenueCat kullanıyorsan önce Funnels + Web Billing. | ★ | jacobrodri_ (2113623373335122152, vaka), RevenueCat (2113016096139997583, tanıtım), gursuyaman (2112907095813058930, görüş) |
| K23 | Edinim kaynağına göre paywall/teklif kişiselleştirmesi neredeyse hiç yapılmıyor (%6): fırsat. | tek veri kaynağı, tanıtım | Adapty (2112499213796003976); araç: RevenueCat Audiences (2113016096139997583) |

## ASO ve edinim

| # | Kural | Kanıt | Kaynaklar |
|---|---|---|---|
| K24 | Ücretli edinimi baştan planla; yeni uygulamada organik mağaza trafiği tek başına yetmiyor. | ★ | gursuyaman (2112907095813058930, görüş), maubaron (2113025482392314181, vaka), jacobrodri_ (2113623373335122152, vaka: 504 aktif reklam) |
| K25 | TikTok: formatı organikte bul → MMP kur → tüm videoları Spark Ad yap → tek geniş kampanya (ABD) → 100$/gün, haftada %15-20 artır → ROAS 1,5x altını kapat → her hafta yeni kreatif. Organik izlenme reklam başarısını öngörmez. | tek kaynak, vaka (100$/gün, %15-20 ve 1,5x vakanın parametreleri; ROAS penceresi belirsiz) | maubaron (2113025482392314181) |
| K26 | ASO'da doymuş, yüksek zorluklu kelimeler yerine niyete uygun kelimeleri hedefle; trafik kanalına göre Custom Product Page kur. | tek kaynak, görüş | istifadilkcesi (2113368640783552609) |
| K27 | Kanıtlanmış bir kalıbı yeni dikeylere taşımak bir portföy yolu; aynı hesapta benzer uygulamalarda 4.3 riskine dikkat (K8). | tek kaynak, vaka | mmdincerdev (2113684378463170622) |

## Araçlar

| # | Kural | Kanıt | Kaynaklar |
|---|---|---|---|
| K28 | Ajanın simülatör ve cihazı kullanabilmesi için araç ver (idb, xcbeautify, mitmproxy, MobAI). | ★ | ilkerulusoy (2082082098039476504), yasinaktimur (2042484704490713149) |
| K29 | Mağaza işlerini CLI'dan yap: iOS için `asc`, Android için `gpc`; metadata repo'da, değişiklik `--dry-run` ile önizlenir. | tek kaynak | doncoderlione (2097420985196581281) |

## Çelişkiler (kural yazılmadı)
- ASO'nun etkisi: istifadilkcesi (önemli) ↔ gursuyaman, niklogvinenko (öldü).
- AI foto/video nişi: itsnotmyai (değmez) ↔ istifadilkcesi (kurala uyana bir şey olmaz).
- Varsayılan plan: Adapty (%67 yıllık seçili) ↔ Keiki (indirimli haftalık seçili).
- Deneme iptal oranı (%44 ilk 24 saat): sadece david_attisaas özetinde; rapor özetinde görülmedi.
