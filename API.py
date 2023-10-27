import requests
from urllib.parse import quote

class DAnimeApi:
    URL_BASE = "https://anime.dmkt-sp.jp/animestore/rest"
    ENDPOINT = {
        "LIST": "WS000108",
        "FIND": "WS000105"
    }

    @staticmethod
    def get_info_link(work_id):
        return f"https://anime.dmkt-sp.jp/animestore/ci_pc?workId={work_id}"

    @staticmethod
    def get_search_link(keyword):
        encoded_keyword = quote(keyword)
        return f"https://anime.dmkt-sp.jp/animestore/sch_pc?searchKey={encoded_keyword}&vodTypeList=svod"

    @staticmethod
    def fetch_all_items(initial_collection_key=1, consonant_key=1):
        url = f"{DAnimeApi.URL_BASE}/{DAnimeApi.ENDPOINT['LIST']}?workTypeList=anime&length=300&initialCollectionKey={initial_collection_key}&consonantKey={consonant_key}&vodTypeList=svod"
        response = requests.get(url)
        return response.json()

    @staticmethod
    def fetch_search_result(keyword):
        encoded_keyword = quote(keyword)
        url = f"{DAnimeApi.URL_BASE}/{DAnimeApi.ENDPOINT['FIND']}?length=10&mainKeyVisualSize=1&sortKey=4&searchKey={encoded_keyword}&vodTypeList=svod"
        response = requests.get(url)
        return response.json()

# 使用例
# アイテム一覧の取得
item_list = DAnimeApi.fetch_all_items()
print("アイテム一覧:", item_list)

# 検索結果の取得
search_result = DAnimeApi.fetch_search_result("キーワード")
print("検索結果:", search_result)

# 作品IDに基づく詳細情報へのリンクの取得
work_id = 12345  # 作品IDを指定
info_link = DAnimeApi.get_info_link(work_id)
print("作品詳細へのリンク:", info_link)

# キーワードに基づく検索ページへのリンクの取得
keyword = "アニメ"  # 検索キーワードを指定
search_link = DAnimeApi.get_search_link(keyword)
print("検索ページへのリンク:", search_link)