from database import get_connection

CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS paises (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    capital VARCHAR(255),
    region VARCHAR(100),
    population BIGINT
);
"""

INSERT_COUNTRY_QUERY = """
INSERT INTO paises (name, capital, region, population)
VALUES (%s, %s, %s, %s)
"""

def save_countries(rows):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(CREATE_TABLE_QUERY)

    for country in rows:
        cursor.execute(INSERT_COUNTRY_QUERY, country)

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ Países insertados correctamente en la base de datos")
