from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

# 데이터베이스 연결 및 커서 생성
db = pymysql.connect(
    host="127.0.0.1", user="root", password="rla456852", db="kream", charset="utf8mb4"
)
cur = db.cursor()

# 쿼리문 실행
sql = "SELECT * FROM kream"
cur.execute(sql)
kream_data = cur.fetchall()

# 전체 페이지 수 계산
items_per_page = 10
total_pages = (len(kream_data) + items_per_page - 1) // items_per_page


# 현재 페이지 및 페이지당 항목 수를 가져오기 위한 함수 정의
def get_current_data(page):
    start_idx = (page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    current_data = kream_data[start_idx:end_idx]
    return current_data


# 홈페이지 라우팅
@app.route("/")
def index():
    # 현재 페이지 및 페이지당 항목 수를 가져오기
    page = int(request.args.get("page", 1))

    # 현재 페이지에 해당하는 데이터만 추출
    current_data = get_current_data(page)

    return render_template(
        "index.html", data_list=current_data, current_page=page, total_pages=total_pages
    )


if __name__ == "__main__":
    app.run(debug=True)
