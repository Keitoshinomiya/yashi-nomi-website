#!/usr/bin/env python3
"""記事末尾に「あわせて読みたい（関連3本）＋LINE新着通知」ブロックを差し込む／更新する。

- 記事カタログは column/index.html のカード（href / data-cats / data-date / 画像 / 見出し）から作る
- 対象: column/*.html・culture/*.html・blog/*.html（index.html は除く）
- <!-- RELATED:START --> 〜 <!-- RELATED:END --> の間を毎回作り直す（何度実行しても同じ結果）
- 初回はマーカーが無いので「一覧に戻る」リンクの直前（無ければ </article> の直前）に挿入する
- 週次ブログ生成（~/.claude/scripts/yashinomi_blog_weekly.sh）の最後にも呼ばれる

使い方: python3 tools/build_related.py [--dry-run]
"""
from __future__ import annotations
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry-run" in sys.argv
LABEL = {"dx": "現場DX・ものづくり", "mieruka": "集客・見える化", "auto": "仕組み化・自動化",
         "amazon": "Amazonコラム", "culture": "ヤシノミの考え方", "blog": "導入事例"}
# 埋め草に使う優先記事（GA4で読了率が高い順・2026-09 時点）
PRIORITY = ["ai-3dprint-jig-lot-seal", "customer-voice-ig-asset", "fba-inventory-valuation"]
LINE_URL = "https://line.me/R/ti/p/@756qpakc"
START, END = "<!-- RELATED:START -->", "<!-- RELATED:END -->"


def catalog():
    html = open(os.path.join(ROOT, "column", "index.html"), encoding="utf-8").read()
    items = []
    for href, cats, date, body in re.findall(
            r'<a href="([^"]+)" class="card[^"]*" data-cats="([^"]*)" data-date="([^"]*)">(.*?)</a>', html, re.S):
        t = re.search(r"<h3[^>]*>(.*?)</h3>", body, re.S)
        img = re.search(r'<img[^>]+src="([^"]+)"', body)
        if not t:
            continue
        path = "/" + os.path.normpath(os.path.join("column", href)).replace(os.sep, "/")
        items.append({
            "path": path, "slug": os.path.basename(path).replace(".html", ""),
            "cats": cats.split(), "date": date,
            "title": re.sub(r"<[^>]+>", "", t.group(1)).strip(),
            "img": "../" + os.path.normpath(os.path.join("column", img.group(1))).replace(os.sep, "/") if img else "",
        })
    return items


def pick(items, self_slug, cats):
    others = [i for i in items if i["slug"] != self_slug]
    same = sorted([i for i in others if cats and i["cats"][0] == cats[0]], key=lambda i: i["date"], reverse=True)
    chosen = same[:3]
    if len(chosen) < 3:
        rest = [i for i in others if i not in chosen]
        rest.sort(key=lambda i: (PRIORITY.index(i["slug"]) if i["slug"] in PRIORITY else 99, i["date"]), reverse=False)
        # PRIORITY順→それ以外は新着順
        pri = [i for i in rest if i["slug"] in PRIORITY]
        newest = sorted([i for i in rest if i["slug"] not in PRIORITY], key=lambda i: i["date"], reverse=True)
        chosen += (pri + newest)[:3 - len(chosen)]
    return chosen


def block(related):
    cards = []
    for r in related:
        cards.append(f'''      <a href="{r["path"]}" class="group block rounded-lg overflow-hidden bg-white hover:no-underline" style="border:1px solid var(--border-color);">
        <img src="{r["img"]}" alt="" loading="lazy" class="w-full object-cover transition-transform duration-500 group-hover:scale-105" style="height:120px;">
        <div class="p-3">
          <span class="text-xs font-bold" style="color:var(--accent-orange);">{LABEL.get(r["cats"][0], "コラム")}</span>
          <p class="text-gray-800 font-bold mt-1" style="font-size:0.92rem;line-height:1.55;">{r["title"]}</p>
        </div>
      </a>''')
    return f'''{START}
    <section class="mt-12 pt-8" style="border-top:1px solid var(--border-color);">
      <p class="font-serif-jp text-lg font-bold mb-4" style="color:var(--primary-color);">あわせて読みたい</p>
      <div class="grid sm:grid-cols-3 gap-4">
{chr(10).join(cards)}
      </div>
      <div class="mt-8 rounded-lg px-6 py-7 text-center" style="background:#f1f7fd;border:1px solid var(--border-color);">
        <p class="font-bold text-gray-800 mb-1" style="font-size:1.02rem;">新しい記事は、LINEでお知らせしています</p>
        <p class="text-gray-600 mb-4" style="font-size:0.9rem;line-height:1.7;">実際に動いている仕組みの話を、月に数本。登録しても相談の義務はありません。</p>
        <a href="{LINE_URL}" target="_blank" rel="noopener" data-placement="article_subscribe" class="inline-block px-7 py-3 rounded-lg font-bold text-white shadow-md transition hover:-translate-y-0.5" style="background:#06C755;font-size:0.95rem;">LINEで新着記事を受け取る</a>
      </div>
    </section>
    {END}'''


def inject(html, new_block):
    if START in html and END in html:
        return re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: new_block, html, count=1, flags=re.S)
    # 「一覧に戻る／トップに戻る」リンクの直前に置く。無ければ </article> の直前
    m = re.search(r'\n[ \t]*<div class="mt-\d+ text-center">\s*<a href="(?:\./|\.\./)index\.html', html)
    if m:
        return html[:m.start()] + "\n\n    " + new_block + html[m.start():]
    i = html.rfind("</article>")
    if i < 0:
        return None
    return html[:i] + new_block + "\n    " + html[i:]


def main():
    items = catalog()
    by_slug = {i["slug"]: i for i in items}
    files = sorted(glob.glob(os.path.join(ROOT, "column", "*.html")) + glob.glob(os.path.join(ROOT, "culture", "*.html"))
                   + glob.glob(os.path.join(ROOT, "blog", "*.html")))
    done = skipped = 0
    for f in files:
        if os.path.basename(f) == "index.html":
            continue
        slug = os.path.basename(f).replace(".html", "")
        section = os.path.basename(os.path.dirname(f))
        cats = by_slug[slug]["cats"] if slug in by_slug else (["culture"] if section == "culture" else ["mieruka"])
        related = pick(items, slug, cats)
        html = open(f, encoding="utf-8").read()
        new = inject(html, block(related))
        if new is None:
            print("SKIP (no </article>):", f); skipped += 1; continue
        if new != html and not DRY:
            open(f, "w", encoding="utf-8").write(new)
        done += 1
        print(f"{section}/{slug}: " + ", ".join(r["slug"] for r in related))
    print(f"related blocks: {done} updated, {skipped} skipped" + (" (dry-run)" if DRY else ""))


if __name__ == "__main__":
    main()
