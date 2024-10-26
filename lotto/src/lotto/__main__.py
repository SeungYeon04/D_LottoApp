import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER
import random 
import os

lottolist = [] #전역범주 리스트 
i = 0 
lottoNum = 0

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, '로또로고.png')

def getNum() : #로또를 위한 함수 
  i = 0 
  global lottolist
  lottolist = []  # 매번 새로 리스트를 초기화
  
  while True : 
    lottoNum = random.randint(1, 45)  # 1부터 45 사이의 번호 생성 
    if lottoNum in lottolist: 
       continue # 중복이니 위로 
    else : 
      lottolist.append(lottoNum)
      i += 1 

    if i == 6 : 
      break 
  
  return lottolist 


# 버튼 클릭 시 실행될 함수
def button_handler(widget, label):
    lottolist = getNum() 
     # 로또 번호를 문자열로 변환하여 라벨에 출력
    result_text = "로또 번호\n" + " ".join(map(str, lottolist))
    label.text = result_text

# 앱을 빌드하는 함수
def build(app):
    box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, background_color="white"))

    logo_image = toga.ImageView(
        toga.Image(image_path),  # PNG 이미지 경로
        style=Pack(height=200, width=230, alignment=CENTER, direction=COLUMN, background_color="white", padding_top=50)  # 이미지 크기와 정렬
    )

    # 결과를 보여줄 라벨
    result_label = toga.Label("로또 번호\n ", style=Pack(padding=10, text_align=CENTER, font_family='이서윤체', font_size=13, background_color="white"))

    # 버튼 생성
    button = toga.Button("로또 번호 생성", on_press=lambda widget: button_handler(widget, result_label), style=Pack(padding=5, text_align=CENTER, width=150, font_family='이서윤체', font_size=15, background_color="white"))
    
    box.add(logo_image)
    box.add(result_label)
    box.add(button)

    return box

# 앱 실행
if __name__ == "__main__":
    app = toga.App("Simple Lotto App", "org.beeware.simple_app", startup=build)
    app.main_loop()
