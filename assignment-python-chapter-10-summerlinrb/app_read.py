import sqlite3


print("Getting Data")
db_name = "chinook.db"
with sqlite3.connect(db_name) as conn:
    sql_command = "SELECT Name, Composer, UnitPrice FROM tracks INNER JOIN playlist_track ON playlist_track.TrackId = tracks.TrackId WHERE playlist_track.PlaylistId = 12;"
    cursor = conn.execute(sql_command)
    trackdata = cursor.fetchall()
    print(trackdata)
