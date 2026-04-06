# 📋 Quick Entry — Sheet Filler

A lightweight Streamlit app that extracts information from a customer message and lets you copy it as a single row directly into Google Sheets. No API, no database, no login required.

---

## What It Does

1. You paste a customer reply into the text box
2. Click **Parse & Extract** — the app reads each field automatically
3. Review and fix any fields if needed
4. Copy the **Data row** and paste it into Google Sheets — each field lands in its own column

---

## Requirements

- Python 3.10 or newer
- Streamlit

---

## Installation

### 1. Download the files

Make sure you have both files in the same folder:

```
your-folder/
├── app.py
└── requirements.txt
```

If you do not have `requirements.txt`, create one with this content:

```
streamlit>=1.32.0
```

---

### 2. Create a virtual environment

Open your terminal, navigate to the folder, then run:

**Windows:**
```bash
cd path\to\your-folder
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux:**
```bash
cd path/to/your-folder
python -m venv venv
source venv/bin/activate
```

You will see `(venv)` appear at the start of your terminal prompt. This means the virtual environment is active.

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the app

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

To stop the app, press `Ctrl+C` in the terminal.

---

## How to Use

### Step 1 — Paste the customer message
Copy the customer's reply and paste it into the left text box. The app works best when the reply follows this format:

```
Name: Ahmad
Company: ABC Sdn Bhd
Product type: Water tank
Quantity: 500
Location: Selangor
Timeline/Urgency: 6 weeks
Customisation: Yes
```

### Step 2 — Click Parse & Extract
The 7 fields on the right will fill in automatically.

### Step 3 — Review and edit
If any field is wrong or missing, click into it and type the correct value.

### Step 4 — Copy the Data row
Scroll down to the **Data row** box:
- Click inside it
- Press `Ctrl+A` to select all
- Press `Ctrl+C` to copy

### Step 5 — Paste into Google Sheets
- Open your Google Sheet
- Click the first empty cell in the next empty row
- Press `Ctrl+V`

Each field will land in its own column automatically.

> **First time only:** Copy the **Header row** and paste it into row 1 of your sheet to set up the column headers.

---

## Fields Captured

| Column | Description |
|---|---|
| Name | Customer's name |
| Company | Company or organisation name |
| Product type | Type of product enquired about |
| Quantity | Number of units requested |
| Location | Customer's location |
| Timeline/Urgency | Delivery timeframe or urgency level |
| Customisation | Whether customisation is needed (Yes / No) |

---

## Tips

- If the customer replied in a freeform paragraph instead of the structured format, just type the values manually into the fields on the right — then copy the row as usual.
- Use the **Clear All** button to reset all fields before entering a new customer.
- The Data row updates live as you edit the fields — no need to click anything after editing.

---

## Troubleshooting

**Fields are empty after clicking Parse & Extract**
The message format does not match. Each field must be on its own line followed by a colon, e.g. `Name: Ahmad`. If the reply is a paragraph, fill in the fields manually.

**Data row is empty**
Make sure you have filled in at least one field. The data row reflects whatever is currently in the fields.

**'streamlit' is not recognised**
Your virtual environment is not active. Run the `activate` command again before running `streamlit run app.py`.

**App does not open in the browser**
Manually open your browser and go to `http://localhost:8501`.