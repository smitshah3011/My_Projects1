import os
import math
from dotenv import find_dotenv, load_dotenv
from groq import Groq
import streamlit as st

load_dotenv(find_dotenv())

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# ── Page config ───────────────────────────────────────────────────
st.set_page_config(
    page_title="AaharAI v2 — Indian Diet & Fitness Planner",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&family=DM+Sans:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
    --bg:        #080A0F;
    --bg2:       #0E1117;
    --bg3:       #141820;
    --border:    rgba(99, 210, 255, 0.12);
    --border-hi: rgba(99, 210, 255, 0.35);
    --gold:      #63D2FF;
    --gold2:     #A78BFA;
    --gold3:     #34D399;
    --text:      #E8EDF5;
    --muted:     #5A6478;
    --muted2:    #8B95A8;
    --danger:    #F87171;
    --warn:      #FBBF24;
    --green:     #34D399;
}

html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    font-family: 'DM Sans', sans-serif;
    color: var(--text);
}
[data-testid="stAppViewContainer"] > .main { background: var(--bg) !important; }
#MainMenu, footer, header, [data-testid="stToolbar"] { display: none !important; }
[data-testid="stDecoration"] { display: none !important; }
[data-testid="stMainBlockContainer"] { padding-top: 0 !important; }

/* ── HERO ── */
.hero {
    background: linear-gradient(135deg, #080A0F 0%, #0D1020 50%, #080A0F 100%);
    border-bottom: 1px solid var(--border);
    padding: 3rem 2rem 2.5rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    margin-bottom: 0;
}
.hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background:
        radial-gradient(ellipse 60% 40% at 20% 50%, rgba(99,210,255,0.06) 0%, transparent 70%),
        radial-gradient(ellipse 50% 40% at 80% 50%, rgba(167,139,250,0.06) 0%, transparent 70%);
    pointer-events: none;
}
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: rgba(99,210,255,0.08);
    border: 1px solid rgba(99,210,255,0.2);
    border-radius: 999px;
    padding: 0.3rem 0.9rem;
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    color: var(--gold);
    text-transform: uppercase;
    margin-bottom: 1.2rem;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.8rem, 6vw, 4.8rem);
    font-weight: 800;
    color: var(--text);
    line-height: 1;
    letter-spacing: -0.02em;
    margin-bottom: 0.6rem;
}
.hero-title .accent { color: var(--gold); }
.hero-title .accent2 { color: var(--gold2); }
.hero-sub {
    font-size: 1rem;
    color: var(--muted2);
    font-weight: 300;
    max-width: 500px;
    margin: 0 auto;
    line-height: 1.75;
}
.hero-tags {
    display: flex;
    justify-content: center;
    gap: 0.6rem;
    margin-top: 1.4rem;
    flex-wrap: wrap;
}
.hero-tag {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 0.25rem 0.7rem;
    font-size: 0.72rem;
    color: var(--muted2);
    font-family: 'DM Mono', monospace;
}

/* ── TAB NAV ── */
.tab-nav {
    display: flex;
    gap: 0;
    background: var(--bg2);
    border-bottom: 1px solid var(--border);
    margin-bottom: 0;
}
.tab-btn {
    flex: 1;
    padding: 1rem;
    text-align: center;
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--muted);
    border-bottom: 2px solid transparent;
    cursor: pointer;
    transition: all 0.2s;
}
.tab-btn.active { color: var(--gold); border-color: var(--gold); }

/* ── PANEL ── */
.panel {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}
.panel-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.panel-title::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
}

/* ── STAT GRID ── */
.stat-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(110px, 1fr));
    gap: 0.6rem;
    margin: 1rem 0;
}
.stat-box {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 0.9rem;
    transition: border-color 0.2s;
}
.stat-box:hover { border-color: var(--border-hi); }
.stat-val {
    font-family: 'Syne', sans-serif;
    font-size: 1.6rem;
    font-weight: 700;
    line-height: 1;
    color: var(--gold);
}
.stat-val.green { color: var(--green); }
.stat-val.purple { color: var(--gold2); }
.stat-val.warn { color: var(--warn); }
.stat-val.danger { color: var(--danger); }
.stat-lbl {
    font-size: 0.67rem;
    color: var(--muted);
    margin-top: 0.25rem;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.06em;
}

/* ── BMI BAR ── */
.bmi-track {
    height: 5px;
    background: var(--bg3);
    border-radius: 999px;
    overflow: hidden;
    margin: 0.6rem 0 0.3rem;
    position: relative;
}
.bmi-fill {
    height: 100%;
    border-radius: 999px;
    transition: width 0.8s cubic-bezier(0.34,1.56,0.64,1);
}
.bmi-labels {
    display: flex;
    justify-content: space-between;
    font-size: 0.6rem;
    color: var(--muted);
    font-family: 'DM Mono', monospace;
}

/* ── MACRO RING LABELS ── */
.macro-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.5rem;
    margin-top: 0.8rem;
}
.macro-item {
    background: var(--bg3);
    border-radius: 8px;
    padding: 0.75rem;
    text-align: center;
    border: 1px solid var(--border);
}
.macro-val {
    font-family: 'Syne', sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
}
.macro-lbl { font-size: 0.62rem; color: var(--muted); font-family: 'DM Mono', monospace; margin-top: 0.1rem; }

/* ── BUTTONS ── */
div[data-testid="stButton"] > button {
    font-family: 'Syne', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.08em !important;
    padding: 0.9rem 2rem !important;
    border-radius: 8px !important;
    border: none !important;
    cursor: pointer !important;
    transition: all 0.2s !important;
    width: 100% !important;
}

/* Diet button - cyan */
div[data-testid="stButton"]:nth-of-type(1) > button {
    background: linear-gradient(135deg, #0EA5E9, #63D2FF) !important;
    color: #080A0F !important;
}
div[data-testid="stButton"]:nth-of-type(1) > button:hover {
    background: linear-gradient(135deg, #38BDF8, #7DE0FF) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 24px rgba(99,210,255,0.25) !important;
}

/* Exercise button - purple */
div[data-testid="stButton"]:nth-of-type(2) > button {
    background: linear-gradient(135deg, #7C3AED, #A78BFA) !important;
    color: #fff !important;
}
div[data-testid="stButton"]:nth-of-type(2) > button:hover {
    background: linear-gradient(135deg, #8B5CF6, #C4B5FD) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 24px rgba(167,139,250,0.3) !important;
}

/* ── INPUTS ── */
[data-testid="stNumberInput"] input,
[data-testid="stTextArea"] textarea,
[data-testid="stSelectbox"] > div > div {
    background: var(--bg3) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.9rem !important;
}
[data-testid="stNumberInput"] input:focus,
[data-testid="stTextArea"] textarea:focus {
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 2px rgba(99,210,255,0.12) !important;
    outline: none !important;
}
label, [data-testid="stWidgetLabel"] {
    color: var(--muted2) !important;
    font-size: 0.78rem !important;
    font-weight: 400 !important;
    letter-spacing: 0.04em !important;
    font-family: 'DM Mono', monospace !important;
}
[data-testid="stRadio"] label { color: var(--text) !important; font-family: 'DM Sans', sans-serif !important; font-size: 0.88rem !important; }

/* ── OUTPUT CARD ── */
.output-card {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 2rem 2.2rem;
    margin-top: 1.5rem;
    position: relative;
    overflow: hidden;
}
.output-card.diet-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #0EA5E9, #63D2FF, #0EA5E9);
}
.output-card.exercise-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #7C3AED, #A78BFA, #7C3AED);
}
.output-card-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 1.2rem;
    padding-bottom: 0.8rem;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 0.6rem;
}

/* ── Markdown inside output ── */
.output-card h1, .output-card h2, .output-card h3 {
    font-family: 'Syne', sans-serif !important;
    color: var(--gold) !important;
    margin: 1.4rem 0 0.5rem !important;
}
.output-card.exercise-card h1,
.output-card.exercise-card h2,
.output-card.exercise-card h3 { color: var(--gold2) !important; }
.output-card strong { color: #C4B5FD; }
.output-card.diet-card strong { color: #7DE0FF; }
.output-card ul, .output-card ol { padding-left: 1.4rem; color: var(--muted2); }
.output-card li { margin-bottom: 0.3rem; line-height: 1.75; }
.output-card p { color: var(--muted2); line-height: 1.85; margin-bottom: 0.6rem; }
.output-card table { width: 100%; border-collapse: collapse; margin: 1rem 0; }
.output-card th {
    background: var(--bg3);
    color: var(--gold);
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 0.6rem 0.8rem;
    border: 1px solid var(--border);
    text-align: left;
}
.output-card.exercise-card th { color: var(--gold2); }
.output-card td {
    padding: 0.55rem 0.8rem;
    border: 1px solid var(--border);
    color: var(--muted2);
    font-size: 0.85rem;
}
.output-card tr:hover td { background: rgba(99,210,255,0.03); }

/* ── ALERT ── */
[data-testid="stAlert"] {
    background: rgba(248,113,113,0.08) !important;
    border: 1px solid rgba(248,113,113,0.25) !important;
    border-radius: 8px !important;
    color: #FCA5A5 !important;
}

/* ── DIVIDER ── */
hr { border-color: var(--border) !important; margin: 1.5rem 0 !important; }

/* ── COL GAP ── */
[data-testid="stHorizontalBlock"] { gap: 1.2rem !important; }

/* ── RADIO ── */
[data-testid="stRadio"] > div { gap: 0.4rem !important; flex-direction: row !important; flex-wrap: wrap !important; }
[data-testid="stRadio"] > div > label {
    background: var(--bg3) !important;
    border: 1px solid var(--border) !important;
    border-radius: 6px !important;
    padding: 0.35rem 0.75rem !important;
    cursor: pointer !important;
    transition: all 0.15s !important;
    font-size: 0.82rem !important;
}
[data-testid="stRadio"] > div > label:hover { border-color: var(--border-hi) !important; }

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 999px; }
::-webkit-scrollbar-thumb:hover { background: var(--border-hi); }

/* ── INFO PILL ── */
.info-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    background: rgba(52,211,153,0.08);
    border: 1px solid rgba(52,211,153,0.2);
    border-radius: 6px;
    padding: 0.3rem 0.7rem;
    font-size: 0.72rem;
    color: var(--green);
    font-family: 'DM Mono', monospace;
    margin-bottom: 0.8rem;
}
</style>
""", unsafe_allow_html=True)


# ── Helper: Calculations ──────────────────────────────────────────

def calc_bmi(height_cm: float, weight_kg: float) -> float:
    h = height_cm / 100
    return round(weight_kg / (h * h), 1)

def bmi_category(bmi: float) -> tuple:
    """Returns (label, hex_color, bar_pct, css_class)"""
    if bmi < 18.5:
        return "Underweight", "#60A5FA", min(bmi / 18.5, 1) * 25, "stat-val"
    elif bmi < 25:
        return "Healthy Weight", "#34D399", 25 + (bmi - 18.5) / 6.5 * 30, "stat-val green"
    elif bmi < 30:
        return "Overweight", "#FBBF24", 55 + (bmi - 25) / 5 * 25, "stat-val warn"
    else:
        return "Obese", "#F87171", min(80 + (bmi - 30) / 10 * 20, 100), "stat-val danger"

def calc_bmr(height_cm, weight_kg, age, gender) -> float:
    if gender == "Male":
        return 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    elif gender == "Female":
        return 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    else:
        return 10 * weight_kg + 6.25 * height_cm - 5 * age - 78

ACTIVITY_MULTIPLIERS = {
    "Sedentary (desk job, no exercise)":         1.2,
    "Lightly active (1–3 days/week)":            1.375,
    "Moderately active (3–5 days/week)":         1.55,
    "Very active (6–7 days/week hard training)": 1.725,
    "Athlete / physical labour":                 1.9,
}

def calc_tdee(bmr: float, activity: str) -> int:
    return int(bmr * ACTIVITY_MULTIPLIERS[activity])

def goal_calories(tdee: int, goal: str) -> tuple:
    if goal == "Lose weight (moderate deficit)":
        target = tdee - 400
    elif goal == "Lose weight (aggressive deficit)":
        target = tdee - 700
    elif goal == "Maintain current weight":
        target = tdee
    elif goal == "Gain lean muscle":
        target = tdee + 300
    else:
        target = tdee + 500
    protein_g = int((target * 0.30) / 4)
    carb_g    = int((target * 0.45) / 4)
    fat_g     = int((target * 0.25) / 9)
    return target, protein_g, carb_g, fat_g

def ideal_weight_range(height_cm: float) -> tuple:
    h = height_cm / 100
    low  = round(18.5 * h * h, 1)
    high = round(24.9 * h * h, 1)
    return low, high

def body_fat_estimate(bmi: float, age: int, gender: str) -> float:
    """Deurenberg formula"""
    s = 1 if gender == "Male" else 0
    return round(1.2 * bmi + 0.23 * age - 10.8 * s - 5.4, 1)


# ── Prompt builders ───────────────────────────────────────────────

def build_diet_prompt(height, weight, age, gender, activity, goal,
                      allergies, preferences, cuisine_pref,
                      bmi, bmi_cat, target_cal, protein_g, carb_g, fat_g) -> str:
    allergy_note = f"Strict avoidances: {allergies}" if allergies.strip() else "No known allergies."
    pref_note    = f"Additional preferences / medical notes: {preferences}" if preferences.strip() else ""
    cuisine_note = f"Preferred regional cuisine: {cuisine_pref}" if cuisine_pref else "Mix of regional Indian cuisines."

    return f"""
You are an expert Indian nutritionist and Ayurvedic wellness coach.

## User Profile
- Age: {age} years | Gender: {gender}
- Height: {height} cm | Weight: {weight} kg
- BMI: {bmi} ({bmi_cat})
- Activity level: {activity}
- Goal: {goal}
- Daily calorie target: {target_cal} kcal
- Macro targets — Protein: {protein_g}g | Carbs: {carb_g}g | Fat: {fat_g}g
- Diet type: Strict vegetarian (no meat, no eggs, no fish)
- {cuisine_note}
- {allergy_note}
- {pref_note}

## Your Task
Generate a **complete, practical 7-day Indian vegetarian diet plan**.

### 1. Quick Health Assessment
2–3 sentences summarising the user's current health status and why the plan suits them.

### 2. Daily Macro Breakdown Table
| Meal | Food Items | Approx Calories | Protein (g) | Carbs (g) |

### 3. Full 7-Day Meal Plan (Monday–Sunday)
For each day:
- **🌅 Early Morning** (6–7 AM)
- **🍳 Breakfast** (8–9 AM) — specific Indian dish, portion size in grams/cups
- **🍎 Mid-Morning Snack** (11 AM)
- **🍽️ Lunch** (1–2 PM) — dal, sabzi, roti/rice portions specified
- **☕ Evening Snack** (4–5 PM)
- **🌙 Dinner** (7–8 PM) — lighter meal

Use regional variety. Vary meals daily. Include affordable, seasonal ingredients.

### 4. Hydration Protocol
Specific water intake targets and timing based on goal and activity level.

### 5. Foods to Strictly Avoid
Relevant to their goal and allergies.

### 6. Ayurvedic Tip of the Week
One powerful home remedy using common Indian kitchen ingredients.

### 7. Weekly Grocery List
Organised by category (grains, vegetables, dairy, spices, etc.)

Be specific with portion sizes. Warm, encouraging tone. Use markdown formatting.
""".strip()


def build_exercise_prompt(height, weight, age, gender, activity, goal,
                          bmi, bmi_cat, fitness_level, injuries,
                          equipment, workout_days) -> str:
    injury_note = f"Injuries / limitations: {injuries}" if injuries.strip() else "No known injuries."
    equip_note  = f"Available equipment: {equipment}" if equipment else "No special equipment (bodyweight only)."

    return f"""
You are an elite certified personal trainer and sports nutritionist with expertise in Indian fitness culture.

## Client Profile
- Age: {age} years | Gender: {gender}
- Height: {height} cm | Weight: {weight} kg
- BMI: {bmi} ({bmi_cat})
- Current fitness level: {fitness_level}
- Activity level: {activity}
- Goal: {goal}
- Available workout days per week: {workout_days}
- {equip_note}
- {injury_note}

## Your Task
Generate a **complete, personalised {workout_days}-day/week exercise program** tailored for this person.

### 1. Fitness Assessment
Brief analysis of the client's current fitness profile and realistic expectations.

### 2. Training Principles for This Client
3–4 science-backed principles guiding this program.

### 3. Full Weekly Workout Schedule
For each workout day, provide:

**Day X — [Muscle Group / Focus]**
| Exercise | Sets | Reps/Duration | Rest | Notes |
Include proper warm-up (5 min) and cool-down (5 min) for each session.
Cover compound movements, isolation work, and mobility.

### 4. Rest Day Protocol
Active recovery recommendations for non-training days.

### 5. Progression Plan
How to progress over 4 weeks (Week 1 → Week 4 overload strategy).

### 6. Indian-Context Workout Tips
Practical tips for working out in Indian conditions (heat, limited equipment, time constraints, yoga integration).

### 7. Key Exercises to Avoid
Based on injury history and fitness level.

### 8. 4-Week Milestone Targets
Realistic measurable goals for each week.

Be extremely specific with sets, reps, rest periods, and form cues.
Use markdown tables for workout schedules. Motivating, coach-like tone.
""".strip()


# ── UI: Hero ──────────────────────────────────────────────────────

st.markdown("""
<div class="hero">
    <div class="hero-badge">⚡ v2.0 — Advanced AI Wellness</div>
    <div class="hero-title">Aahar<span class="accent">AI</span> <span class="accent2">+Fit</span></div>
    <div class="hero-sub">Personalised Indian diet plans & AI-generated workout programs — built around your body, your goals, your life.</div>
    <div class="hero-tags">
        <span class="hero-tag">🥗 7-Day Meal Plans</span>
        <span class="hero-tag">💪 Custom Workouts</span>
        <span class="hero-tag">📊 BMI + Macros</span>
        <span class="hero-tag">🧘 Ayurvedic Tips</span>
        <span class="hero-tag">🛒 Grocery Lists</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ── UI: Input form ────────────────────────────────────────────────

st.markdown("<br>", unsafe_allow_html=True)
col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.markdown('<div class="panel"><div class="panel-title">📐 Body Metrics</div>', unsafe_allow_html=True)
    age    = st.number_input("Age (years)", min_value=10, max_value=100, value=25, step=1)
    c1, c2 = st.columns(2)
    with c1:
        height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170, step=1)
    with c2:
        weight = st.number_input("Weight (kg)", min_value=30, max_value=250, value=70, step=1)
    gender = st.selectbox("Biological Sex", ["Male", "Female", "Other"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="panel"><div class="panel-title">🎯 Goals & Activity</div>', unsafe_allow_html=True)
    activity = st.selectbox("Activity Level", list(ACTIVITY_MULTIPLIERS.keys()))
    goal = st.selectbox("Primary Goal", [
        "Lose weight (moderate deficit)",
        "Lose weight (aggressive deficit)",
        "Maintain current weight",
        "Gain lean muscle",
        "Gain weight (bulking)",
    ])
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    # ── Live stats panel ──────────────────────────────────────────
    if height > 0 and weight > 0 and age > 0:
        bmi = calc_bmi(height, weight)
        bmi_cat, bmi_color, bar_pct, bmi_css = bmi_category(bmi)
        bmr  = calc_bmr(height, weight, age, gender)
        tdee = calc_tdee(bmr, activity)
        target_cal, protein_g, carb_g, fat_g = goal_calories(tdee, goal)
        iw_low, iw_high = ideal_weight_range(height)
        bf_est = body_fat_estimate(bmi, age, gender)

        st.markdown(f"""
        <div class="panel">
        <div class="panel-title">📊 Live Health Snapshot</div>
        <div class="stat-grid">
            <div class="stat-box">
                <div class="{bmi_css}" style="color:{bmi_color}">{bmi}</div>
                <div class="stat-lbl">BMI · {bmi_cat}</div>
            </div>
            <div class="stat-box">
                <div class="stat-val">{tdee}</div>
                <div class="stat-lbl">Maintenance kcal</div>
            </div>
            <div class="stat-box">
                <div class="stat-val green">{target_cal}</div>
                <div class="stat-lbl">Target kcal</div>
            </div>
            <div class="stat-box">
                <div class="stat-val purple">{bf_est}%</div>
                <div class="stat-lbl">Est. Body Fat</div>
            </div>
            <div class="stat-box">
                <div class="stat-val" style="font-size:1.1rem">{iw_low}–{iw_high}</div>
                <div class="stat-lbl">Ideal Weight (kg)</div>
            </div>
            <div class="stat-box">
                <div class="stat-val" style="font-size:1.15rem">{int(bmr)}</div>
                <div class="stat-lbl">BMR (kcal)</div>
            </div>
        </div>
        <div style="margin: 0.8rem 0 0.3rem">
            <div style="font-size:0.65rem; color:var(--muted); font-family:'DM Mono',monospace; margin-bottom:0.3rem">BMI SCALE</div>
            <div class="bmi-track">
                <div class="bmi-fill" style="width:{bar_pct}%;background:{bmi_color};"></div>
            </div>
            <div class="bmi-labels"><span>Underweight</span><span>Normal</span><span>Overweight</span><span>Obese</span></div>
        </div>
        <div style="margin-top:1rem; font-size:0.65rem; color:var(--muted); font-family:'DM Mono',monospace; margin-bottom:0.4rem">MACRO TARGETS</div>
        <div class="macro-row">
            <div class="macro-item">
                <div class="macro-val" style="color:#63D2FF">{protein_g}g</div>
                <div class="macro-lbl">Protein</div>
            </div>
            <div class="macro-item">
                <div class="macro-val" style="color:#FBBF24">{carb_g}g</div>
                <div class="macro-lbl">Carbs</div>
            </div>
            <div class="macro-item">
                <div class="macro-val" style="color:#F472B6">{fat_g}g</div>
                <div class="macro-lbl">Fats</div>
            </div>
        </div>
        </div>
        """, unsafe_allow_html=True)

        # store for use below
        st.session_state["_bmi"]        = bmi
        st.session_state["_bmi_cat"]    = bmi_cat
        st.session_state["_bmi_color"]  = bmi_color
        st.session_state["_tdee"]       = tdee
        st.session_state["_target_cal"] = target_cal
        st.session_state["_protein_g"]  = protein_g
        st.session_state["_carb_g"]     = carb_g
        st.session_state["_fat_g"]      = fat_g
    else:
        st.info("Fill in your body metrics to see your live health snapshot.")

    # ── Health Notes ──────────────────────────────────────────────
    st.markdown('<div class="panel"><div class="panel-title">🩺 Health Notes</div>', unsafe_allow_html=True)
    allergies = st.text_area(
        "Allergies or foods to avoid",
        placeholder="e.g. peanuts, dairy, gluten, high-sugar foods…",
        height=80,
    )
    preferences = st.text_area(
        "Medical conditions / extra preferences (optional)",
        placeholder="e.g. Type 2 diabetes, PCOS, high BP, thyroid…",
        height=80,
    )
    cuisine_pref = st.selectbox("Preferred Regional Cuisine", [
        "Mixed (North + South Indian)",
        "North Indian (Punjabi, UP, Delhi)",
        "South Indian (Tamil, Kerala, Andhra)",
        "West Indian (Gujarati, Maharashtrian)",
        "East Indian (Bengali, Odia)",
        "Continental / Fusion",
    ])
    st.markdown('</div>', unsafe_allow_html=True)


# ── Exercise section ──────────────────────────────────────────────

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div class="panel"><div class="panel-title">💪 Exercise Preferences</div>', unsafe_allow_html=True)

ex_col1, ex_col2, ex_col3 = st.columns(3)
with ex_col1:
    fitness_level = st.selectbox("Current Fitness Level", [
        "Complete Beginner",
        "Beginner (< 6 months training)",
        "Intermediate (6 months–2 years)",
        "Advanced (2+ years)",
        "Athlete",
    ])
with ex_col2:
    equipment = st.selectbox("Available Equipment", [
        "No equipment (bodyweight only)",
        "Resistance bands",
        "Dumbbells at home",
        "Full home gym",
        "Commercial gym access",
    ])
with ex_col3:
    workout_days = st.selectbox("Workout Days / Week", [3, 4, 5, 6], index=1)

injuries = st.text_input(
    "Injuries or physical limitations (optional)",
    placeholder="e.g. knee pain, lower back issues, shoulder injury…"
)
st.markdown('</div>', unsafe_allow_html=True)


# ── Action buttons ────────────────────────────────────────────────

btn_col1, btn_col2 = st.columns(2)
with btn_col1:
    gen_diet = st.button("🥗 Generate 7-Day Diet Plan", use_container_width=True)
with btn_col2:
    gen_exercise = st.button("💪 Generate Exercise Program", use_container_width=True)


# ── Diet Plan generation ──────────────────────────────────────────

if gen_diet:
    if not (height and weight and age):
        st.error("Please fill in height, weight, and age before generating.")
    else:
        bmi        = st.session_state.get("_bmi", calc_bmi(height, weight))
        bmi_cat    = st.session_state.get("_bmi_cat", bmi_category(bmi)[0])
        tdee       = st.session_state.get("_tdee", 0)
        target_cal = st.session_state.get("_target_cal", tdee)
        protein_g  = st.session_state.get("_protein_g", 0)
        carb_g     = st.session_state.get("_carb_g", 0)
        fat_g      = st.session_state.get("_fat_g", 0)

        if tdee == 0:
            bmr        = calc_bmr(height, weight, age, gender)
            tdee       = calc_tdee(bmr, activity)
            target_cal, protein_g, carb_g, fat_g = goal_calories(tdee, goal)

        prompt = build_diet_prompt(
            height, weight, age, gender, activity, goal,
            allergies, preferences, cuisine_pref,
            bmi, bmi_cat, target_cal, protein_g, carb_g, fat_g,
        )

        st.markdown('<div class="output-card diet-card"><div class="output-card-title">🥗 Your Personalised 7-Day Diet Plan</div>', unsafe_allow_html=True)
        output_area = st.empty()
        full_response = ""

        try:
            stream = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an expert Indian nutritionist, Ayurvedic wellness coach, and registered dietitian. "
                            "You give detailed, practical, warm dietary advice rooted in Indian culinary traditions. "
                            "Always use markdown formatting with clear headers, tables, and bullet points. "
                            "Be specific with portions in grams or cups. Include regional Indian dishes."
                        ),
                    },
                    {"role": "user", "content": prompt},
                ],
                model="llama-3.3-70b-versatile",
                temperature=0.45,
                max_tokens=4000,
                stream=True,
            )

            for chunk in stream:
                delta = chunk.choices[0].delta.content or ""
                full_response += delta
                output_area.markdown(full_response + "▌")

            output_area.markdown(full_response)

        except Exception as e:
            st.error(f"Error generating diet plan: {e}")

        st.markdown('</div>', unsafe_allow_html=True)


# ── Exercise Program generation ───────────────────────────────────

if gen_exercise:
    if not (height and weight and age):
        st.error("Please fill in height, weight, and age before generating.")
    else:
        bmi     = st.session_state.get("_bmi", calc_bmi(height, weight))
        bmi_cat = st.session_state.get("_bmi_cat", bmi_category(bmi)[0])

        prompt = build_exercise_prompt(
            height, weight, age, gender, activity, goal,
            bmi, bmi_cat, fitness_level, injuries,
            equipment, workout_days,
        )

        st.markdown('<div class="output-card exercise-card"><div class="output-card-title">💪 Your Personalised Exercise Program</div>', unsafe_allow_html=True)
        output_area = st.empty()
        full_response = ""

        try:
            stream = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an elite certified personal trainer (NASM-CPT, CSCS), sports nutritionist, "
                            "and movement specialist with 15+ years experience training clients in India. "
                            "You design science-backed, progressive workout programs with precise sets, reps, rest, "
                            "and form cues. Use markdown tables for schedules. Be motivating and coach-like. "
                            "Always include warm-up and cool-down. Adapt for Indian context."
                        ),
                    },
                    {"role": "user", "content": prompt},
                ],
                model="llama-3.3-70b-versatile",
                temperature=0.42,
                max_tokens=4000,
                stream=True,
            )

            for chunk in stream:
                delta = chunk.choices[0].delta.content or ""
                full_response += delta
                output_area.markdown(full_response + "▌")

            output_area.markdown(full_response)

        except Exception as e:
            st.error(f"Error generating exercise program: {e}")

        st.markdown('</div>', unsafe_allow_html=True)


# ── Footer ────────────────────────────────────────────────────────

st.markdown("""
<hr>
<div style="text-align:center; padding: 1.5rem 0; color: var(--muted); font-family:'DM Mono',monospace; font-size:0.65rem; letter-spacing:0.1em;">
    AAHAR<span style="color:var(--gold)">AI</span> v2.0 &nbsp;·&nbsp; FOR INFORMATIONAL PURPOSES ONLY &nbsp;·&nbsp; CONSULT A DOCTOR BEFORE MAJOR DIETARY CHANGES
</div>
""", unsafe_allow_html=True)
