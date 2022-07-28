# Close Empty Windows

A Gedit plugin that allows user to skip the extra Ctrl-w when done with a file, like a browser.

Gedit is the default text editor in my GNOME Shell, but it's my secondary editor; I launch a bigger editor from the Overview for most of my work. But when I double click a text file inside a ZIP file, Gedit is perfectly suitable except for one minor annoyance: the "empty window" state! After I finish viewing a file, I habitually press Ctrl-w, and instead of going away, the window hangs around with nothing in it. I no longer need it at that point, I'm never going to use it after that, and no other program I use does this.

This plugin address that problem. When you close the last tab in a window, the window auto closes instead of entering an "empty" state, just like a normal application.

## Installation

1. ```
   mkdir -p ~/.local/share/gedit/plugins
   git clone https://github.com/HebaruSan/gedit-close-empty-windows.git ~/.local/share/gedit/plugins/gedit-close-empty-windows
   ```

1. Open Gedit
2. Preferences → Plugins
3. Check the box next to "Close Empty Windows"
