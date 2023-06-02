from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import StringProperty 
from kivy.core.window import Window 
from kivy.lang import Builder
import sqlite3
from kivy.uix.screenmanager import ScreenManager, Screen

# 日本語を適用させる
import japanize_kivy

# sample.kvを読み込む
Builder.load_file('./top.kv')

# Windowの背景色を変更 (黒 → 白)
#Window.clearcolor = (1, 1, 1, 1)

# ウィジェットクラス
class Top(Widget):
    # プロパティの追加
    text = StringProperty()
    def __init__(self, **kwargs):
        super(Top, self).__init__(**kwargs)
        # 初期値の設定
        self.text = 'マイジャグ専用分析'

    # コールバック用の関数を定義
    def callback(self, **kwargs):
        # 呼び出された際に、textの値を更新
        self.text = 'kivy : 基礎学習'
        # sqlite3
        #con = sqlite3.connect('sample.db')
        # カーソルの生成
        #cur = con.cursor()
        #cur.execute('CREATE TABLE IF NOT EXISTS person (id int, name str, age int)')
        #cur.execute('INSERT INTO person VALUES(1, "田中", 20)')
        #con.commit()
# メインクラス
class Test(App):
    def build(self):
        # ウィジェットクラスを返す
        return Top()
class Screen_One(Screen):
    pass
 
class Screen_Two(Screen):
    pass

if __name__ == "__main__":
    # アプリを起動
    Test().run()