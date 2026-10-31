# Kurallar ve kaynakları

> Bu dosya iki playbook'tan üretilir: `Bilgi Bankası/YouTube & İçerik/00 YouTube & İçerik.md` (YT) ve `Bilgi Bankası/Video Araçları/00 Video Araçları.md` (VA). Elle düzenleme; playbook'ları güncelle, sonra bu dosyayı yenile.
> ★ = en az 2 bağımsız kaynak. ★★ = 4 ve üstü. ★ (küme) = kaynaklar sadece 0xwhrrari ve beamnxw; bağımsızlıkları şüpheli, orta güven. Kaynak id'leri X yer işareti id'leridir.
> Bağımsızlık: Adam_DelDuca'nın 4 kaydı tek kaynak; TubeLabHQ Adam_DelDuca ile aynı küme sayıldı. Hiçbir kural "denendi" değil.
> **Tanıtım (`tanitim: true`):** Adam_DelDuca (4 not), TubeLabHQ, ShaunYoung_YT, ErnestoSOFTWARE, natiakourdadze (2112913968670892052), AndyL5cc, WiroAI. ★ sayımı tanıtımı ayırmıyor; bütün kaynakları tanıtım olan kurallar işaretli.
> **Denetim (2026-10-26):** kural 5, 7, 27 ve 31'in Kanıt sütunu düzeltildi ve playbook'lara (YT 5, 7, 18; VA 13) taşındı.

## Senaryo ve kanca
| # | Kural | Kanıt | Kaynaklar | Playbook |
|---|---|---|---|---|
| 1 | İlk 2-3 saniyede kanca: kimin neyi kaybedebileceği belli olsun; "Selam, bu videoda…" ile açma. | ★ | vibeeval (2113736879476555939), TubeLabHQ (2112891684677935149), 0xwhrrari (2112166940081004693) | YT 1 |
| 2 | Kanca bir merak boşluğu açar, cevabı videonun içine erteler (tek soru, iddialı cümle, önce-sonra görüntü). | ★ | vibeeval, TubeLabHQ, ShaunYoung_YT (2111528539447087353) | YT 2 |
| 3 | 45-60 sn'de 2-3 döngü: risk → büyük soru → ters köşe → yeniden kanca; ters köşe başta söylenenle çelişmez. | tek kaynak (vaka) | vibeeval | YT 3 |
| 4 | Açılışı altı kalıptan seç: soğuk açılış, ham görüntü, "sen" bakışı, nesneyi göster, iddialı cümle, kişisel itiraf. | tek kaynak (tanıtım) | TubeLabHQ | YT 4 |
| 5 | Senaryoyu outlier videoların ya da en uzun yayındaki reklamların transkript yapısından türet; yapıyı al, içeriği kendin üret. | ★★ (0xwhrrari/beamnxw tek küme sayılınca 4 küme; 3'ü tanıtım) | Adam_DelDuca (2113229912844689713) / TubeLabHQ, ErnestoSOFTWARE (2111878898552102934), 0xwhrrari, beamnxw (2113275303808160226), AndyL5cc (2109133876702703805) | YT 5 |
| 6 | Claude'un ilk taslağı başlangıçtır; kanca ve olgusal iddiaları yayından önce insan kontrol eder. | ★ | vibeeval, tom_doerr (2036587518196396354), 0xwhrrari | YT 6 |

## Niş ve konu
| # | Kural | Kanıt | Kaynaklar | Playbook |
|---|---|---|---|---|
| 7 | Nişi doğrula: küçük kanallarda outlier izlenme, RPM ~5$+, 100 fikir, yüz gerekmiyor. | ★ (eşikler tek kaynak; iki kaynak da tanıtım) | Adam_DelDuca (2113261707325792669), ShaunYoung_YT | YT 7 |
| 8 | Konuyu talep sinyalinden çek: çok yorumlu Reddit soruları, trend ve outlier videolar, Google Trends. | ★ | Adam_DelDuca (2112899336887476512), tom_doerr | YT 8 |
| 9 | Tutan formatı seri yap ve bırakma. | ★★ | Adam_DelDuca, ShaunYoung_YT, jacobrodri_ (2112980072684458180), ozcnkrtn (2038548032602419646) | YT 9 |

## Üretim hattı
| # | Kural | Kanıt | Kaynaklar | Playbook |
|---|---|---|---|---|
| 10 | Hattı tek işli, ayrı çalıştırılabilir adımlara böl: konu → senaryo → ses → görsel → kurgu → yayın. | ★★ | wjsidiss (2082524786198970514), tom_doerr, Aykutuces (2076690210482532804), Adam_DelDuca (2112861480185897207) | YT 10 |
| 11 | Altyazıyı metinden üret ve sesle hizala (paragraf süresine oranla ya da kelime düzeyinde). | ★ | wjsidiss, tom_doerr, AndyL5cc | YT 11 |
| 12 | Explainer ve belgesel için Edge TTS yeterli; çalışan sürümü sabitle. | ★ | wjsidiss, tom_doerr | YT 12 |
| 13 | Büyük ffmpeg işlerini kademeli birleştir; katmanlı seste `amix=normalize=0`. | tek kaynak (vaka) | wjsidiss | YT 13 |
| 14 | Görseli açık arşivden al; Wikimedia'da 1-2 kelimelik sorgu ve istekler arası bekleme. | tek kaynak (vaka) | wjsidiss | YT 14 |

## Kodla motion ve launch videosu
| # | Kural | Kanıt | Kaynaklar | Playbook |
|---|---|---|---|---|
| 15 | Vibe prompt değil yönetmen brief'i; ürün gerçeklerini film kararlarından ayır. | ★ (küme) | 0xwhrrari, beamnxw | VA 1 |
| 16 | Gerçek ürün ekranı, logo ya da metrik uydurtma; eksik varlıkta ajan durur ve sorar. | ★ (küme) | 0xwhrrari, beamnxw | VA 2 |
| 17 | Referansa tek görev ver, ondan ölçülebilir kararlar çıkar; konusunu, logosunu, metnini kopyalama. | ★ | 0xwhrrari, beamnxw, AndyL5cc | VA 3 |
| 18 | Çekim listesiyle yaz: giriş durumu, çıkış durumu, amaç; üretken video promptunda da çekim, diyalog, ses, kamera katmanları. | ★ | 0xwhrrari, beamnxw, ozcnkrtn | VA 4 |
| 19 | Zamanı kare numarasına bağla; deterministik, seekable render, seed'li rastgelelik. | ★ (küme) | 0xwhrrari, beamnxw | VA 5 |
| 20 | Export'tan önce still/contact sheet; kusuru kare numarası, kanıt ve yerel düzeltmeyle onar. | ★ (küme) | 0xwhrrari, beamnxw | VA 6 |
| 21 | Ses olayları görüntüyle aynı zaman çizelgesinde. | ★ (küme) | 0xwhrrari, beamnxw | VA 7 |
| 22 | Uzun ajan koşularına onay kapıları; ajan geri dönülmez marka kararı vermez. | ★ (küme) | 0xwhrrari, beamnxw | VA 8 |
| 23 | Kararları dosyada tut ki sonraki video aynı tabandan başlasın. | ★ (küme) | 0xwhrrari, beamnxw | VA 9 |
| 24 | 16:9 ve 9:16 ayrı kompozisyon; kırparak türetme. | tek kaynak | 0xwhrrari | VA 10 |

## AI ile görsel ve video
| # | Kural | Kanıt | Kaynaklar | Playbook |
|---|---|---|---|---|
| 25 | Ürün/UI/tipografi için kodla motion; fotogerçek insan ve karakter için üretken video ya da 3D. | ★ | 0xwhrrari, KinGao476942 (2112729924943634602), beamnxw | VA 11 |
| 26 | Karakter tekrar edecekse önce kimliği kilitle (karakter kartı, referans kimlik), sonra sahne üret. | ★ | leo_xiaolei (2102674531655770534), Aykutuces | VA 12 |
| 27 | Viral ya da reklam yapısını çoğaltırken zamanlamayı kelimeye bağla, parçaları değiştirerek varyant üret. | tek kaynak (iddia, tanıtım) | AndyL5cc | VA 13 |

## Paketleme, dağıtım ve reklam
| # | Kural | Kanıt | Kaynaklar | Playbook |
|---|---|---|---|---|
| 28 | Başlık ve thumbnail'i ölç: 5-6 aday, skor ya da A/B. | ★ | wjsidiss, Adam_DelDuca | YT 15 |
| 29 | Thumbnail hikayeyi tıklamadan anlatsın (önce → sonra). | tek kaynak (vaka, tanıtım) | ShaunYoung_YT | YT 16 |
| 30 | YouTube açıklaması: anahtar kelime ilk 2 satırda, zaman damgaları, en fazla 3 hashtag. | tek kaynak | wjsidiss | YT 17 |
| 31 | Yorumu lead'e çevir: anahtar kelimeli CTA + otomatik DM. | ★ (iki kaynak da tanıtım) | natiakourdadze (2112913968670892052), Adam_DelDuca | YT 18 |
| 32 | Tek ham konuşan kafa çekiminden ayrı 9:16 ve 16:9 kesimler. | tek kaynak (vaka, tanıtım) | ErnestoSOFTWARE | YT 19 |
| 33 | Reklam kreatifini Ad Library'de en uzun yayında kalan reklamların yapısından türet. | ★ | ErnestoSOFTWARE, 1tunademir (2113343805365596459), AndyL5cc | YT 20 |

## Özet
- 33 kural: 3 ★★, 14 ★, 7 ★ (küme), 9 tek kaynak.
- Bağımsız çok kaynaklı (★ ve ★★) 17 kural skill'in çekirdeği; "küme" kuralları iş akışı 5'te orta güvenle kullanılıyor.
