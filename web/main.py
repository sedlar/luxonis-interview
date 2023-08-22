from aiohttp import web
import psycopg2
import aiohttp_jinja2
import jinja2

DB_DSN = "postgresql://postgres:postgres@db/db"


@aiohttp_jinja2.template("sell_flats.jinja2")
async def show_sell_flats(_):
    connection = psycopg2.connect(DB_DSN)
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT title, image_url FROM flats")
        rows = cursor.fetchall()
        offers = [{"title": title, "image_url": image_url} for title, image_url in rows]
        return {"offers": offers}
    finally:
        if connection:
            connection.close()


app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("templates"))
app.add_routes([web.get("/", show_sell_flats)])

if __name__ == "__main__":
    web.run_app(app)
