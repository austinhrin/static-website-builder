## Static Website Builder

This project was made to be able to untilize jinja2 templating as a way to build static websites. Basically write the html in modular templates and run the script to build the static html files. Previously I was trying to do this with Flask but that proved to be unneeded and more difficult to work with...

The way this works is you put your templates in the templates folder, if you have json files for storing your text then put that in the json folder, then run `python main.py` and it will build the files in the build folder.