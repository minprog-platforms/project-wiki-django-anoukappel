# Application Name

Encyclopedia

## Design document
### Entry page:
visiting /wiki/TITLE where TITLE is the title of an encyclopedia entry
- should call the appropriate util Function
- if entry does not exist, an error page indicating that their requested page was not found.

![This is an image](/wiki/fotos/entry_page.jpg)

### Index page:
Should be able to click on links en go through that page.
![This is an image](/wiki/fotos/index_page.jpg)

### Search:
Allow the user to type a query, user should be redirected to that entry's page.
If the query does not exist, should find list of substrings.
you should be able to click on those links.

### New Page:
a page where you can create a new encyclopedia entry: you should be able to:
    * enter a title, and in a textarea, enter the markdown content for the page.
    * click button to save Page
    * if page with title already exists-> present error message.
    * else encyclopedia should be saved on disk en user should be taken to entry's page.
![This is an image](/wiki/fotos/new_page.jpg)
