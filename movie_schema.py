import kuzu

# 🎥 Creating movie database
db = kuzu.Database("movie_db")
conn = kuzu.Connection(db)

# 👤 User Node Table
conn.execute("""
CREATE NODE TABLE User(
    name STRING,
    age INT64,
    PRIMARY KEY(name)
)
""")

# 🎞️ Movie Node Table
conn.execute("""
CREATE NODE TABLE Movie(
    name STRING,
    year INT64,
    PRIMARY KEY(name)
)
""")

# 🎭 Genre Node Table
conn.execute("""
CREATE NODE TABLE Genre(
    name STRING,
    PRIMARY KEY(name)
)
""")

# ❤️ User likes Genre
conn.execute("""
CREATE REL TABLE LIKES(
    FROM User TO Genre
)
""")

# 🎬 Movie belongs to Genre
conn.execute("""
CREATE REL TABLE BELONGS_TO(
    FROM Movie TO Genre
)
""")

# 👀 User watched Movie
conn.execute("""
CREATE REL TABLE WATCHED(
    FROM User TO Movie
)
""")

print("✅ Schema created successfully 🎉")