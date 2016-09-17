Tutoral: https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK


## Changes
1. The tutorial says to not mess with the manage.py file. I decided to in order to get this project to run in another port.
2. The video tutorial ends with:
  * ~~non-functional "Add New Song" button on the details view~~
  * ~~non-functional "Favorite" buttons~~
  * non-functional "Search" menu option
  * ~~non-functional "Songs" menu option~~
  * ~~non-functional "Delete" buttons for songs~~
  * ~~non-functional "Logout" menu option~~
  * ~~questionable view for people who have not logged in (should probably have "Login" and "Register" buttons when people are not logged in)~~
  * ~~Disconnected user-registration form~~
  * ~~No way to log users in without using the admin panel~~
3. Modifications:
  * Changed when the navbar images become active.
  * On the index page, the delete-album's glyphicon was changed to a red background.
  * Changed how the album's info on the details view is shown.
  * Modified the URL structure for updating album details and favoriting albums.
  * Broke down the details template into another base template.
  * "Add New Song" button works and redirects to the album's details view after a song has been added.
  * Added a "track number" field for the Song model.
  * Took out "genre" and added "year" field for Albums model.
  * Added a button to edit album details in the details-base file.
  * Added a button to highlight when a song is being edited.
  * The "Delete" function for songs work, and stays on the album page.
  * The "Favorite" function for albums and songs work, and stays on the album page when favoriting a song.
  * Removed the hidden fields on forms.
  * Added a "reset" button on forms.
  * Specified keyword arguments in templates.
  * Created a page listing all songs, which will cause the "Songs" menu option to become active.
  * Deleting an album or song deletes the uploaded files from storage as well.
  * When the user is logged out, the button now shows "Register" and "Login" options.