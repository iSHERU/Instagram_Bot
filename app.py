from instagrapi import Client
import time
import random
from run import hash_list

with open("credentials.txt", "r") as f:
    username, password = f.read().splitlines()

client = Client()
try:
    client.login(username, password)
    print(f"Logged in as {username}")
    time.sleep(5)
except Exception as e:
    print(f"Login failed: {e}")
    exit()

hashtag_list = hash_list()

def main():
    username_list = []
    
    while True:
        hashtag = random.choice(hashtag_list)
        print(f"{hashtag} selected.")

        try:
            media = client.hashtag_medias_recent(hashtag, 9)

            # add comments of your choice here
            comments = [
                "Awesome post!",
                "Fantastic!",
                "Good work.",
                "Love it!"
            ]
        
            for media_item in media:
                if media_item.user.username in username_list:
                    print(f"Skipped. {media_item.user.username}")
                    continue

                username_list.append(media_item.user.username)

                # Choose a random comment
                comment = random.choice(comments)
                client.media_comment(media_item.id, comment)
                print(f"Commented: {comment}")

                sleep_time = random.randint(50, 60)
                print(f"Sleeping for {sleep_time} seconds.")
                time.sleep(sleep_time)

        except Exception as e:
            print(f"An error occurred: {e}")
            client.login(username, password)

if __name__ == "__main__":
    main()
