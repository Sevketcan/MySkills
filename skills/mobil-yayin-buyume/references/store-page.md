# Store page (ASO)

## Steps

1. **Keywords:** target keywords that match intent and are reachable instead of saturated, high-difficulty ones: look for pockets with real demand where the leaders don't rank at the top (K26).
2. **Custom Product Pages:** consider one per traffic channel, so a user who arrives from an ad sees the ad's promise on the page (K26).
3. **Screenshots:** one value proposition per screen, little text, simplified from a real screen (K12). Duo screenshots: [foldable-screens.md](foldable-screens.md). The App Store preview video is produced with `video-icerik-uretimi`.
4. **Metadata in the repo:** keep the text and images in the repo and send them through the CLI or the store API: `asc` (iOS), `gpc` or the Play Developer API (Android). Preview changes with `--dry-run` first; the `.p8` key and the service-account JSON stay out of the repo (K29).
5. **Name and subtitle:** no other company's brand or product name (5.2.1) (K8). Consider planning name and subtitle changes instead of changing them often (K36).
   - Naming the app after the searched keyword is a reported tactic for utility apps. In crowded niches a generic keyword name sits close to look-alike and 4.3 territory, so check it against K8 before choosing it.
6. **Plan distribution separately:** assume ASO alone won't be enough (K24); see [web-funnel-acquisition.md](web-funnel-acquisition.md). The sources disagree on how much ASO matters; the conflict is listed in [kurallar.md](kurallar.md).

The sources don't cover the App Store keyword field's technical details; use Apple's current documentation for those.
