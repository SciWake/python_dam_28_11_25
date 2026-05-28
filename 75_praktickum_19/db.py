def create_database(connection):
    db_name = "hh_data"
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`;")

    return db_name


def create_table(connection):
    with connection.cursor() as cursor:
        query = """
        CREATE TABLE IF NOT EXISTS info (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(150) NOT NULL,
            company VARCHAR(150),
            url VARCHAR(500) NOT NULL UNIQUE
        )
        """
        cursor.execute(query)


def insert_data(connection, data: list[tuple]):
    with connection.cursor() as cursor:
        query = """
        INSERT IGNORE INTO info (title, company, url) VALUES (%s, %s, %s);
        """
        cursor.executemany(query, data)
    connection.commit()
