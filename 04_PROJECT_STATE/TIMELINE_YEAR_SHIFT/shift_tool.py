#!/usr/bin/env python3
"""
THE QUIET TIDE — In-universe timeline year shift 2026 -> 2024 (all in-universe years -2).

Classification policy (documented in the final report):
- SHIFT: every fictional in-universe year >= 1990 by exactly -2.
- KEEP:  (a) every year < 1990 — the deep-history chronology is densely
         interwoven with real-world history (the bible's "public record"
         technique: Havana 1962, Berlin 1989, etc.); shifting it would
         falsify real dates and redesign canon. No stated relative interval
         ties a pre-1990 date to the story present, so keeping them breaks
         nothing.
         (b) real-history-anchored years >= 1990 (context-specific): 1991 lost
         decade, 1992 Rio, 1993 Waco, 1994 Kobe/Rhine, 1995 Aum/recharter,
         1996 Dolly, 1999-2000 Y2K/Port Survey, 2000 (tied to 1991-1999),
         2001 9/11, 2004 Sunda tsunami, 2008 Lehman, 2010 Eyjafjallajokull,
         2011 Fukushima, 2013 Snowden, 2014 Crimea, 2015 Paris, 2017 Jakarta
         flood, 2020-2021 pandemic, 2021 Suez, 2022 Kyiv.
- DOC ISO dates (2026-09-19/20/21/22/23 locks etc.) are never touched.
- FINAL_WORLD_BIBLE/CHAPTERS/ (frozen prose) is never touched.
- Word-count metrics in audits are never touched.
"""
import re, os, sys, hashlib, json
from pathlib import Path

ROOT = Path.home() / "workspace/world_bible/work_rar"
CHAPTERS_DIR = ROOT / "FINAL_WORLD_BIBLE/CHAPTERS"

WEEKDAYS = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
            "Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

ISO_RE = re.compile(r'\b(1[5-9]\d\d|20[0-2]\d)-(0[1-9]|1[0-2])(-([0-2][0-9]|3[01]))?\b')
YEAR_RE = re.compile(r'\b(199[0-9]|20[0-2][0-9])\b')
RANGE4_RE = re.compile(r'\b(\d{3,4})([–—-])(\d{4})\b')
RANGE2_RE = re.compile(r'\b(\d{4})([–—-])(\d{2})\b')
ARROW_RE = re.compile(r'\b(\d{4})→(\d{4})\b')
PRESENT_RE = re.compile(r'\b(\d{4})([–—-])(present)\b')

STORY_ISO_MARKERS = ["DATE-TIME","TIMELINE","JST","night shift","verified","family-dinner",
                     "family dinner","Pram arrives","arrives in Hamaura","planning figure",
                     "canon event","reclassification","until 20","EVENT-"]
DOC_ISO_MARKERS = ["LOCKED","LOCK ","finaliz","approv","audit","creat","Phase","govern",
                   "repair","measur","integrat","directiv","WIB","sha256","consolidat",
                   "Date:","worklog","baseline","checksum","manifest","Author",
                   "C-14-","AD-12-","Project phase","reconciled","filed by","Worker:"]

# story ISO days for 2026-09 (finite known set); 19/21 always doc; 20/22/23 context-dependent
STORY_ISO_DAYS = {"01","02","04","05","06","07","08","09","10","11","12","13","14",
                  "15","16","17","18","24","25"}
MIXED_ISO_DAYS = {"20","22","23"}

def classify_iso(m, line):
    s = m.group(0)
    year, mon = s[:4], s[5:7]
    if year == "2026" and mon == "09":
        day = s[8:10]
        if day in STORY_ISO_DAYS:
            return "STORY"
        if day in ("19","21"):
            return "DOC"
        if day in MIXED_ISO_DAYS:
            # DOC by default; STORY only on precise blueprint/chapter-date evidence.
            # (Avoids substring traps like "TIMELINE" inside "DAICHI_TIMELINE.md".)
            win = line[max(0,m.start()-100):m.end()+100]
            if "**TIMELINE" in win or "**DATE-TIME" in win:
                return "STORY"
            if "TIMELINE →" in win or "DATE-TIME →" in win:
                return "STORY"
            if "→" in win and re.search(r'\b(Mon|Tue|Wed|Thu|Fri|Sat|Sun)(day)?\b', win):
                return "STORY"
            if re.search(r'\b(Mon|Tue|Wed|Thu|Fri|Sat|Sun)(day)?\b.{0,20}2026-09-(20|22|23)', win) \
               and "JST" in win:
                return "STORY"
            if "night shift" in win and re.search(r'\b(Mon|Tue|Wed|Thu|Fri|Sat|Sun)(day)?\b', win):
                return "STORY"
            if "until 2026-09-20" in win or "from 2026-09-20" in win:
                return "STORY"
            if "family-dinner" in win or "family dinner" in win:
                return "STORY"
            return "DOC"
        return "DOC"
    # Other ISO dates. Rules:
    #  - year < 1990 -> DOC (deep-history ISOs like Hiroshima 1945-08,
    #    Tunguska 1908-06-30, Lisbon 1755-11): never shifted.
    #  - year >= 1990: shift only if classify_year says SHIFT for this
    #    context (real-anchored ones like Suez 2021-03, Fukushima 2011-03
    #    return KEEP) AND the line carries a story marker.
    win = line[max(0,m.start()-80):m.end()+80]
    if int(year) < 1990:
        return "DOC"
    if classify_year(year, win) != "SHIFT":
        return "DOC"
    if any(k in win for k in STORY_ISO_MARKERS):
        return "STORY"
    if any(k in win for k in DOC_ISO_MARKERS):
        return "DOC"
    return "DOC"  # fail closed

def classify_year(y, win):
    """Return 'SHIFT' or 'KEEP' for a standalone year with context window.

    SCOPE DECISION (documented in final report): shift fictional in-universe
    years >= 1990 only. Years < 1990 are kept: the deep-history chronology is
    densely interwoven with real-world history (public-record technique:
    Havana 1962, Berlin 1989, Saigon 1975, etc.); shifting it would falsify
    real dates and redesign canon. No stated interval ties a pre-1990 date to
    the story present, so keeping them breaks nothing.
    Real-anchored years >= 1990 are kept contextually (see list below).
    """
    y = int(y)
    if y < 1990:
        return "KEEP"
    wl = win.lower()
    if y == 1991 and re.search(r'lost decade|soviet|vault|reconstituted|department', wl): return "KEEP"
    if y == 1992 and "rio" in wl: return "KEEP"
    if y == 1993 and "waco" in wl: return "KEEP"
    if y == 1994 and re.search(r'kobe|rhine', wl): return "KEEP"
    if y == 1995 and re.search(r'aum|sarin|recharter|charter|kobe|tokyo static|event-060', wl): return "KEEP"
    if y == 1996 and "dolly" in wl: return "KEEP"
    if y == 1999 and re.search(r'port survey|millennium|y2k|event-064|survey zoned|1999 survey|lost decade|soviet', wl): return "KEEP"
    if y == 2000: return "KEEP"  # millennium/Y2K-adjacent (High Tide rise, masquerade span)
    if y == 2001 and re.search(r'ground zero|9/11|event-065', wl): return "KEEP"
    if y == 2004 and re.search(r'sunda|tsunami', wl): return "KEEP"
    if y == 2008 and "lehman" in wl: return "KEEP"
    if y == 2010 and "eyjafjallaj" in wl: return "KEEP"
    if y == 2011 and "fukushima" in wl: return "KEEP"
    if y == 2013 and "snowden" in wl: return "KEEP"
    if y == 2014 and "crimea" in wl: return "KEEP"
    if y == 2015 and "paris" in wl: return "KEEP"
    if y == 2017 and "jakarta flood" in wl: return "KEEP"
    if y == 2020 and re.search(r'pandemic|event-081|dip-and-rebound', wl): return "KEEP"
    if y == 2021 and re.search(r'pandemic|event-081|suez', wl): return "KEEP"
    if y == 2022 and re.search(r'kyiv|ukraine', wl): return "KEEP"
    return "SHIFT"

def shift_y(y):
    return str(int(y) - 2)

def main():
    apply = "--apply" in sys.argv
    md5_before, md5_after = {}, {}
    changes, flags, iso_log, weekday_risks = [], [], [], []
    files = []
    for base in (ROOT/"FINAL_WORLD_BIBLE", ROOT/"REBOOT_DESIGN"):
        for p in sorted(base.rglob("*.md")):
            if p.is_relative_to(CHAPTERS_DIR):
                continue
            files.append(p)

    for p in files:
        rel = str(p.relative_to(ROOT))
        raw = p.read_bytes()
        md5_before[rel] = hashlib.md5(raw).hexdigest()
        text = raw.decode("utf-8")
        lines = text.split("\n")
        new_lines = []
        file_changed = False

        for ln, line in enumerate(lines, 1):
            orig = line
            # --- metric protections (word counts) ---
            placeholders = {}
            def _ph(key, val):
                tok = f"\x00{key}{len(placeholders)}\x00"
                placeholders[tok] = val
                return tok
            line = re.sub(r'\(\d{3,4} → \d{3,4}', lambda m: _ph("METRIC", m.group(0)), line)
            line = re.sub(r'\|\s*\d{3}\s*\|\s*\d{4}\s*\|\s*\d{4}\s*\|',
                           lambda m: _ph("METRIC", m.group(0)), line)
            line = re.sub(r'^\d{4} \d{3}_[A-Za-z]',
                           lambda m: _ph("METRIC", m.group(0)), line)
            # calendar-verification notes: "(verified: 2026-09-04 = Friday)" documents
            # a true calendar fact explaining the weekday choice; keep verbatim
            line = re.sub(r'\(verified:[^)]*\)',
                           lambda m: _ph("METRIC", m.group(0)), line)
            # --- ISO dates: classify then shift story ones ---
            def _iso_sub(m):
                cls = classify_iso(m, line)
                iso_log.append({"file":rel,"line":ln,"date":m.group(0),"class":cls})
                if cls == "STORY":
                    return shift_y(m.group(0)[:4]) + m.group(0)[4:]
                return _ph("DOCISO", m.group(0))
            line = ISO_RE.sub(_iso_sub, line)
            # --- immediately protect ALL remaining ISO-shaped tokens (story-shifted
            #     and doc) so later passes cannot re-process them ---
            line = re.sub(r'\b(1[5-9]\d\d|20[0-2]\d)-(0[1-9]|1[0-2])(-([0-2][0-9]|3[01]))?\b',
                          lambda m: _ph("ISO", m.group(0)), line)
            # --- ranges (results wrapped in placeholders: single-pass, no re-shift) ---
            def _r4(m):
                a, sep, b = m.group(1), m.group(2), m.group(3)
                if len(a) != 4:
                    return m.group(0)
                win = line[max(0,m.start()-60):m.end()+60]
                ca, cb = classify_year(a, win), classify_year(b, win)
                na = shift_y(a) if ca == "SHIFT" else a
                nb = shift_y(b) if cb == "SHIFT" else b
                if "FLAG" in (ca, cb):
                    flags.append({"file":rel,"line":ln,"date":m.group(0),
                                  "issue":"range endpoint ambiguous","recommendation":"author review"})
                return _ph("RANGE", na + sep + nb)
            line = RANGE4_RE.sub(_r4, line)
            def _r2(m):
                a, sep, b2 = m.group(1), m.group(2), m.group(3)
                win = line[max(0,m.start()-60):m.end()+60]
                full_b = a[:2] + b2
                ca, cb = classify_year(a, win), classify_year(full_b, win)
                if ca == "SHIFT" and cb == "SHIFT":
                    nb = shift_y(full_b)
                    return _ph("RANGE", shift_y(a) + sep + nb[2:])
                if "FLAG" in (ca, cb):
                    flags.append({"file":rel,"line":ln,"date":m.group(0),
                                  "issue":"range endpoint ambiguous","recommendation":"author review"})
                return _ph("RANGE", m.group(0))
            line = RANGE2_RE.sub(_r2, line)
            def _par(m):
                a, b = m.group(1), m.group(2)
                win = line[max(0,m.start()-60):m.end()+60]
                if classify_year(a, win) == "SHIFT" and classify_year(b, win) == "SHIFT":
                    return _ph("ARROW", shift_y(a) + "→" + shift_y(b))
                return _ph("ARROW", m.group(0))
            line = ARROW_RE.sub(_par, line)
            def _pres(m):
                a = m.group(1)
                win = line[max(0,m.start()-60):m.end()+60]
                if classify_year(a, win) == "SHIFT":
                    return _ph("RANGE", shift_y(a) + m.group(2) + "present")
                return _ph("RANGE", m.group(0))
            line = PRESENT_RE.sub(_pres, line)
            # --- standalone years ---
            def _yr(m):
                y = m.group(1)
                win = line[max(0,m.start()-150):m.end()+150]
                # don't touch placeholder-adjacent content
                cls = classify_year(y, win)
                if cls == "SHIFT":
                    return shift_y(y)
                if cls == "FLAG":
                    flags.append({"file":rel,"line":ln,"date":y,
                                  "issue":"ambiguous real-history anchoring",
                                  "context":win.strip()[:120]})
                return y
            line = YEAR_RE.sub(_yr, line)
            # --- restore placeholders ---
            for tok, val in placeholders.items():
                line = line.replace(tok, val)
            if line != orig:
                file_changed = True
                changes.append({"file":rel,"line":ln,"before":orig.strip()[:220],
                                "after":line.strip()[:220]})
                if any(w in line for w in WEEKDAYS) or "every-other-Sunday" in line:
                    weekday_risks.append({"file":rel,"line":ln,"text":line.strip()[:220]})
            new_lines.append(line)

        if file_changed:
            if apply:
                p.write_text("\n".join(new_lines), encoding="utf-8")
                md5_after[rel] = hashlib.md5(p.read_bytes()).hexdigest()
            else:
                md5_after[rel] = "(dry-run)"
        else:
            md5_after[rel] = md5_before[rel]

    out = {"files_scanned": len(files),
           "files_changed": sum(1 for f in files if str(f.relative_to(ROOT)) in
                                [c["file"] for c in changes]),
           "total_changes": len(changes),
           "md5_before": md5_before, "md5_after": md5_after,
           "changes": changes, "flags": flags,
           "iso_classifications": iso_log, "weekday_risks": weekday_risks}
    outp = Path(__file__).parent / ("shift_result.json" if apply else "shift_dryrun.json")
    outp.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"scanned={len(files)} changed_files~{out['files_changed']} "
          f"line_changes={len(changes)} flags={len(flags)} "
          f"iso_story={sum(1 for i in iso_log if i['class']=='STORY')} "
          f"iso_doc={sum(1 for i in iso_log if i['class']=='DOC')} "
          f"weekday_risks={len(weekday_risks)} -> {outp.name}")

if __name__ == "__main__":
    main()
