# 🎬 Netflix Data Analysis Project

This is a beginner-friendly data analysis project using real Netflix data. The project explores trends in Netflix's content over time, types of content, country and genre distributions, and more — all using Python, Pandas, and Matplotlib.

---

## 📁 Dataset

The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows) and includes information about movies and TV shows available on Netflix as of 2021. It contains the following columns:

- `show_id`
- `type` (Movie/TV Show)
- `title`
- `director`
- `cast`
- `country`
- `date_added`
- `release_year`
- `rating`
- `duration`
- `listed_in` (Genres)
- `description`

---

## 📊 What This Project Does

- Loads and cleans Netflix data using Pandas
- Visualizes:
  - Distribution of Movies vs TV Shows
  - Growth of content over time
  - Top 10 content-producing countries
  - Top 10 genres on Netflix
- Uses:
  - `pandas` for data manipulation
  - `matplotlib` for visualization
  - `numpy` for numerical operations

---

## 📦 Requirements

Make sure you have Python 3.8+ installed. Then install the required libraries:

```bash
python3 -m venv venv
source venv/bin/activate
pip install pandas matplotlib numpy
```
