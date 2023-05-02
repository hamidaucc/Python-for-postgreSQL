import psycopg2  as p

conn = p.connect(host="localhost",database="user" ,user="user" ,password="123", port="5432")
cursor=conn.cursor()
"""
cursor.execute('''CREATE TABLE store
               (Id INT PRIMARY KEY,
               City TEXT,
               Category TEXT,
               SubCategory TEXT,
               Sales REAL,
               Quantity INT, 
               Discount REAL,
               Profit REAL);'''
            )
"""

def create_table(curson):
    cursor.execute("""DROP TABLE IF EXISTS staging_beers;
        CREATE UNLOGGED TABLE staging_beers (
            id                  INTEGER,
            name                TEXT,
            tagline             TEXT,
            first_brewed        DATE,
            description         TEXT,
            image_url           TEXT,
            abv                 DECIMAL,
            ibu                 DECIMAL,
            target_fg           DECIMAL,
            target_og           DECIMAL,
            ebc                 DECIMAL,
            srm                 DECIMAL,
            ph                  DECIMAL,
            attenuation_level   DECIMAL,
            brewers_tips        TEXT,
            contributed_by      TEXT,
            volume              INTEGER
        );
    """)
with cursor as C:
    create_table(C)
    print("Done")
cursor.execute('''SELECT * FROM users;''')
conn.commit()
conn.close()

