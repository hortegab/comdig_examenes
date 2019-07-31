#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Mpsk
# Generated: Wed Dec 21 14:21:17 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from b_Raised_cosine import b_Raised_cosine  # grc-generated hier_block
from b_accum_cc import b_accum_cc  # grc-generated hier_block
from b_quantizer_fb import b_quantizer_fb  # grc-generated hier_block
from b_sampler_cc import b_sampler_cc  # grc-generated hier_block
from b_tunner import b_tunner  # grc-generated hier_block
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import E3TRadio
import math
import numpy
import random
import sip


class MPSK(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Mpsk")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Mpsk")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "MPSK")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.Nq = Nq = 256
        self.Constelacion = Constelacion = [1.+0.j,   0.+1.j,   -1.+0.j,  0.-1.j ]
        self.Nbsym = Nbsym = int(math.log(len(Constelacion),2))
        self.Nbsam = Nbsam = math.log(Nq,2)
        self.samp_rate = samp_rate = 44000
        self.Np = Np = Nbsam/Nbsym
        self.Rs = Rs = samp_rate*Np
        self.Sps = Sps = 8
        self.Fs_cs = Fs_cs = Rs
        self.Fs_u = Fs_u = Fs_cs*Sps
        self.run_stop = run_stop = True
        self.rolloff = rolloff = 0.5
        self.ntaps = ntaps = 512
        self.Tmax_scope = Tmax_scope = 0.0005
        self.Rb = Rb = Rs*Nbsym
        self.M = M = len(Constelacion)
        self.Kruido = Kruido = 0.03
        self.Fs_9 = Fs_9 = Fs_u
        self.Fs_10 = Fs_10 = Fs_cs
        self.Fc = Fc = 2000000
        self.BWaudio = BWaudio = samp_rate/2
        self.B = B = Fs_u

        ##################################################
        # Blocks
        ##################################################
        self.pestana = Qt.QTabWidget()
        self.pestana_widget_0 = Qt.QWidget()
        self.pestana_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_0)
        self.pestana_grid_layout_0 = Qt.QGridLayout()
        self.pestana_layout_0.addLayout(self.pestana_grid_layout_0)
        self.pestana.addTab(self.pestana_widget_0, "P1.Fs_u")
        self.pestana_widget_1 = Qt.QWidget()
        self.pestana_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_1)
        self.pestana_grid_layout_1 = Qt.QGridLayout()
        self.pestana_layout_1.addLayout(self.pestana_grid_layout_1)
        self.pestana.addTab(self.pestana_widget_1, "P1.Fs_cs")
        self.pestana_widget_2 = Qt.QWidget()
        self.pestana_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_2)
        self.pestana_grid_layout_2 = Qt.QGridLayout()
        self.pestana_layout_2.addLayout(self.pestana_grid_layout_2)
        self.pestana.addTab(self.pestana_widget_2, "P1.samp_rate")
        self.pestana_widget_3 = Qt.QWidget()
        self.pestana_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_3)
        self.pestana_grid_layout_3 = Qt.QGridLayout()
        self.pestana_layout_3.addLayout(self.pestana_grid_layout_3)
        self.pestana.addTab(self.pestana_widget_3, "P1.Fs_9")
        self.pestana_widget_4 = Qt.QWidget()
        self.pestana_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_4)
        self.pestana_grid_layout_4 = Qt.QGridLayout()
        self.pestana_layout_4.addLayout(self.pestana_grid_layout_4)
        self.pestana.addTab(self.pestana_widget_4, "P1.Fs_10")
        self.pestana_widget_5 = Qt.QWidget()
        self.pestana_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_5)
        self.pestana_grid_layout_5 = Qt.QGridLayout()
        self.pestana_layout_5.addLayout(self.pestana_grid_layout_5)
        self.pestana.addTab(self.pestana_widget_5, "P2.B")
        self.pestana_widget_6 = Qt.QWidget()
        self.pestana_layout_6 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_6)
        self.pestana_grid_layout_6 = Qt.QGridLayout()
        self.pestana_layout_6.addLayout(self.pestana_grid_layout_6)
        self.pestana.addTab(self.pestana_widget_6, "P2.BWaudio")
        self.pestana_widget_7 = Qt.QWidget()
        self.pestana_layout_7 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_7)
        self.pestana_grid_layout_7 = Qt.QGridLayout()
        self.pestana_layout_7.addLayout(self.pestana_grid_layout_7)
        self.pestana.addTab(self.pestana_widget_7, "P2.PSD comparativa en antena Rx")
        self.pestana_widget_8 = Qt.QWidget()
        self.pestana_layout_8 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_8)
        self.pestana_grid_layout_8 = Qt.QGridLayout()
        self.pestana_layout_8.addLayout(self.pestana_grid_layout_8)
        self.pestana.addTab(self.pestana_widget_8, "P2.senal en 8")
        self.pestana_widget_9 = Qt.QWidget()
        self.pestana_layout_9 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_9)
        self.pestana_grid_layout_9 = Qt.QGridLayout()
        self.pestana_layout_9.addLayout(self.pestana_grid_layout_9)
        self.pestana.addTab(self.pestana_widget_9, "Rx Constelacion")
        self.top_layout.addWidget(self.pestana)
        self._Kruido_range = Range(0, 1, 0.001, 0.03, 200)
        self._Kruido_win = RangeWidget(self._Kruido_range, self.set_Kruido, "Nivel del Ruido", "counter_slider", float)
        self.top_grid_layout.addWidget(self._Kruido_win, 1,3,1,1)
        _run_stop_check_box = Qt.QCheckBox("Inicial/Parar")
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.iteritems())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 1,0,1,1)
        self.qtgui_time_sink_x_1_1_0_0_2 = qtgui.time_sink_c(
        	8, #size
        	Fs_10, #samp_rate
        	"Rx. b_sampler_c c. Puede verificar aqui  la frecuencia de muestreo Fs_10", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_1_0_0_2.set_update_time(0.10)
        self.qtgui_time_sink_x_1_1_0_0_2.set_y_axis(-0.2, 0.2)
        
        self.qtgui_time_sink_x_1_1_0_0_2.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1_1_0_0_2.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_1_0_0_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1_0_0_2.enable_autoscale(False)
        self.qtgui_time_sink_x_1_1_0_0_2.enable_grid(False)
        self.qtgui_time_sink_x_1_1_0_0_2.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_1_1_0_0_2.disable_legend()
        
        labels = ["Tx", "Rx", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_1_1_0_0_2.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1_1_0_0_2.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1_1_0_0_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1_0_0_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1_0_0_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1_0_0_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1_0_0_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1_0_0_2.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_1_0_0_2_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1_0_0_2.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_4.addWidget(self._qtgui_time_sink_x_1_1_0_0_2_win, 0,0,1,1)
        self.qtgui_time_sink_x_1_1_0_0_0 = qtgui.time_sink_f(
        	int(Tmax_scope*samp_rate), #size
        	samp_rate, #samp_rate
        	"Tx.Audio. Se puede mediar aqui el samp_rate", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_1_1_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_1_0_0_0.set_y_axis(-150, 150)
        
        self.qtgui_time_sink_x_1_1_0_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1_1_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_1_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_1_1_0_0_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_1_1_0_0_0.disable_legend()
        
        labels = ["cuantizado", "original, amplificado en 100 ", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_1_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1_0_0_0.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_2.addWidget(self._qtgui_time_sink_x_1_1_0_0_0_win, 1,0,1,1)
        self.qtgui_time_sink_x_1_1_0_0 = qtgui.time_sink_f(
        	int(Tmax_scope*samp_rate*Np), #size
        	Fs_cs, #samp_rate
        	"Tx. Packed to Unpacked. La frec de muestreo aqui es igual a la Rs,  a Fs_cs y a Fs_10", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_1_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_1_0_0.set_y_axis(-1, M)
        
        self.qtgui_time_sink_x_1_1_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1_1_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_1_0_0.enable_grid(False)
        self.qtgui_time_sink_x_1_1_0_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_1_1_0_0.disable_legend()
        
        labels = ["Tx", "Rx", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_1_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_1_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1_0_0.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_1.addWidget(self._qtgui_time_sink_x_1_1_0_0_win, 0,0,1,1)
        self.qtgui_time_sink_x_1_1 = qtgui.time_sink_c(
        	Sps*8, #size
        	Fs_u, #samp_rate
        	"Tx. USRP Sink. Fs_u puede verificarse a partir de medir el tiempo de muestreo", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1_1.set_y_axis(-1.5, 1.5)
        
        self.qtgui_time_sink_x_1_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1_1.enable_grid(False)
        self.qtgui_time_sink_x_1_1.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_1_1.disable_legend()
        
        labels = ["I", "Q", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_1_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_0.addWidget(self._qtgui_time_sink_x_1_1_win, 1,0,1,2)
        self.qtgui_time_sink_x_1_0_0 = qtgui.time_sink_c(
        	Sps*8, #size
        	Fs_9, #samp_rate
        	"Rx. b_Accum_c c.Puede verificar aqui el tiempo de muestreo y la frecuencia de muestreo Fs_9", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0_0.set_y_axis(-0.2, 0.2)
        
        self.qtgui_time_sink_x_1_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_1_0_0.disable_legend()
        
        labels = ["I", "Q", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_1_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0_0.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_3.addWidget(self._qtgui_time_sink_x_1_0_0_win, 0,0,1,2)
        self.qtgui_time_sink_x_1_0 = qtgui.time_sink_c(
        	Sps*10, #size
        	Fs_10, #samp_rate
        	"b_tunner. Senal en el tiempo", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0.set_y_axis(-0.3, 0.3)
        
        self.qtgui_time_sink_x_1_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_1_0.disable_legend()
        
        labels = ["I", "Q", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_1_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_8.addWidget(self._qtgui_time_sink_x_1_0_win, 0,0,1,2)
        self.qtgui_freq_sink_x_0_0_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	Fc, #fc
        	Fs_u, #bw
        	"Rx. PSD en antena. Mueva la palanca Avg a cero para un mejor promediado", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_1.set_y_axis(-80, -30)
        self.qtgui_freq_sink_x_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_1.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0_1.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_1.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0_0_1.enable_control_panel(True)
        
        if not True:
          self.qtgui_freq_sink_x_0_0_1.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_1.set_plot_pos_half(not True)
        
        labels = ["Sin Filtro Coseno Alzado", "Con Filtro Coseno Alzado", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_1.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_7.addWidget(self._qtgui_freq_sink_x_0_0_1_win, 0,0,1,2)
        self.qtgui_freq_sink_x_0_0_0 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"PSD senal Audio. Verifique aqui el ancho de banda atribuido a esta senal", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0_0_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_freq_sink_x_0_0_0.disable_legend()
        
        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0_0_0.set_plot_pos_half(not False)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_6.addWidget(self._qtgui_freq_sink_x_0_0_0_win, 0,0,1,2)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	Fc, #fc
        	Fs_u, #bw
        	"Tx PSD en antena. Verifique aqui el ancho de banda B", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_freq_sink_x_0_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_5.addWidget(self._qtgui_freq_sink_x_0_0_win, 0,0,1,2)
        self.qtgui_const_sink_x_0_1 = qtgui.const_sink_c(
        	1024*4, #size
        	"Rx - Tunner versus muestreador", #name
        	2 #number of inputs
        )
        self.qtgui_const_sink_x_0_1.set_update_time(0.10)
        self.qtgui_const_sink_x_0_1.set_y_axis(-.15, .15)
        self.qtgui_const_sink_x_0_1.set_x_axis(-.25, .25)
        self.qtgui_const_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_1.enable_autoscale(False)
        self.qtgui_const_sink_x_0_1.enable_grid(False)
        
        if not True:
          self.qtgui_const_sink_x_0_1.disable_legend()
        
        labels = ["Tunner", "Muestreador", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [1, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_1_win = sip.wrapinstance(self.qtgui_const_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_9.addWidget(self._qtgui_const_sink_x_0_1_win, 0,0,1,1)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((Constelacion), 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, Fs_u,True)
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(Nbsym, gr.GR_MSB_FIRST)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((100., ))
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.b_tunner_0 = b_tunner(
            fdesv=0,
            phi=0,
            samp_rate=Fs_u,
        )
        self.b_sampler_cc_0 = b_sampler_cc(
            DelayDiez=Sps-1,
            Sps=Sps,
        )
        self.b_quantizer_fb_0 = b_quantizer_fb(
            ValorPico=1,
        )
        self.b_accum_cc_0 = b_accum_cc(
            M=0,
            N=Sps,
        )
        self.b_Raised_cosine_0 = b_Raised_cosine(
            ntaps=ntaps,
            rolloff=rolloff,
            samp_rate=Fs_u,
            sps=Sps,
        )
        self.audio_source_0 = audio.source(samp_rate, "", True)
        self.E3TRadio_zero_order_hold2_cc_0 = E3TRadio.zero_order_hold2_cc(Sps)
        self.E3TRadio_usrp2usrp1_cc_0_0 = E3TRadio.usrp2usrp1_cc(Fs_u, 0.8, 0, 0., Kruido, 10., 0., B/2.)
        self.E3TRadio_usrp2usrp1_cc_0 = E3TRadio.usrp2usrp1_cc(Fs_u, 0.8, 0, 0., Kruido, 10., 0., B/2.)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_usrp2usrp1_cc_0, 0), (self.b_tunner_0, 0))    
        self.connect((self.E3TRadio_usrp2usrp1_cc_0, 0), (self.qtgui_freq_sink_x_0_0_1, 0))    
        self.connect((self.E3TRadio_usrp2usrp1_cc_0_0, 0), (self.qtgui_freq_sink_x_0_0_1, 1))    
        self.connect((self.E3TRadio_zero_order_hold2_cc_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.audio_source_0, 0), (self.b_quantizer_fb_0, 0))    
        self.connect((self.audio_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.audio_source_0, 0), (self.qtgui_freq_sink_x_0_0_0, 0))    
        self.connect((self.b_Raised_cosine_0, 0), (self.E3TRadio_usrp2usrp1_cc_0_0, 0))    
        self.connect((self.b_accum_cc_0, 0), (self.b_sampler_cc_0, 0))    
        self.connect((self.b_accum_cc_0, 0), (self.qtgui_time_sink_x_1_0_0, 0))    
        self.connect((self.b_quantizer_fb_0, 0), (self.blocks_char_to_float_0_0, 0))    
        self.connect((self.b_quantizer_fb_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))    
        self.connect((self.b_sampler_cc_0, 0), (self.qtgui_const_sink_x_0_1, 1))    
        self.connect((self.b_sampler_cc_0, 1), (self.qtgui_time_sink_x_1_1_0_0_2, 0))    
        self.connect((self.b_tunner_0, 0), (self.b_accum_cc_0, 0))    
        self.connect((self.b_tunner_0, 0), (self.qtgui_const_sink_x_0_1, 0))    
        self.connect((self.b_tunner_0, 0), (self.qtgui_time_sink_x_1_0, 0))    
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_1_1_0_0, 0))    
        self.connect((self.blocks_char_to_float_0_0, 0), (self.qtgui_time_sink_x_1_1_0_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_1_1_0_0_0, 1))    
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.blocks_char_to_float_0, 0))    
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.E3TRadio_usrp2usrp1_cc_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_time_sink_x_1_1, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.E3TRadio_zero_order_hold2_cc_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.b_Raised_cosine_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "MPSK")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_Nq(self):
        return self.Nq

    def set_Nq(self, Nq):
        self.Nq = Nq
        self.set_Nbsam(math.log(self.Nq,2))

    def get_Constelacion(self):
        return self.Constelacion

    def set_Constelacion(self, Constelacion):
        self.Constelacion = Constelacion
        self.set_M(len(self.Constelacion))
        self.set_Nbsym(int(math.log(len(self.Constelacion),2)))
        self.digital_chunks_to_symbols_xx_0.set_symbol_table((self.Constelacion))

    def get_Nbsym(self):
        return self.Nbsym

    def set_Nbsym(self, Nbsym):
        self.Nbsym = Nbsym
        self.set_Np(self.Nbsam/self.Nbsym)
        self.set_Rb(self.Rs*self.Nbsym)

    def get_Nbsam(self):
        return self.Nbsam

    def set_Nbsam(self, Nbsam):
        self.Nbsam = Nbsam
        self.set_Np(self.Nbsam/self.Nbsym)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_BWaudio(self.samp_rate/2)
        self.set_Rs(self.samp_rate*self.Np)
        self.qtgui_time_sink_x_1_1_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(0, self.samp_rate)

    def get_Np(self):
        return self.Np

    def set_Np(self, Np):
        self.Np = Np
        self.set_Rs(self.samp_rate*self.Np)

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.set_Fs_cs(self.Rs)
        self.set_Rb(self.Rs*self.Nbsym)

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_Fs_u(self.Fs_cs*self.Sps)
        self.E3TRadio_zero_order_hold2_cc_0.set_retardo(self.Sps)
        self.b_Raised_cosine_0.set_sps(self.Sps)
        self.b_accum_cc_0.set_N(self.Sps)
        self.b_sampler_cc_0.set_DelayDiez(self.Sps-1)
        self.b_sampler_cc_0.set_Sps(self.Sps)

    def get_Fs_cs(self):
        return self.Fs_cs

    def set_Fs_cs(self, Fs_cs):
        self.Fs_cs = Fs_cs
        self.set_Fs_10(self.Fs_cs)
        self.set_Fs_u(self.Fs_cs*self.Sps)
        self.qtgui_time_sink_x_1_1_0_0.set_samp_rate(self.Fs_cs)

    def get_Fs_u(self):
        return self.Fs_u

    def set_Fs_u(self, Fs_u):
        self.Fs_u = Fs_u
        self.set_B(self.Fs_u)
        self.set_Fs_9(self.Fs_u)
        self.b_Raised_cosine_0.set_samp_rate(self.Fs_u)
        self.b_tunner_0.set_samp_rate(self.Fs_u)
        self.blocks_throttle_0.set_sample_rate(self.Fs_u)
        self.qtgui_time_sink_x_1_1.set_samp_rate(self.Fs_u)
        self.qtgui_freq_sink_x_0_0_1.set_frequency_range(self.Fc, self.Fs_u)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.Fc, self.Fs_u)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff
        self.b_Raised_cosine_0.set_rolloff(self.rolloff)

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.b_Raised_cosine_0.set_ntaps(self.ntaps)

    def get_Tmax_scope(self):
        return self.Tmax_scope

    def set_Tmax_scope(self, Tmax_scope):
        self.Tmax_scope = Tmax_scope

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.qtgui_time_sink_x_1_1_0_0.set_y_axis(-1, self.M)

    def get_Kruido(self):
        return self.Kruido

    def set_Kruido(self, Kruido):
        self.Kruido = Kruido
        self.E3TRadio_usrp2usrp1_cc_0.set_Vruido(self.Kruido)
        self.E3TRadio_usrp2usrp1_cc_0_0.set_Vruido(self.Kruido)

    def get_Fs_9(self):
        return self.Fs_9

    def set_Fs_9(self, Fs_9):
        self.Fs_9 = Fs_9
        self.qtgui_time_sink_x_1_0_0.set_samp_rate(self.Fs_9)

    def get_Fs_10(self):
        return self.Fs_10

    def set_Fs_10(self, Fs_10):
        self.Fs_10 = Fs_10
        self.qtgui_time_sink_x_1_0.set_samp_rate(self.Fs_10)
        self.qtgui_time_sink_x_1_1_0_0_2.set_samp_rate(self.Fs_10)

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc
        self.qtgui_freq_sink_x_0_0_1.set_frequency_range(self.Fc, self.Fs_u)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.Fc, self.Fs_u)

    def get_BWaudio(self):
        return self.BWaudio

    def set_BWaudio(self, BWaudio):
        self.BWaudio = BWaudio

    def get_B(self):
        return self.B

    def set_B(self, B):
        self.B = B
        self.E3TRadio_usrp2usrp1_cc_0.set_BW(self.B/2.)
        self.E3TRadio_usrp2usrp1_cc_0_0.set_BW(self.B/2.)


def main(top_block_cls=MPSK, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
