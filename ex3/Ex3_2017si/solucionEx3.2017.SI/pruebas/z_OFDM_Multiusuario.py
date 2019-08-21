#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Z Ofdm Multiusuario
# Generated: Thu Jul 27 13:30:37 2017
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
from b_M_PAM_bb import b_M_PAM_bb  # grc-generated hier_block
from b_PCM_Encoder_Bb import b_PCM_Encoder_Bb  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
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
import sip


class z_OFDM_Multiusuario(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Z Ofdm Multiusuario")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Z Ofdm Multiusuario")
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

        self.settings = Qt.QSettings("GNU Radio", "z_OFDM_Multiusuario")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.Constelacion = Constelacion = [(1+1.j)/4.24,(3+1.j)/4.24,(3+3.j)/4.24,(1+3.j)/4.24,(-1+1.j)/4.24,(-3+1.j)/4.24,(-3+3.j)/4.24,(-1+3.j)/4.24,(-1-1.j)/4.24,(-3-1.j)/4.24,(-3-3.j)/4.24,(-1-3.j)/4.24,(1-1.j)/4.24,(3-1.j)/4.24,(3-3.j)/4.24,(1-3.j)/4.24]
        self.M = M = len(Constelacion)
        self.Rb_c1 = Rb_c1 = 1000000
        self.No_dB = No_dB = -60
        self.Es_No_dB = Es_No_dB = 20
        self.Bps = Bps = int(math.log(M,2))
        self.Rs_c1 = Rs_c1 = Rb_c1/Bps
        self.N_c1 = N_c1 = 17
        self.Fc = Fc = 900000000
        self.Es_dB = Es_dB = Es_No_dB+No_dB
        self.r_c1 = r_c1 = 8390
        self.landa = landa = 300000000./Fc
        self.Rs = Rs = Rs_c1/N_c1
        self.Es = Es = math.pow(10,Es_dB/10.)
        self.lfs = lfs = (4*math.pi*r_c1/landa)**2
        self.Pr_subp = Pr_subp = Es*Rs
        self.Pt_subp = Pt_subp = Pr_subp*lfs
        self.N_c2 = N_c2 = 8
        self.N = N = 32
        self.samp_rate_usrp_tx = samp_rate_usrp_tx = 400000000
        self.samp_rate_d = samp_rate_d = Rs*N
        self.code = code = '010110011011101100010101011111101001001110001011010001101010001'
        self.Pt = Pt = Pt_subp*(N_c1+N_c2)
        self.Ktx = Ktx = 1024
        self.samp_rate = samp_rate = samp_rate_usrp_tx/Ktx
        self.run_stop = run_stop = True
        self.payload = payload = 128
        self.Sps = Sps = 2
        self.Rolloff = Rolloff = 0.9
        self.Pt_dB = Pt_dB = 10*math.log(Pt,10)
        self.Pe = Pe = 0.00001
        self.Nnou = Nnou = N-N_c1-N_c2
        self.NbpCode = NbpCode = len(code)+10.
        self.Ktx_d_0 = Ktx_d_0 = samp_rate_usrp_tx/samp_rate_d
        self.Ktx_d = Ktx_d = samp_rate_usrp_tx/samp_rate_d
        self.Kruido = Kruido = 0.01
        self.B = B = Rs*N

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
        self.pestana.addTab(self.pestana_widget_2, "Espectro Banda Base")
        self.pestana_widget_3 = Qt.QWidget()
        self.pestana_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_3)
        self.pestana_grid_layout_3 = Qt.QGridLayout()
        self.pestana_layout_3.addLayout(self.pestana_grid_layout_3)
        self.pestana.addTab(self.pestana_widget_3, "Espectro Paso Bandas")
        self.top_grid_layout.addWidget(self.pestana, 3,0,1,3)
        self._Kruido_range = Range(0, 1, 0.005, 0.01, 200)
        self._Kruido_win = RangeWidget(self._Kruido_range, self.set_Kruido, "Nivel del Ruido", "counter_slider", float)
        self.top_grid_layout.addWidget(self._Kruido_win, 1,0,1,1)
        _run_stop_check_box = Qt.QCheckBox("Inicial/Parar")
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.iteritems())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0,0,1,1)
        self.rational_resampler_xxx_0_1 = filter.rational_resampler_ccc(
                interpolation=samp_rate,
                decimation=samp_rate_d,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	Fc, #fc
        	samp_rate*2, #bw
        	"PSD senal OFDM", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_freq_sink_x_0_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)
        
        labels = ["Tx", "Rx", "", "", "",
                  "", "", "", "", ""]
        widths = [2, 1, 1, 1, 1,
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
        self.pestana_grid_layout_3.addWidget(self._qtgui_freq_sink_x_0_0_win, 0,0,1,2)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"PSD senal OFDM", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["Tx", "Rx", "", "", "",
                  "", "", "", "", ""]
        widths = [2, 1, 1, 1, 1,
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
        self.pestana_grid_layout_2.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,2)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	8 #number of inputs
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        
        if not True:
          self.qtgui_const_sink_x_0_0.disable_legend()
        
        labels = ["Rx.Us0", "Rx.Us1", "Rx.Us2", "Rx.Us3", "Rx.Us4",
                  "Rx.Us5", "Rx.Us6", "Rx.Us7", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "red", "red"]
        styles = [1, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(8):
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
        self.fft_vxx_1_0 = fft.fft_vcc(N, True, (), False, 1)
        self.fft_vxx_1 = fft.fft_vcc(N, False, (), False, 1)
        self.digital_diff_encoder_bb_0_0 = digital.diff_encoder_bb(M)
        self.digital_diff_encoder_bb_0 = digital.diff_encoder_bb(M)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc((Constelacion), 1)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((Constelacion), 1)
        self.blocks_vector_to_streams_0 = blocks.vector_to_streams(gr.sizeof_gr_complex*1, N)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, N)
        self.blocks_streams_to_vector_0 = blocks.streams_to_vector(gr.sizeof_gr_complex*1, N)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, N)
        self.blocks_stream_to_streams_0_0 = blocks.stream_to_streams(gr.sizeof_gr_complex*1, N_c2)
        self.blocks_stream_to_streams_0 = blocks.stream_to_streams(gr.sizeof_gr_complex*1, N_c1)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((1./N, ))
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_char*1, "/home/comdig1/Dropbox/EnUbuntuFull/ClaseComDig/LibroAplicativos/capitulo 3/Ex3SI2017/solucionEx3.2017.SI/texto2.txt", True)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, "/home/comdig1/Dropbox/EnUbuntuFull/ClaseComDig/LibroAplicativos/capitulo 3/Ex3SI2017/solucionEx3.2017.SI/texto1.txt", True)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.b_PCM_Encoder_Bb_0_0 = b_PCM_Encoder_Bb(
            code=code,
            payload=payload,
        )
        self.b_PCM_Encoder_Bb_0 = b_PCM_Encoder_Bb(
            code=code,
            payload=payload,
        )
        self.b_M_PAM_bb_0_0 = b_M_PAM_bb(
            M=M,
            Nbps=8,
        )
        self.b_M_PAM_bb_0 = b_M_PAM_bb(
            M=M,
            Nbps=8,
        )
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, Kruido, 48)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.b_M_PAM_bb_0, 0), (self.digital_diff_encoder_bb_0, 0))    
        self.connect((self.b_M_PAM_bb_0_0, 0), (self.digital_diff_encoder_bb_0_0, 0))    
        self.connect((self.b_PCM_Encoder_Bb_0, 0), (self.b_M_PAM_bb_0, 0))    
        self.connect((self.b_PCM_Encoder_Bb_0_0, 0), (self.b_M_PAM_bb_0_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_stream_to_vector_0_0, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.b_PCM_Encoder_Bb_0, 0))    
        self.connect((self.blocks_file_source_0_0, 0), (self.b_PCM_Encoder_Bb_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_0_1, 0))    
        self.connect((self.blocks_null_source_0, 0), (self.blocks_streams_to_vector_0, 25))    
        self.connect((self.blocks_null_source_0, 1), (self.blocks_streams_to_vector_0, 26))    
        self.connect((self.blocks_null_source_0, 2), (self.blocks_streams_to_vector_0, 27))    
        self.connect((self.blocks_null_source_0, 3), (self.blocks_streams_to_vector_0, 28))    
        self.connect((self.blocks_null_source_0, 4), (self.blocks_streams_to_vector_0, 29))    
        self.connect((self.blocks_null_source_0, 5), (self.blocks_streams_to_vector_0, 30))    
        self.connect((self.blocks_null_source_0, 6), (self.blocks_streams_to_vector_0, 31))    
        self.connect((self.blocks_stream_to_streams_0, 0), (self.blocks_streams_to_vector_0, 0))    
        self.connect((self.blocks_stream_to_streams_0, 1), (self.blocks_streams_to_vector_0, 1))    
        self.connect((self.blocks_stream_to_streams_0, 10), (self.blocks_streams_to_vector_0, 10))    
        self.connect((self.blocks_stream_to_streams_0, 11), (self.blocks_streams_to_vector_0, 11))    
        self.connect((self.blocks_stream_to_streams_0, 12), (self.blocks_streams_to_vector_0, 12))    
        self.connect((self.blocks_stream_to_streams_0, 13), (self.blocks_streams_to_vector_0, 13))    
        self.connect((self.blocks_stream_to_streams_0, 14), (self.blocks_streams_to_vector_0, 14))    
        self.connect((self.blocks_stream_to_streams_0, 15), (self.blocks_streams_to_vector_0, 15))    
        self.connect((self.blocks_stream_to_streams_0, 16), (self.blocks_streams_to_vector_0, 16))    
        self.connect((self.blocks_stream_to_streams_0, 2), (self.blocks_streams_to_vector_0, 2))    
        self.connect((self.blocks_stream_to_streams_0, 3), (self.blocks_streams_to_vector_0, 3))    
        self.connect((self.blocks_stream_to_streams_0, 4), (self.blocks_streams_to_vector_0, 4))    
        self.connect((self.blocks_stream_to_streams_0, 5), (self.blocks_streams_to_vector_0, 5))    
        self.connect((self.blocks_stream_to_streams_0, 6), (self.blocks_streams_to_vector_0, 6))    
        self.connect((self.blocks_stream_to_streams_0, 7), (self.blocks_streams_to_vector_0, 7))    
        self.connect((self.blocks_stream_to_streams_0, 8), (self.blocks_streams_to_vector_0, 8))    
        self.connect((self.blocks_stream_to_streams_0, 9), (self.blocks_streams_to_vector_0, 9))    
        self.connect((self.blocks_stream_to_streams_0_0, 0), (self.blocks_streams_to_vector_0, 17))    
        self.connect((self.blocks_stream_to_streams_0_0, 1), (self.blocks_streams_to_vector_0, 18))    
        self.connect((self.blocks_stream_to_streams_0_0, 2), (self.blocks_streams_to_vector_0, 19))    
        self.connect((self.blocks_stream_to_streams_0_0, 3), (self.blocks_streams_to_vector_0, 20))    
        self.connect((self.blocks_stream_to_streams_0_0, 4), (self.blocks_streams_to_vector_0, 21))    
        self.connect((self.blocks_stream_to_streams_0_0, 5), (self.blocks_streams_to_vector_0, 22))    
        self.connect((self.blocks_stream_to_streams_0_0, 6), (self.blocks_streams_to_vector_0, 23))    
        self.connect((self.blocks_stream_to_streams_0_0, 7), (self.blocks_streams_to_vector_0, 24))    
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.fft_vxx_1_0, 0))    
        self.connect((self.blocks_streams_to_vector_0, 0), (self.fft_vxx_1, 0))    
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_vector_to_streams_0, 10), (self.blocks_null_sink_0, 2))    
        self.connect((self.blocks_vector_to_streams_0, 11), (self.blocks_null_sink_0, 3))    
        self.connect((self.blocks_vector_to_streams_0, 12), (self.blocks_null_sink_0, 4))    
        self.connect((self.blocks_vector_to_streams_0, 13), (self.blocks_null_sink_0, 5))    
        self.connect((self.blocks_vector_to_streams_0, 14), (self.blocks_null_sink_0, 6))    
        self.connect((self.blocks_vector_to_streams_0, 15), (self.blocks_null_sink_0, 7))    
        self.connect((self.blocks_vector_to_streams_0, 16), (self.blocks_null_sink_0, 8))    
        self.connect((self.blocks_vector_to_streams_0, 17), (self.blocks_null_sink_0, 9))    
        self.connect((self.blocks_vector_to_streams_0, 18), (self.blocks_null_sink_0, 10))    
        self.connect((self.blocks_vector_to_streams_0, 19), (self.blocks_null_sink_0, 11))    
        self.connect((self.blocks_vector_to_streams_0, 20), (self.blocks_null_sink_0, 12))    
        self.connect((self.blocks_vector_to_streams_0, 21), (self.blocks_null_sink_0, 13))    
        self.connect((self.blocks_vector_to_streams_0, 22), (self.blocks_null_sink_0, 14))    
        self.connect((self.blocks_vector_to_streams_0, 23), (self.blocks_null_sink_0, 15))    
        self.connect((self.blocks_vector_to_streams_0, 24), (self.blocks_null_sink_0, 16))    
        self.connect((self.blocks_vector_to_streams_0, 25), (self.blocks_null_sink_0, 17))    
        self.connect((self.blocks_vector_to_streams_0, 26), (self.blocks_null_sink_0, 18))    
        self.connect((self.blocks_vector_to_streams_0, 27), (self.blocks_null_sink_0, 19))    
        self.connect((self.blocks_vector_to_streams_0, 28), (self.blocks_null_sink_0, 20))    
        self.connect((self.blocks_vector_to_streams_0, 29), (self.blocks_null_sink_0, 21))    
        self.connect((self.blocks_vector_to_streams_0, 30), (self.blocks_null_sink_0, 22))    
        self.connect((self.blocks_vector_to_streams_0, 31), (self.blocks_null_sink_0, 23))    
        self.connect((self.blocks_vector_to_streams_0, 8), (self.blocks_null_sink_0, 0))    
        self.connect((self.blocks_vector_to_streams_0, 9), (self.blocks_null_sink_0, 1))    
        self.connect((self.blocks_vector_to_streams_0, 0), (self.qtgui_const_sink_x_0_0, 0))    
        self.connect((self.blocks_vector_to_streams_0, 1), (self.qtgui_const_sink_x_0_0, 1))    
        self.connect((self.blocks_vector_to_streams_0, 5), (self.qtgui_const_sink_x_0_0, 5))    
        self.connect((self.blocks_vector_to_streams_0, 2), (self.qtgui_const_sink_x_0_0, 2))    
        self.connect((self.blocks_vector_to_streams_0, 6), (self.qtgui_const_sink_x_0_0, 6))    
        self.connect((self.blocks_vector_to_streams_0, 3), (self.qtgui_const_sink_x_0_0, 3))    
        self.connect((self.blocks_vector_to_streams_0, 7), (self.qtgui_const_sink_x_0_0, 7))    
        self.connect((self.blocks_vector_to_streams_0, 4), (self.qtgui_const_sink_x_0_0, 4))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_stream_to_streams_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.blocks_stream_to_streams_0_0, 0))    
        self.connect((self.digital_diff_encoder_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))    
        self.connect((self.digital_diff_encoder_bb_0_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))    
        self.connect((self.fft_vxx_1, 0), (self.blocks_vector_to_stream_0, 0))    
        self.connect((self.fft_vxx_1_0, 0), (self.blocks_vector_to_streams_0, 0))    
        self.connect((self.rational_resampler_xxx_0_1, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.rational_resampler_xxx_0_1, 0), (self.qtgui_freq_sink_x_0_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "z_OFDM_Multiusuario")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_Constelacion(self):
        return self.Constelacion

    def set_Constelacion(self, Constelacion):
        self.Constelacion = Constelacion
        self.set_M(len(self.Constelacion))
        self.digital_chunks_to_symbols_xx_0.set_symbol_table((self.Constelacion))
        self.digital_chunks_to_symbols_xx_0_0.set_symbol_table((self.Constelacion))

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_Bps(int(math.log(self.M,2)))
        self.b_M_PAM_bb_0.set_M(self.M)
        self.b_M_PAM_bb_0_0.set_M(self.M)

    def get_Rb_c1(self):
        return self.Rb_c1

    def set_Rb_c1(self, Rb_c1):
        self.Rb_c1 = Rb_c1
        self.set_Rs_c1(self.Rb_c1/self.Bps)

    def get_No_dB(self):
        return self.No_dB

    def set_No_dB(self, No_dB):
        self.No_dB = No_dB
        self.set_Es_dB(self.Es_No_dB+self.No_dB)

    def get_Es_No_dB(self):
        return self.Es_No_dB

    def set_Es_No_dB(self, Es_No_dB):
        self.Es_No_dB = Es_No_dB
        self.set_Es_dB(self.Es_No_dB+self.No_dB)

    def get_Bps(self):
        return self.Bps

    def set_Bps(self, Bps):
        self.Bps = Bps
        self.set_Rs_c1(self.Rb_c1/self.Bps)

    def get_Rs_c1(self):
        return self.Rs_c1

    def set_Rs_c1(self, Rs_c1):
        self.Rs_c1 = Rs_c1
        self.set_Rs(self.Rs_c1/self.N_c1)

    def get_N_c1(self):
        return self.N_c1

    def set_N_c1(self, N_c1):
        self.N_c1 = N_c1
        self.set_Nnou(self.N-self.N_c1-self.N_c2)
        self.set_Pt(self.Pt_subp*(self.N_c1+self.N_c2))
        self.set_Rs(self.Rs_c1/self.N_c1)

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc
        self.set_landa(300000000./self.Fc)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.Fc, self.samp_rate*2)

    def get_Es_dB(self):
        return self.Es_dB

    def set_Es_dB(self, Es_dB):
        self.Es_dB = Es_dB
        self.set_Es(math.pow(10,self.Es_dB/10.))

    def get_r_c1(self):
        return self.r_c1

    def set_r_c1(self, r_c1):
        self.r_c1 = r_c1
        self.set_lfs((4*math.pi*self.r_c1/self.landa)**2)

    def get_landa(self):
        return self.landa

    def set_landa(self, landa):
        self.landa = landa
        self.set_lfs((4*math.pi*self.r_c1/self.landa)**2)

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.set_B(self.Rs*self.N)
        self.set_Pr_subp(self.Es*self.Rs)
        self.set_samp_rate_d(self.Rs*self.N)

    def get_Es(self):
        return self.Es

    def set_Es(self, Es):
        self.Es = Es
        self.set_Pr_subp(self.Es*self.Rs)

    def get_lfs(self):
        return self.lfs

    def set_lfs(self, lfs):
        self.lfs = lfs
        self.set_Pt_subp(self.Pr_subp*self.lfs)

    def get_Pr_subp(self):
        return self.Pr_subp

    def set_Pr_subp(self, Pr_subp):
        self.Pr_subp = Pr_subp
        self.set_Pt_subp(self.Pr_subp*self.lfs)

    def get_Pt_subp(self):
        return self.Pt_subp

    def set_Pt_subp(self, Pt_subp):
        self.Pt_subp = Pt_subp
        self.set_Pt(self.Pt_subp*(self.N_c1+self.N_c2))

    def get_N_c2(self):
        return self.N_c2

    def set_N_c2(self, N_c2):
        self.N_c2 = N_c2
        self.set_Nnou(self.N-self.N_c1-self.N_c2)
        self.set_Pt(self.Pt_subp*(self.N_c1+self.N_c2))

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.set_B(self.Rs*self.N)
        self.set_Nnou(self.N-self.N_c1-self.N_c2)
        self.set_samp_rate_d(self.Rs*self.N)
        self.blocks_multiply_const_vxx_0.set_k((1./self.N, ))

    def get_samp_rate_usrp_tx(self):
        return self.samp_rate_usrp_tx

    def set_samp_rate_usrp_tx(self, samp_rate_usrp_tx):
        self.samp_rate_usrp_tx = samp_rate_usrp_tx
        self.set_Ktx_d(self.samp_rate_usrp_tx/self.samp_rate_d)
        self.set_Ktx_d_0(self.samp_rate_usrp_tx/self.samp_rate_d)
        self.set_samp_rate(self.samp_rate_usrp_tx/self.Ktx)

    def get_samp_rate_d(self):
        return self.samp_rate_d

    def set_samp_rate_d(self, samp_rate_d):
        self.samp_rate_d = samp_rate_d
        self.set_Ktx_d(self.samp_rate_usrp_tx/self.samp_rate_d)
        self.set_Ktx_d_0(self.samp_rate_usrp_tx/self.samp_rate_d)

    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code
        self.set_NbpCode(len(self.code)+10.)
        self.b_PCM_Encoder_Bb_0.set_code(self.code)
        self.b_PCM_Encoder_Bb_0_0.set_code(self.code)

    def get_Pt(self):
        return self.Pt

    def set_Pt(self, Pt):
        self.Pt = Pt
        self.set_Pt_dB(10*math.log(self.Pt,10))

    def get_Ktx(self):
        return self.Ktx

    def set_Ktx(self, Ktx):
        self.Ktx = Ktx
        self.set_samp_rate(self.samp_rate_usrp_tx/self.Ktx)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.Fc, self.samp_rate*2)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_payload(self):
        return self.payload

    def set_payload(self, payload):
        self.payload = payload
        self.b_PCM_Encoder_Bb_0.set_payload(self.payload)
        self.b_PCM_Encoder_Bb_0_0.set_payload(self.payload)

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps

    def get_Rolloff(self):
        return self.Rolloff

    def set_Rolloff(self, Rolloff):
        self.Rolloff = Rolloff

    def get_Pt_dB(self):
        return self.Pt_dB

    def set_Pt_dB(self, Pt_dB):
        self.Pt_dB = Pt_dB

    def get_Pe(self):
        return self.Pe

    def set_Pe(self, Pe):
        self.Pe = Pe

    def get_Nnou(self):
        return self.Nnou

    def set_Nnou(self, Nnou):
        self.Nnou = Nnou

    def get_NbpCode(self):
        return self.NbpCode

    def set_NbpCode(self, NbpCode):
        self.NbpCode = NbpCode

    def get_Ktx_d_0(self):
        return self.Ktx_d_0

    def set_Ktx_d_0(self, Ktx_d_0):
        self.Ktx_d_0 = Ktx_d_0

    def get_Ktx_d(self):
        return self.Ktx_d

    def set_Ktx_d(self, Ktx_d):
        self.Ktx_d = Ktx_d

    def get_Kruido(self):
        return self.Kruido

    def set_Kruido(self, Kruido):
        self.Kruido = Kruido
        self.analog_noise_source_x_0.set_amplitude(self.Kruido)

    def get_B(self):
        return self.B

    def set_B(self, B):
        self.B = B


def main(top_block_cls=z_OFDM_Multiusuario, options=None):

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
