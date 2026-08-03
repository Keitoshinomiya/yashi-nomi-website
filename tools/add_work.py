#!/usr/bin/env python3
"""つくったもの（トップの Works 節）に写真を1枚追加する。

使い方:
    python3 tools/add_work.py <画像パス> "キャプション" [--step つくる] [--date 2026-08-01]

やること:
    1. 画像を長辺1200pxに縮小して images/works/ に保存（iPhone写真をそのまま置かないため）
    2. works.json に1行追加

キャプションのルール（重要）:
    「何を・いつ」だけ書く。「〜できます」「〜対応可能」は書かない。
    書いた瞬間に作品集がサービスの見本に変わる。
        OK : 「試作したパーツ。3回失敗した」
        NG : 「3Dプリンタでの試作も対応できます」
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import unicodedata

from PIL import Image, ImageOps

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEST_DIR = ROOT / "images" / "works"
MANIFEST = ROOT / "works.json"
MAX_EDGE = 1200
STEPS = ("つくる", "見せる", "売る", "直す")


def slugify(text: str, fallback: str) -> str:
    """キャプションからASCIIのファイル名を作る。

    日本語はASCIIに落とすとほぼ何も残らないので、4文字未満になったら
    fallback（work-YYYYMMDD 形式）を使う。"""
    ascii_only = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_only).strip("-").lower()[:40]
    return slug if len(slug) >= 4 else fallback


def load_manifest() -> list:
    if not MANIFEST.exists():
        return []
    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        sys.exit(f"works.json が壊れています: {e}")
    return data if isinstance(data, list) else []


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("image", help="追加したい画像のパス")
    p.add_argument("caption", help="キャプション（何を・いつ。売り文句は書かない）")
    p.add_argument("--step", default="つくる", choices=STEPS, help="工程タグ（既定: つくる）")
    p.add_argument("--date", default="", help="YYYY-MM-DD。省略時は並び順の先頭に来ない")
    args = p.parse_args()

    src = pathlib.Path(args.image).expanduser()
    if not src.exists():
        sys.exit(f"画像が見つかりません: {src}")

    items = load_manifest()
    DEST_DIR.mkdir(parents=True, exist_ok=True)

    stem = slugify(args.caption, f"work-{(args.date or 'undated').replace('-', '')}")
    name = f"{stem}.jpg"
    n = 2
    while (DEST_DIR / name).exists():
        name = f"{stem}-{n}.jpg"
        n += 1

    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im)          # iPhoneの向き情報を反映
        im = im.convert("RGB")
        im.thumbnail((MAX_EDGE, MAX_EDGE))
        im.save(DEST_DIR / name, "JPEG", quality=82, optimize=True)
        size = im.size

    entry = {"img": f"images/works/{name}", "cap": args.caption, "step": args.step}
    if args.date:
        entry["date"] = args.date
    items.append(entry)
    MANIFEST.write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    kb = (DEST_DIR / name).stat().st_size // 1024
    print(f"追加しました: images/works/{name}  {size[0]}x{size[1]}  {kb}KB")
    print(f"  {args.step} / {args.caption}")
    print(f"現在 {len(items)} 件。公開するには commit して push してください。")


if __name__ == "__main__":
    main()
