import keyboard, os, subprocess

"""
Modify the following paths & buttons to your environment & liking.
"""
path_to_playable_songs = os.path.abspath(r"C:\Users\zachw\Desktop\AxS Comp")
path_to_liked_songs = os.path.abspath(r"C:\Users\zachw\Desktop\songs")
path_to_disliked_songs = os.path.abspath(r"C:\Users\zachw\Desktop\disliked-songs")
song_list = os.listdir(path_to_playable_songs)
like_key = 'f24'
dislike_key = 'f23'
replay_key = 'f22'



##################################################################
### Handling Like/Dislike, iterating through each song in dir. ###

i = 0
os.startfile(path_to_playable_songs + "\\" + song_list[i])

while i != len(song_list):
    keypress = keyboard.read_event()
    
    # Handle keypresses, assign when G1 / G2 keys pressed. Plays next song until end of list
    # F24 (G1 macro) = liked songs
    if keypress.event_type == keyboard.KEY_DOWN and keypress.name == like_key:
        os.replace(path_to_playable_songs + "\\" +  song_list[i], path_to_liked_songs + "\\" +  song_list[i])
        i += 1
        os.startfile(path_to_playable_songs + '\\' + song_list[i])

    # F23 (G2 macro) = disliked songs
    if keypress.event_type == keyboard.KEY_DOWN and keypress.name == dislike_key:
        os.replace(path_to_playable_songs + "\\" +  song_list[i], path_to_disliked_songs + "\\" +  song_list[i])
        i += 1
        os.startfile(path_to_playable_songs + '\\' + song_list[i])

    # F22 (G5 macro) = replay song
    if keypress.event_type == keyboard.KEY_DOWN and keypress.name == replay_key:
        os.startfile(path_to_playable_songs + '\\' + song_list[i])

# Exit Media Player
subprocess.call(["taskkill","/F","/IM","Microsoft.Media.Player.exe"])
