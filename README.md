Tutoral: https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK


## Changes
1. The tutorial says to not mess with the manage.py file. I decided to in order to get this project to run in another port.
2. The video tutorial ends with:
  * ~~non-functional "Add New Song" button on the details view~~
  * non-functional "Favorite" buttons
  * non-functional "Search" menu option
  * non-functional "Songs" menu option (not exactly sure what this was supposed to do...)
  * non-functional "Logout" menu option
  * questionable view for people who have not logged in (should probably have "Login" and "Register" buttons when people are not logged in)
3. Modifications:
  * Changed when the menu buttons become active.
  * On the index page, the delete-album's glyphicon was changed to a red background.
  * Changed how the album's info on the details view is shown.
  * Modified the URL structure for updating album details and added an "edit" button inside the details view.
  * "Add New Song" button works and redirects to the album's details view after a song has been added.
  * Added a "track number" field for the Song model.
