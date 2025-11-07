# image-board-thread-file-scraper

Simply scrapes files from an image board thread url, using Playwright

1. Create a .env file in the root directory

2. Copy the contents from the file .env.example into the .env

3. Copy the web address from any image thread from any 4chan site, that has images.

4. When the main program is ran, a Playwright instant boots up and all the images and videos from the image thread are saved.

TODO:

- urllib.error.HTTPError: HTTP Error 429: Too Many Requests
- Handler for '404 Not Found'
