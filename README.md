# 🧮 Population Sample Size Calculator


![Built With](https://img.shields.io/badge/Built%20With-Excel%20%2B%20Python-06b6d4?style=flat&labelColor=333)
![Libraries](https://img.shields.io/badge/Libraries-Pandas%20%7C%20Seaborn%20%7C%20SciPy-6366f1?style=flat&labelColor=333)
![Visualization](https://img.shields.io/badge/Visualization-Seaborn%20Heatmap-9333ea?style=flat&labelColor=333)
![Status](https://img.shields.io/badge/Status-Complete-facc15?style=flat&labelColor=333)
![Use Case](https://img.shields.io/badge/Use%20Case-Surveys%20%26%20A%2FB%20Testing-14b8a6?style=flat&labelColor=333)
![Validation](https://img.shields.io/badge/Validation-Python%20Benchmarking-3b82f6?style=flat&labelColor=333)
![License](https://img.shields.io/badge/License-Apache%202.0-f59e0b?style=flat&labelColor=333)




*A practical tool for analysts, researchers, and product teams to determine how many responses are needed for reliable insights.*

---

### 🧩 Overview

> "How many people do I really need to survey?"

This project answers that question by building a dynamic sample size calculator in Excel using foundational statistical formulas. It helps users calculate required sample sizes based on margin of error, population size, and confidence level — and visualizes how these factors interact through a color-coded heatmap.

---

### 🔧 Key Features

- ✅ Calculates required **sample size for both infinite and finite populations**
- ✅ Supports dynamic inputs for:
    - Confidence level (Z)
    - Margin of error (E)
    - Estimated proportion (p)
    - Total population (N)
- 🔐 Formula cells are locked and protected
- 📊 Includes an interactive **heatmap visualization**
- 📉 Includes a reference table validated against Python output

---

### 📈 Heatmap: Sample Size by Precision and Population

> The heatmap shows how sample size needs increase with lower margins of error and higher population sizes.

🟥 = Fewer responses required (lower accuracy)  
🟨 = Moderate response requirement  
🟩 = High sample size needed (high precision)  

📌 Even for very large populations, the required sample size levels off — a powerful insight for cost-conscious teams.

![Sample Size Heatmap](https://user-images.githubusercontent.com/your-github-image-link.png)

---

### 🔢 Formulas Used

#### Infinite Population (m):

```
m = (Z^2 * p * (1 - p)) / E^2
```

#### Finite Population (n):

```
n = m / (1 + ((m - 1) / N))
```

Where:

- `Z` = Z-score (e.g., 1.96 for 95% confidence)
- `p` = Estimated proportion (0.5 = maximum variability)
- `E` = Margin of error
- `N` = Total population

---

### 🧠 What I Learned

- How to translate statistical methods into business-friendly Excel tools
- Best practices for modeling finite population correction
- How to validate Excel models using Python
- Designing for usability and data communication (heatmaps, locking, etc.)

---

### 🧪 Use Cases

- Market research & surveys
- A/B testing sample validation
- UX and user research
- Political polling & field data collection
- Budgeting for statistically valid outreach

---

### 🧰 Tools Used

- Microsoft Excel (dynamic calculator, heatmap formatting)
- Python (validation and benchmarking)
- Notion (documentation & publishing)

---

### 📁 Project Files

- 📥 [Download Excel Calculator (.xlsx)](https://docs.google.com/spreadsheets/d/1yiLE44kDklfP7Qfb3cO3dCF2az3FW4_5/edit?usp=drive_link)
- 🐍 [Python Validation Script (.ipynb)](https://github.com/your-repo-link/sample-size-validation.ipynb)
- 📊 [Reference Table PDF](https://drive.google.com/file/d/1tbnXN10hiLPEzjtRT4Lv7r5rCNTPEp9N/view?usp=drive_link)
