# -*- coding: utf-8 -*-
import wx
from multiplatform_widgets import widgets

class sessionManagerWindow(wx.Dialog):
 def __init__(self):
  super(sessionManagerWindow, self).__init__(parent=None, title="Session manager", size=wx.DefaultSize)
  panel = wx.Panel(self)
  sizer = wx.BoxSizer(wx.VERTICAL)
  label = wx.StaticText(panel, -1, u"Select a twitter account to start " + application.name, size=wx.DefaultSize)
  listSizer = wx.BoxSizer(wx.HORIZONTAL)
  self.list = widgets.list(panel, u"Account", style=wx.LC_SINGLE_SEL|wx.LC_REPORT)
  listSizer.Add(label, 0, wx.ALL, 5)
  listSizer.Add(self.list.list, 0, wx.ALL, 5)
  sizer.Add(listSizer, 0, wx.ALL, 5)
  self.new = wx.Button(panel, -1, u"New account", size=wx.DefaultSize)
  self.remove = wx.Button(panel, -1, _(u"Remove account"))
  ok = wx.Button(panel, wx.ID_OK, size=wx.DefaultSize)
  ok.SetDefault()
  cancel = wx.Button(panel, wx.ID_CANCEL, size=wx.DefaultSize)
  buttons = wx.BoxSizer(wx.HORIZONTAL)
  buttons.Add(self.new, 0, wx.ALL, 5)
  buttons.Add(ok, 0, wx.ALL, 5)
  buttons.Add(cancel, 0, wx.ALL, 5)
  sizer.Add(buttons, 0, wx.ALL, 5)
  panel.SetSizer(sizer)
  min = sizer.CalcMin()
  self.SetClientSize(min)

 def fill_list(self, sessionsList):
  for i in sessionsList:
   self.list.insert_item(False, i)
  if self.list.get_count() > 0:
   self.list.select_item(0)
  self.list.list.SetSize(self.list.list.GetBestSize())

 def ok(self, ev):
  if self.list.get_count() == 0:
   wx.MessageDialog(None, _(u"You need to configure an account."), _(u"Account Error"), wx.ICON_ERROR).ShowModal()
   return
  self.controller.do_ok()
  self.EndModal(wx.ID_OK)

 def new_account_dialog(self):
  return wx.MessageDialog(self, _(u"The request for the required Twitter authorisation to continue will be opened on your browser. You only need to do it once. Would you like to autorhise a new account now?"), _(u"Authorisation"), wx.YES_NO).ShowModal()

 def add_new_session_to_list(self):
  total = self.list.get_count()
  name = _(u"Authorised account %d") % (total+1)
  self.list.insert_item(False, name)
  if self.list.get_count() == 1:
   self.list.select_item(0)

 def show_unauthorised_error(self):
  wx.MessageDialog(None, _(u"Your access token is invalid or the authorisation has failed. Please try again."), _(u"Invalid user token"), wx.ICON_ERROR).ShowModal()

 def get_response(self):
  return self.ShowModal()

 def remove_account_dialog(self):
  return wx.MessageDialog(self, _(u"Do you really want to delete this account?"), _(u"Remove account"), wx.YES_NO).ShowModal()

 def get_selected(self):
  return self.list.get_selected()

 def remove_session(self, sessionID):
  self.list.remove_item(sessionID)

