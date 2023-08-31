import sqlite3
from datetime import datetime

class PotholesDB:
    def __init__(self, db_name='potholes.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def init_db(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS potholes (
            id INTEGER PRIMARY KEY,
            longitude REAL,
            latitude REAL,
            type TEXT,
            date TEXT
        )
        ''')
        self.conn.commit()

    def insert(self, longitude, latitude, pothole_type):
        current_date = datetime.now().strftime('%Y-%m-%d')
        self.cursor.execute('''
        INSERT INTO potholes (longitude, latitude, type, date)
        VALUES (?, ?, ?, ?)
        ''', (longitude, latitude, pothole_type, current_date))
        self.conn.commit()

    def delete(self, entry_id):
        self.cursor.execute('DELETE FROM potholes WHERE id=?', (entry_id,))
        self.conn.commit()

    def batch_insert(self, data_list):
        current_date = datetime.now().strftime('%Y-%m-%d')
        for _, (latitude, longitude), pothole_type in data_list:
            self.insert(longitude, latitude, pothole_type)

    def close(self):
        self.conn.close()


def main():
    db = PotholesDB()
    db.init_db()

    data = [
        ('/Users/yehudanevo/PycharmProjects/embedded-embedded-group-04/hazards_detection/pothole_coordinates/Pothole0.jpg', (31.819977, 35.257502), 'Pothole'),
        ('/Users/yehudanevo/PycharmProjects/embedded-embedded-group-04/hazards_detection/pothole_coordinates/Pothole10.jpg', (31.799272, 35.200192), 'Pothole')
    ]

    db.batch_insert(data)
    db.close()

if __name__ == '__main__':
    main()


