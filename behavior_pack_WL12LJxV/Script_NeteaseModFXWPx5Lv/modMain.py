# -*- coding: utf-8 -*-

from mod.common.mod import Mod


@Mod.Binding(name="Script_NeteaseModFXWPx5Lv", version="0.0.1")
class Script_NeteaseModFXWPx5Lv(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def Script_NeteaseModFXWPx5LvServerInit(self):
        pass

    @Mod.DestroyServer()
    def Script_NeteaseModFXWPx5LvServerDestroy(self):
        pass

    @Mod.InitClient()
    def Script_NeteaseModFXWPx5LvClientInit(self):
        pass

    @Mod.DestroyClient()
    def Script_NeteaseModFXWPx5LvClientDestroy(self):
        pass
