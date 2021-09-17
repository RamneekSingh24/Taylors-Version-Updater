# Taylors-Version-Updater
## Requirements:
- python >= 3.0
- spotipy >= 2.0

## Steps
- After cloning the repo, install the library spotipy using  
  ```bash
    pip install spotipy
  ```
- Go to https://developer.spotify.com/dashboard/applications and login.
- Create a new app and get your **client id** and **client secret**.
- Go to your app => edit settings => and add http://localhost in **redirect uri.**
- Update the client id, client secret and cleint uri fields in the .env. Note: paste the value after = without quotes(' ').
- Run the script in terminal
  ```bash
    python3 tv_updater.py
  ```
- A webpage asking for acceptance will open, click on accept and copy the next url that opens.
-  The terminal will ask you for the url, paste it and hit enter.
-  Done! (The previous two steps are only for the first time, subsequent usage will not require you to do those)
