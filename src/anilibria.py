from random import choices
from requests import Session, Response

class Anilibria:
	def __init__(self) -> None:
		self.api = "https://api.anilibria.tv"
		self.public_api = "https://www.anilibria.tv/public"
		self.session_id = None
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
			"X-Requested-With": "XMLHttpRequest"
		}

	def _post(self, endpoint: str, data: dict) -> Response:
		return self.session.post(f"{self.public_api}{endpoint}", json=data).json()

	def _get(self, endpoint: str, params: dict = None) -> Response:
		return self.session.get(endpoint, params=params).json()

	def _captcha(self) -> str:
		return "".join(
			choices(f"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_-", k=462)).replace("--", "-")

	def login(
			self,
			email: str,
			password: str) -> dict:
		data = {
			"csrf": 1,
			"mail": email,
			"passwd": password
		}
		response = self._post("/login.php", data)
		if "sessionId" in response:
			self.session_id = response["sessionId"]
			self.session.headers["Cookie"] = f"PHPSESSID={self.session_id}"
		return response

	def register(
			self,
			login: str,
			email: str,
			password: str) -> dict:
		data = {
			"g-recaptcha-response": self._captcha(),
			"login": login,
			"mail": email,
			"passwd": password
		}
		return self._post("/registration.php", data)

	def search_anime(
			self,
			search: str,
			small: int = 1) -> dict: 
		data = {
			"search": search,
			"small": small
		}
		return self._post("/search.php", data)

	def report_error(self, message: str, url: str) -> dict:
		data = {
			"mes": message,
			"url": url,
			"g-recaptcha-response": self._captcha(),
			"recaptcha": 2
		}
		return self._post("/error.php", data)

	def get_catalog(
			self,
			year: int = None,
			genre: str = None, 
			season: str = None,
			page: int = 1,
			sort: int = 2,
			finish: int = 2,
			x_page: str = "catalog") -> dict:
		data = {
			"page": page,
			"search": {
				"year": year,
				"genre": genre,
				"season": season
			},
			"xpage": x_page,
			"sort": sort,
			"finish": finish
		}
		return self._post("/catalog.php", data)

	def get_random_anime(self) -> dict:
		data = {
			"js": 1
		}
		return self._post("/random.php", data)

	def get_title(self, code: str) -> dict:
		return self._get(
			f"{self.api}/v2/getTitle?code={code}")

	def get_updates(
			self,
			filter: str,
			limit: int = 5) -> dict:
		params = {
			"filter": filter,
			"limit": limit
		}
		return self._get(
			f"{self.api}/v2/getUpdates", params)

	def get_changes(
			self,
			filter: str = "type,status",
			limit: int = 5) -> dict:
		params = {
			"filter": filter,
			"limit": limit
		}
		return self._get(
			f"{self.api}/v2/getChanges", params)

	def get_schedule(self, days: int) -> dict:
		return self._get(
			f"{self.api}/v2/getSchedule?days={days}")

	def get_caching_nodes(self) -> dict:
		return self._get(f"{self.api}/v2/getCachingNodes")

	def get_random_title(self) -> dict:
		return self._get(f"{self.api}/v2/getRandomTitle")

	def get_youtube_videos(self, limit: int = 10) -> dict:
		return self._get(
			f"{self.api}/v2/getYouTube?limit={limit}")

	def get_feed(self, limit: int = 10) -> dict:
		return self._get(
			f"{self.api}/v2/getFeed?limit={limit}")

	def get_years(self) -> dict:
		return self._get(
			f"{self.api}/v2/getYears")

	def get_genres(self, sorting_type: int = 0) -> dict:
		return self._get(
			f"{self.api}/v2/getGenres?sorting_type={sorting_type}")

	def search_titles(
			self,
			search: str,
			limit: int = 10) -> dict:
		params = {
			"search": search,
			"limit": limit
		}
		return self._get(
			f"{self.api}/v2/searchTitles", params)

	def get_team(self) -> dict:
		return self._get(
			f"{self.api}/v2/getTeam")

	def get_seed_stats(
			self,
			users: str = None,
			limit: int = 10) -> dict:
		return self._get(
			f"{self.api}/v2/getSeedStats?users={users}" if users else f"{self.api}/v2/getSeedStats?limit={limit}")

	def get_rss(
			self,
			rss_type: str,
			limit: int = 5) -> dict:
		params = {
			"rss_type": rss_type,
			"limit": limit
		}
		return self._get(
			f"{self.api}/v2/getRSS", params)

	def get_favorite_titles(self, session: str) -> dict:
		return self._get(
			f"{self.api}/v2/getFavorites?session={session}")

	def add_title_to_favorites(
			self,
			session: str,
			title_id: int) -> dict:
		params = {
			"session": session,
			"title_id": title_id
		}
		return self.session.put(
			f"{self.api}/v2/addFavorite", params=params).json()

	def delete_title_from_favorites(
			self, 
			session: str,
			title_id: int) -> dict:
		params = {
			"session": session,
			"title_id": title_id
		}
		return self.session.delete(
			f"{self.api}/v2/delFavorite", params=params).json()
