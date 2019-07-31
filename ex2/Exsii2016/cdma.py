#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: BPSK_Decisor
# Author: Homero Ortega. Universidad industrial de Santander
# Generated: Fri Feb  3 23:22:49 2017
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
from b_Eye_Diagram import b_Eye_Diagram  # grc-generated hier_block
from b_Raised_cosine import b_Raised_cosine  # grc-generated hier_block
from b_USRP_2_USRP import b_USRP_2_USRP  # grc-generated hier_block
from b_de_ds_spreadspect_cc import b_de_ds_spreadspect_cc  # grc-generated hier_block
from b_ds_spreadspect_cc import b_ds_spreadspect_cc  # grc-generated hier_block
from b_tunner_sampler import b_tunner_sampler  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import E3TRadio
import cmath
import math
import random
import sip


class cdma(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "BPSK_Decisor")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("BPSK_Decisor")
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

        self.settings = Qt.QSettings("GNU Radio", "cdma")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.B = B = 3000000
        self.RollOff = RollOff = 0.5
        self.BW = BW = B/2
        self.SF = SF = 16
        self.Rch = Rch = 2*BW/(1+RollOff)
        self.Constelacion1 = Constelacion1 = [1.  +  1.j,  -1  +  1.j,   -1.  -  1.j,   1.  -  1.j ]
        self.spch = spch = 4
        self.Rs = Rs = Rch/SF
        self.ChipsSysDelay = ChipsSysDelay = 28
        self.Bps1 = Bps1 = int(math.log(len(Constelacion1),2))
        self.samp_rate = samp_rate = Rch*spch
        self.run_stop = run_stop = True
        self.c1 = c1 = [1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,1,-1,1,-1 ]
        self.SymSysDelay = SymSysDelay = int(math.ceil(float(ChipsSysDelay)/SF))
        self.Rb1 = Rb1 = Rs*Bps1
        self.Nscope_span = Nscope_span = 1
        self.Fc = Fc = 80e6
        self.Canal_phi_offset = Canal_phi_offset = 0.
        self.Canal_Ruido = Canal_Ruido = 0.1
        self.Canal_Foffset = Canal_Foffset = 0.

        ##################################################
        # Blocks
        ##################################################
        self.Instrumentos = Qt.QTabWidget()
        self.Instrumentos_widget_0 = Qt.QWidget()
        self.Instrumentos_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Instrumentos_widget_0)
        self.Instrumentos_grid_layout_0 = Qt.QGridLayout()
        self.Instrumentos_layout_0.addLayout(self.Instrumentos_grid_layout_0)
        self.Instrumentos.addTab(self.Instrumentos_widget_0, "Tx tiempo")
        self.Instrumentos_widget_1 = Qt.QWidget()
        self.Instrumentos_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Instrumentos_widget_1)
        self.Instrumentos_grid_layout_1 = Qt.QGridLayout()
        self.Instrumentos_layout_1.addLayout(self.Instrumentos_grid_layout_1)
        self.Instrumentos.addTab(self.Instrumentos_widget_1, "PSD")
        self.Instrumentos_widget_2 = Qt.QWidget()
        self.Instrumentos_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Instrumentos_widget_2)
        self.Instrumentos_grid_layout_2 = Qt.QGridLayout()
        self.Instrumentos_layout_2.addLayout(self.Instrumentos_grid_layout_2)
        self.Instrumentos.addTab(self.Instrumentos_widget_2, "Tunning")
        self.Instrumentos_widget_3 = Qt.QWidget()
        self.Instrumentos_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Instrumentos_widget_3)
        self.Instrumentos_grid_layout_3 = Qt.QGridLayout()
        self.Instrumentos_layout_3.addLayout(self.Instrumentos_grid_layout_3)
        self.Instrumentos.addTab(self.Instrumentos_widget_3, "Rx tiempo")
        self.Instrumentos_widget_4 = Qt.QWidget()
        self.Instrumentos_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Instrumentos_widget_4)
        self.Instrumentos_grid_layout_4 = Qt.QGridLayout()
        self.Instrumentos_layout_4.addLayout(self.Instrumentos_grid_layout_4)
        self.Instrumentos.addTab(self.Instrumentos_widget_4, "Constelaciones")
        self.top_grid_layout.addWidget(self.Instrumentos, 1,0,1,3)
        self._ChipsSysDelay_range = Range(0, 500, 1, 28, 200)
        self._ChipsSysDelay_win = RangeWidget(self._ChipsSysDelay_range, self.set_ChipsSysDelay, "Retardo en chips del sistema Tx-Rx", "counter_slider", int)
        self.top_grid_layout.addWidget(self._ChipsSysDelay_win, 0,2,1,1)
        self._Canal_Ruido_range = Range(0., 1., 1./1000., 0.1, 200)
        self._Canal_Ruido_win = RangeWidget(self._Canal_Ruido_range, self.set_Canal_Ruido, "Ruido en el canal", "counter_slider", float)
        self.top_grid_layout.addWidget(self._Canal_Ruido_win, 0,1,1,1)
        _run_stop_check_box = Qt.QCheckBox("run_stop")
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.iteritems())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0,0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=spch,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_c(
        	Nscope_span*SF, #size
        	Rch, #samp_rate
        	"Tx. Usuario con sobremuestreo", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1.set_y_axis(-1.5, 1.5)
        
        self.qtgui_time_sink_x_0_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_0_1.disable_legend()
        
        labels = ["Re", "Im", "", "", "",
                  "", "", "", "", ""]
        widths = [3, 1, 1, 1, 1,
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
                    self.qtgui_time_sink_x_0_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.Instrumentos_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_1_win, 0,0,1,1)
        self.qtgui_time_sink_x_0_0_1 = qtgui.time_sink_c(
        	Nscope_span*SF, #size
        	Rch, #samp_rate
        	"comparacion de senal enviada y recibida", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_1.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_0_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_0_0_1.disable_legend()
        
        labels = ["Tx (Re)", "Tx(Im)", "Rx (Re)", "Rx(Im)", "",
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
        
        for i in xrange(2*2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_0_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1.pyqwidget(), Qt.QWidget)
        self.Instrumentos_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_0_1_win, 3,0,1,1)
        self.qtgui_time_sink_x_0_0_0_1 = qtgui.time_sink_c(
        	Nscope_span*SF*spch, #size
        	samp_rate, #samp_rate
        	"Tx.salida del Raised Cosine", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_1.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_0_0_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_0_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_1.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_0_0_0_1.disable_legend()
        
        labels = ["Re", "Im", "", "", "",
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
                    self.qtgui_time_sink_x_0_0_0_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_0_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_1.pyqwidget(), Qt.QWidget)
        self.Instrumentos_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_0_0_1_win, 3,0,1,1)
        self.qtgui_time_sink_x_0_0_0_0 = qtgui.time_sink_c(
        	Nscope_span*SF, #size
        	Rch, #samp_rate
        	"Rx.Multiplicador del de_ds_spreadspect_cc", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0.set_y_axis(-0.2, 0.2)
        
        self.qtgui_time_sink_x_0_0_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_0_0_0_0.disable_legend()
        
        labels = ["", "", "", "", "",
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
                    self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.Instrumentos_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_0_0_0_win, 1,0,1,1)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_c(
        	Nscope_span*SF, #size
        	Rch, #samp_rate
        	"Tx.senal ds ss", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_0_0_0.disable_legend()
        
        labels = ["Re", "Im", "", "", "",
                  "", "", "", "", ""]
        widths = [4, 4, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 3, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.Instrumentos_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_0_0_win, 2,0,1,1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_c(
        	Nscope_span*SF, #size
        	Rch, #samp_rate
        	"Tx.cod", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()
        
        labels = ["Re", "Im", "", "", "",
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
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.Instrumentos_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_0_win, 1,0,1,1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-80, 10)
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_freq_sink_x_0_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)
        
        labels = ["Tx.Info del usuario", "Rx.Salida del USRP_2_USRP", "Rx. Salida del usrp2usrp", "", "",
                  "", "", "", "", ""]
        widths = [3, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.Instrumentos_grid_layout_1.addWidget(self._qtgui_freq_sink_x_0_0_win, 1,0,1,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	Rch, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-80, 10)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["Tx.Info del usuario", "Tx. Senal ensanchada", "Rx. Salida del usrp2usrp", "", "",
                  "", "", "", "", ""]
        widths = [3, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.Instrumentos_grid_layout_1.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,1)
        self.qtgui_const_sink_x_0_0_2 = qtgui.const_sink_c(
        	1024, #size
        	"Rx", #name
        	3 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_2.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_2.set_y_axis(-0.2, 0.2)
        self.qtgui_const_sink_x_0_0_2.set_x_axis(-0.2, 0.2)
        self.qtgui_const_sink_x_0_0_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_2.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0_2.enable_grid(False)
        
        if not True:
          self.qtgui_const_sink_x_0_0_2.disable_legend()
        
        labels = ["En el canal", "Salida del multiplicador", "salida del muestreador", "", "",
                  "", "", "", "", ""]
        widths = [4, 6, 12, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_2.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_2.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_2.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_2.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_2.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_2.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_0_2_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_2.pyqwidget(), Qt.QWidget)
        self.Instrumentos_grid_layout_4.addWidget(self._qtgui_const_sink_x_0_0_2_win, 1,1,1,1)
        self.qtgui_const_sink_x_0_0_1_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_1_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_1_0_0.set_y_axis(-0.2, 0.2)
        self.qtgui_const_sink_x_0_0_1_0_0.set_x_axis(-0.2, 0.2)
        self.qtgui_const_sink_x_0_0_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_1_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0_1_0_0.enable_grid(False)
        
        if not True:
          self.qtgui_const_sink_x_0_0_1_0_0.disable_legend()
        
        labels = ["Tx", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_1_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_1_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_1_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_1_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_0_1_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_1_0_0.pyqwidget(), Qt.QWidget)
        self.Instrumentos_grid_layout_1.addWidget(self._qtgui_const_sink_x_0_0_1_0_0_win, 2,0,1,1)
        self.qtgui_const_sink_x_0_0_1 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_1.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_1.set_y_axis(-0.2, 0.2)
        self.qtgui_const_sink_x_0_0_1.set_x_axis(-0.2, 0.2)
        self.qtgui_const_sink_x_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_1.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0_1.enable_grid(False)
        
        if not True:
          self.qtgui_const_sink_x_0_0_1.disable_legend()
        
        labels = ["Tx", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_0_1_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_1.pyqwidget(), Qt.QWidget)
        self.Instrumentos_grid_layout_4.addWidget(self._qtgui_const_sink_x_0_0_1_win, 3,0,1,2)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis(-0.2, 0.2)
        self.qtgui_const_sink_x_0_0.set_x_axis(-0.2, 0.2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        
        if not True:
          self.qtgui_const_sink_x_0_0.disable_legend()
        
        labels = ["Tx", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.Instrumentos_grid_layout_4.addWidget(self._qtgui_const_sink_x_0_0_win, 2,0,1,2)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"Tx- usuario", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        
        if not True:
          self.qtgui_const_sink_x_0.disable_legend()
        
        labels = ["Tx", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.Instrumentos_grid_layout_4.addWidget(self._qtgui_const_sink_x_0_win, 1,0,1,1)
        self.low_pass_filter_0_0_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, Rs, Rs/16., firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, Rch, Rs, Rs/16., firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, BW, BW/16., firdes.WIN_HAMMING, 6.76))
        self.blocks_vector_source_x_0 = blocks.vector_source_c([ -1  +  1.j,  -1  +  1.j,  -1  +  1.j, -1  +  1.j], True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.1, ))
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, SymSysDelay)
        self.blocks_complex_to_float_0_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.b_tunner_sampler_0 = b_tunner_sampler(
            DelayTuningInicial=0,
            GrosorLineasOjo=20,
            samp_rate=samp_rate,
            sps=spch,
            AlphaLineasOjo=0.5,
        )
        self.Instrumentos_grid_layout_2.addWidget(self.b_tunner_sampler_0, 1,0,1,1)
        self.b_ds_spreadspect_cc_0 = b_ds_spreadspect_cc(
            SF=SF,
            codigo=c1,
        )
        self.b_de_ds_spreadspect_cc_0 = b_de_ds_spreadspect_cc(
            ChipsSysDelay=ChipsSysDelay,
            SF=SF,
            codigo=c1,
        )
        self.b_USRP_2_USRP_0_0 = b_USRP_2_USRP(
            B=B,
            Fc=Fc,
            Foffset=Canal_Foffset,
            Katt=10.,
            Phoffset=Canal_phi_offset,
            Toffset=0,
            Vruido=Canal_Ruido,
            samp_rate=samp_rate,
        )
        self.b_Raised_cosine_0 = b_Raised_cosine(
            ntaps=spch*4,
            rolloff=RollOff,
            samp_rate=samp_rate,
            sps=spch,
        )
        self.b_Eye_Diagram_0 = b_Eye_Diagram(
            AlphaLineas=0.5,
            Delay=0,
            GrosorLineas=20,
            N_eyes=2,
            Samprate=samp_rate,
            Sps=SF,
            Title="Rx. b_de_ds_spreadspect_cc. Diagrama de Ojo",
            Ymax=.15,
            Ymin=-.15,
        )
        self.Instrumentos_grid_layout_3.addWidget(self.b_Eye_Diagram_0, 2,0,1,1)
        self.E3TRadio_zero_order_hold2_cc_0 = E3TRadio.zero_order_hold2_cc(spch)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_zero_order_hold2_cc_0, 0), (self.low_pass_filter_0_0_0_0, 0))    
        self.connect((self.b_Raised_cosine_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.b_USRP_2_USRP_0_0, 0), (self.low_pass_filter_0_0, 0))    
        self.connect((self.b_USRP_2_USRP_0_0, 0), (self.qtgui_freq_sink_x_0_0, 1))    
        self.connect((self.b_USRP_2_USRP_0_0, 0), (self.qtgui_time_sink_x_0_0_0_1, 0))    
        self.connect((self.b_USRP_2_USRP_0_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.b_de_ds_spreadspect_cc_0, 3), (self.blocks_complex_to_float_0, 0))    
        self.connect((self.b_de_ds_spreadspect_cc_0, 1), (self.blocks_complex_to_float_0_0, 0))    
        self.connect((self.b_de_ds_spreadspect_cc_0, 1), (self.qtgui_const_sink_x_0_0_2, 2))    
        self.connect((self.b_de_ds_spreadspect_cc_0, 2), (self.qtgui_const_sink_x_0_0_2, 1))    
        self.connect((self.b_de_ds_spreadspect_cc_0, 2), (self.qtgui_time_sink_x_0_0_0_0, 0))    
        self.connect((self.b_de_ds_spreadspect_cc_0, 0), (self.qtgui_time_sink_x_0_0_1, 1))    
        self.connect((self.b_ds_spreadspect_cc_0, 2), (self.E3TRadio_zero_order_hold2_cc_0, 0))    
        self.connect((self.b_ds_spreadspect_cc_0, 0), (self.b_Raised_cosine_0, 0))    
        self.connect((self.b_ds_spreadspect_cc_0, 2), (self.low_pass_filter_0_0_0, 0))    
        self.connect((self.b_ds_spreadspect_cc_0, 2), (self.qtgui_const_sink_x_0, 0))    
        self.connect((self.b_ds_spreadspect_cc_0, 0), (self.qtgui_freq_sink_x_0, 1))    
        self.connect((self.b_ds_spreadspect_cc_0, 1), (self.qtgui_time_sink_x_0_0, 0))    
        self.connect((self.b_ds_spreadspect_cc_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))    
        self.connect((self.b_ds_spreadspect_cc_0, 2), (self.qtgui_time_sink_x_0_1, 0))    
        self.connect((self.b_tunner_sampler_0, 0), (self.b_de_ds_spreadspect_cc_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.b_Eye_Diagram_0, 0))    
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.b_Eye_Diagram_0, 1))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0_0_1, 0))    
        self.connect((self.blocks_null_source_0, 0), (self.qtgui_const_sink_x_0_0, 0))    
        self.connect((self.blocks_null_source_0, 1), (self.qtgui_const_sink_x_0_0_1, 0))    
        self.connect((self.blocks_null_source_0, 2), (self.qtgui_const_sink_x_0_0_1_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.b_USRP_2_USRP_0_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.b_ds_spreadspect_cc_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_delay_0, 0))    
        self.connect((self.low_pass_filter_0_0, 0), (self.b_tunner_sampler_0, 0))    
        self.connect((self.low_pass_filter_0_0_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.low_pass_filter_0_0_0_0, 0), (self.qtgui_freq_sink_x_0_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_const_sink_x_0_0_2, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "cdma")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_B(self):
        return self.B

    def set_B(self, B):
        self.B = B
        self.set_BW(self.B/2)
        self.b_USRP_2_USRP_0_0.set_B(self.B)

    def get_RollOff(self):
        return self.RollOff

    def set_RollOff(self, RollOff):
        self.RollOff = RollOff
        self.set_Rch(2*self.BW/(1+self.RollOff))
        self.b_Raised_cosine_0.set_rolloff(self.RollOff)

    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW
        self.set_Rch(2*self.BW/(1+self.RollOff))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW, self.BW/16., firdes.WIN_HAMMING, 6.76))

    def get_SF(self):
        return self.SF

    def set_SF(self, SF):
        self.SF = SF
        self.set_Rs(self.Rch/self.SF)
        self.set_SymSysDelay(int(math.ceil(float(self.ChipsSysDelay)/self.SF)))
        self.b_Eye_Diagram_0.set_Sps(self.SF)
        self.b_de_ds_spreadspect_cc_0.set_SF(self.SF)
        self.b_ds_spreadspect_cc_0.set_SF(self.SF)

    def get_Rch(self):
        return self.Rch

    def set_Rch(self, Rch):
        self.Rch = Rch
        self.set_Rs(self.Rch/self.SF)
        self.set_samp_rate(self.Rch*self.spch)
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(1, self.Rch, self.Rs, self.Rs/16., firdes.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.Rch)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.Rch)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.Rch)
        self.qtgui_time_sink_x_0_0_0_0.set_samp_rate(self.Rch)
        self.qtgui_time_sink_x_0_0_1.set_samp_rate(self.Rch)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.Rch)

    def get_Constelacion1(self):
        return self.Constelacion1

    def set_Constelacion1(self, Constelacion1):
        self.Constelacion1 = Constelacion1
        self.set_Bps1(int(math.log(len(self.Constelacion1),2)))

    def get_spch(self):
        return self.spch

    def set_spch(self, spch):
        self.spch = spch
        self.set_samp_rate(self.Rch*self.spch)
        self.E3TRadio_zero_order_hold2_cc_0.set_retardo(self.spch)
        self.b_Raised_cosine_0.set_ntaps(self.spch*4)
        self.b_Raised_cosine_0.set_sps(self.spch)
        self.b_tunner_sampler_0.set_sps(self.spch)

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.set_Rb1(self.Rs*self.Bps1)
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(1, self.Rch, self.Rs, self.Rs/16., firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.Rs, self.Rs/16., firdes.WIN_HAMMING, 6.76))

    def get_ChipsSysDelay(self):
        return self.ChipsSysDelay

    def set_ChipsSysDelay(self, ChipsSysDelay):
        self.ChipsSysDelay = ChipsSysDelay
        self.set_SymSysDelay(int(math.ceil(float(self.ChipsSysDelay)/self.SF)))
        self.b_de_ds_spreadspect_cc_0.set_ChipsSysDelay(self.ChipsSysDelay)

    def get_Bps1(self):
        return self.Bps1

    def set_Bps1(self, Bps1):
        self.Bps1 = Bps1
        self.set_Rb1(self.Rs*self.Bps1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.b_Eye_Diagram_0.set_Samprate(self.samp_rate)
        self.b_Raised_cosine_0.set_samp_rate(self.samp_rate)
        self.b_USRP_2_USRP_0_0.set_samp_rate(self.samp_rate)
        self.b_tunner_sampler_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW, self.BW/16., firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.Rs, self.Rs/16., firdes.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0_0_0_1.set_samp_rate(self.samp_rate)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_c1(self):
        return self.c1

    def set_c1(self, c1):
        self.c1 = c1
        self.b_de_ds_spreadspect_cc_0.set_codigo(self.c1)
        self.b_ds_spreadspect_cc_0.set_codigo(self.c1)

    def get_SymSysDelay(self):
        return self.SymSysDelay

    def set_SymSysDelay(self, SymSysDelay):
        self.SymSysDelay = SymSysDelay
        self.blocks_delay_0.set_dly(self.SymSysDelay)

    def get_Rb1(self):
        return self.Rb1

    def set_Rb1(self, Rb1):
        self.Rb1 = Rb1

    def get_Nscope_span(self):
        return self.Nscope_span

    def set_Nscope_span(self, Nscope_span):
        self.Nscope_span = Nscope_span

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc
        self.b_USRP_2_USRP_0_0.set_Fc(self.Fc)

    def get_Canal_phi_offset(self):
        return self.Canal_phi_offset

    def set_Canal_phi_offset(self, Canal_phi_offset):
        self.Canal_phi_offset = Canal_phi_offset
        self.b_USRP_2_USRP_0_0.set_Phoffset(self.Canal_phi_offset)

    def get_Canal_Ruido(self):
        return self.Canal_Ruido

    def set_Canal_Ruido(self, Canal_Ruido):
        self.Canal_Ruido = Canal_Ruido
        self.b_USRP_2_USRP_0_0.set_Vruido(self.Canal_Ruido)

    def get_Canal_Foffset(self):
        return self.Canal_Foffset

    def set_Canal_Foffset(self, Canal_Foffset):
        self.Canal_Foffset = Canal_Foffset
        self.b_USRP_2_USRP_0_0.set_Foffset(self.Canal_Foffset)


def main(top_block_cls=cdma, options=None):

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
