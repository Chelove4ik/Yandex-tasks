from gtts import gTTS
from requests import get


class Musixmatch:
    def __init__(self, api_key):
        self.api_key = api_key
        self.site = 'https://api.musixmatch.com/ws/1.1/'

    def search_track(self, q):
        url = self.site + 'track.search'
        params = {'apikey': self.api_key, 'q': q}
        resp = get(url, params=params).json()
        return resp

    def get_lyrics(self, track_id):
        if not track_id.isdigit():
            track_id = self.search_track(track_id)['message']['body']['track_list'][0]['track']['track_id']
        url = self.site + 'track.lyrics.get'
        params = {'apikey': self.api_key, 'track_id': track_id}
        resp = get(url, params=params).json()
        return resp

    def search_artist(self, artist):
        url = self.site + 'artist.search'
        params = {'apikey': self.api_key, 'q_artist': artist, 'page_size': 1}
        resp = get(url, params=params).json()
        if not resp['message']['body']['artist_list']:
            return 'Артист не найден'
        else:
            return resp

    def get_artist_info(self, artist):
        art_id = self.search_artist(artist)['message']['body']['artist_list'][0]['artist']['artist_id']

        url = self.site + 'artist.get'
        params = {'apikey': self.api_key, 'artist_id': art_id}
        resp = get(url, params=params).json()
        return resp


def gtts(text, lang, id):
    gTTS(text=text, lang=lang, slow=False).save(f"{id}.mp3")
