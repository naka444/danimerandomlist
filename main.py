import random
import time

# 母音子音のKey
INITIAL_TABLE = [
    ['あ', 'い', 'う', 'え', 'お'],
    ['か', 'き', 'く', 'け', 'こ'],
    ['さ', 'し', 'す', 'せ', 'そ'],
    ['た', 'ち', 'つ', 'て', 'と'],
    ['な', 'に', 'ぬ', 'ね', 'の'],
    ['は', 'ひ', 'ふ', 'へ', 'ほ'],
    ['ま', 'み', 'む', 'め', 'も'],
    ['や', '＿', 'ゆ', '＿', 'よ'],
    ['ら', 'り', 'る', 'れ', 'ろ'],
    ['わ', 'を', 'ん', '＿', '＿']
]

# スプレッドシートのデータをシミュレート
class Spreadsheet:
    def __init__(self):
        self.data = []

    def appendRow(self, row):
        self.data.append(row)

    def getRange(self, row_start, col_start, row_end, col_end):
        return [row[col_start - 1:col_end] for row in self.data[row_start - 1:row_end]]

    def clear(self):
        self.data = []

    def getDataRange(self):
        return len(self.data)

class DA_API:
    @staticmethod
    def fetchAllItem(ik, ck):
        # ここにAPI呼び出しのロジックを追加する
        pass

BOOKID = "your_spreadsheet_id_here"
SHEET_WORKLIST = "WorkList"

def setWorkItemList():
    sheet = Spreadsheet()

    # シートのヘッダー行を作成
    sheet.appendRow(["workId", "workTitle", "mainKeyVisualPath"])

    # 作品一覧を取得しシートに記入する
    for ik in range(len(INITIAL_TABLE)):
        for ck in range(len(INITIAL_TABLE[ik])):
            if INITIAL_TABLE[ik][ck] != "＿":
                json_data = DA_API.fetchAllItem(ik + 1, ck + 1)
                data = [[d['workId'], d['workInfo']['workTitle'], d['workInfo']['mainKeyVisualPath'].replace('_[0-9].png', '_1.png')] for d in json_data['data']['workList']]
                time.sleep(2)  # 2秒待機
                if data:
                    sheet.appendRow(data)
                    print(f"{INITIAL_TABLE[ik][ck]} から始まる作品一覧の取得完了")
                else:
                    print(f"{INITIAL_TABLE[ik][ck]} から始まる作品なし")

def getRandomWorkItem():
    sheet = Spreadsheet()

    # ランダムな行の選択
    row_min = 2
    row_max = sheet.getDataRange()
    row = random.randint(row_min, row_max)

    # 選択した作品の情報の取得
    data = sheet.getRange(row, 1, row, 3)[0]
    return {
        "workId": data[0],
        "workTitle": data[1],
        "mainKeyVisualPath": data[2]
    }

# 実行例
setWorkItemList()
random_work_item = getRandomWorkItem()
print("ランダムな作品情報:", random_work_item)