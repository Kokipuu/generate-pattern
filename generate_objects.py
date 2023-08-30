import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle as MatplotlibRectangle, RegularPolygon
import datetime


class GenerateObject:

    # A4サイズ, 図形の初期化
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.shapes = []

    # 図形の設定
    def add_shape(self, shape_type, size, position, color, angle):
        if shape_type == "circle":
            self.shapes.append({"type": "circle", 
                                "size": size, 
                                "position": position, 
                                "color": color, 
                                "angle": angle})
            
        elif shape_type == "triangle":
            self.shapes.append({"type": "triangle", 
                                "size": size, 
                                "position": position, 
                                "color": color, 
                                "angle": angle})
            
        elif shape_type == "rectangle":
            self.shapes.append({"type": "rectangle", 
                                "size": size, 
                                "position": position, 
                                "color": color, 
                                "angle": angle})
        else:
            print("Unsupported shape type")

    # 図形の描画
    def draw(self, background_color, output_path):
        fig, ax = plt.subplots(figsize=(self.width, self.height), dpi=100)
        fig.set_facecolor(background_color)  # 背景色の設定
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.axis("off")

        for shape in self.shapes:
            shape_type = shape["type"]
            size = shape["size"]
            position = shape["position"]
            color = shape["color"]
            angle = shape["angle"]

            if shape_type == "circle":
                circle = Circle(position, size, color=color)
                ax.add_patch(circle)

            elif shape_type == "triangle":
                triangle = RegularPolygon(position, numVertices=3, radius=size, orientation=angle, color=color)  # numVerticesを変えることで正三角形, 正方形, 正五角形...と変更できる
                ax.add_patch(triangle)

            elif shape_type == "rectangle":
                rect = MatplotlibRectangle((position[0] - size[0]/2, position[1] - size[1]/2), 
                                           size[0], 
                                           size[1], 
                                           angle = angle, 
                                           color=color, 
                                           rotation_point=position)
                ax.add_patch(rect)

        plt.gca().set_aspect('equal', adjustable='box')
        save_graph(output_path)
    


def generate_random_point(x_range, y_range):
    x = np.random.uniform(0, x_range)
    y = np.random.uniform(0, y_range)
    return x, y


def genareta_radom_size(size, shape_type):
    if shape_type == "circle":
        s = np.random.uniform(0, size)
        return s
    elif shape_type == "triangle":
        s = np.random.uniform(0, size)
        return s
    elif shape_type == "rectangle":
        s_width = np.random.uniform(0, size)
        s_height = np.random.uniform(0, size)
        return s_width, s_height
    else:
        return "Unsupported shape type"


def save_graph(output_path):
    plt.savefig(output_path)



###############################################################################################################

""""保存先のディレクトリ設定"""
# フォルダを生成するディレクトリのパスを指定
output_directory = 'C:/Users/puu02/Documents/03_JobHanting/summer_intern/Bosch/programm/generate_pattern/pattern'  # your path

# """生成パターンを日付に指定"""
# 現在の日付と時間を取得
current_datetime = datetime.datetime.now()
date_str = current_datetime.strftime('%Y-%m-%d')
time_str = current_datetime.strftime('%H-%M-%S')
# # フォルダ名を生成
# output_name = f'{date_str}_{time_str}.png'
# # 保存先の絶対パスを生成
# folder_path = os.path.join(output_directory, output_name)


if __name__ == '__main__':

    WIDTH, HEIGHT = 21, 29.7  # A4サイズ
    X_RANGE, Y_RANGE = 21, 29.7  # 図形位置の乱数範囲
    SEED = 10  # 乱数のseed

    """変更箇所 start"""
    SHAPE_TYPE = "rectangle"   # 図形の選択
    NUM = 500  # 図形の個数
    SHAPE_SIZE = 1  # 図形のサイズ
    PATTERN_COLOR = "black"  # パターンの色
    BG_COLOR = "gray"  # 背景の色
    ROTATION_MIN = 0  # 回転の最小値 (deg)
    ROTATION_MAX = 90  # 回転の最大値 (deg)

    ROTATION = False  # 回転する: True, 回転しない: False
    SIZE = False  # ランダムにサイズ変更: True, サイズ一定: False
    """変更箇所 end"""

    np.random.seed(SEED)  # 乱数のseedを固定
    main_rectangle = GenerateObject(width=WIDTH, height=HEIGHT)  # 図形オブジェクトの作成

    if SIZE:
        for _ in range(NUM):
            x, y = generate_random_point(X_RANGE, Y_RANGE)  # 図形の位置を一様分布から生成
            if ROTATION:
                angle = np.random.uniform(ROTATION_MIN, ROTATION_MAX)  # 図形の回転を一様分布から生成
            else:
                angle = 0
            
            if SHAPE_TYPE == "circle":
                size = genareta_radom_size(SHAPE_SIZE, SHAPE_TYPE)  # 図形のサイズを一様分布から生成
                main_rectangle.add_shape(shape_type="circle", size=size, position=(x, y), color=PATTERN_COLOR, angle=angle)
            elif SHAPE_TYPE == "triangle":
                size = genareta_radom_size(SHAPE_SIZE, SHAPE_TYPE)  # 図形のサイズを一様分布から生成
                main_rectangle.add_shape(shape_type="triangle", size=size, position=(x, y), color=PATTERN_COLOR, angle=angle)
            elif SHAPE_TYPE == "rectangle":
                s_width, s_height = genareta_radom_size(SHAPE_SIZE, SHAPE_TYPE)  # 図形のサイズを一様分布から生成
                main_rectangle.add_shape(shape_type="rectangle", size=(s_width, s_height), position=(x, y), color=PATTERN_COLOR, angle=angle)
    
    else: 
        for _ in range(NUM):
            x, y = generate_random_point(X_RANGE, Y_RANGE)  # 図形の位置を一様分布から生成
            if ROTATION:
                angle = np.random.uniform(ROTATION_MIN, ROTATION_MAX)  # 図形の回転を一様分布から生成
            else:
                angle = 0

            if SHAPE_TYPE == "circle":
                size = SHAPE_SIZE
                main_rectangle.add_shape(shape_type="circle", size=size, position=(x, y), color=PATTERN_COLOR, angle=angle)
            elif SHAPE_TYPE == "triangle":
                size = SHAPE_SIZE
                main_rectangle.add_shape(shape_type="triangle", size=size, position=(x, y), color=PATTERN_COLOR, angle=angle)
            elif SHAPE_TYPE == "rectangle":
                s_width, s_height = SHAPE_SIZE, SHAPE_SIZE
                main_rectangle.add_shape(shape_type="rectangle", size=(s_width, s_height), position=(x, y), color=PATTERN_COLOR, angle=angle)


    # フォルダ名を生成
    output_name = f'{SHAPE_TYPE}_p-{PATTERN_COLOR}_bg-{BG_COLOR}_size-{SHAPE_SIZE}_sizerand-{SIZE}_rotationrand-{ROTATION}_{date_str}_{time_str}.png'
    # 保存先の絶対パスを生成
    folder_path = os.path.join(output_directory, output_name)

    # 生成パターンの保存
    main_rectangle.draw(BG_COLOR, folder_path)
