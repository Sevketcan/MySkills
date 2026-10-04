# Koleksiyonu geliştirme düzeni

## Tek kaynak

Kişisel Unity paketleri özelleştirmeleri koruyan ana kaynak. Plugin'in 25 aynı adlı skill'i kullanıcı konfigürasyonunda kapatılır; 6 farklı skill ve plugin'in kendi durumu korunur. MCP ayarları değiştirilmez. Plugin önbelleğine yazılmaz.

Önce önizleme, sonra uygulama:

    python3 scripts/configure-skill-sources.py
    python3 scripts/configure-skill-sources.py --apply

Python 3.11+ ve Codex CLI gerekir. Script kurulu sürümü CLI envanterinden bulur. Unity plugin'i güncellenince yeni dosya yolları için yeniden çalıştırın. İlgisiz ayarlar korunur; mevcut elle yazılmış çakışan override varsa script değişiklik yapmadan durur. Konfigürasyon yedekleri Codex skill-backups dizinindedir. Yeni kataloğu yüklemek için Codex'i yeniden başlatın.

Dosya yolu üzerinden devre dışı bırakma [resmi olarak desteklenir](https://learn.chatgpt.com/docs/build-skills#enable-or-disable-local-codex-skills). Bu, explicit-only kullanım politikası değildir: plugin'in tekrarlanan kopyası kapatılır, kişisel ana kopya otomatik seçilebilir kalır.

## Proje tercihleri

fullstack-dev artık bütün Next.js/NestJS işlerinde kişisel tercihleri dayatmaz. Seçilen projeye AGENTS.md ve onu içeri alan CLAUDE.md kurulabilir:

    python3 scripts/apply-project-profile.py /mutlak/proje/yolu
    python3 scripts/apply-project-profile.py /mutlak/proje/yolu --apply

Şablon skills/fullstack-dev/assets/project-profile içinde; kurucu ilgili skill'in scripts dizininde de taşınabilir. Farklı mevcut talimat varsa ezilmez. O proje için kullanıcı tercihleriyle birleştirilir. Bu işlem başka projeleri ve global agent ayarlarını değiştirmez. Proje servis adları, portları ve ortam dosyası politikası mevcut projeden alınır.

## Yeni skill eşiği

skill-reviews.json yeni bir keşfedilebilir giriş için şu bilgileri ister:

- reason: tool-contract, project-preference veya observed-failure
- evidence: gerçek araç sözleşmesi, kullanıcı tercihi veya gözlenen hata
- positive_trigger: hangi somut istekte seçilmeli
- negative_trigger: yakın ama seçilmemesi gereken istek
- validation: yararı nasıl doğrulanacak

Önceden incelenen 43 isim ayrı kayıtlıdır; bu kayıt ampirik başarı iddiası değildir. Yeni girişte gerekçe eksikse koleksiyon doğrulaması ve gerçek repo senkronizasyonunun öneri doğrulaması değişikliği reddeder.

Bir örnek:

    {
      "reason": "tool-contract",
      "evidence": "Connector, JSON sözlüğünü result değişkeninden alıyor.",
      "positive_trigger": "Bu connector üzerinden sahne bilgisini oku.",
      "negative_trigger": "Genel Python dictionary kullanımını açıkla.",
      "validation": "Connector fixture'ında doğru değişkenden JSON alındığını kontrol et."
    }

Temel programlama bilgisi, genel tasarım öğütleri ve tek bir yanlış çıktı tek başına yeni giriş gerektirmez. Önce mevcut skill'i daraltma, referans veya script seçeneklerini değerlendirin.

## Tekrarlanabilir karşılaştırma

    python3 scripts/benchmark-skills.py --dry-run
    python3 scripts/benchmark-skills.py --provider both --repeats 3 --output evals/results/next-review

CLI hesapları/kimlik doğrulaması hazır olmalı. Gerçek model çağrıları kullanım kotası veya API maliyeti tüketir. Kullanıcının ayarlı model tercihi korunur; provider hatası görev başarısızlığı sayılmaz. Zaman aşımı sınırlıdır; her işlem izole geçici klasörde çalışır. Anahtarlar repo'ya kopyalanmaz; hata metinlerinde ortamdan gelen sırlar ayıklanır.

Üç görev: küçük Python düzeltmesi, mevcut Flask/SQLite kapsamını koruma ve Blender connector sözleşmesi. Her provider kendi skill açık/kapalı çiftiyle karşılaştırılır. İlk pilot tek tekrar; sonraki tekrarların sırası dönüşümlüdür. Güncel runner prompt/skill hash'i, süre, raporlanan kullanım, provider sonucu ve rubrik kontrolünü kaydeder.

Bu runner skill gövdesini açıkça eklemenin etkisini ölçer. Otomatik skill seçimi, gerçek repo düzenleme, gerçek Editor işlemleri, büyük görevler ve bütün referans ağacı ölçülmez. JSON alanları üzerinden mekanik plan kontrolleri tam semantik doğrulama değildir. İlk pilot Codex tool çağrısı sayısını kaydetmedi; güncel runner beklenmeyen çağrıları event akışından sayar. Claude'da araçlar CLI üzerinden kapalıdır.

## Deterministik export

skills/blender-mcp/scripts/export_selected_glb.py, istenen objeleri GLB'ye export eder, çıktı dosyasını kontrol eder ve seçim/aktif objeyi geri yükler. Kaynak .blend kaydedilmez; objelerin transform'ları değiştirilmez. Mevcut hedef için overwrite argümanı gerekir.

Örnek:

    blender --background SOURCE.blend --python skills/blender-mcp/scripts/export_selected_glb.py -- --output DESTINATION.glb --objects AssetName

Bu çalışmada mock bpy üzerinden hata ve başarı durumları doğrulandı. Gerçek Blender export uyumluluğu henüz çalıştırılmadı. SpriteAtlas için mevcut 38 C# kaynak zaten deterministik örnekler sağlıyor; aynı işi yapan yeni bir kurucu eklenmedi.
