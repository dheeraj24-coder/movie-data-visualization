import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# Load Dataset
# ==========================
df = pd.read_csv("movies.csv")

# ==========================
# Data Cleaning
# ==========================
df["imdb_rating"] = pd.to_numeric(df["imdb_rating"], errors="coerce")
df["year_of_release"] = pd.to_numeric(df["year_of_release"], errors="coerce")

df = df.dropna(subset=["imdb_rating", "year_of_release"])

# ==========================
# Create Figure
# ==========================
fig, ax = plt.subplots(2, 2, figsize=(18, 12))

# Full Background Color
fig.patch.set_facecolor("lightcyan")

# =====================================================
# 1. LINE CHART
# Average IMDb Rating by Year
# =====================================================
line_data = (
    df.groupby("year_of_release")["imdb_rating"]
    .mean()
    .sort_index()
)

ax[0,0].set_facecolor("lavender")

ax[0,0].plot(
    line_data.index,
    line_data.values,
    color="blue",
    marker="o",
    linewidth=3
)

ax[0,0].set_title("Average IMDb Rating by Year",
                  fontsize=14,
                  fontweight="bold")

ax[0,0].set_xlabel("Year")
ax[0,0].set_ylabel("IMDb Rating")
ax[0,0].grid(True)



# =====================================================
# 2. BAR CHART
# Top 10 Highest Rated Movies
# =====================================================
top_movies = df.nlargest(10, "imdb_rating")

bar_colors = [
    "red",
    "green",
    "blue",
    "orange",
    "purple",
    "pink",
    "gold",
    "cyan",
    "brown",
    "teal"
]

ax[0,1].set_facecolor("honeydew")

ax[0,1].bar(
    top_movies["title_x"],
    top_movies["imdb_rating"],
    color=bar_colors
)

ax[0,1].set_title("Top 10 Highest Rated Movies",
                  fontsize=14,
                  fontweight="bold")

ax[0,1].set_xlabel("Movies")
ax[0,1].set_ylabel("IMDb Rating")

plt.setp(ax[0,1].get_xticklabels(),
         rotation=60,
         ha="right")



# =====================================================
# 3. PIE CHART
# Top 6 Genres
# =====================================================
genre_counts = (
    df["genres"]
    .str.split(",")
    .explode()
    .str.strip()
    .value_counts()
    .head(6)
)

pie_colors = [
    "red",
    "blue",
    "green",
    "orange",
    "purple",
    "gold"
]

ax[1,0].set_facecolor("mistyrose")

ax[1,0].pie(
    genre_counts.values,
    labels=genre_counts.index,
    colors=pie_colors,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True
)

ax[1,0].set_title("Top Movie Genres",
                  fontsize=14,
                  fontweight="bold")



# =====================================================
# 4. DONUT CHART
# Adult vs Non Adult Movies
# =====================================================
adult = (
    df["is_adult"]
    .replace({0: "Non Adult", 1: "Adult"})
    .value_counts()
)

donut_colors = ["green", "tomato"]

ax[1,1].set_facecolor("lightyellow")

ax[1,1].pie(
    adult.values,
    labels=adult.index,
    colors=donut_colors,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True,
    wedgeprops={"width":0.45}
)

centre_circle = plt.Circle((0,0),0.60,color="white")
ax[1,1].add_artist(centre_circle)

ax[1,1].set_title("Adult vs Non Adult Movies",
                  fontsize=14,
                  fontweight="bold")



# =====================================================
# Dashboard Title
# =====================================================
plt.suptitle(
    "Movie Dataset Dashboard",
    fontsize=20,
    fontweight="bold",
    color="darkblue"
)

plt.tight_layout(rect=[0,0,1,0.96])

plt.show()
