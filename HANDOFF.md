# HANDOFF: 業務改善（店舗DX）サービスラインの追加

最終更新: 2026-06-01 ／ 前セッションからの引き継ぎ。新セッションはこれを読めば文脈ゼロから復帰できる。

## 背景（なぜやるか）
EARNEST（友人の美容サロン／大阪心斎橋）の立て直しで、再現可能な"運用代行の型"が出来た：
**現状の見える化（予約・売上を経路別集計）／集客HP制作／公式LINE構築／日次レポート自動化／GA4**。
これを yashi-nomi の **新サービスライン**として商品化し、新規顧客獲得につなげる。
Amazon運用代行と本質が同じ（＝デジタル運用の代行）なので、自然な拡張。

## 決まったこと（このセッションでの合意）
1. **見せ方**: Amazonと**並ぶサービスライン**として `index.html` 内に独立セクション追加。別ブランドにはしない。
2. **ターゲット**: **小規模店舗全般に汎用**。業種固有ではなく"店舗共通のお困りごと"でパッケージを切る。案件が溜まったら美容など得意業種に型を寄せる方針。
3. **サービス6メニュー**（各「お困りごと → やること → 成果」の3点セット）:
   - ① 現状の見える化（経路別の予約/売上を自動集計・前日比モニタリング）
   - ② 集客HP制作（スマホ最適×予約直結／媒体外SEO／アクセス解析）
   - ③ 公式LINE構築（再来・リピート自動化／流入経路判定連動）
   - ④ 日次/週次レポート自動化（毎朝スプシ＆チャット配信／異常検知）
   - ⑤ 広告・SEO・SNS運用（任意）
   - ⑥ 単発スポット（スプシ整備／単発分析／業務棚卸し）
4. **料金フレーム（仮・要確定）**: 初期構築（一括）＝見える化¥150,000〜／HP¥200,000〜／LINE¥80,000〜、＋ 月額運用・レポート ¥30,000〜。既存Amazonプラン（¥80,000〜¥130,000/月）と整合させた例示。
5. **旗艦事例**: EARNEST を Before/After で。**現状は匿名**（「大阪・心斎橋／美容サロン」）。実名・写真・具体数字の掲載は**友人の許可後**。
6. **ライン名称**: 仮「**店舗DX・運用代行**」。要・最終決定。

## 成果物の在りか
- **プレビュー（実物）**: `preview/gyomu-kaizen.html`
  - yashi-nomi の CSS/トークンを完全流用済み。**そのまま `#services`〜`#plans` の間に差し込めるHTML**。
  - `.gitignore` 済み（仮価格のため本番に出さない）。ブラウザで `open preview/gyomu-kaizen.html`。

## 残タスク（次セッションの作業）
- [ ] 料金の**確定値**を入れる（仮→実値）
- [ ] EARNEST **実名掲載の許可**を確認 → OKなら名前・写真・数字を反映
- [ ] **ライン名称**の最終決定
- [ ] `index.html` の `#services`〜`#plans` 間に**正式セクションとして組み込み**（preview の中身を移植）
- [ ] ヘッダーのMENU（モバイルメニュー含む）に導線追加
- [ ] 必要なら専用LP / 紹介ブログ記事 / 営業用PDF（同素材から）

## 参考：EARNEST側の技術資産（流用元）
- サイト本体: `~/Desktop/Claude プロジェクト一覧/EARNEST/web-v2`（Astro）
- レポート自動化: `~/earnest_daily_report/`（calendar_fetch/snapshot 等）
- 集計スプシ: `1N-hGEEjEFnxd-jH06mEWfbw-o8eVXkvskCBw9CwqZmw`

## 進め方の鉄則（横断PJ共通）
記憶はチャットではなく**repoに置く**。決定は HANDOFF.md、規約は CLAUDE.md に追記し、次のセッションは「読むだけ」で温まった状態から始める。

---

## 2026-06-12 深夜：トップページ大幅リニューアル（★未公開・プレビュー確認待ち）

**状態：working treeに未コミットで保持。`git push`するまで本番には出ない。**
バックアップ：`preview/index-backup-2026-06-11.html`（gitignore済・リニューアル前の完全コピー）

### 変更内容（index.html）
1. **ヒーロー刷新**：Swiperスライダー（4枚回転）を廃止 → 静的1メッセージ型。
   左＝ボトルネックコピー＋CTA2本（無料相談=金／30秒セルフ診断=ゴースト）＋信頼チップ3つ。
   右＝「毎朝7:00に届くSlack朝刊」の実物風モック（#hero、CSSのみ・画像不使用）
2. **セルフ診断（#selfcheck）を事例直後へ移動**（旧：最下部→新：case-studyとblogの間）
3. **モバイル固定CTAバー新設**（LINE緑＋無料相談紺、lg未満のみ。既存フローティングLINEボタンはlg以上のみに変更）
4. **#contact／footerをブランドネイビー化**＋footerに住所・コラム一覧・LINEリンク追加
5. **OGP画像新設**：`images/ogp.jpg`（1200×630、ヘッドレスChromeで生成）→ og:image/twitter:image差し替え
6. Swiper CSS/JS削除（高速化）、実績バンドの数字を明朝化、ナビ「ブログ」→「コラム」
7. GAクリック計測のhero判定セレクタを `.hero-static` に更新済み

### 検証済み
デスクトップ1366px・モバイル390pxのフルページ確認／コンソールエラーなし／
ブログフィルター動作（既定6件）／モバイルメニュー開閉／固定バー表示／フッター表示

### 公開手順（オーナーOK後）
`git add index.html images/ogp.jpg && git commit && git push`
※ 同じく未公開：`column/amazon-ads-self-improvement-loop.html`（広告自己改善ループ記事・プレビュー確認待ち。
カード画像は /tmp/card-adsloop.jpg → 公開時に images/card-adsloop.jpg へ配置＋トップ/一覧にカード追加が必要）


## 2026-06-12 全面公開済み（b59f08f）
上記リニューアル一式（トップ・/check/診断・OGP・チェックリストPDF・LINE中心CTA）は本番公開済み。
バックアップ preview/index-backup-2026-06-11.html は旧版として保持。

## 2026-09-11 GA4分析にもとづく6改善（公開済み）
GA4（プロパティ357932107・hostName=yashi-nomi.com で絞る）の直近30日: 日本146セッション／111人、Direct(US)59はボット。
読まれているのは 3Dプリンタ治具／お客様の声IG素材／FBA棚卸し。記事に検索着地した人は直帰ゼロ、トップ着地は直帰58%。
- **記事の出口**: 全42記事の末尾に「あわせて読みたい（同カテゴリ3本）＋LINE新着通知」ブロック。生成は `tools/build_related.py`（`<!-- RELATED:START/END -->` を毎回作り直す。週次ブログ生成スクリプトの最後でも自動実行）
- **トップ**: 自社ブランドカードを文字帯→実物写真（works/ の画像流用）。コラムは読了率上位3本を `data-pin` で先頭固定＋新着3本。コラム下にLINE購読ブロック
- **フォーム**: Netlify honeypot（`bot-field`）追加。9月は送信10件中7件が海外スパムだった
- **計測**: トップのLINE系CTAは記事と同じ `line_click`＋`placement`（top_hero / top_contact / top_sticky / top_float / top_blog_subscribe）、診断は `cta_click`。汎用 click_tracking にも placement 追加。記事側は `data-placement` 属性を優先。ブログテンプレ（~/Desktop/50_yashinomi_sns/blog_template.html）に記事計測スクリプトを追加（それまで新記事は未計測だった）
- **LINE配信**: 週次ブログ公開成功時に Messaging API broadcast で友だちに新記事URL（utm_source=line）を送る（yashinomi_blog_weekly.sh 4.5）
- レポート再実行: `python3 ~/.claude/scripts/yashinomi_ga4_report.py --days 30`
- **オーナー作業（未）**: ①Search Console の yashi-nomi.com に `amazon-tracker@eastern-concord-412616.iam.gserviceaccount.com` をユーザー追加（検索語が取れるようになる） ②IGプロフィールのURLを `流入経路のURL.md` のUTM付きに差し替え（現状は素のトップURL） ③GA4のキーイベントに `line_click` を登録

## 2026-09-12 手書き記事「最初の100個は、自宅の机で組んだ」公開
- `column/suicom-min-lot-home-assembly.html`（Amazonコラム／本人の口述をもとに執筆・本人確認済み）。写真6枚はPhotosライブラリ（2023年2〜3月）からAppleScript `search for "満寿美町"` で原本を取得（`~/Desktop/01_claude-outputs/5_自社サイト・他事業/suicom_firstlot_photos/` に書き出し原本を保存。家族写真も混ざるので公開物には使わない）
- 手書き記事の手順: テンプレ差し込み → `images/card-<slug>.jpg`（実写切り出し）→ column/index.html と index.html にカード → sitemap.xml → `python3 tools/build_related.py`
