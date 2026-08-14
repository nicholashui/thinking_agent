#!/usr/bin/env python3
import os
import re
import sys
import time
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    print("Installing python-dotenv...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-dotenv"])
    from dotenv import load_dotenv

try:
    import requests
except ImportError:
    print("Installing requests...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR / "docs"
INPUT_PATH = DOCS_DIR / "training_agent_book.md"
OUTPUT_PATH = DOCS_DIR / "training_agent_book_hk.md"
ENV_PATH = BASE_DIR / ".env"

SYSTEM_PROMPT = """你係一個專業嘅技術文件翻譯員，將英文翻譯成**香港繁體中文（書面語正式文體）**。最重要係：**所有 Markdown 結構、語法、檔案路徑、代碼必須原封不動，只翻譯純文字內容。**

## 黃金規則（絕對必須遵守）：

### 1. Markdown 結構一字不變
- 標題符號 `#` `##` `###` `####` 保留原樣，數量唔好變，位置唔好變
  - ✅ 正確：`## 第二章 — 演變：每個版本改動嘅原因`
  - ❌ 錯誤：`第二章** — 演變`（刪除咗 `##`）
- 分隔線 `---` 原封不動，唔好刪除、唔好改
- 圖片 `![Alt 文字](路徑)`：只翻譯 `Alt 文字`，括號入面嘅路徑**完全唔好改**
  - ✅ 正確：`![運作循環](svg/operating_loop.svg)`
  - ❌ 錯誤：`![Operating Loop](svg/operating_loop_tc.svg)`
- 列表 `- * 1. 2. 3.` 符號保留，只翻譯後面文字
- 清單縮排保留，空格數唔好變
- 粗體 `**文字**` 同斜體 `*文字*` 符號保留，只翻譯星號中間嘅內容
  - ✅ 正確：`**驗證：** 26 個場景`
- 超連結 `[文字](url)`：只翻譯方括號入面嘅文字，URL 完全唔好改

### 2. 代碼（絕對唔好翻譯）
- 代碼區塊：` ```語言 ` 開頭到 ` ``` ` 結尾，**入面所有內容原封不動，一個字都唔好改**
  - 包括偽代碼、文字公式、狀態圖、名稱列表等任何喺代碼區塊入面嘅內容
- 行內代碼 `` `代碼` ``：反引號中間所有內容**完全唔好改**
  - ✅ 正確：八個狀態其中之一為 `RESOURCE_LIMITED`
  - ❌ 錯誤：`資源不足`（翻譯咗代碼內容）
- 技術代碼名詞：出現喺普通句子入面但冇反引號包住，但明顯係程式/系統名稱嘅 (e.g. `LoopMonitor`, `BudgetController`, `Cynefin`, `WHAT`, `WHY`, `HOW`, `DO`, `REVIEW`, `META-CONTROL`, `VERIFY`, `Safety Kernel`, `EvaluationPlane`, `Gro`, `ReAct`, `Tree-of-Thoughts`) — 呢啲**保留原英文**，唔好翻譯

### 3. 表格（結構完全保留）
- `|` 管線符號一個都唔好少，數量唔好變
- `|---|---|` 分隔行原封不動，連破折號數量同冒號位置都唔好改
- 只翻譯表格格內嘅文字內容
- 表格行嘅順序完全唔好變，包括第 1 行 header、第 2 行 separator、其餘 data rows

### 4. 翻譯風格
- **香港繁體中文書面語**，唔好使用口語化廣東話字（例如「嘅」「咁」「佢」用喺 YouTube 腳本就可以，但呢份係技術書籍文件，要用正式中文「的」「如此」「它」「其」）
  - ✅ 正確：「的」「它」「因此」「然而」「此外」「換言之」
  - ❌ 錯誤：「嘅」「佢」「咁樣」「跟住」「講起」
- 語氣：正式、學術、技術文件風格，準確、清晰、一致
- 專有名詞保持一致：例如每個章節都出現嘅 `graceful state` → 統一譯做「優雅狀態」；`stage gate` → 統一「階段閘門」；`control flow` → 統一「控制流程」；`provenance` → 統一「出處/來源」；`allowlist` → 「允許清單」；`escalate` → 「升級」；`verify` → 「驗證」

### 5. 其他唔好改嘅內容
- 日期 `August 7, 2026`、數字 `36 scenarios`、百分比 `33.6 %` 保留數字，單位可翻譯
- 人名、學術文獻引用標記保留
- 章節編號 `§31`、`§15.4`、`§22.3` 保留原樣
- 狀態代號 `SOLVED`, `APPROXIMATED`, `NEEDS_EVIDENCE`, `NEEDS_EXPERIMENT`, `INFEASIBLE`, `UNSAFE`, `ESCALATED`, `RESOURCE_LIMITED` — 首次出現時格式：`已解決 (SOLVED)`，之後可直接 `SOLVED` 或視乎上下文，但代碼本身一定要保留原狀態字

## 回應要求
- 直接輸出完整翻譯後嘅 Markdown，**唔好加任何前言、解釋、註解、總結**
- 輸出嘅 Markdown 要同輸入嘅行數大致對應，段落順序唔好變
- 如果遇到唔確定嘅翻譯，優先保留英文加括號註解，例如：`演算法（Algorithm）`
"""


def load_env():
    if ENV_PATH.exists():
        load_dotenv(ENV_PATH)
    api_key = os.getenv("POE_API_KEY")
    base_url = os.getenv("POE_BASE_URL", "https://api.poe.com/v1")
    model = os.getenv("POE_BASE_MODEL", "grok-4.1-fast-non-reasoning")
    if not api_key:
        raise ValueError("POE_API_KEY not found in .env or environment")
    return api_key, base_url.rstrip("/"), model


def load_input_markdown():
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        return f.read()


def split_markdown_by_headings(md_text):
    lines = md_text.splitlines(keepends=True)
    heading_re = re.compile(r"^(#{1,6})\s+(.+)$")

    sections = []
    current_lines = []
    current_heading = None

    for line in lines:
        m = heading_re.match(line.rstrip("\n").rstrip("\r"))
        if m:
            if current_lines:
                if current_heading is not None or any(l.strip() for l in current_lines):
                    sections.append("".join(current_lines).rstrip())
            current_lines = [line]
            current_heading = m.group(2)
        else:
            current_lines.append(line)

    if current_lines:
        if current_heading is not None or any(l.strip() for l in current_lines):
            sections.append("".join(current_lines).rstrip())

    non_empty = []
    for s in sections:
        if s.strip():
            non_empty.append(s)
    return non_empty


def call_llm(api_key, base_url, model, system_prompt, user_content, max_retries=3, retry_delay=10):
    url = f"{base_url}/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
        "temperature": 0.3,
    }

    for attempt in range(1, max_retries + 1):
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=600)
            resp.raise_for_status()
            data = resp.json()
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"].strip()
            else:
                raise ValueError(f"Unexpected API response: {data}")
        except Exception as e:
            print(f"  Attempt {attempt}/{max_retries} failed: {e}")
            if attempt < max_retries:
                wait = retry_delay * attempt
                print(f"  Retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise


def main():
    print("Loading environment...")
    api_key, base_url, model = load_env()
    print(f"Model: {model}")

    print(f"\nLoading: {INPUT_PATH}")
    md_text = load_input_markdown()
    print(f"Input length: {len(md_text)} chars")

    print("\nSplitting by headings (# / ## / ###)...")
    sections = split_markdown_by_headings(md_text)
    print(f"Found {len(sections)} sections")
    for i, s in enumerate(sections):
        first_line = s.splitlines()[0][:100] if s.splitlines() else "(empty)"
        print(f"  [{i+1:3d}] {len(s):>5d} chars | {first_line}")

    print("\nTranslating sections to Traditional Chinese (HK, formal written)...")
    print("=" * 80)
    translated_sections = []
    for i, section in enumerate(sections):
        sidx = i + 1
        total = len(sections)
        section_header = section.splitlines()[0][:80] if section.splitlines() else ""
        print(f"\n>>> Section {sidx}/{total}: {len(section)} chars")
        print(f"    Head: {section_header}")
        try:
            user_msg = (
                f"呢份係書籍嘅第 {sidx}/{total} 節。請嚴格遵守 system prompt 所有規則，"
                f"保留全部 Markdown 結構、代碼、表格、圖片路徑，只翻譯文字內容做香港繁體中文（正式書面語）。\n\n"
                f"--- 以下係要翻譯嘅 Markdown 內容 ---\n\n"
                f"{section}"
            )
            translated = call_llm(api_key, base_url, model, SYSTEM_PROMPT, user_msg)
            translated_sections.append(translated)
            preview = translated.replace("\n", " ")[:140]
            print(f"    OK ({len(translated)} chars)")
            print(f"    Preview: {preview}...")
        except Exception as e:
            print(f"    ERROR: {e}")
            print(f"    -> Falling back to original EN section")
            fallback = (
                f"\n\n> [翻譯失敗：第 {sidx} 節 - {e}]\n"
                f"> 以下保留原文：\n\n"
                f"{section}"
            )
            translated_sections.append(fallback)
        time.sleep(1.5)

    print("\n" + "=" * 80)
    print("Combining translated sections...")
    output = "\n\n".join(translated_sections) + "\n"

    print(f"Writing output: {OUTPUT_PATH}")
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"\nDone! Output saved to: {OUTPUT_PATH}")
    print(f"  Input:  {len(md_text)} chars (EN)")
    print(f"  Output: {len(output)} chars (Traditional Chinese HK)")
    print(f"  Sections: {len(translated_sections)} / {len(sections)}")


if __name__ == "__main__":
    main()
