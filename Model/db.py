import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Saptak@203',
            db='KWIC',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connection.cursor()

    def truncate_table(self):
        query = "TRUNCATE TABLE KWIC"
        self.cursor.execute(query)
        self.connection.commit()
    def insert_data(self, data):
        # delete_query = "DELETE FROM KWIC"
        # self.cursor.execute(delete_query)
        self.truncate_table()

        # Insert the new, combined, and deduplicated data
        insert_query = "INSERT INTO KWIC (Web_links, Description) VALUES (%s, %s)"
        for item in data:
                self.cursor.execute(insert_query,item)
        self.connection.commit()

    def fetch_data(self):
        query = "SELECT Web_links, Description FROM KWIC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def close(self):
        self.connection.close()
#
if __name__ == '__main__':
    d=Database()
    f=d.fetch_data()
    print(f)