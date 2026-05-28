import html
import re
import sys
from extractor.parsers.text import read_text_file


def strip_rtf_fallback(raw: str) -> str:
    raw = re.sub(r"\\'[0-9a-fA-F]{2}", " ", raw)
    raw = re.sub(r"\\par[d]?", "\n", raw)
    raw = re.sub(r"\\tab", "\t", raw)
    raw = re.sub(r"\\[a-zA-Z]+-?\d* ?", "", raw)
    raw = raw.replace("{", "").replace("}", "")
    return html.unescape(raw)


def extract_rtf(rtf_path: str) -> tuple[str, str]:
    raw = read_text_file(rtf_path)
    if raw is None:
        print("ERROR: Could not read RTF file", file=sys.stderr)
        sys.exit(1)

    try:
        from striprtf.striprtf import rtf_to_text
        text = rtf_to_text(raw)
        if text.strip():
            return text, "striprtf"
    except ImportError:
        pass
    except Exception:
        pass

    return strip_rtf_fallback(raw), "rtf-regex"
