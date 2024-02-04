import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="rla456852",
    db="airbnb",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)

with connection.cursor() as cursor:
    # 문제 1 : Python Book 제품 추가
    # sql = "INSERT INTO Products(productName, price, stockQuantity) VALUES (%s, %s, %s)"
    # cursor.execute(sql, ("Python Book", 10000, 10))
    # connection.commit()

    # # 문제 2 : 고객 목록 조회
    # sql = "SELECT * FROM Customers"
    # cursor.execute(sql)
    # for row in cursor.fetchall():
    #     print(row)

    # 문제 3: 제품 재고 업데이트
    # sql = "UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID = %s"
    # cursor.execute(sql, (1, 1))
    # connection.commit()

    # 문제 4: 고객별 총 주문 금액 계산
    # sql = "SELECT customerID, SUM(totalAmount) FROM Orders GROUP BY customerID"
    # cursor.execute(sql)
    # for row in cursor.fetchall():
    #     print(row)

    # 문제 5: 고객 이메일 업데이트
    # sql = "UPDATE Customers SET email = %s WHERE customerID = %s"
    # cursor.execute(sql, ("abcd@update.com", 1))
    # connection.commit()

    # 문제 6: 주문 취소
    # sql = "DELETE FROM Orders WHERE orderID = %s"
    # cursor.execute(sql, (15))
    # connection.commit()

    # 문제 7: 특정 제품 검색
    # sql = "SELECT * FROM Products WHERE productName LIKE %s"
    # cursor.execute(sql, ("%Book%"))
    # for row in cursor.fetchall():
    #     print(row)

    # 문제 8: 특정 고객의 모든 주문 조회
    # sql = "SELECT * FROM Orders WHERE customerID = %s"
    # cursor.execute(sql, (1))
    # for row in cursor.fetchall():
    #     print(row)

    # 문제 9: 가장 많이 주문한 고객 찾기
    sql = """
        SELECT customerID, COUNT(*) AS orderCount 
        FROM Orders GROUP BY customerID 
        ORDER BY orderCount DESC LIMIT 1
        """  # 고객별 주문 횟수 정렬

    cursor.execute(sql)
    data = cursor.fetchone()
    print(data)


cursor.close()
