import kuzu

# 🎥 Connecting to database
db = kuzu.Database("movie_db")
conn = kuzu.Connection(db)

# 👤 Users
conn.execute("""
MERGE (:User {
    name:'Abhijith',
    age:21
})
""")

conn.execute("""
MERGE (:User {
    name:'Rahul',
    age:23
})
""")

conn.execute("""
MERGE (:User {
    name:'Priya',
    age:22
})
""")

conn.execute("""
MERGE (:User {
    name:'Arjun',
    age:24
})
""")

conn.execute("""
MERGE (:User {
    name:'Sneha',
    age:20
})
""")

# 🎭 Genres
conn.execute("""
MERGE (:Genre {
    name:'Sci-Fi'
})
""")

conn.execute("""
MERGE (:Genre {
    name:'Action'
})
""")

conn.execute("""
MERGE (:Genre {
    name:'Drama'
})
""")

conn.execute("""
MERGE (:Genre {
    name:'Comedy'
})
""")

conn.execute("""
MERGE (:Genre {
    name:'Thriller'
})
""")

# 🎬 Movies
conn.execute("""
MERGE (:Movie {
    name:'Interstellar',
    year:2014
})
""")

conn.execute("""
MERGE (:Movie {
    name:'Inception',
    year:2010
})
""")

conn.execute("""
MERGE (:Movie {
    name:'John Wick',
    year:2014
})
""")

conn.execute("""
MERGE (:Movie {
    name:'The Prestige',
    year:2006
})
""")

conn.execute("""
MERGE (:Movie {
    name:'Avengers Endgame',
    year:2019
})
""")

conn.execute("""
MERGE (:Movie {
    name:'Titanic',
    year:1997
})
""")

conn.execute("""
MERGE (:Movie {
    name:'The Hangover',
    year:2009
})
""")

conn.execute("""
MERGE (:Movie {
    name:'Shutter Island',
    year:2010
})
""")

conn.execute("""
MERGE (:Movie {
    name:'Iron Man',
    year:2008
})
""")

conn.execute("""
MERGE (:Movie {
    name:'Joker',
    year:2019
})
""")

conn.execute("""
MERGE (:Movie {
    name:'Batman Begins',
    year:2005
})
""")

# ❤️ Users Like Genres

conn.execute("""
MATCH (u:User), (g:Genre)
WHERE u.name='Abhijith' AND g.name='Sci-Fi'
MERGE (u)-[:LIKES]->(g)
""")

conn.execute("""
MATCH (u:User), (g:Genre)
WHERE u.name='Rahul' AND g.name='Action'
MERGE (u)-[:LIKES]->(g)
""")

conn.execute("""
MATCH (u:User), (g:Genre)
WHERE u.name='Priya' AND g.name='Drama'
MERGE (u)-[:LIKES]->(g)
""")

conn.execute("""
MATCH (u:User), (g:Genre)
WHERE u.name='Arjun' AND g.name='Thriller'
MERGE (u)-[:LIKES]->(g)
""")

conn.execute("""
MATCH (u:User), (g:Genre)
WHERE u.name='Sneha' AND g.name='Comedy'
MERGE (u)-[:LIKES]->(g)
""")

# 🎞️ Movies belong to Genres

conn.execute("""
MATCH (m:Movie), (g:Genre)
WHERE m.name='Interstellar' AND g.name='Sci-Fi'
MERGE (m)-[:BELONGS_TO]->(g)
""")

conn.execute("""
MATCH (m:Movie), (g:Genre)
WHERE m.name='Inception' AND g.name='Sci-Fi'
MERGE (m)-[:BELONGS_TO]->(g)
""")

conn.execute("""
MATCH (m:Movie), (g:Genre)
WHERE m.name='John Wick' AND g.name='Action'
MERGE (m)-[:BELONGS_TO]->(g)
""")

conn.execute("""
MATCH (m:Movie), (g:Genre)
WHERE m.name='Avengers Endgame' AND g.name='Action'
MERGE (m)-[:BELONGS_TO]->(g)
""")

conn.execute("""
MATCH (m:Movie), (g:Genre)
WHERE m.name='Titanic' AND g.name='Drama'
MERGE (m)-[:BELONGS_TO]->(g)
""")

conn.execute("""
MATCH (m:Movie), (g:Genre)
WHERE m.name='The Prestige' AND g.name='Drama'
MERGE (m)-[:BELONGS_TO]->(g)
""")

conn.execute("""
MATCH (m:Movie), (g:Genre)
WHERE m.name='The Hangover' AND g.name='Comedy'
MERGE (m)-[:BELONGS_TO]->(g)
""")

conn.execute("""
MATCH (m:Movie), (g:Genre)
WHERE m.name='Shutter Island' AND g.name='Thriller'
MERGE (m)-[:BELONGS_TO]->(g)
""")

conn.execute("""
MATCH (m:Movie), (g:Genre)
WHERE m.name='Iron Man' AND g.name='Action'
MERGE (m)-[:BELONGS_TO]->(g)
""")

conn.execute("""
MATCH (m:Movie), (g:Genre)
WHERE m.name='Joker' AND g.name='Drama'
MERGE (m)-[:BELONGS_TO]->(g)
""")

# 👀 Users Watched Movies

conn.execute("""
MATCH (u:User), (m:Movie)
WHERE u.name='Abhijith' AND m.name='Interstellar'
MERGE (u)-[:WATCHED]->(m)
""")

conn.execute("""
MATCH (u:User), (m:Movie)
WHERE u.name='Rahul' AND m.name='John Wick'
MERGE (u)-[:WATCHED]->(m)
""")

conn.execute("""
MATCH (u:User), (m:Movie)
WHERE u.name='Priya' AND m.name='Titanic'
MERGE (u)-[:WATCHED]->(m)
""")

conn.execute("""
MATCH (u:User), (m:Movie)
WHERE u.name='Arjun' AND m.name='Shutter Island'
MERGE (u)-[:WATCHED]->(m)
""")

conn.execute("""
MATCH (u:User), (m:Movie)
WHERE u.name='Sneha' AND m.name='The Hangover'
MERGE (u)-[:WATCHED]->(m)
""")

print("✅ Movie Data Inserted Successfully 🎉🍿")