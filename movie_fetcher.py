# Simulated version. Later, we’ll use pyrogram to fetch from @Premiummovies0_bot
async def get_movies_from_source(query):
    return [
        {"id": "101", "title": f"{query} 720p"},
        {"id": "102", "title": f"{query} 1080p"},
    ]
