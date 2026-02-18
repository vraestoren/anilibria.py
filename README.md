<div align="center">

# anilibria.py
<img src="https://anilibria.app/res/images/og_image.jpg?1598792059" width="400"/>

An Web-API for the [AniLibria](https://www.anilibria.tv) API — a Russian anime streaming platform.

</div>

## Quick Start
```python
import anilibria

client = anilibria.Anilibria()
client.login(email="example@gmail.com", password="password")
```

## Usage

#### Search & Browse
```python
# Search for anime
client.search_anime(search="Наруто")

# Get anime catalog filtered by year and genre
client.get_catalog(year=2023, genre="Экшен", season="winter")

# Get a random title
client.get_random_title()

# Get recent updates
client.get_updates(filter="names,posters", limit=10)

# Get schedule by day (0 = Monday, 6 = Sunday)
client.get_schedule(days=0)
```

#### Favorites
```python
# Get, add, or remove favorites (requires session)
client.get_favorite_titles(session="your_session_id")
client.add_title_to_favorites(session="your_session_id", title_id=123)
client.delete_title_from_favorites(session="your_session_id", title_id=123)
```

#### Misc
```python
client.get_feed()
client.get_youtube_videos(limit=5)
client.get_team()
client.get_rss(rss_type="rss")
```
