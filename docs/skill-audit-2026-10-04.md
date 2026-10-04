# Skill koleksiyonu incelemesi — 4 Ekim 2026

## Sonuç

Koleksiyonda bazı talimatlar modeli gereksiz yere sınırlıyor. Sorun yalnızca skill sayısı değil: genel programlama bilgisinin tekrarı, geniş tetikleyiciler, her işte aynı süreç ve tek proje tercihinin bütün projelere uygulanması.

Özel araç sözleşmeleri, çalıştırılabilir yardımcılar, sürüme duyarlı API tuzakları ve kişisel tercihler değerli. Bunlar korunarak katalog sadeleştirildi. Modelin genel bilgisi tek başına yerel connector davranışını veya senin tercihlerini bilmesini sağlamaz.

## Ölçüm

| Kişisel koleksiyon | Önce | Sonra |
| --- | ---: | ---: |
| Üst paket | 48 | 43 |
| Keşfedilebilir SKILL.md girişi | 137 | 43 |
| Description alanlarının toplam karakteri | 29.098 | 6.137 |

Giriş sayısı %68,6, description karakterleri %78,9 azaldı. Bu ölçüm sistem skill'lerini ve plugin paketlerini içermez. Karakter sayısı token ölçümü değildir. Skill gövdeleri koşullu okunur; büyük bir dosyanın varlığı bütün görevlerde tamamının yüklendiği anlamına gelmez.

[137 girişin karar ve yeni konum listesi](skill-inventory-2026-10-04.csv) ve [ölçüm verisi](skill-inventory-metrics-2026-10-04.json).

## Kararlar

| Alan | Önceki sorun | Uygulanan değişiklik |
| --- | --- | --- |
| Unity REST / Blender belgeleri | Ebeveyn yönlendirmesine ek olarak 89 bağımsız alt giriş | GUIDE.md / INDEX.md referansları; şemalar, API tuzakları ve örnekler korundu |
| game-feel, game-ui-ux, input-systems, save-systems, procedural-gen | Genel oyun programlama tarifleri ve gereksiz varsayılanlar | gdd-studio/references/engine-neutral altında isteğe bağlı tarifler |
| fullstack-dev | 1005 karakterlik tetikleyici, her projeye zorunlu stack ve mimari | Kişisel stack seçildiğinde geçerli tercihler; mevcut proje ve kullanıcı kapsamı öncelikli |
| Blender MCP | Her 3D işinde tetiklenme, Cogito ölçülerinin ve eski Windows yolunun genel kurala dönüşmesi | Connector sözleşmeleri girişte; proje tarifleri koşullu referansta |
| Unity MCP | Her işlemde kaynak okuma ve uzun örnek akışı | Derleme, hedef kimliği, hash ve timeout tuzakları girişte; ayrıntılar referansta |
| SpriteAtlas | Her işte tam prebuild/Addressables pipeline ve mevcut koda yeniden izin soruları | Mevcut pipeline, yetkilendirilmiş düzeltme ve gereken teslim kontrolü esas |
| Unity Search | Her nesne aramasını Search penceresine zorlama | Search arayüzü veya sorgu sözdizimi isteyen görevlere daraltma |
| Three.js | Beş skill veya dört referansı peşinen okuma; anahtar varsa üretim zorunluluğu | İhtiyaca göre uzman seçimi; üretim istenen kapsam ve görsel hedefe bağlı |
| Dream Loop | Genel kalite isteğini özel üretim sürecine yönlendirme; dış kaynak kısıtını başka sağlayıcıyla aşma | Adı verilen sürece daraltma; kullanıcı kısıtları bütün kaynaklar için geçerli |

Diğer Unity paketleri somut API örnekleri, araç akışları ve kaynaklar sağladıkları için korundu; description alanları görev odaklı kısaltıldı. Playwright'ın mevcut özgül tetikleyicisi korundu. Scriptler, C# örnekleri, kaynak atıfları ve lisans bildirimleri kaldırılmadı.

Bu değişiklik “bütün ayrıntılı rehberler gereksiz” sonucuna dayanmıyor. Daha az otomatik keşif, daha dar talimat ve gerektiğinde ayrıntıya erişim hedefleniyor.

## Kalan plugin tekrarları

Kurulu Unity plugin'iyle 25 kişisel üst paket aynı isimde örtüşüyor. İlk incelemede bunların 12'si birebir aynı, 13'ü yerel değişiklikliydi. Güncel kişisel metinler artık plugin kopyalarıyla birebir aynı olmak zorunda değil.

Plugin önbelleği ve Unity araç bağlantıları değiştirilmedi. Bu nedenle uygulamanın toplam kataloğu 43 skill'e düşmüş değildir. Sonraki karar, yerel özelleştirmeler ve araç bağımlılıkları kontrol edilerek bu paketler için tek aktif kaynak seçmek olmalı.

## Model kalitesi konusunda sınır

A/B görev testi yapılmadı. Yapısal yük ve kapsam sorunları düzeltildi; Codex veya Claude'un her görevde daha iyi sonuç vereceği henüz ölçülmüş değil.

Karşılaştırma için aynı model/sürüm ve başlangıçla üç görev uygun: küçük kod düzeltmesi, belirsiz tasarım kararı, karmaşık Unity/Blender araç işi. Başarı, kapsam dışı değişiklikler, gereksiz sorular, token ve araç çağrısı sayısı birlikte ölçülmeli. Genel görevlerde gereksiz rehber yüklemeyi azaltıp özel araçlarda gerekli ayrıntıyı korumak temel hipotez.

## Kurulum ve geri dönüş

Değişiklikler hem Codex hem Claude kişisel kurulumuna uygulandı. Yeni katalog için iki uygulamayı da yeniden başlatmak gerekir. Bu açık güncellemede Claude'un normalde ayrı kaynaktan gelen fullstack ve Unity kopyaları da yenilendi.

Çalışma dalı codex/skill-simplification. GitHub'a gönderim yapılmadı; otomatik yayın bu dalda çalışmaz.

İlk tam yedek yolu:

    /Users/soern/Library/Application Support/MySkills/backups/skill-review-20261004T144917Z

Yedek repo skill ağacını, iki kişisel kurulumu, manifest'i ve senkronizasyon baz çizgisini içerir. Kurucunun sonraki yedekleri agent'ın skill-backups dizinindedir. Geri dönüşte repo, iki kurulum ve baz çizgisi beraber ele alınmalı; tek taraftan silinen dosyalar normal senkronizasyonda geri gelebilir.

Başka makinede yerel kurucuyu --target both --all ile çalıştırın; Windows karşılığı -Target both -All. Kurucu beş eski paketi katalog dışına yedekler ve güncellenen paket ağaçlarını değiştirir. retired-skills.json eski beş paketin ve 89 alt girişin sync/export üzerinden geri gelmesini engeller. Senkronizasyon başka makinelerde eski kopyaları kendiliğinden silmez; önce kurulum güncellemesi gerekir.

## Doğrulama

- Koleksiyon doğrulayıcısı ve skill-creator quick_validate: 43 giriş başarılı.
- 16 otomatik test: mevcut 13 test; eski paket/alt girişin geri gelmemesi ve iki agent'ta dry-run, dosyaları yedekleme, tekrar kurulum için 3 yeni test.
- Bash kurulum ve senkronizasyon betiklerinin sözdizimi başarılı.
- Taşınan Markdown bağlantıları kontrol edildi; gerçek yeni kırık bağlantı kalmadı. İnceleme sırasında önceden bozuk Fal ve ProBuilder bağlantıları da düzeltildi.
- İki gerçek kişisel kurulum güncellendi; ardından senkronizasyon 0 değişiklikle tamamlandı.
- PowerShell kurucusu bu macOS ortamında çalıştırılamadı. Arşivleme değişikliği Bash akışıyla aynı mantığı uygular; Windows doğrulaması henüz yapılmadı.
