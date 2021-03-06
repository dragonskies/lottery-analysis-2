#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.4 on Tue Nov  3 09:05:41 2020
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class AboutDialog(wx.Dialog):
    description = "Describe your project"
    details = "Add details"

    def __init__(self, *args, **kwds):
        # begin wxGlade: AboutDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.panel_4 = wx.Panel(self, wx.ID_ANY)
        self.about_text = wx.StaticText(self.panel_4, wx.ID_ANY, "Title", style=wx.ALIGN_LEFT)
        self.about_title_txt = wx.TextCtrl(self.panel_4, wx.ID_ANY, "Title of your project")
        self.panel_5 = wx.Panel(self, wx.ID_ANY)
        self.about2_text = wx.StaticText(self.panel_5, wx.ID_ANY, "About project:", style=wx.ALIGN_LEFT)
        self.about_txt = wx.TextCtrl(self.panel_5, wx.ID_ANY, "What your project is about")
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.panel_3 = wx.Panel(self.panel_1, wx.ID_ANY)
        self.Ok_button = wx.Button(self.panel_1, wx.ID_ANY, "button_1")
        self.panel_2 = wx.Panel(self.panel_1, wx.ID_ANY)
        self.Bind(wx.EVT_BUTTON, self.click_ok, id=self.Ok_button.GetId())

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: AboutDialog.__set_properties
        self.SetTitle("About Lottery Analysis")
        self.about_text.SetLabel(self.description)
        self.about2_text.SetLabel(self.details)
        self.Ok_button.SetLabel("OK")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AboutDialog.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(self.about_text, 0, wx.ALIGN_CENTER, 0)
        sizer_3.Add(self.about_title_txt, 0, wx.ALIGN_CENTER, 0)
        self.panel_4.SetSizer(sizer_3)
        sizer_1.Add(self.panel_4, 1, wx.EXPAND, 0)
        sizer_4.Add(self.about2_text, 0, wx.ALIGN_CENTER, 0)
        sizer_4.Add(self.about_txt, 0, wx.ALIGN_CENTER, 0)
        self.panel_5.SetSizer(sizer_4)
        sizer_1.Add(self.panel_5, 1, wx.EXPAND, 0)
        sizer_2.Add(self.panel_3, 1, wx.EXPAND, 0)
        sizer_2.Add(self.Ok_button, 0, wx.ALIGN_CENTER, 0)
        sizer_2.Add(self.panel_2, 1, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def set_description(self, str_description):
        self.description = str_description

    def set_details(self, str_details):
        self.details = str_details

    def click_ok(self, event):
        self.Close()

# end of class AboutDialog

