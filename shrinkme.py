import httpx
from config import SHRINKME_API_KEY

async def generate_shortlink(user_id):
    url = f"https://shrinkme.io/api?api={SHRINKME_API_KEY}&url=https://t.me/rozimoviebot&alias=verify_{user_id}"
    async with httpx.AsyncClient() as client:
        res = await client.get(url)
        data = res.json()
        return data["shortenedUrl"]
