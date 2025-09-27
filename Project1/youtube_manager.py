import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            data = json.load(file)
            print("Data loaded successfully.")
            print(type(data))
            return data
    except FileNotFoundError:
        return []


def save_data(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file, indent=4)

def list_all_videos(videos):
    print("*"*11, "List of all youtube videos", "*"*11)
    for index, video in enumerate(videos, start = 1):
        print(f"{index}. {video['title']} - {video['time']} - {video['url']}")
    print("*"*50)
    

def add_new_video(videos):
    name = input("Enter video title: ")
    time = input("Enter video time: ")
    url = input("Enter video URL: ")
    videos.append({'title': name, 'time': time, 'url': url})
    save_data(videos)
    print("Video added successfully.")

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to update: ")) - 1
    if 0 <= index < len(videos):
        name = input("Enter new video title: ")
        time = input("Enter new video time: ")
        url = input("Enter new video URL: ")
        videos[index] = {'title': name, 'time': time, 'url': url}
        save_data(videos)
        print("Video updated successfully.")
    else:
        print("Invalid index. Please try again.")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to delete: ")) - 1
    if 0 <= index < len(videos):
        videos.pop(index)
        save_data(videos)
        print("Video deleted successfully.")
    else:
        print("Invalid index. Please try again.")


def main():
    videos = []
    videos = load_data()
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
                list_all_videos(videos)
            case '2':
                add_new_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")
                
                
if __name__ == "__main__":
    main()