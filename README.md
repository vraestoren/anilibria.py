<div align="center">

# anilibria.py
<img src="https://anilibria.app/res/images/og_image.jpg?1598792059" width="400"/>

An Web-API for the [AniLibria](https://www.anilibria.tv) API — a Russian anime streaming platform.

</div>

## Quick Start
```python
from anilibria import Anilibria

anilibria = Anilibria()
anilibria.login(email="example@gmail.com", password="password")
```

## Usage

#### Search & Browse
```python
# Search for anime
anilibria.search_anime(search="Наруто")

# Get anime catalog filtered by year and genre
anilibria.get_catalog(year=2023, genre="Экшен", season="winter")

# Get a random title
anilibria.get_random_title()

# Get recent updates
anilibria.get_updates(filter="names,posters", limit=10)

# Get schedule by day (0 = Monday, 6 = Sunday)
anilibria.get_schedule(days=0)
```

#### Favorites
```python
# Get, add, or remove favorites (requires session)
anilibria.get_favorite_titles(session="")
anilibria.add_title_to_favorites(session="", title_id=123)
anilibria.delete_title_from_favorites(session="", title_id=123)
```

#### Misc
```python
anilibria.get_feed()
anilibria.get_youtube_videos(limit=5)
anilibria.get_team()
anilibria.get_rss(rss_type="rss")
```
