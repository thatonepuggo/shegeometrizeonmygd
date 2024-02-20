# shegeometrizeonmygd
adds an image to gd from geometrize JSONs.

## how to run
- get [geode](https://geode-sdk.org/install/).
- get the mod `WSLiveEditor`. this will let the app interface with the gd editor.
- enter a level. the image will paste at the beginning of the level, so pan the camera there.
- set color channel 10 to `#ff0000`.
- go to [geometrize](https://www.samcodes.co.uk/project/geometrize-haxe-web/).
- click `open image` and add an image.
- click `settings` (above the canvas).
- you can tweak other options, but the main thing you want to do is to **disable** all other shapes, and enable circles only.
- set a max shapes cap. anything over 1000 is usually detailed enough but it depends on your image.
- click `run`.
- once it is done, click `save json`. you can use any folder, but it's recommended to save the file 
somewhere in this directory so it's easier to run.
- get [python](https://www.python.org/downloads/).
- get pip by running `pip -m ensurepip --upgrade` in a terminal.
- restart the terminal.
- run `pip install -r requirements.txt` in this folder.
- run `python main.py </path/to/your/json>`.