import psycopg2

DB_DSN = "postgresql://postgres:postgres@db/db"


class SrealityPipeline:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def open_spider(self, _):
        self.connection = psycopg2.connect(DB_DSN)
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM FLATS;")

    def process_item(self, item, _):
        self.cursor.execute(
            "INSERT INTO flats (title, image_url) VALUES(%s, %s);",
            (
                item.title,
                item.image_url,
            ),
        )
        self.connection.commit()

    def close_spider(self, _):
        if self.connection:
            self.connection.close()
