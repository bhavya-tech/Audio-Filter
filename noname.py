# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1024,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer5.Add( self.m_filePicker1, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Import", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button2, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer5, 0, 0, 3 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2.Add( self.m_panel2, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_slider1 = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_INVERSE|wx.SL_MIN_MAX_LABELS|wx.SL_VALUE_LABEL|wx.SL_VERTICAL )
		bSizer3.Add( self.m_slider1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button21 = wx.Button( self, wx.ID_ANY, u"export", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button21, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer6, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.render )
		self.m_panel2.Bind( wx.EVT_SIZE, self.render )
		self.m_slider1.Bind( wx.EVT_SCROLL, self.render_power )
		self.m_panel3.Bind( wx.EVT_SIZE, self.render_power )
		self.m_panel4.Bind( wx.EVT_SIZE, self.render_output )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def render( self, event ):
		event.Skip()


	def render_power( self, event ):
		event.Skip()


	def render_output( self, event ):
		event.Skip()


