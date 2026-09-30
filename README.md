# Puppy Health & Activity Tracker

A lightweight Python script using **pandas** to monitor, analyze, and report daily puppy health metrics, activity levels, and growth trends.

---

# Features

- **Automated Calculations:** Computes average daily walk time, nap frequency, and weekly weight trends.
- **Conditional Tagging:** Uses `numpy.where` to classify days as *Active* or *Chill* based on exercise thresholds.
- **Activity Filtering:** Quickly identifies low-exercise days to adjust routines.
- **CSV Export:** Generates a structured summary report (`puppy_weekly_report.csv`) compatible with Excel and Google Sheets.

---

# Tech Stack

- **Language:** Python 3.x
- **Libraries:** `pandas`, `numpy`

---

# Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/puppy-health-tracker.git](https://github.com/your-username/puppy-health-tracker.git)
   cd puppy-health-tracker
