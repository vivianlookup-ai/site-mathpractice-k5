#!/usr/bin/env python3
"""
MathPractice K5 — PDF Worksheet Generator
Generates printable math worksheets for all grades K-5.

Professional layout with:
- Title block with grade/topic/difficulty
- Name / Date / Score fields
- 2-column problem grid with numbering
- Answer key on separate page (3-column)
- mathpracticek5.com branding

Usage: python3 scripts/generate_pdfs.py
Output: public/worksheets/{grade}-{topic}-{n}.pdf
"""

import os
import random
import math
import datetime
from pathlib import Path
from fpdf import FPDF

# ── Paths ──────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR.parent / "public" / "worksheets"

# ── Register Unicode fonts (DejaVu from brew) ─────────────────
DEJAVU_DIR = Path.home() / "Library" / "Fonts"

MM = 1.0  # fpdf2 uses mm by default
A4_W, A4_H = 210, 297
MARGIN = 18
COL_W = (A4_W - 2 * MARGIN - 8) / 2  # ~91mm per column
ANSWER_COL_W = (A4_W - 2 * MARGIN - 10) / 3  # ~58mm per answer col
LINE_H = 5.5  # base line height
CONTENT_W = A4_W - 2 * MARGIN  # usable width

# ── Grade label mapping ────────────────────────────────────────
GRADE_LABELS = {
    "k": "Kindergarten", "1": "Grade 1", "2": "Grade 2",
    "3": "Grade 3", "4": "Grade 4", "5": "Grade 5",
}


def init_pdf():
    """Create an FPDF instance with Unicode fonts registered."""
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_font("DejaVu", "", str(DEJAVU_DIR / "DejaVuSans.ttf"))
    pdf.add_font("DejaVu", "B", str(DEJAVU_DIR / "DejaVuSans-Bold.ttf"))
    pdf.add_font("DejaVuMono", "", str(DEJAVU_DIR / "DejaVuSansMono.ttf"))
    return pdf


# ══════════════════════════════════════════════════════════════
# Math problem generators (unchanged from previous version)
# ══════════════════════════════════════════════════════════════

def make_addition(seed, difficulty):
    rng = random.Random(seed)
    problems = []
    for _ in range(24):
        if difficulty == "easy":
            a = rng.randint(1, 9); b = rng.randint(1, 9)
        elif difficulty == "medium":
            a = rng.randint(10, 99); b = rng.randint(10, 99)
        else:
            a = rng.randint(100, 999); b = rng.randint(100, 999)
        problems.append((f"{a} + {b}", str(a + b)))
    return problems

def make_subtraction(seed, difficulty):
    rng = random.Random(seed)
    problems = []
    for _ in range(24):
        if difficulty == "easy":
            a = rng.randint(5, 18); b = rng.randint(1, a)
        elif difficulty == "medium":
            a = rng.randint(50, 99); b = rng.randint(1, a)
        else:
            a = rng.randint(100, 999); b = rng.randint(1, a)
        problems.append((f"{a} - {b}", str(a - b)))
    return problems

def make_multiplication(seed, difficulty):
    rng = random.Random(seed)
    problems = []
    for _ in range(24):
        if difficulty == "easy":
            a = rng.randint(2, 12); b = rng.randint(2, 12)
        elif difficulty == "medium":
            a = rng.randint(10, 99); b = rng.randint(2, 9)
        else:
            a = rng.randint(10, 99); b = rng.randint(10, 99)
        problems.append((f"{a} x {b}", str(a * b)))
    return problems

def make_division(seed, difficulty):
    rng = random.Random(seed)
    problems = []
    for _ in range(24):
        if difficulty in ("easy", "medium"):
            b = rng.randint(2, 12); q = rng.randint(1, 12 if difficulty == "easy" else 99)
            a = b * q
            problems.append((f"{a} / {b}", str(q)))
        else:
            b = rng.randint(4, 12); q = rng.randint(10, 99)
            a = b * q; a += rng.randint(1, b-1)
            problems.append((f"{a} / {b}", f"{a // b} R{a % b}"))
    return problems

def make_fractions(seed, difficulty):
    rng = random.Random(seed)
    problems = []
    for i in range(24):
        if difficulty == "easy":
            d = rng.choice([2, 3, 4]); n = rng.randint(1, d-1)
            problems.append((f"Shade {n}/{d}", f"{n}/{d}"))
        elif difficulty == "medium":
            d1 = rng.choice([2, 3, 4, 5, 6, 8]); n1 = rng.randint(1, d1-1)
            d2 = rng.choice([2, 3, 4, 5, 6, 8]); n2 = rng.randint(1, d2-1)
            cmp = ">" if n1/d1 > n2/d2 else "<" if n1/d1 < n2/d2 else "="
            problems.append((f"{n1}/{d1} __ {n2}/{d2}", cmp))
        else:
            d = rng.choice([4, 6, 8, 10, 12])
            if i < 12:
                n1 = rng.randint(1, d-1); n2 = rng.randint(1, d - n1)
                problems.append((f"{n1}/{d} + {n2}/{d}", f"{n1+n2}/{d}"))
            else:
                n1 = rng.randint(2, d-1); n2 = rng.randint(1, n1-1)
                problems.append((f"{n1}/{d} - {n2}/{d}", f"{n1-n2}/{d}"))
    return problems

def make_counting(seed, difficulty):
    rng = random.Random(seed)
    problems = []
    for i in range(20):
        if difficulty == "easy":
            count = rng.randint(1, 10); objs = rng.choice(["*", "@", "#", "%", "&"])
            problems.append((f"Count: {' '.join([objs]*count)}", str(count)))
        elif difficulty == "medium":
            start = rng.randint(1, 15); missing = rng.randint(start, start + 4)
            seq = [str(n) if n != missing else "__" for n in range(start, start+6)]
            problems.append((" ".join(seq), str(missing)))
        else:
            start = rng.randint(10, 20)
            problems.append((f"Count backwards from {start}", " ".join(str(n) for n in range(start, start-6, -1))))
    return problems

def make_number_recognition(seed, difficulty):
    rng = random.Random(seed)
    problems = []
    for i in range(20):
        n = rng.randint(0, 20)
        opts = rng.sample([x for x in range(0, 21) if x != n], 3) + [n]
        rng.shuffle(opts)
        problems.append((f"Circle {n}: {' '.join(str(x) for x in opts)}", str(n)))
    return problems

def make_shapes(seed, difficulty):
    rng = random.Random(seed)
    shapes = ["circle", "square", "triangle", "rectangle", "star", "diamond"]
    problems = []
    for i in range(16):
        shape = rng.choice(shapes); count = rng.randint(2, 8)
        problems.append((f"Draw {count} {shape}s", f"({count} {shape}s drawn)"))
    return problems

def make_patterns(seed, difficulty):
    rng = random.Random(seed)
    items = ["A", "B", "C", "X", "Y", "Z"]
    problems = []
    for i in range(16):
        pattern_len = rng.randint(2, 3); base = [rng.choice(items) for _ in range(pattern_len)]
        pattern = (base * 3)[:pattern_len * 3 - 1]
        answer = base[pattern_len - 1]
        problems.append((f"Complete: {' '.join(pattern)} __", answer))
    return problems

def make_comparing_numbers(seed, difficulty):
    rng = random.Random(seed)
    problems = []
    for i in range(20):
        lo, hi = {"easy": (1, 10), "medium": (1, 50), "hard": (1, 100)}.get(difficulty, (1, 50))
        a = rng.randint(lo, hi); b = rng.randint(lo, hi)
        cmp = ">" if a > b else "<" if a < b else "="
        problems.append((f"{a} __ {b}", cmp))
    return problems

def make_place_value(seed, difficulty):
    rng = random.Random(seed)
    problems = []
    for i in range(20):
        if difficulty == "easy":
            n = rng.randint(10, 99); t, o = n // 10, n % 10
            problems.append((f"{n} = __ tens + __ ones", f"{t} tens + {o} ones"))
        elif difficulty == "medium":
            n = rng.randint(100, 999); h, t, o = n // 100, (n // 10) % 10, n % 10
            problems.append((f"{n} = __ hundreds + __ tens + __ ones", f"{h}H {t}T {o}O"))
        else:
            n = rng.randint(1000, 9999); th, h, t, o = n // 1000, (n // 100) % 10, (n // 10) % 10, n % 10
            problems.append((f"Write {n} in expanded form", f"{th*1000}+{h*100}+{t*10}+{o}"))
    return problems

def make_time(seed, difficulty):
    rng = random.Random(seed)
    problems = []
    for i in range(16):
        h = rng.randint(1, 12)
        if difficulty == "easy": m = rng.choice([0, 30])
        elif difficulty == "medium": m = rng.choice([0, 15, 30, 45])
        else: m = rng.choice([5, 10, 20, 25, 35, 40, 50, 55])
        problems.append((f"Draw the time: {h}:{m:02d}", f"({h}:{m:02d})"))
    return problems

def make_money(seed, difficulty):
    rng = random.Random(seed)
    coins = [("penny", 1), ("nickel", 5), ("dime", 10), ("quarter", 25)]
    problems = []
    for i in range(16):
        if difficulty == "easy":
            c_name, c_val = rng.choice(coins[:3]); count = rng.randint(2, 10)
            problems.append((f"Count {count} {c_name}s", f"${count*c_val/100:.2f}"))
        elif difficulty == "medium":
            selected = rng.sample(coins, rng.randint(2, 3)); total = 0; desc = []
            for n, v in selected: c = rng.randint(1, 4); total += c * v; desc.append(f"{c} {n}")
            problems.append((f"You have {' + '.join(desc)}. How much?", f"${total/100:.2f}"))
        else:
            amt = rng.randint(50, 500); paid = rng.choice([100, 200, 500, 1000])
            while paid < amt: paid *= 2
            problems.append((f"Cost: ${amt/100:.2f}, Paid: ${paid/100:.2f}. Change?", f"${(paid-amt)/100:.2f}"))
    return problems

def make_word_problems(seed, difficulty):
    rng = random.Random(seed)
    names = ["Emma", "Liam", "Olivia", "Noah", "Ava", "Ethan", "Sophia", "Mason", "Mia", "Lucas"]
    problems = []
    for i in range(12):
        n1, n2 = rng.sample(names, 2)
        if difficulty == "easy":
            a = rng.randint(1, 19); b = rng.randint(1, 20 - a)
            if rng.random() < 0.5:
                problems.append((f"{n1} has {a} apples. {n2} gives her {b} more. Total?", str(a + b)))
            else:
                problems.append((f"{n1} has {a+b} crayons. She gives {a} to {n2}. Left?", str(b)))
        elif difficulty == "medium":
            a = rng.randint(5, 50); b = rng.randint(2, 9)
            if rng.random() < 0.5:
                problems.append((f"{n1} reads {a} pages/day. How many in {b} days?", str(a * b)))
            else:
                problems.append((f"Share {a*b} stickers among {b} friends. Each gets?", str(a)))
        else:
            a = rng.randint(10, 100); b = rng.randint(2, 12); c = rng.randint(2, 12)
            problems.append((f"{n1} buys {b} packs of {a} stickers. {n2} has {c} packs. Total?", str(a*b + a*c)))
    return problems

def make_measurement(seed, difficulty):
    rng = random.Random(seed)
    problems = []
    for i in range(16):
        if difficulty == "easy":
            a = rng.randint(1, 11); b = rng.randint(1, 12 - a)
            problems.append((f"{a} inches + {b} inches = __ inches", str(a + b)))
        elif difficulty == "medium":
            a = rng.randint(1, 99); b = rng.randint(1, 100 - a)
            problems.append((f"{a} cm + {b} cm = __ cm", str(a + b)))
        else:
            a = rng.randint(1, 10); b = rng.randint(2, 5)
            problems.append((f"Rectangle {a}cm x {b}cm. Perimeter?", str(2*(a+b)) + " cm"))
    return problems

def make_geometry(seed, difficulty):
    rng = random.Random(seed)
    shapes = ["square", "rectangle", "triangle", "hexagon", "octagon", "pentagon"]
    side_map = {"triangle": "3", "square": "4", "rectangle": "4", "pentagon": "5", "hexagon": "6", "octagon": "8"}
    problems = []
    for i in range(16):
        if difficulty == "easy":
            s = rng.choice(shapes)
            problems.append((f"How many sides does a {s} have?", side_map[s]))
        elif difficulty == "medium":
            a = rng.randint(3, 15); b = rng.randint(3, 15)
            problems.append((f"Area of {a} x {b} rectangle", str(a * b)))
        else:
            a = rng.randint(3, 12)
            problems.append((f"Perimeter of square side {a}", str(4 * a)))
    return problems

def make_decimals(seed, difficulty):
    rng = random.Random(seed)
    problems = []
    for i in range(20):
        if difficulty == "easy":
            n = rng.uniform(0.1, 9.9)
            problems.append((f"Write in words: {n:.1f}", f"{n:.1f}"))
        elif difficulty == "medium":
            a = rng.uniform(1, 99); b = rng.uniform(1, 99 - a)
            problems.append((f"{a:.1f} + {b:.1f}", f"{a+b:.1f}"))
        else:
            a = rng.uniform(1, 99); b = rng.uniform(1, 99 - a)
            problems.append((f"{a:.2f} + {b:.2f}", f"{a+b:.2f}"))
    return problems

def make_fractions_and_decimals(seed, difficulty):
    rng = random.Random(seed)
    problems = []
    for i in range(20):
        d = rng.choice([10, 100]); n = rng.randint(1, d-1); dec = n / d
        if rng.random() < 0.5:
            problems.append((f"{n}/{d} = __ (decimal)", f"{dec:.{len(str(d))-1}f}"))
        else:
            problems.append((f"{dec:.{len(str(d))-1}f} = __ (fraction)", f"{n}/{d}"))
    return problems

def make_fraction_operations(seed, difficulty):
    rng = random.Random(seed)
    problems = []
    for i in range(20):
        d = rng.choice([4, 6, 8, 10, 12])
        if i < 10:
            n1 = rng.randint(1, d-1); n2 = rng.randint(1, d - n1)
            problems.append((f"{n1}/{d} + {n2}/{d}", f"{n1+n2}/{d}"))
        else:
            n1 = rng.randint(2, d-1); n2 = rng.randint(1, n1)
            problems.append((f"{n1}/{d} x {n2}/{d}", f"{n1*n2}/{d*d}"))
    return problems

def make_volume(seed, difficulty):
    rng = random.Random(seed)
    problems = []
    for i in range(16):
        if difficulty == "easy":
            s = rng.randint(1, 5)
            problems.append((f"Volume of {s}x{s}x{s} cube", f"{s**3} cubic units"))
        elif difficulty == "medium":
            l = rng.randint(2, 8); w = rng.randint(2, 8); h = rng.randint(2, 8)
            problems.append((f"Volume of {l}x{w}x{h} prism", f"{l*w*h} cubic units"))
        else:
            l = rng.randint(3, 12); w = rng.randint(3, 12); h = rng.randint(3, 12)
            problems.append((f"Volume of {l}x{w}x{h} box", f"{l*w*h} cubic units"))
    return problems

def make_order_of_operations(seed, difficulty):
    rng = random.Random(seed)
    problems = []
    for i in range(16):
        a, b, c = rng.randint(2, 9), rng.randint(2, 9), rng.randint(2, 9)
        if difficulty == "easy":
            problems.append((f"{a} + {b} x {c}", str(a + b * c)))
        elif difficulty == "medium":
            d = rng.randint(2, 9)
            problems.append((f"({a}+{b}) x ({c}-{d})", str((a+b)*(c-d))))
        else:
            d, e = rng.randint(2, 9), rng.randint(2, 9)
            problems.append((f"{a}² + {b}x({c}+{d})-{e}", str(a*a + b*(c+d)-e)))
    return problems


# ── Topic -> problem generator mapping ───────────────────────────
TOPIC_GENERATORS = {
    "addition": make_addition,
    "subtraction": make_subtraction,
    "multiplication": make_multiplication,
    "division": make_division,
    "fractions": make_fractions,
    "fractions-basics": make_fractions,
    "fraction-operations": make_fraction_operations,
    "fractions-and-decimals": make_fractions_and_decimals,
    "counting": make_counting,
    "number-recognition": make_number_recognition,
    "shapes": make_shapes,
    "patterns": make_patterns,
    "comparing-numbers": make_comparing_numbers,
    "place-value": make_place_value,
    "time": make_time,
    "money": make_money,
    "word-problems": make_word_problems,
    "measurement": make_measurement,
    "geometry": make_geometry,
    "decimals": make_decimals,
    "volume": make_volume,
    "order-of-operations": make_order_of_operations,
}


def difficulty_from_index(i, total):
    """Assign difficulty: 1st third Easy, 2nd Medium, 3rd Hard."""
    if i < max(1, total // 3):
        return "easy"
    elif i < max(1, total * 2 // 3):
        return "medium"
    else:
        return "hard"


# ══════════════════════════════════════════════════════════════
# PDF Layout — Professional Edition
# ══════════════════════════════════════════════════════════════

def draw_title_block(pdf, grade_label, topic_name, ws_num, total_ws, diff):
    """Draw centered title block with grade, topic, and worksheet info."""
    # Domain brand line
    pdf.set_font("DejaVu", "", 8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 5, "mathpracticek5.com", new_x="LMARGIN", new_y="NEXT", align="R")
    pdf.set_text_color(0, 0, 0)
    pdf.ln(2)

    # Grade badge + Topic title
    pdf.set_font("DejaVu", "B", 20)
    pdf.cell(0, 11, f"{grade_label} — {topic_name}", new_x="LMARGIN", new_y="NEXT", align="C")

    # Worksheet subtitle
    pdf.set_font("DejaVu", "", 11)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 7, f"Worksheet {ws_num} of {total_ws}  •  {diff.title()} Difficulty",
             new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.set_text_color(0, 0, 0)

    # Thin decorative line
    pdf.ln(1)
    y_line = pdf.get_y()
    pdf.set_draw_color(200, 200, 200)
    pdf.line(MARGIN, y_line, A4_W - MARGIN, y_line)
    pdf.ln(5)


def draw_info_line(pdf):
    """Draw Name / Date / Score line with separators."""
    pdf.set_font("DejaVu", "", 10)
    pdf.set_text_color(80, 80, 80)

    # Three columns: Name | Date | Score
    col_w = (CONTENT_W - 10) / 3

    # Name
    pdf.cell(col_w, 7, "Name: _________________________________")
    # Date
    today = datetime.date.today().strftime("%B %d, %Y")
    pdf.cell(col_w, 7, f"Date: ___________________")
    # Score
    pdf.cell(col_w, 7, "Score: _____ / _____", align="R")
    pdf.ln(10)
    pdf.set_text_color(0, 0, 0)


def draw_section_separator(pdf):
    """Light dashed-style separator line."""
    y = pdf.get_y()
    pdf.set_draw_color(220, 220, 220)
    pdf.line(MARGIN, y, A4_W - MARGIN, y)
    pdf.ln(4)


def render_problems(pdf, problems):
    """Render problems in a 2-column numbered grid."""
    cols = 2
    rows = math.ceil(len(problems) / cols)
    cell_w = COL_W
    cell_h = 9

    pdf.set_font("DejaVuMono", "", 9.5)
    pdf.set_text_color(30, 30, 30)

    for row in range(rows):
        y_start = pdf.get_y()

        # Check page break before each row
        if y_start + cell_h > pdf.h - 20:
            pdf.add_page()
            y_start = pdf.get_y()

        for col in range(cols):
            idx = row * cols + col
            if idx >= len(problems):
                break
            problem_text, _ = problems[idx]
            x = MARGIN + col * (cell_w + 8)
            pdf.set_xy(x, y_start)

            # Number circle
            num_text = f"{idx+1}."
            pdf.set_font("DejaVu", "B", 9)
            pdf.set_text_color(80, 80, 80)
            w_num = pdf.get_string_width(num_text) + 2
            pdf.cell(w_num, cell_h, num_text)

            # Problem text
            pdf.set_font("DejaVuMono", "", 9.5)
            pdf.set_text_color(30, 30, 30)
            pdf.cell(cell_w - w_num, cell_h, f"  {problem_text}")

        # Move to next row
        pdf.set_y(y_start + cell_h)

    pdf.set_text_color(0, 0, 0)
    pdf.ln(3)


def render_answer_key(pdf, problems, grade_label, topic_name, ws_num):
    """Render answer key on a new page in 3-column format."""
    pdf.add_page()

    # Header
    pdf.set_font("DejaVu", "B", 16)
    pdf.cell(0, 10, "Answer Key", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.set_font("DejaVu", "", 9)
    pdf.set_text_color(120, 120, 120)
    pdf.cell(0, 6, f"{grade_label} — {topic_name} — Worksheet {ws_num}",
             new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.set_text_color(0, 0, 0)
    pdf.ln(2)

    # Decorative line
    y = pdf.get_y()
    pdf.set_draw_color(200, 200, 200)
    pdf.line(MARGIN, y, A4_W - MARGIN, y)
    pdf.ln(5)

    # 3-column answer grid
    acols = 3
    arows = math.ceil(len(problems) / acols)
    acell_w = ANSWER_COL_W
    acell_h = 7

    pdf.set_font("DejaVuMono", "", 9)
    for row in range(arows):
        y_start = pdf.get_y()
        if y_start + acell_h > pdf.h - 20:
            pdf.add_page()
            y_start = pdf.get_y()

        for col in range(acols):
            idx = row * acols + col
            if idx >= len(problems):
                break
            _, answer = problems[idx]
            x = MARGIN + col * (acell_w + 5)
            pdf.set_xy(x, y_start)
            pdf.cell(acell_w, acell_h, f"{idx+1}.  {answer}")

        pdf.set_y(y_start + acell_h)


def make_worksheet_pdf(pdf, grade_id, topic_name,
                       ws_num, total_ws,
                       include_answer_key=True):
    """
    Render a complete worksheet with professional layout.
    """
    diff = difficulty_from_index(ws_num - 1, total_ws)
    seed = f"{grade_id}-{topic_name.lower().replace(' ','-')}-{ws_num}"

    # ── Generate problems ──
    topic_key = topic_name.lower().replace(" ", "-")
    name_map = {
        "fractions-basics": "fractions-basics",
        "fraction-operations": "fraction-operations",
        "fractions-&-decimals": "fractions-and-decimals",
        "telling-time": "time",
        "money-math": "money",
    }
    gen_key = name_map.get(topic_key, topic_key)
    generator = TOPIC_GENERATORS.get(gen_key, make_addition)
    problems = generator(seed, diff)

    grade_label = GRADE_LABELS.get(grade_id, f"Grade {grade_id}")

    # ── Page 1: Title + Info + Problems ──
    pdf.add_page()

    # Brand + Title
    draw_title_block(pdf, grade_label, topic_name, ws_num, total_ws, diff)

    # Name / Date / Score
    draw_info_line(pdf)

    # Problems
    render_problems(pdf, problems)

    # ── Page 2: Answer Key ──
    if include_answer_key:
        render_answer_key(pdf, problems, grade_label, topic_name, ws_num)

    return problems


# ══════════════════════════════════════════════════════════════
# Batch generation
# ══════════════════════════════════════════════════════════════

def generate_all():
    """Generate all worksheets for all grades and topics."""
    print(f"Generating worksheets to: {OUTPUT_DIR}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    grade_spec = {
        "k": {
            "name": "Kindergarten",
            "topics": [
                ("counting", "Counting", 5),
                ("number-recognition", "Number Recognition", 4),
                ("shapes", "Shapes", 4),
                ("patterns", "Patterns", 3),
                ("comparing-numbers", "Comparing Numbers", 4),
            ]
        },
        "1": {
            "name": "Grade 1",
            "topics": [
                ("addition", "Addition", 5),
                ("subtraction", "Subtraction", 5),
                ("place-value", "Place Value", 4),
                ("time", "Telling Time", 4),
                ("money", "Money Math", 4),
                ("word-problems", "Word Problems", 3),
            ]
        },
        "2": {
            "name": "Grade 2",
            "topics": [
                ("addition", "Addition", 5),
                ("subtraction", "Subtraction", 5),
                ("place-value", "Place Value", 4),
                ("measurement", "Measurement", 4),
                ("money", "Money Math", 4),
                ("time", "Telling Time", 3),
            ]
        },
        "3": {
            "name": "Grade 3",
            "topics": [
                ("multiplication", "Multiplication", 5),
                ("division", "Division", 5),
                ("fractions-basics", "Fractions Basics", 5),
                ("addition", "Addition", 4),
                ("subtraction", "Subtraction", 4),
                ("geometry", "Geometry", 4),
                ("word-problems", "Word Problems", 3),
            ]
        },
        "4": {
            "name": "Grade 4",
            "topics": [
                ("fractions", "Fractions", 5),
                ("multiplication", "Multiplication", 5),
                ("division", "Division", 5),
                ("addition", "Addition", 4),
                ("subtraction", "Subtraction", 4),
                ("geometry", "Geometry", 4),
                ("word-problems", "Word Problems", 3),
            ]
        },
        "5": {
            "name": "Grade 5",
            "topics": [
                ("decimals", "Decimals", 5),
                ("fractions-and-decimals", "Fractions & Decimals", 5),
                ("fraction-operations", "Fraction Operations", 5),
                ("multiplication", "Multiplication", 4),
                ("division", "Division", 4),
                ("volume", "Volume", 4),
                ("order-of-operations", "Order of Operations", 3),
            ]
        },
    }

    total = 0
    for gid, gspec in grade_spec.items():
        for tid, tname, count in gspec["topics"]:
            for ws_num in range(1, count + 1):
                filename = f"{gid}-{tid}-{ws_num}.pdf"
                filepath = OUTPUT_DIR / filename

                pdf = init_pdf()
                make_worksheet_pdf(
                    pdf=pdf,
                    grade_id=gid,
                    topic_name=tname,
                    ws_num=ws_num,
                    total_ws=count,
                    include_answer_key=True,
                )
                pdf.output(str(filepath))
                total += 1
                if total % 10 == 0:
                    print(f"  Generated {total} worksheets...")

    print(f"\nDone! Generated {total} PDF worksheets in: {OUTPUT_DIR}")
    return total


if __name__ == "__main__":
    generate_all()
