#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Z Ofdm Multiconstelacion
# Generated: Fri Dec 22 08:49:44 2017
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
from b_MS import b_MS  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import cmath
import math
import numpy
import random
import sip


class z_OFDM_MultiConstelacion(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Z Ofdm Multiconstelacion")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Z Ofdm Multiconstelacion")
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

        self.settings = Qt.QSettings("GNU Radio", "z_OFDM_MultiConstelacion")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.Tsym = Tsym = 3.2e-6
        self.Rs = Rs = 1/Tsym
        self.N = N = 16
        self.B = B = Rs*N
        self.Fc = Fc = 2*B
        self.f = f = 902.1875e6
        self.Fmax = Fmax = Fc+B/2
        self.Fc_dado = Fc_dado = 900e6
        self.sobremuestreo = sobremuestreo = 4
        self.samp_rate = samp_rate = int(Rs*N)
        self.run_stop = run_stop = True
        self.k = k = (f-Fc_dado)/Rs
        self.Kruido = Kruido = 0.035
        self.Fmuestreo = Fmuestreo = int(Fmax*8)
        self.Constelacion3 = Constelacion3 = [1+.0j,-1+.0j, .0+1j,0 -1j,  0.7+0.7j,  0.7-0.7j,  -0.7+0.7j,  -0.7-0.7j ]
        self.Constelacion2 = Constelacion2 = [1.5+.0j,-1.5+.0j, .0+1.5j,0 -1.5j, 0.5+.0j,-0.5+.0j, .0+0.5j,0 -0.5j ]
        self.Constelacion1 = Constelacion1 = [1+.0j,-1+.0j ]

        ##################################################
        # Blocks
        ##################################################
        self.pestana = Qt.QTabWidget()
        self.pestana_widget_0 = Qt.QWidget()
        self.pestana_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_0)
        self.pestana_grid_layout_0 = Qt.QGridLayout()
        self.pestana_layout_0.addLayout(self.pestana_grid_layout_0)
        self.pestana.addTab(self.pestana_widget_0, "En el tiempo")
        self.pestana_widget_1 = Qt.QWidget()
        self.pestana_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_1)
        self.pestana_grid_layout_1 = Qt.QGridLayout()
        self.pestana_layout_1.addLayout(self.pestana_grid_layout_1)
        self.pestana.addTab(self.pestana_widget_1, "Constelacion")
        self.pestana_widget_2 = Qt.QWidget()
        self.pestana_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_2)
        self.pestana_grid_layout_2 = Qt.QGridLayout()
        self.pestana_layout_2.addLayout(self.pestana_grid_layout_2)
        self.pestana.addTab(self.pestana_widget_2, "Espectro")
        self.top_grid_layout.addWidget(self.pestana, 3,0,1,3)
        self._Kruido_range = Range(0, 1, 0.005, 0.035, 200)
        self._Kruido_win = RangeWidget(self._Kruido_range, self.set_Kruido, "Nivel del Ruido", "counter_slider", float)
        self.top_grid_layout.addWidget(self._Kruido_win, 1,0,1,1)
        _run_stop_check_box = Qt.QCheckBox("Inicial/Parar")
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.iteritems())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0,0,1,1)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=2,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_1_1 = qtgui.time_sink_c(
        	64, #size
        	Rs, #samp_rate
        	"Rx De-TDM", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1_1.set_y_axis(-2, 2)
        
        self.qtgui_time_sink_x_1_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1_1.enable_grid(False)
        self.qtgui_time_sink_x_1_1.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_1_1.disable_legend()
        
        labels = ["Re", "Im", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 2, -1, -1, -1,
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
        self.qtgui_time_sink_x_1 = qtgui.time_sink_c(
        	64, #size
        	samp_rate, #samp_rate
        	"u[n]", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-2, 2)
        
        self.qtgui_time_sink_x_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_1.disable_legend()
        
        labels = ["Re", "Im", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 2, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_0.addWidget(self._qtgui_time_sink_x_1_win, 0,0,1,2)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	Fc_dado, #fc
        	samp_rate*2, #bw
        	"Ss(f)", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [3, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["red", "red", "green", "black", "cyan",
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
        self.pestana_grid_layout_2.addWidget(self._qtgui_freq_sink_x_0_0_win, 1,1,1,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Sz(f)", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [3, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_2.addWidget(self._qtgui_freq_sink_x_0_win, 0,1,1,1)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"p[n]", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        
        if not True:
          self.qtgui_const_sink_x_0_0.disable_legend()
        
        labels = ["Rx", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [1, 0, 0, 0, 0,
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
        self.pestana_grid_layout_1.addWidget(self._qtgui_const_sink_x_0_0_win, 0,1,1,1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        
        if not True:
          self.qtgui_const_sink_x_0.disable_legend()
        
        labels = ["Tx", "Rx DeTDM", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [1, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
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
        self.pestana_grid_layout_1.addWidget(self._qtgui_const_sink_x_0_win, 0,0,1,1)
        self.fft_vxx_1_0 = fft.fft_vcc(N, True, (), False, 1)
        self.fft_vxx_1 = fft.fft_vcc(N, False, (), False, 1)
        self.blocks_vector_to_stream_2 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, N)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, N)
        self.blocks_streams_to_vector_0 = blocks.streams_to_vector(gr.sizeof_gr_complex*1, N)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, N)
        self.blocks_stream_to_streams_0 = blocks.stream_to_streams(gr.sizeof_gr_complex*1, N)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_3 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_2 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_1_1_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_1_1 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_1_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_1 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_2_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_2 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_1 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_0_1_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_0_1 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((1./N, ))
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.b_MS_0 = b_MS(
            Constelacion=Constelacion1,
            N=1,
        )
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, Kruido, 48)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.b_MS_0, 0), (self.blocks_streams_to_vector_0, 7))    
        self.connect((self.b_MS_0, 0), (self.qtgui_const_sink_x_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_stream_to_vector_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.blocks_null_source_0, 0), (self.blocks_streams_to_vector_0, 0))    
        self.connect((self.blocks_null_source_0, 0), (self.blocks_streams_to_vector_0, 1))    
        self.connect((self.blocks_null_source_0, 0), (self.blocks_streams_to_vector_0, 10))    
        self.connect((self.blocks_null_source_0, 0), (self.blocks_streams_to_vector_0, 11))    
        self.connect((self.blocks_null_source_0, 0), (self.blocks_streams_to_vector_0, 12))    
        self.connect((self.blocks_null_source_0, 0), (self.blocks_streams_to_vector_0, 13))    
        self.connect((self.blocks_null_source_0, 0), (self.blocks_streams_to_vector_0, 14))    
        self.connect((self.blocks_null_source_0, 0), (self.blocks_streams_to_vector_0, 15))    
        self.connect((self.blocks_null_source_0, 0), (self.blocks_streams_to_vector_0, 2))    
        self.connect((self.blocks_null_source_0, 0), (self.blocks_streams_to_vector_0, 3))    
        self.connect((self.blocks_null_source_0, 0), (self.blocks_streams_to_vector_0, 4))    
        self.connect((self.blocks_null_source_0, 0), (self.blocks_streams_to_vector_0, 5))    
        self.connect((self.blocks_null_source_0, 0), (self.blocks_streams_to_vector_0, 6))    
        self.connect((self.blocks_null_source_0, 0), (self.blocks_streams_to_vector_0, 8))    
        self.connect((self.blocks_null_source_0, 0), (self.blocks_streams_to_vector_0, 9))    
        self.connect((self.blocks_stream_to_streams_0, 0), (self.blocks_null_sink_0, 0))    
        self.connect((self.blocks_stream_to_streams_0, 1), (self.blocks_null_sink_0_0, 0))    
        self.connect((self.blocks_stream_to_streams_0, 3), (self.blocks_null_sink_0_0_0, 0))    
        self.connect((self.blocks_stream_to_streams_0, 8), (self.blocks_null_sink_0_0_0_0, 0))    
        self.connect((self.blocks_stream_to_streams_0, 12), (self.blocks_null_sink_0_0_0_1, 0))    
        self.connect((self.blocks_stream_to_streams_0, 15), (self.blocks_null_sink_0_0_0_1_0, 0))    
        self.connect((self.blocks_stream_to_streams_0, 5), (self.blocks_null_sink_0_0_1, 0))    
        self.connect((self.blocks_stream_to_streams_0, 10), (self.blocks_null_sink_0_0_2, 0))    
        self.connect((self.blocks_stream_to_streams_0, 13), (self.blocks_null_sink_0_0_2_0, 0))    
        self.connect((self.blocks_stream_to_streams_0, 2), (self.blocks_null_sink_0_1, 0))    
        self.connect((self.blocks_stream_to_streams_0, 6), (self.blocks_null_sink_0_1_0, 0))    
        self.connect((self.blocks_stream_to_streams_0, 11), (self.blocks_null_sink_0_1_1, 0))    
        self.connect((self.blocks_stream_to_streams_0, 14), (self.blocks_null_sink_0_1_1_0, 0))    
        self.connect((self.blocks_stream_to_streams_0, 4), (self.blocks_null_sink_0_2, 0))    
        self.connect((self.blocks_stream_to_streams_0, 9), (self.blocks_null_sink_0_3, 0))    
        self.connect((self.blocks_stream_to_streams_0, 7), (self.qtgui_const_sink_x_0, 1))    
        self.connect((self.blocks_stream_to_streams_0, 7), (self.qtgui_time_sink_x_1_1, 0))    
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.fft_vxx_1_0, 0))    
        self.connect((self.blocks_streams_to_vector_0, 0), (self.fft_vxx_1, 0))    
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_vector_to_stream_2, 0), (self.blocks_stream_to_streams_0, 0))    
        self.connect((self.blocks_vector_to_stream_2, 0), (self.qtgui_const_sink_x_0_0, 0))    
        self.connect((self.blocks_vector_to_stream_2, 0), (self.qtgui_time_sink_x_1, 0))    
        self.connect((self.fft_vxx_1, 0), (self.blocks_vector_to_stream_0, 0))    
        self.connect((self.fft_vxx_1_0, 0), (self.blocks_vector_to_stream_2, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_0_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "z_OFDM_MultiConstelacion")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_Tsym(self):
        return self.Tsym

    def set_Tsym(self, Tsym):
        self.Tsym = Tsym
        self.set_Rs(1/self.Tsym)

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.set_B(self.Rs*self.N)
        self.set_k((self.f-self.Fc_dado)/self.Rs)
        self.set_samp_rate(int(self.Rs*self.N))
        self.qtgui_time_sink_x_1_1.set_samp_rate(self.Rs)

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.set_B(self.Rs*self.N)
        self.set_samp_rate(int(self.Rs*self.N))
        self.blocks_multiply_const_vxx_0.set_k((1./self.N, ))

    def get_B(self):
        return self.B

    def set_B(self, B):
        self.B = B
        self.set_Fc(2*self.B)
        self.set_Fmax(self.Fc+self.B/2)

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc
        self.set_Fmax(self.Fc+self.B/2)

    def get_f(self):
        return self.f

    def set_f(self, f):
        self.f = f
        self.set_k((self.f-self.Fc_dado)/self.Rs)

    def get_Fmax(self):
        return self.Fmax

    def set_Fmax(self, Fmax):
        self.Fmax = Fmax
        self.set_Fmuestreo(int(self.Fmax*8))

    def get_Fc_dado(self):
        return self.Fc_dado

    def set_Fc_dado(self, Fc_dado):
        self.Fc_dado = Fc_dado
        self.set_k((self.f-self.Fc_dado)/self.Rs)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.Fc_dado, self.samp_rate*2)

    def get_sobremuestreo(self):
        return self.sobremuestreo

    def set_sobremuestreo(self, sobremuestreo):
        self.sobremuestreo = sobremuestreo

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.Fc_dado, self.samp_rate*2)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k

    def get_Kruido(self):
        return self.Kruido

    def set_Kruido(self, Kruido):
        self.Kruido = Kruido
        self.analog_noise_source_x_0.set_amplitude(self.Kruido)

    def get_Fmuestreo(self):
        return self.Fmuestreo

    def set_Fmuestreo(self, Fmuestreo):
        self.Fmuestreo = Fmuestreo

    def get_Constelacion3(self):
        return self.Constelacion3

    def set_Constelacion3(self, Constelacion3):
        self.Constelacion3 = Constelacion3

    def get_Constelacion2(self):
        return self.Constelacion2

    def set_Constelacion2(self, Constelacion2):
        self.Constelacion2 = Constelacion2

    def get_Constelacion1(self):
        return self.Constelacion1

    def set_Constelacion1(self, Constelacion1):
        self.Constelacion1 = Constelacion1
        self.b_MS_0.set_Constelacion(self.Constelacion1)


def main(top_block_cls=z_OFDM_MultiConstelacion, options=None):

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
