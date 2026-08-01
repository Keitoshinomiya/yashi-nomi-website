# yashi-nomi.com（合同会社ヤシノミ 公式サイト）

このリポジトリの作業ルール。新しいセッションは**まずこれと `HANDOFF.md` を読む**こと。

## ⚡ トークン効率ルール（重要・必ず守る）

このリポジトリは1ファイルが巨大（index.html は約150KB）。読み方を誤ると
トークンを大量消費するため、以下を厳守すること。

- **HTMLファイルを全文 Read しない。** 必ず Grep で該当箇所を特定し、
  `offset`/`limit` で必要な数十行だけ読む。
- 編集は **Edit で該当ブロックのピンポイント修正**に限定する。
  ファイル全体の Write・全文書き換えは原則禁止。
- `preview/` 配下の旧版HTML（index-renewal / index-tenpo-unei / amazon 等）は
  指示がない限り読まない・触らない。
- 「どこを直すか」が曖昧なときは、まず Grep で候補を出し、
  対象箇所を私に確認してから読む。
- 複数ファイルを横断する作業は、一度に全部開かず1ファイルずつ処理する。

## このサイトの正体
- 合同会社ヤシノミ（大阪府池田市）の公式コーポレートサイト。本業は **Amazon運用支援・ECコンサル**。
- **静的HTML**。ビルド工程なし。`index.html`（1枚・約150KB）＋ `blog/*.html`。
- ホスティング: **Netlify（GitHub連携で自動デプロイ）**。`origin = github.com/Keitoshinomiya/yashi-nomi-website`。
- `netlify.toml` は `functions = "netlify/functions"` のみ。**publishはリポジトリ直下** → `main` にpushしたものは即公開。

## ⚠️ デプロイ上の注意
- **`main` への commit/push = 本番公開**。下書きは `main` に載せない。
- `preview/` は `.gitignore` 済み（仮価格の下書きを誤公開しないため）。
- 大きな変更は確認用に別ブランチ or ローカルプレビューで。

## デザイントークン（2026-08-01「白と緑だけ」に刷新＝オーナー指示。旧レトロ配色には戻さないこと）
定義元は **`assets/site.css` の `:root`** と **index.html の `<style>`**。両方を必ず一致させる。
- フォント: 見出し `Noto Serif JP`／本文 `Noto Sans JP`+`Inter`
- `--primary-color:#23AC38`（ヤシノミ・ロゴグリーン）/ `--primary-color-dark:#166A24`（グラデ明端 `#4FC25F`／最暗 `#0F5119`）
- `--accent-orange:#166A24`（深緑）・`--accent-gold:#BFEFC7`（淡緑）※**変数名は既存互換で据え置き。中身は緑**。橙・金は入れない
- 文字 `#1A1A1A`／`--text-medium:#4B4B4B`／`--text-light:#7C7C7C`（茶系グレーは使わない）
- ページ背景 **`#FFFFFF`** / `--bg-light:#F3F9F3` / 罫線 `--border-color:#E6E6E6`
- 濃色ブロック（ヒーロー・フッター・カード見出し帯）＝ `#123D1B`。濃緑の上では `--accent-orange`（深緑）が沈むので `--accent-gold`（淡緑）に逃がす（`.hero-static .amazon-orange-text` / `footer .amazon-orange-text` に指定済み）
- LINE緑 `#06C755` はLINE系CTA専用。シグネチャーストライプ `.brand-stripe` は緑3階調×白
- ⚠️ **記事本文ページ（column/*.html・culture/*.html・blog/*.html）とブログカード画像は旧配色（紺#0a3d62×オレンジ#FF9900）のまま**（オーナー判断：全部揃えない）。一覧ページ `column/index.html` の枠・フィルターは白×緑適用済み
- ⚠️ `check/index.html`（30秒診断）のバーは「良い→注意→警告」の意味を持つ3色スケールなので緑一色にしない
- モバイルではトップの各カードグリッドを `.m-carousel` で横スワイプ化。新セクション追加時もカードが3枚以上並ぶ場合は同クラスを付与
- ⚠️ **`.m-carousel` の `touch-action` を `pan-x` 単独に戻さないこと**（縦スクロールが死ぬ）。斜め流れと縦スクロール不可は両立しないため、JSの方向ロック `lockCarouselAxis()`（index.html末尾）で解決している
- 詳細規定: `~/Desktop/50_yashinomi_sns/BRAND_COLORS.md`

## 流用できるコンポーネントclass（既存定義あり）
- カード: `.card` / `.card-icon-bg`
- 見出し: `.section-title-en`（英・小）/ `.section-title-jp`（和・大）/ `.section-subtitle`
- ボタン: `.btn` / `.btn-primary`（青グラデ）/ `.btn-accent-gold`（金）/ `.btn-outline-primary`
- アニメーション: AOS（`data-aos="fade-up"` 等）。※Swiperは2026-06-12に廃止済み（ヒーローは静的）

## セクション構成（index.html の id 順）
`#services`（事業内容）→ `#features` → `#diagnosis`（Amazon運用タイプ診断）→ `#case-study` → `#blog` → `#plans`（料金）→ `#kpi-goal` → `#faq` → `#company` → `#contact`

## 共通リンク・計測
- 無料相談予約CTA: `https://calendar.app.google/TZrQ5YLexng2gPRV8`
- GA4: `G-PBN7WNCX8N`（gtag、クリックイベント計測あり）

## 編集の流儀
- `index.html` を直接編集。新セクションは**既存の card / section パターンに合わせる**（上記class流用）。
- 価格・実績などの**事実は勝手に作らない**。仮値は「(仮)」明示。確定値はオーナー（四宮さん）に確認。
