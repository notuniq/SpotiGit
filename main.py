import requests
import base64
import time

import setup
def get_current_track():
    headers = {
        "Authorization": f"Bearer {setup.SPOTIFY_TOKEN}"
    }
    response = requests.get("https://api.spotify.com/v1/me/player/currently-playing", headers=headers)
    
    if response.status_code == 200:
        current_track = response.json()
        artist = current_track['item']['artists'][0]['name']
        track_name = current_track['item']['name']
        return f"{artist} - {track_name}"
    else:
        return None


def update_readme_on_github(new_music):

    headers = {
        "Authorization": f"token {setup.GITHUB_TOKEN}"
    }


    repo_owner = setup.REPO_OWNER
    repo_name = setup.REPO_NAME
    file_path = setup.FILE_PATH


    response = requests.get(
        f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}",
        headers=headers
    )
    response_json = response.json()


    content = base64.b64decode(response_json['content']).decode('utf-8')


    index = content.find(setup.CONTENT_FIND)


    if index != -1:

        next_line_index = content.find('\n', index)
        if next_line_index != -1:

            new_content = content[:index] + f'{setup.CONTENT_FIND} {new_music}\n' + content[next_line_index + 1:]
            
            encoded_content = base64.b64encode(new_content.encode('utf-8')).decode('utf-8')

            data = {
                "message": "Update currently playing song",
                "content": encoded_content,
                "sha": response_json['sha']
            }

            response = requests.put(
                f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}",
                headers=headers,
                json=data
            )

            if response.status_code == 200:
                print('Changed!')
            else:
                print(response.text)
        else:
            print("Next line not found")
    else:
        print("currently playing: not found")


previous_track = None
while True:
    current_track = get_current_track()
    if current_track:
        if current_track != previous_track:
            print("Currently playing:", current_track)
            update_readme_on_github(current_track)
            previous_track = current_track
    else:
        print("No track is currently playing.")

    time.sleep(setup.SLEEP)
