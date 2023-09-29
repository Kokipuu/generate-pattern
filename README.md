# generate-pattern

Diaprity mapを検証するための画像を出力する．
変更パラメータは以下の通りである．

    """変更箇所 start"""
    SHAPE_TYPE = "rectangle"   # 図形の選択: circle, triangle, rectangle
    NUM = 900  # 図形の目安個数(OVERLAP=Falseのときは描けない場合あり)
    SHAPE_SIZE = 0.4  # 図形のサイズ
    PATTERN_COLOR = "black"  # パターンの色
    BG_COLOR = "gray"  # 背景の色
    ROTATION_MIN = 0  # 回転の最小値 (deg)
    ROTATION_MAX = 90  # 回転の最大値 (deg)

    ROTATION = False  # 回転する: True, 回転しない: False
    SIZE = False  # ランダムにサイズ変更: True, サイズ一定: False
    OVERLAP = False  # patternが重ねる: True, 重ならない: False
    """変更箇所 end"""


