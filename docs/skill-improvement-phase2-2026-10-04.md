# İkinci iyileştirme turu — 4 Ekim 2026

## Uygulanan düzen

- Kişisel kurulumlar 43 skill olarak kaldı. Unity plugin'inin 25 aynı adlı girişine config.toml içinde disabled override yazıldı. Plugin'in kendisi, 6 farklı girişi ve mevcut MCP ayarları korundu; önbellek değiştirilmedi. Claude CLI'da kurulu plugin bulunmadığından onun kişisel kopyaları zaten tek kaynaktı.
- configure-skill-sources.py önizleme, yedek, kurulu sürüm keşfi ve tekrar çalıştırma desteği sağlıyor. Aynı ayara ikinci uygulama değişiklik yapmıyor.
- fullstack-dev yalnızca profil kurulumu veya açıkça bu profili kullanan projelerde devreye girecek şekilde daraltıldı. Tercihler opt-in AGENTS.md/CLAUDE.md şablonunda; farklı mevcut talimatlar ezilmiyor.
- Repo'ya kısa bakım AGENTS.md/CLAUDE.md eklendi. Yeni girişler için gerekçe, kanıt, olumlu/olumsuz tetikleyici ve doğrulama planı koleksiyon doğrulamasında zorunlu.
- Blender GLB export yardımcısı hedef objeleri sınırlıyor, çıktı dosyasını kontrol ediyor ve seçimi geri yüklüyor. Hata/başarı akışı mock bpy ile test edildi; gerçek Blender export yapılmadı. SpriteAtlas'ın mevcut C# kaynaklarına ikinci bir aynı kurucu eklenmedi.
- Her iki kişisel kuruluma güncelleme uygulandı; son senkronizasyon 0 farkla tamamlandı.

## Ölçümün kapsamı

İlk pilot: 3 görev × 2 koşul × 2 provider = 12 gerçek model çağrısı. Ardından Claude connector görevi için 2 ek çağrı yapıldı. Codex gpt-6.1-sol, Claude claude-opus-4-6[1m] kullandı; bunlar kullanıcının mevcut CLI model tercihlerinden alındı.

Görevler küçük Python düzeltmesi, mevcut Flask/SQLite kapsamını koruma ve Blender connector sözleşmesi. Skill koşulunda giriş metni açıkça verildi; diğerinde verilmedi. Gerçek repo düzenleme, otomatik skill keşfi ve canlı Editor işlemleri ölçülmedi. Araç/test planı hakkındaki cevaplar gerçek işlem başarısı değildir.

| Deneme | Provider | Koşul | Rubrik geçen görev |
| --- | --- | --- | --- |
| phase2-pilot | claude | without-skill | 2/3 |
| phase2-pilot | claude | with-skill | 2/3 |
| phase2-pilot | codex | without-skill | 3/3 |
| phase2-pilot | codex | with-skill | 3/3 |
| phase2-connector-followup | claude | without-skill | 1/1 |
| phase2-connector-followup | claude | with-skill | 1/1 |

İlk genel görevlerde iki model de skill olmadan doğru çıktı üretti; bu örneklerde ek başarı avantajı görünmedi. Codex connector denemesinde de iki durumda doğru sözleşmeyi kullandı.

İlk Claude connector çıktısı skillsiz koşulda sonucu scene_objects değişkeninden döndürmeyi önerdi; kullanılan connector result sözlüğünü bekliyor. Skill bu noktayı düzeltti. Bununla birlikte skill koşulunda bpy.data.objects kullanarak diğer sahnelerin objelerini de kapsadı. Rehbere aktif sahne için bpy.context.scene.objects ayrımı eklendi. Sonraki çiftte iki çıktı da bu iki sözleşmeyi doğru kullandı. Bu küçük örnek özel araç bilgilerinin yararlı olabileceğini gösterir; genel kalite üstünlüğünü veya her modelde gerekliliğini kanıtlamaz.

İlk otomatik rubrik bpy'yi yeni bağımlılık saydı. Elle incelemede bu sınıflandırma düzeltildi ve aktif sahne kontrolü eklendi. Save operatörü tercihi ile gerçek dosya kalıcılığı birbirinden ayrıldı: explicit save_as_mainfile alternatifi de geçerli sayıldı. Bütün koşullar aynı v3 rubriğiyle yeniden değerlendirildi; orijinal notlar her kayıt içinde korundu. Sonraki görev metni bu belirsizliği açıkça kaldırıyor. Bu nedenle pilot keşif çalışmasıdır, önceden sabitlenmiş bağımsız benchmark sonucu değildir.

Süre/kullanım kayıtları ham JSON'larda duruyor. Tek tekrar, sıra, önbellek ve provider farkları nedeniyle hız veya maliyet üstünlüğü çıkarmadık. İlk pilot Codex tool-call olaylarını saklamadı; sayısı ölçülmemiş olarak işaretlendi. Güncel runner gelecekte prompt/skill hash'i, provider kullanımını ve beklenmeyen tool çağrılarını kaydeder.

## Doğrulama ve çalışma sınırları

23 otomatik test başarılı: kaynak seçiminin ayar/araç koruması ve tekrar çalıştırılması, eksik karşılıkta atomik ret, profil dosyalarını koruma, yeni skill eşiği, benchmark davranış ve rubrik kontrolleri, export başarısı/hatasında seçim geri yükleme ve önceki senkronizasyon/kurulum testleri.

43 giriş koleksiyon doğrulamasını geçti; yerel Markdown bağlantılarında kırık bağlantı bulunmadı. Native app-server, dosya bazlı disable ayarının kişisel bir giriş için enabled=false olarak uygulandığını doğruladı. Standalone CLI app-server bu sorguda uzak Unity plugin girişlerini listelemedi; masaüstü remote kataloğunun 25 giriş filtresi uygulaması yeniden başlatmadan sonra görülmeli. Bu nedenle bütün masaüstü kataloğunun canlı sayımı yapılmış gibi raporlamıyoruz. Desteklenen ayar formatı [resmi rehberde](https://learn.chatgpt.com/docs/build-skills#enable-or-disable-local-codex-skills) belgeleniyor.

Bağımlılık connector'ü kurulu uzak Unity sürümünü genel public plugin listesinde çözemedi. Yerel manifest sadece skills alanı içeriyor; mevcut MCP ayarları ayrı. Plugin'i kaldırmadığımız için çözülemeyen bağımlılık metadata'sına dayanarak herhangi bir araç bağlantısı silinmedi.

Windows kurulumu veya gerçek Blender/Unity çalıştırması bu turda doğrulanmadı. Kaynak seçimi Python 3.11+ gerektirir; plugin güncellemelerinden sonra sürüm yollarını yenilemek için tekrar çalıştırılmalı.

Config değişikliği öncesi ek yedek: 
/Users/soern/Library/Application Support/MySkills/backups/phase2-20261004T175257Z

GitHub'a gönderim yapılmadı; çalışma dalı codex/skill-simplification. Yeni katalog için Codex ve Claude yeniden başlatılmalı.

[Uygulama komutları ve bakım düzeni](skill-maintenance.md), [ilk pilot ham verileri](../evals/results/phase2-pilot/summary.json), [connector takip denemesi](../evals/results/phase2-connector-followup/summary.json).
