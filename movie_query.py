import kuzu

# 🎥 Connecting to database
db = kuzu.Database("movie_db")
conn = kuzu.Connection(db)

# 🔍 Recommendation Query For ALL Users
result = conn.execute("""
MATCH (u:User)-[:LIKES]->(g:Genre)<-[:BELONGS_TO]-(m:Movie)
WHERE NOT EXISTS {
    MATCH (u)-[:WATCHED]->(m)
}
RETURN u.name, m.name
""")

print("🎬 Movie Recommendations For Users 🍿\n")

# 📢 Printing recommendations
while result.has_next():
    row = result.get_next()

    user_name = row[0]
    movie_name = row[1]

    print(f"👤 {user_name} ➜ ⭐ {movie_name}")