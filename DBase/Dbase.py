import sqlite3

DEFAULT_SETTINGS = [
    {
        'Show_Info_Video': 'Выкл.'
    }
]

PATH_DATABASE = r'C:\Users\Admin\PycharmProjects\SendPhotoBot\DBase\settings.db'


def connect():
    connection = sqlite3.connect(PATH_DATABASE)
    return connection


def create_database():
    connection = connect()
    cursor = connection.cursor()

    sql = """ CREATE TABLE IF NOT EXISTS settings(
        show_info_video TEXT NOT NULL,
        UNIQUE ("show_info_video") ON CONFLICT IGNORE
    
    ) """

    cursor.execute(sql)
    connection.commit()


def add_default_settings():
    connection = connect()
    cursor = connection.cursor()

    for elem in DEFAULT_SETTINGS:
        status = elem['Show_Info_Video']
        cursor.execute(""" INSERT INTO settings VALUES(?)""", (status,))

    connection.commit()


def update_show_info_video(data):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute(f""" UPDATE settings SET show_info_video='{data}' """)
    connection.commit()


def select_show_info_video():
    try:
        connection = connect()
        cursor = connection.cursor()

        sql = """ SELECT show_info_video FROM settings"""

        cursor.execute(sql)

        result = cursor.fetchone()

        return result[0]
    except Exception as ex:
        print(ex)
        add_default_settings()
        return 'Выкл.'


def remove_show_info_video():
    connection = connect()
    cursor = connection.cursor()

    cursor.execute(""" DELETE FROM settings WHERE show_info_video="Выкл." OR show_info_video="Вкл." """)
    connection.commit()


