# -*- coding: utf-8 -*-
#
#  closeemptywindows.py - Close Empty Windows
#
#  This program is in the public domain.

from gi.repository import GObject, Gio, Gedit

class CloseEmptyWindowsWindowActivatable(GObject.Object,
                                         Gedit.WindowActivatable):
    window = GObject.property(type=Gedit.Window)

    def __init__(self) -> None:
        GObject.Object.__init__(self)

    def do_activate(self) -> None:
        self.signal_id = self.window.connect('tab-removed',
                                             self._on_tab_removed)

    def do_deactivate(self) -> None:
        self.window.disconnect(self.signal_id)

    def _on_tab_removed(self, window: Gedit.Window, tab: Gedit.Tab) -> None:
        if not window.get_documents():
            window.close()
