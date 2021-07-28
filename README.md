# Kirin Playlist Maker 

## Introduction: 

KPM is a project that makes a playlist for you to discover new songs based on your interests.
For that it uses the Spotify API along with Python to get good recomendations so you can enjoy good music after your own tastes.

## Connecting To Spotify:

* To start connecting to Spotify we need to first get a way to work with the API in Python. For that we'll use the _spotipy_ library:
>`pip install spotipy`
* The next step is to get an app running in the _Spotify Developer Dashboard_. For that we just need to go to the [web app](https://developer.spotify.com/dashboard/applications) and create a new application. This will provide the client and secret ID's that we'll need later.
* On the application settings you want to add the _Redirect URI_ used to log into _Spotify_. The _URI_ you want to add there is:
>`http:\\localhost:8080`
* After that is done we need to set up the `.env` file.
* We will need to add our credentials here. For that we will replace the following pameters with the ID and Secret we got on the Spotify App:
>`SPOTIPY_CLIENT_ID='Your Client ID'`
>
>`SPOTIPY_CLIENT_SECRET='Your Client Secret'`
* Finally, when all this is done we can start working with the app.

## Running The Aplication:

Now that all the set up is done you can run the app with python:
>`python spt.py`

After that you will be prompted with the different parameters that you can change.
When those are all filled, the program will ask you for a _Spotify Song Url_. This is used as a sample for the playlist.
The ptogram will then present you with all the recomendations.
Give the playlist a name and you're ready to go, everything is saved to a new playlist on your Spotify Library.
