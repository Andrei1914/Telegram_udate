import sqlite3
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
       CREATE TABLE IF NOT EXISTS Products(
        id INT PRIMARY KEY NOT NULL,
        Title TEXT NOT NULL,
        Description TEXT,
        Price INT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INT PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INT NOT NULL,
        balance INT NOT NULL
        )
    ''')


    connection.commit()


def get_all_products():
    cursor.execute('''
    SELECT * FROM Products
    ''')
    return cursor.fetchall()



def add_user(username, email, age):
    cursor.execute(f'INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)', (f"{username}",f"{email}",f"{age}", 1000))
    connection.commit()


def is_include(username):
    chek_user = cursor.execute("SELECT username FROM Users WHERE username =?", (username,))
    return not(cursor.fetchone() is None)
    
    # chek_user = cursor.execute("SELECT * FROM Products WHERE Title =?", (Title,))
    # if chek_user.fetchall() is None:
    #     cursor.execute(f'''
    #     INSERT INTO Users VALUES('{Title}','{Description}','{Price}')
    #     ''')
# cursor.execute("CREATE INDEX IF NOT EXISTS IDX_email ON Users(email)")
# for i in range(1, 11):
# cursor.execute("INSERT INTO Products(id, Title, Description, Price) VALUES(?, ?, ?, ?)", (1, "Chalk", f"Сухая магнезия — это специальное средство, предназначенное для улучшения сцепления рук с различными поверхностями во время спортивных тренировок, таких как скалолазание, гимнастика и силовые упражнения", "300"))
# cursor.execute("INSERT INTO Products(id, Title, Description, Price) VALUES(?, ?, ?, ?)", (2, "Bars", f"Напольные брусья — это компактное и многофункциональное спортивное оборудование, предназначенное для различных упражнений, укрепляющих верхнюю часть тела. Они идеально подходят для тренировки таких мышц, как грудные, плечевые, трицепсы и мышцы спины. Напольные брусья могут использоваться как в домашних условиях, так и в спортивных залах.", "6000" ))
# cursor.execute("INSERT INTO Products(id, Title, Description, Price) VALUES(?, ?, ?, ?)", (3, "Horizontal_bar", f"Настенный турник — это прочное и надежное оборудование для силовых тренировок, предназначенное для крепления к стене. Он идеально подходит для выполнения подтягиваний, которые укрепляют спину, плечи и руки. Настенный турник экономит пространство и подходит для установки в домашних условиях, на спортивных площадках или в залах.", "10000"))
# cursor.execute("INSERT INTO Products(id, Title, Description, Price) VALUES(?, ?, ?, ?)", (4, "paralets", f"Напольные паралетсы — это стильное и функциональное оборудование для занятий гимнастикой и силовыми тренировками. Они позволяют выполнять отжимания, стойки на руках и различные элементы с поднятыми руками, что способствует развитию силы, гибкости и координации. Паралетсы компактны и легки в использовании, что делает их идеальными для домашних тренировок и студий. ", "4500"))
# cursor.execute("UPDATE Users SET age = ? WHERE username = ?", ("25", "newuser_0"))
# cursor.execute("DELETE FROM Users WHERE Id = ?", ("11", ))
# cursor.execute("SELECT Age, AVG(Age) FROM Users GROUP by Age")
# for i in range(1, 11):
#     cursor.execute("UPDATE Users SET balance = ? WHERE id % 2 == 0", ("500", ))


# connection.commit()
# connection.close()