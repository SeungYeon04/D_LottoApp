import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

# 버튼 클릭 시 실행될 함수
def button_handler(widget):
    print("버튼이 클릭되었습니다!")

# 앱을 빌드하는 함수
def build(app):
    box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER))

    # 버튼 생성
    button = toga.Button("Click Me", on_press=button_handler, style=Pack(padding=10))
    box.add(button)

    return box

# 앱 실행
if __name__ == "__main__":
    app = toga.App("Simple App", "org.beeware.simple_app", startup=build)
    app.main_loop()
