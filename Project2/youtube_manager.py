import sqlite3

con = sqlite3.connect('youtube_manager.db')
cursor  = con.cursor()

print("Database opened successfully")

cursor.execute('''
               create table if not exists videos(
                   id integer primary key,
                   title text not null,
                   time text not null,
                   url text not null
               )
''')

def list_all_videos():
    cursor.execute("select * from videos")
    videos = cursor.fetchall()
    if not videos:
        print("No videos fount.")
    else:
        print("*"*10, "List of all youtube videos", "*"*10)
        for idx, video in enumerate(videos, start=1):
            print(f"{video[0]}. {video[1]} - {video[2]} - {video[3]}")
    print("*"*50)
            
            
def add_new_video():
    name = input("Enter video title: ")
    time = input("Enter video time: ")
    url = input("Enter video URL: ")
    cursor.execute("insert into videos (title, time, url) values (?, ?, ?)", (name, time, url))
    con.commit()
    print("Video added successfully.")
    
def update_video():
    list_all_videos()
    index = int(input("Enter the id of the video to update: "))
    cursor.execute("select * from videos where id=?", (index,))
    video = cursor.fetchone()
    if video:
        name = input("Enter new video title: ")
        time = input("Enter new video time: ")
        url = input("Enter new video URL: ")
        cursor.execute("update videos set title=?, time=?, url=? where id=?", (name, time, url, index))
        con.commit()
        print("Video updated successfully.")
    else:
        print("Invalid id. Please try again.")
        
def delete_video():
    list_all_videos()
    index = int(input("Enter the id of the video to delete: "))
    cursor.execute("select * from videos where id=?", (index,))
    video = cursor.fetchone()
    if video:
        cursor.execute("delete from videos where id=?", (index,))
        con.commit()
        print("Video deleted successfully.")
    else:
        print("Invalid id. Please try again.")

def main():
    while True:
        print("Youtube Manager | Main Menu")
        print("1. List all youtube videos")
        print("2. Add a new youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice (1-5): ")
        
        match choice:
            case '1':
                list_all_videos()
            case '2':
                add_new_video()
            case '3':
                update_video()
            case '4':
                delete_video()
            case '5':
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

    con.close()

if __name__ == '__main__':
    main()