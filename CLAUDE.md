# yashi-nomi.com（合同会社ヤシノミ 公式サイト）

このリポジトリの作業ルール。新しいセッションは**まずこれと `HANDOFF.md` を読む**こと。

## ⚡ トークン効率ルール（重要・必ず守る）

このリポジトリは1ファイルが巨大（index.html は約132KB）。読み方を誤ると
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
- **静的HTML**。ビルド工程なし。`index.html`（1枚・約85KB）＋ `blog/*.html`。
- ホスティング: **Netlify（GitHub連携で自動デプロイ）**。`origin = github.com/Keitoshinomiya/yashi-nomi-website`。
- `netlify.toml` は `functions = "netlify/functions"` のみ。**publishはリポジトリ直下** → `main` にpushしたものは即公開。

## ⚠️ デプロイ上の注意
- **`main` への commit/push = 本番公開**。下書きは `main` に載せない。
- `preview/` は `.gitignore` 済み（仮価格の下書きを誤公開しないため）。
- 大きな変更は確認用に別ブランチ or ローカルプレビューで。

## デザイントークン（2026-06-12 レトロパレットに刷新。index.html の `<style>` と一致させること）
- フォント: 見出し `Noto Serif JP`／本文 `Noto Sans JP`+`Inter`
- `--primary-color:#2F7351`（ヴィンテージグリーン）/ `--primary-color-dark:#1C4734`
- `--accent-orange:#C2551B`（テラコッタ）/ `--accent-gold:#E8A23D`（マスタード）
- 文字 `#2B2218`（焦げ茶）/ ページ背景 `#FBF6EA`（クリーム）/ 罫線 `#E2D9C6`
- LINE緑 `#06C755` はLINE系CTA専用。シグネチャー＝レトロストライプ `.brand-stripe`
- ⚠️ **コラム・カルチャー記事の本文ページとカード画像は旧配色（紺#0a3d62×オレンジ#FF9900）のまま維持する**（オーナー判断：全部揃えない）。記事を新規作成する時も既存記事のトーンに合わせる。一覧ページ（column/index.html）の枠・フィルターはレトロ適用済み
- モバイルではトップの各カードグリッドを `.m-carousel`（CSSスクロールスナップ）で横スワイプ化している。新セクション追加時もカードが3枚以上並ぶ場合は同クラスを付与
- 詳細規定: `~/Desktop/yashinomi_sns/BRAND_COLORS.md`

## 流用できるコンポーネントclass（既存定義あり）
- カード: `.card` / `.card-icon-bg`
- 見出し: `.section-title-en`（英・小）/ `.section-title-jp`（和・大）/ `.section-subtitle`
- ボタン: `.btn` / `.btn-primary`（青グラデ）/ `.btn-accent-gold`（金）/ `.btn-outline-primary`
- アニメーション: AOS（`data-aos="fade-up"` 等）、Swiper（ヒーロー）

## セクション構成（index.html の id 順）
`#services`（事業内容）→ `#features` → `#diagnosis`（Amazon運用タイプ診断）→ `#case-study` → `#blog` → `#plans`（料金）→ `#kpi-goal` → `#faq` → `#company` → `#contact`

## 共通リンク・計測
- 無料相談予約CTA: `https://calendar.app.google/TZrQ5YLexng2gPRV8`
- GA4: `G-PBN7WNCX8N`（gtag、クリックイベント計測あり）

## 編集の流儀
- `index.html` を直接編集。新セクションは**既存の card / section パターンに合わせる**（上記class流用）。
- 価格・実績などの**事実は勝手に作らない**。仮値は「(仮)」明示。確定値はオーナー（四宮さん）に確認。
