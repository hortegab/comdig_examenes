#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Z Ofdm Multiconstelacion
# Generated: Wed Dec 13 10:21:39 2017
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
from b_USRP_2_USRP_v2 import b_USRP_2_USRP_v2  # grc-generated hier_block
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
        self.samp_rate_op1 = samp_rate_op1 = 390625
        self.samp_rate = samp_rate = samp_rate_op1
        self.N = N = 8
        self.Constelacion1 = Constelacion1 = [1+.0j,-1+.0j, .0+1j,0 -1j ]
        self.sobremuestreo_pasobandas = sobremuestreo_pasobandas = 2
        self.samp_rate_op3 = samp_rate_op3 = 3125000
        self.samp_rate_op2 = samp_rate_op2 = 781250
        self.run_stop = run_stop = True
        self.phi = phi = 0.
        self.Rs = Rs = samp_rate/N
        self.NodB = NodB = -63
        self.Gain_USRP_Tx_dB = Gain_USRP_Tx_dB = 30.
        self.Gain_USRP_Rx_dB = Gain_USRP_Rx_dB = 0.
        self.Fc = Fc = 900e6
        self.Constelacion3 = Constelacion3 = [1+.0j,-1+.0j, .0+1j,0 -1j,  0.7+0.7j,  0.7-0.7j,  -0.7+0.7j,  -0.7-0.7j ]
        self.Constelacion2 = Constelacion2 = [1.5+.0j,-1.5+.0j, .0+1.5j,0 -1.5j, 0.5+.0j,-0.5+.0j, .0+0.5j,0 -0.5j ]
        self.Ch_Frec_offset = Ch_Frec_offset = 0
        self.Ch_Delay = Ch_Delay = 0
        self.Bps1 = Bps1 = int(math.log(len(Constelacion1),2))

        ##################################################
        # Blocks
        ##################################################
        self.controls = Qt.QTabWidget()
        self.controls_widget_0 = Qt.QWidget()
        self.controls_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.controls_widget_0)
        self.controls_grid_layout_0 = Qt.QGridLayout()
        self.controls_layout_0.addLayout(self.controls_grid_layout_0)
        self.controls.addTab(self.controls_widget_0, "Ch_Offsets")
        self.controls_widget_1 = Qt.QWidget()
        self.controls_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.controls_widget_1)
        self.controls_grid_layout_1 = Qt.QGridLayout()
        self.controls_layout_1.addLayout(self.controls_grid_layout_1)
        self.controls.addTab(self.controls_widget_1, "Ch_Taps")
        self.controls_widget_2 = Qt.QWidget()
        self.controls_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.controls_widget_2)
        self.controls_grid_layout_2 = Qt.QGridLayout()
        self.controls_layout_2.addLayout(self.controls_grid_layout_2)
        self.controls.addTab(self.controls_widget_2, "Tuning")
        self.top_grid_layout.addWidget(self.controls, 0,1,1,1)
        self._phi_range = Range(-numpy.pi, numpy.pi, numpy.pi/100., 0., 200)
        self._phi_win = RangeWidget(self._phi_range, self.set_phi, "Angulo", "counter_slider", float)
        self.controls_grid_layout_0.addWidget(self._phi_win, 0,3,1,1)
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
        self._NodB_range = Range(-140., 0., 1., -63, 200)
        self._NodB_win = RangeWidget(self._NodB_range, self.set_NodB, "Ch_No(dB)", "counter", float)
        self.controls_grid_layout_0.addWidget(self._NodB_win, 0,0,1,1)
        self._Gain_USRP_Tx_dB_range = Range(0., 130, 1, 30., 200)
        self._Gain_USRP_Tx_dB_win = RangeWidget(self._Gain_USRP_Tx_dB_range, self.set_Gain_USRP_Tx_dB, "Gain_USRP_Tx (dB)", "counter", float)
        self.controls_grid_layout_2.addWidget(self._Gain_USRP_Tx_dB_win, 0,1,1,1)
        self._Gain_USRP_Rx_dB_range = Range(0., 130, 1, 0., 200)
        self._Gain_USRP_Rx_dB_win = RangeWidget(self._Gain_USRP_Rx_dB_range, self.set_Gain_USRP_Rx_dB, "Gain_USRP_Rx (dB)", "counter", float)
        self.controls_grid_layout_2.addWidget(self._Gain_USRP_Rx_dB_win, 0,2,1,1)
        self._Ch_Frec_offset_range = Range(0, 100, 0.01, 0, 200)
        self._Ch_Frec_offset_win = RangeWidget(self._Ch_Frec_offset_range, self.set_Ch_Frec_offset, "Ch_Frec_offset (Hz)", "counter", float)
        self.controls_grid_layout_0.addWidget(self._Ch_Frec_offset_win, 0,1,1,1)
        self._Ch_Delay_range = Range(0, 1000, 1, 0, 200)
        self._Ch_Delay_win = RangeWidget(self._Ch_Delay_range, self.set_Ch_Delay, "Ch_Delay", "counter", int)
        self.controls_grid_layout_0.addWidget(self._Ch_Delay_win, 0,2,1,1)
        _run_stop_check_box = Qt.QCheckBox("Inicial/Parar")
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.iteritems())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0,0,1,1)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=sobremuestreo_pasobandas,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	Fc, #fc
        	samp_rate*sobremuestreo_pasobandas, #bw
        	"Opcion 1. PSD cerca a los usuarios", #name
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
        
        labels = ["Rx.R1", "Rx.Con Ecualizacion", "", "", "",
                  "", "", "", "", ""]
        widths = [4, 1, 1, 1, 1,
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
        self.fft_vxx_1_0 = fft.fft_vcc(N, True, (), False, 1)
        self.fft_vxx_1 = fft.fft_vcc(N, False, (), False, 1)
        self.blocks_vector_to_streams_0 = blocks.vector_to_streams(gr.sizeof_gr_complex*1, N)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, N)
        self.blocks_streams_to_vector_0 = blocks.streams_to_vector(gr.sizeof_gr_complex*1, N)
        self.blocks_streams_to_stream_0 = blocks.streams_to_stream(gr.sizeof_gr_complex*1, 2)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, N)
        self.blocks_stream_to_streams_0 = blocks.stream_to_streams(gr.sizeof_gr_complex*1, 2)
        self.blocks_null_source_0_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_2 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_1 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_1 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_0_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((1./N, ))
        self.b_USRP_2_USRP_v2_0 = b_USRP_2_USRP_v2(
            Ch_Loss_dB=30.,
            Ch_NodB=NodB,
            Ch_Phoffset=phi,
            Ch_Toffset=Ch_Delay,
            Rx_B=samp_rate,
            Rx_Fc=Fc+Ch_Frec_offset,
            Rx_Gain_dB=Gain_USRP_Rx_dB,
            Rx__samp_rate=samp_rate,
            Tx_B=samp_rate,
            Tx_Fc=Fc,
            Tx_Gain_dB=Gain_USRP_Tx_dB,
            Tx__samp_rate=samp_rate,
        )
        self.b_MS_0_2 = b_MS(
            Constelacion=Constelacion1,
            N=1,
        )
        self.b_MS_0_0_0 = b_MS(
            Constelacion=Constelacion1,
            N=1,
        )
        self.b_MS_0 = b_MS(
            Constelacion=Constelacion1,
            N=1,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.b_MS_0, 0), (self.blocks_stream_to_streams_0, 0))    
        self.connect((self.b_MS_0_0_0, 0), (self.blocks_streams_to_stream_0, 0))    
        self.connect((self.b_MS_0_2, 0), (self.blocks_streams_to_stream_0, 1))    
        self.connect((self.b_USRP_2_USRP_v2_0, 0), (self.blocks_stream_to_vector_0_0, 0))    
        self.connect((self.b_USRP_2_USRP_v2_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.b_USRP_2_USRP_v2_0, 0))    
        self.connect((self.blocks_null_source_0, 0), (self.blocks_streams_to_vector_0, 3))    
        self.connect((self.blocks_null_source_0, 0), (self.blocks_streams_to_vector_0, 4))    
        self.connect((self.blocks_null_source_0, 0), (self.blocks_streams_to_vector_0, 5))    
        self.connect((self.blocks_null_source_0, 0), (self.blocks_streams_to_vector_0, 6))    
        self.connect((self.blocks_null_source_0_0, 0), (self.blocks_streams_to_vector_0, 0))    
        self.connect((self.blocks_stream_to_streams_0, 0), (self.blocks_streams_to_vector_0, 1))    
        self.connect((self.blocks_stream_to_streams_0, 1), (self.blocks_streams_to_vector_0, 2))    
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.fft_vxx_1_0, 0))    
        self.connect((self.blocks_streams_to_stream_0, 0), (self.blocks_streams_to_vector_0, 7))    
        self.connect((self.blocks_streams_to_vector_0, 0), (self.fft_vxx_1, 0))    
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_vector_to_streams_0, 6), (self.blocks_null_sink_0, 0))    
        self.connect((self.blocks_vector_to_streams_0, 5), (self.blocks_null_sink_0_0, 0))    
        self.connect((self.blocks_vector_to_streams_0, 4), (self.blocks_null_sink_0_0_0, 0))    
        self.connect((self.blocks_vector_to_streams_0, 1), (self.blocks_null_sink_0_0_0_0, 0))    
        self.connect((self.blocks_vector_to_streams_0, 0), (self.blocks_null_sink_0_0_0_0_0, 0))    
        self.connect((self.blocks_vector_to_streams_0, 2), (self.blocks_null_sink_0_0_1, 0))    
        self.connect((self.blocks_vector_to_streams_0, 3), (self.blocks_null_sink_0_1, 0))    
        self.connect((self.blocks_vector_to_streams_0, 7), (self.blocks_null_sink_0_2, 0))    
        self.connect((self.fft_vxx_1, 0), (self.blocks_vector_to_stream_0, 0))    
        self.connect((self.fft_vxx_1_0, 0), (self.blocks_vector_to_streams_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "z_OFDM_MultiConstelacion")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate_op1(self):
        return self.samp_rate_op1

    def set_samp_rate_op1(self, samp_rate_op1):
        self.samp_rate_op1 = samp_rate_op1
        self.set_samp_rate(self.samp_rate_op1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_Rs(self.samp_rate/self.N)
        self.b_USRP_2_USRP_v2_0.set_Rx_B(self.samp_rate)
        self.b_USRP_2_USRP_v2_0.set_Rx__samp_rate(self.samp_rate)
        self.b_USRP_2_USRP_v2_0.set_Tx_B(self.samp_rate)
        self.b_USRP_2_USRP_v2_0.set_Tx__samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.Fc, self.samp_rate*self.sobremuestreo_pasobandas)

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.set_Rs(self.samp_rate/self.N)
        self.blocks_multiply_const_vxx_0.set_k((1./self.N, ))

    def get_Constelacion1(self):
        return self.Constelacion1

    def set_Constelacion1(self, Constelacion1):
        self.Constelacion1 = Constelacion1
        self.set_Bps1(int(math.log(len(self.Constelacion1),2)))
        self.b_MS_0.set_Constelacion(self.Constelacion1)
        self.b_MS_0_0_0.set_Constelacion(self.Constelacion1)
        self.b_MS_0_2.set_Constelacion(self.Constelacion1)

    def get_sobremuestreo_pasobandas(self):
        return self.sobremuestreo_pasobandas

    def set_sobremuestreo_pasobandas(self, sobremuestreo_pasobandas):
        self.sobremuestreo_pasobandas = sobremuestreo_pasobandas
        self.qtgui_freq_sink_x_0.set_frequency_range(self.Fc, self.samp_rate*self.sobremuestreo_pasobandas)

    def get_samp_rate_op3(self):
        return self.samp_rate_op3

    def set_samp_rate_op3(self, samp_rate_op3):
        self.samp_rate_op3 = samp_rate_op3

    def get_samp_rate_op2(self):
        return self.samp_rate_op2

    def set_samp_rate_op2(self, samp_rate_op2):
        self.samp_rate_op2 = samp_rate_op2

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_phi(self):
        return self.phi

    def set_phi(self, phi):
        self.phi = phi
        self.b_USRP_2_USRP_v2_0.set_Ch_Phoffset(self.phi)

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs

    def get_NodB(self):
        return self.NodB

    def set_NodB(self, NodB):
        self.NodB = NodB
        self.b_USRP_2_USRP_v2_0.set_Ch_NodB(self.NodB)

    def get_Gain_USRP_Tx_dB(self):
        return self.Gain_USRP_Tx_dB

    def set_Gain_USRP_Tx_dB(self, Gain_USRP_Tx_dB):
        self.Gain_USRP_Tx_dB = Gain_USRP_Tx_dB
        self.b_USRP_2_USRP_v2_0.set_Tx_Gain_dB(self.Gain_USRP_Tx_dB)

    def get_Gain_USRP_Rx_dB(self):
        return self.Gain_USRP_Rx_dB

    def set_Gain_USRP_Rx_dB(self, Gain_USRP_Rx_dB):
        self.Gain_USRP_Rx_dB = Gain_USRP_Rx_dB
        self.b_USRP_2_USRP_v2_0.set_Rx_Gain_dB(self.Gain_USRP_Rx_dB)

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc
        self.b_USRP_2_USRP_v2_0.set_Rx_Fc(self.Fc+self.Ch_Frec_offset)
        self.b_USRP_2_USRP_v2_0.set_Tx_Fc(self.Fc)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.Fc, self.samp_rate*self.sobremuestreo_pasobandas)

    def get_Constelacion3(self):
        return self.Constelacion3

    def set_Constelacion3(self, Constelacion3):
        self.Constelacion3 = Constelacion3

    def get_Constelacion2(self):
        return self.Constelacion2

    def set_Constelacion2(self, Constelacion2):
        self.Constelacion2 = Constelacion2

    def get_Ch_Frec_offset(self):
        return self.Ch_Frec_offset

    def set_Ch_Frec_offset(self, Ch_Frec_offset):
        self.Ch_Frec_offset = Ch_Frec_offset
        self.b_USRP_2_USRP_v2_0.set_Rx_Fc(self.Fc+self.Ch_Frec_offset)

    def get_Ch_Delay(self):
        return self.Ch_Delay

    def set_Ch_Delay(self, Ch_Delay):
        self.Ch_Delay = Ch_Delay
        self.b_USRP_2_USRP_v2_0.set_Ch_Toffset(self.Ch_Delay)

    def get_Bps1(self):
        return self.Bps1

    def set_Bps1(self, Bps1):
        self.Bps1 = Bps1


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
