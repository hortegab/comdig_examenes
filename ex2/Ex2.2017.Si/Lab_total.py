#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Lab Total
# Generated: Wed Jun  7 06:19:10 2017
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
from b_FLL_tunner import b_FLL_tunner  # grc-generated hier_block
from b_M_PAM_bb import b_M_PAM_bb  # grc-generated hier_block
from b_PCM_Encoder_Bb import b_PCM_Encoder_Bb  # grc-generated hier_block
from b_RRaised_cosine_cc import b_RRaised_cosine_cc  # grc-generated hier_block
from b_de_M_PAM_bb import b_de_M_PAM_bb  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
from scipy import fftpack
import cmath
import math
import numpy
import random
import sip
import time


class Lab_total(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Lab Total")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Lab Total")
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

        self.settings = Qt.QSettings("GNU Radio", "Lab_total")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 250e3
        self.Sps = Sps = 2
        self.rolloff = rolloff = 0.9
        self.Constelacion = Constelacion = [1.+0.j,   0.+1.j,   -1.+0.j,  0.-1.j ]
        self.B = B = samp_rate/Sps
        self.W = W = B/(2.*(1.+rolloff))
        self.M = M = len(Constelacion)
        self.code1 = code1 = '010110011011101100010101011111101001001110001011010001101010001'
        self.Rs = Rs = 2*W
        self.Bps = Bps = int(math.log(M,2))
        self.tap4 = tap4 = 1
        self.tap3 = tap3 = 1
        self.tap2 = tap2 = 1
        self.tap1 = tap1 = 0.25
        self.payload = payload = 128
        self.ntaps = ntaps = Sps*16
        self.nfilts = nfilts = 32
        self.Rb = Rb = Rs*Bps
        self.NbpCode = NbpCode = len(code1)+10.
        self.run_stop = run_stop = True
        self.rrc_taps_rx = rrc_taps_rx = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(Sps), rolloff, ntaps*nfilts)
        self.eq_gain = eq_gain = 0.01
        self.Tmax_scope = Tmax_scope = 64./Rs
        self.SymbTune = SymbTune = 2
        self.Sps_o = Sps_o = 2
        self.Rbi = Rbi = Rb/(1+NbpCode/payload)
        self.NodB = NodB = -80
        self.MiconstellationObject = MiconstellationObject = digital.constellation_calcdist((Constelacion), (), 4, 1).base()
        self.Gain_USRP_Tx_dB = Gain_USRP_Tx_dB = 50.
        self.Gain_USRP_Rx_dB = Gain_USRP_Rx_dB = 10
        self.Fc = Fc = 700e6
        self.Ch_taps = Ch_taps = fftpack.ifftshift(fftpack.ifft([tap3, tap4, 1.0, tap1, tap2]))
        self.Ch_Jitter = Ch_Jitter = 0
        self.Ch_Frec_offset = Ch_Frec_offset = 0
        self.Ch_Delay = Ch_Delay = 0

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
        self.Instrumentos = Qt.QTabWidget()
        self.Instrumentos_widget_0 = Qt.QWidget()
        self.Instrumentos_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Instrumentos_widget_0)
        self.Instrumentos_grid_layout_0 = Qt.QGridLayout()
        self.Instrumentos_layout_0.addLayout(self.Instrumentos_grid_layout_0)
        self.Instrumentos.addTab(self.Instrumentos_widget_0, "Capa0.Canal y precanal")
        self.Instrumentos_widget_1 = Qt.QWidget()
        self.Instrumentos_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Instrumentos_widget_1)
        self.Instrumentos_grid_layout_1 = Qt.QGridLayout()
        self.Instrumentos_layout_1.addLayout(self.Instrumentos_grid_layout_1)
        self.Instrumentos.addTab(self.Instrumentos_widget_1, "Capas.Pre-modulacion")
        self.Instrumentos_widget_2 = Qt.QWidget()
        self.Instrumentos_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Instrumentos_widget_2)
        self.Instrumentos_grid_layout_2 = Qt.QGridLayout()
        self.Instrumentos_layout_2.addLayout(self.Instrumentos_grid_layout_2)
        self.Instrumentos.addTab(self.Instrumentos_widget_2, "Capa1. Modulacion")
        self.Instrumentos_widget_3 = Qt.QWidget()
        self.Instrumentos_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Instrumentos_widget_3)
        self.Instrumentos_grid_layout_3 = Qt.QGridLayout()
        self.Instrumentos_layout_3.addLayout(self.Instrumentos_grid_layout_3)
        self.Instrumentos.addTab(self.Instrumentos_widget_3, "Capa2. CodificacionDeSimbolos")
        self.top_grid_layout.addWidget(self.Instrumentos, 1,0,1,2)
        self.canal = Qt.QTabWidget()
        self.canal_widget_0 = Qt.QWidget()
        self.canal_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.canal_widget_0)
        self.canal_grid_layout_0 = Qt.QGridLayout()
        self.canal_layout_0.addLayout(self.canal_grid_layout_0)
        self.canal.addTab(self.canal_widget_0, "Constelacion")
        self.canal_widget_1 = Qt.QWidget()
        self.canal_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.canal_widget_1)
        self.canal_grid_layout_1 = Qt.QGridLayout()
        self.canal_layout_1.addLayout(self.canal_grid_layout_1)
        self.canal.addTab(self.canal_widget_1, "Espectro")
        self.Instrumentos_grid_layout_0.addWidget(self.canal, 1,0,1,1)
        self._SymbTune_range = Range(0, 1000, 1, 2, 200)
        self._SymbTune_win = RangeWidget(self._SymbTune_range, self.set_SymbTune, "SymbTuning", "counter", int)
        self.controls_grid_layout_2.addWidget(self._SymbTune_win, 0,0,1,1)
        self._Gain_USRP_Tx_dB_range = Range(0., 130, 1, 50., 200)
        self._Gain_USRP_Tx_dB_win = RangeWidget(self._Gain_USRP_Tx_dB_range, self.set_Gain_USRP_Tx_dB, "Gain_USRP_Tx (dB)", "counter", float)
        self.controls_grid_layout_2.addWidget(self._Gain_USRP_Tx_dB_win, 0,1,1,1)
        self._Gain_USRP_Rx_dB_range = Range(0., 130, 1, 10, 200)
        self._Gain_USRP_Rx_dB_win = RangeWidget(self._Gain_USRP_Rx_dB_range, self.set_Gain_USRP_Rx_dB, "Gain_USRP_Rx (dB)", "counter", float)
        self.controls_grid_layout_2.addWidget(self._Gain_USRP_Rx_dB_win, 0,2,1,1)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(Fc, 0)
        self.uhd_usrp_source_0.set_gain(Gain_USRP_Rx_dB, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(Fc, 0)
        self.uhd_usrp_sink_0.set_gain(Gain_USRP_Tx_dB, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self._tap4_range = Range(0, 1, 0.01, 1, 200)
        self._tap4_win = RangeWidget(self._tap4_range, self.set_tap4, "tap4", "slider", float)
        self.controls_grid_layout_1.addWidget(self._tap4_win, 0,3,1,1)
        self._tap3_range = Range(0.25, 1, 0.01, 1, 200)
        self._tap3_win = RangeWidget(self._tap3_range, self.set_tap3, "tap3", "slider", float)
        self.controls_grid_layout_1.addWidget(self._tap3_win, 0,2,1,1)
        self._tap2_range = Range(0, 1, 0.01, 1, 200)
        self._tap2_win = RangeWidget(self._tap2_range, self.set_tap2, "tap2", "slider", float)
        self.controls_grid_layout_1.addWidget(self._tap2_win, 0,1,1,1)
        self._tap1_range = Range(0, 1, 0.01, 0.25, 200)
        self._tap1_win = RangeWidget(self._tap1_range, self.set_tap1, "tap1", "slider", float)
        self.controls_grid_layout_1.addWidget(self._tap1_win, 0,0,1,1)
        _run_stop_check_box = Qt.QCheckBox("Inicial/Parar")
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.iteritems())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0,0,1,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	Rs, #bw
        	"", #name
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
        self.canal_grid_layout_1.addWidget(self._qtgui_freq_sink_x_0_win, 0,1,1,1)
        self.qtgui_const_sink_x_0_1 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_1.set_update_time(0.10)
        self.qtgui_const_sink_x_0_1.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_1.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_1.enable_autoscale(False)
        self.qtgui_const_sink_x_0_1.enable_grid(False)
        
        if not True:
          self.qtgui_const_sink_x_0_1.disable_legend()
        
        labels = ["Rx.R1", "", "", "Filtro RRC y MPSK Timing Recovery", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "blue", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
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
        self.canal_grid_layout_0.addWidget(self._qtgui_const_sink_x_0_1_win, 1,0,1,1)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(Sps, 2*math.pi/100.0, (rrc_taps_rx), nfilts, nfilts/2, 1.5, Sps_o)
        self.digital_lms_dd_equalizer_cc_0 = digital.lms_dd_equalizer_cc(11, eq_gain, Sps_o, MiconstellationObject)
        self.digital_diff_encoder_bb_0 = digital.diff_encoder_bb(M)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(M)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(MiconstellationObject)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((Constelacion), 1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, "/home/comdig2/Dropbox/EnUbuntuFull/ClaseComDig/LibroAplicativos/Capitilo 2/Lab2.5/gato_in.png", True)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, "/home/comdig2/Dropbox/EnUbuntuFull/ClaseComDig/LibroAplicativos/Capitilo 2/Lab2.5/texto_out.txt", False)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.blks2_packet_decoder_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code=code1,
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0.recv_pkt(ok, payload),
        	),
        )
        self.b_de_M_PAM_bb_0 = b_de_M_PAM_bb(
            M=M,
            SymbTune=0,
        )
        self.b_RRaised_cosine_cc_0 = b_RRaised_cosine_cc(
            Ganancia=1.,
            Interpolation=Sps,
            ntaps=ntaps*Sps,
            rolloff=rolloff,
            sps=Sps,
        )
        self.b_PCM_Encoder_Bb_0 = b_PCM_Encoder_Bb(
            code=code1,
            payload=payload,
        )
        self.b_M_PAM_bb_0 = b_M_PAM_bb(
            M=M,
            Nbps=8,
        )
        self.b_FLL_tunner_0 = b_FLL_tunner(
            ConstellationObject=MiconstellationObject,
        )
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)
        self.Pre_modulacion = Qt.QTabWidget()
        self.Pre_modulacion_widget_0 = Qt.QWidget()
        self.Pre_modulacion_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Pre_modulacion_widget_0)
        self.Pre_modulacion_grid_layout_0 = Qt.QGridLayout()
        self.Pre_modulacion_layout_0.addLayout(self.Pre_modulacion_grid_layout_0)
        self.Pre_modulacion.addTab(self.Pre_modulacion_widget_0, "Capa8.Mensaje continuo")
        self.Pre_modulacion_widget_1 = Qt.QWidget()
        self.Pre_modulacion_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Pre_modulacion_widget_1)
        self.Pre_modulacion_grid_layout_1 = Qt.QGridLayout()
        self.Pre_modulacion_layout_1.addLayout(self.Pre_modulacion_grid_layout_1)
        self.Pre_modulacion.addTab(self.Pre_modulacion_widget_1, "Capa7.Cuantificacion")
        self.Pre_modulacion_widget_2 = Qt.QWidget()
        self.Pre_modulacion_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Pre_modulacion_widget_2)
        self.Pre_modulacion_grid_layout_2 = Qt.QGridLayout()
        self.Pre_modulacion_layout_2.addLayout(self.Pre_modulacion_grid_layout_2)
        self.Pre_modulacion.addTab(self.Pre_modulacion_widget_2, "Capa6.PCM")
        self.Pre_modulacion_widget_3 = Qt.QWidget()
        self.Pre_modulacion_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Pre_modulacion_widget_3)
        self.Pre_modulacion_grid_layout_3 = Qt.QGridLayout()
        self.Pre_modulacion_layout_3.addLayout(self.Pre_modulacion_grid_layout_3)
        self.Pre_modulacion.addTab(self.Pre_modulacion_widget_3, "Capa5.Otrastecnicas")
        self.Pre_modulacion_widget_4 = Qt.QWidget()
        self.Pre_modulacion_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Pre_modulacion_widget_4)
        self.Pre_modulacion_grid_layout_4 = Qt.QGridLayout()
        self.Pre_modulacion_layout_4.addLayout(self.Pre_modulacion_grid_layout_4)
        self.Pre_modulacion.addTab(self.Pre_modulacion_widget_4, "Capa4.CodificacionBinaria")
        self.Pre_modulacion_widget_5 = Qt.QWidget()
        self.Pre_modulacion_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Pre_modulacion_widget_5)
        self.Pre_modulacion_grid_layout_5 = Qt.QGridLayout()
        self.Pre_modulacion_layout_5.addLayout(self.Pre_modulacion_grid_layout_5)
        self.Pre_modulacion.addTab(self.Pre_modulacion_widget_5, "Capa3.M-PAM")
        self.Instrumentos_grid_layout_1.addWidget(self.Pre_modulacion, 1,0,1,1)
        self._NodB_range = Range(-140., 0., 1., -80, 200)
        self._NodB_win = RangeWidget(self._NodB_range, self.set_NodB, "Ch_No(dB)", "counter", float)
        self.controls_grid_layout_0.addWidget(self._NodB_win, 0,0,1,1)
        self._Ch_Jitter_range = Range(-.9, .9, 0.01, 0, 200)
        self._Ch_Jitter_win = RangeWidget(self._Ch_Jitter_range, self.set_Ch_Jitter, "Ch_Jitter", "slider", float)
        self.controls_grid_layout_0.addWidget(self._Ch_Jitter_win, 0,3,1,1)
        self._Ch_Frec_offset_range = Range(0, 100, 0.0001, 0, 200)
        self._Ch_Frec_offset_win = RangeWidget(self._Ch_Frec_offset_range, self.set_Ch_Frec_offset, "Ch_Frec_offset (Hz)", "counter", float)
        self.controls_grid_layout_0.addWidget(self._Ch_Frec_offset_win, 0,1,1,1)
        self._Ch_Delay_range = Range(0, 1000, 1, 0, 200)
        self._Ch_Delay_win = RangeWidget(self._Ch_Delay_range, self.set_Ch_Delay, "Ch_Delay", "counter", int)
        self.controls_grid_layout_0.addWidget(self._Ch_Delay_win, 0,2,1,1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))    
        self.connect((self.b_FLL_tunner_0, 0), (self.digital_constellation_decoder_cb_0, 0))    
        self.connect((self.b_FLL_tunner_0, 0), (self.qtgui_const_sink_x_0_1, 0))    
        self.connect((self.b_FLL_tunner_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.b_M_PAM_bb_0, 0), (self.digital_diff_encoder_bb_0, 0))    
        self.connect((self.b_PCM_Encoder_Bb_0, 0), (self.b_M_PAM_bb_0, 0))    
        self.connect((self.b_RRaised_cosine_cc_0, 0), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.b_de_M_PAM_bb_0, 0), (self.blks2_packet_decoder_0, 0))    
        self.connect((self.blks2_packet_decoder_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.b_PCM_Encoder_Bb_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.b_RRaised_cosine_cc_0, 0))    
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_diff_decoder_bb_0, 0))    
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.b_de_M_PAM_bb_0, 0))    
        self.connect((self.digital_diff_encoder_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))    
        self.connect((self.digital_lms_dd_equalizer_cc_0, 0), (self.b_FLL_tunner_0, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_lms_dd_equalizer_cc_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.analog_agc2_xx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Lab_total")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_B(self.samp_rate/self.Sps)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_B(self.samp_rate/self.Sps)
        self.set_ntaps(self.Sps*16)
        self.set_rrc_taps_rx(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.Sps), self.rolloff, self.ntaps*self.nfilts))
        self.b_RRaised_cosine_cc_0.set_Interpolation(self.Sps)
        self.b_RRaised_cosine_cc_0.set_ntaps(self.ntaps*self.Sps)
        self.b_RRaised_cosine_cc_0.set_sps(self.Sps)

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff
        self.set_W(self.B/(2.*(1.+self.rolloff)))
        self.set_rrc_taps_rx(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.Sps), self.rolloff, self.ntaps*self.nfilts))
        self.b_RRaised_cosine_cc_0.set_rolloff(self.rolloff)

    def get_Constelacion(self):
        return self.Constelacion

    def set_Constelacion(self, Constelacion):
        self.Constelacion = Constelacion
        self.set_M(len(self.Constelacion))
        self.digital_chunks_to_symbols_xx_0.set_symbol_table((self.Constelacion))

    def get_B(self):
        return self.B

    def set_B(self, B):
        self.B = B
        self.set_W(self.B/(2.*(1.+self.rolloff)))

    def get_W(self):
        return self.W

    def set_W(self, W):
        self.W = W
        self.set_Rs(2*self.W)

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_Bps(int(math.log(self.M,2)))
        self.b_M_PAM_bb_0.set_M(self.M)
        self.b_de_M_PAM_bb_0.set_M(self.M)

    def get_code1(self):
        return self.code1

    def set_code1(self, code1):
        self.code1 = code1
        self.set_NbpCode(len(self.code1)+10.)
        self.b_PCM_Encoder_Bb_0.set_code(self.code1)

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.set_Rb(self.Rs*self.Bps)
        self.set_Tmax_scope(64./self.Rs)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.Rs)

    def get_Bps(self):
        return self.Bps

    def set_Bps(self, Bps):
        self.Bps = Bps
        self.set_Rb(self.Rs*self.Bps)

    def get_tap4(self):
        return self.tap4

    def set_tap4(self, tap4):
        self.tap4 = tap4
        self.set_Ch_taps(fftpack.ifftshift(fftpack.ifft([self.tap3, self.tap4, 1.0, self.tap1, self.tap2])))

    def get_tap3(self):
        return self.tap3

    def set_tap3(self, tap3):
        self.tap3 = tap3
        self.set_Ch_taps(fftpack.ifftshift(fftpack.ifft([self.tap3, self.tap4, 1.0, self.tap1, self.tap2])))

    def get_tap2(self):
        return self.tap2

    def set_tap2(self, tap2):
        self.tap2 = tap2
        self.set_Ch_taps(fftpack.ifftshift(fftpack.ifft([self.tap3, self.tap4, 1.0, self.tap1, self.tap2])))

    def get_tap1(self):
        return self.tap1

    def set_tap1(self, tap1):
        self.tap1 = tap1
        self.set_Ch_taps(fftpack.ifftshift(fftpack.ifft([self.tap3, self.tap4, 1.0, self.tap1, self.tap2])))

    def get_payload(self):
        return self.payload

    def set_payload(self, payload):
        self.payload = payload
        self.set_Rbi(self.Rb/(1+self.NbpCode/self.payload))
        self.b_PCM_Encoder_Bb_0.set_payload(self.payload)

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_rrc_taps_rx(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.Sps), self.rolloff, self.ntaps*self.nfilts))
        self.b_RRaised_cosine_cc_0.set_ntaps(self.ntaps*self.Sps)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps_rx(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.Sps), self.rolloff, self.ntaps*self.nfilts))

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.set_Rbi(self.Rb/(1+self.NbpCode/self.payload))

    def get_NbpCode(self):
        return self.NbpCode

    def set_NbpCode(self, NbpCode):
        self.NbpCode = NbpCode
        self.set_Rbi(self.Rb/(1+self.NbpCode/self.payload))

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_rrc_taps_rx(self):
        return self.rrc_taps_rx

    def set_rrc_taps_rx(self, rrc_taps_rx):
        self.rrc_taps_rx = rrc_taps_rx
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rrc_taps_rx))

    def get_eq_gain(self):
        return self.eq_gain

    def set_eq_gain(self, eq_gain):
        self.eq_gain = eq_gain
        self.digital_lms_dd_equalizer_cc_0.set_gain(self.eq_gain)

    def get_Tmax_scope(self):
        return self.Tmax_scope

    def set_Tmax_scope(self, Tmax_scope):
        self.Tmax_scope = Tmax_scope

    def get_SymbTune(self):
        return self.SymbTune

    def set_SymbTune(self, SymbTune):
        self.SymbTune = SymbTune

    def get_Sps_o(self):
        return self.Sps_o

    def set_Sps_o(self, Sps_o):
        self.Sps_o = Sps_o

    def get_Rbi(self):
        return self.Rbi

    def set_Rbi(self, Rbi):
        self.Rbi = Rbi

    def get_NodB(self):
        return self.NodB

    def set_NodB(self, NodB):
        self.NodB = NodB

    def get_MiconstellationObject(self):
        return self.MiconstellationObject

    def set_MiconstellationObject(self, MiconstellationObject):
        self.MiconstellationObject = MiconstellationObject
        self.b_FLL_tunner_0.set_ConstellationObject(self.MiconstellationObject)

    def get_Gain_USRP_Tx_dB(self):
        return self.Gain_USRP_Tx_dB

    def set_Gain_USRP_Tx_dB(self, Gain_USRP_Tx_dB):
        self.Gain_USRP_Tx_dB = Gain_USRP_Tx_dB
        self.uhd_usrp_sink_0.set_gain(self.Gain_USRP_Tx_dB, 0)
        	

    def get_Gain_USRP_Rx_dB(self):
        return self.Gain_USRP_Rx_dB

    def set_Gain_USRP_Rx_dB(self, Gain_USRP_Rx_dB):
        self.Gain_USRP_Rx_dB = Gain_USRP_Rx_dB
        self.uhd_usrp_source_0.set_gain(self.Gain_USRP_Rx_dB, 0)
        	

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc
        self.uhd_usrp_sink_0.set_center_freq(self.Fc, 0)
        self.uhd_usrp_source_0.set_center_freq(self.Fc, 0)

    def get_Ch_taps(self):
        return self.Ch_taps

    def set_Ch_taps(self, Ch_taps):
        self.Ch_taps = Ch_taps

    def get_Ch_Jitter(self):
        return self.Ch_Jitter

    def set_Ch_Jitter(self, Ch_Jitter):
        self.Ch_Jitter = Ch_Jitter

    def get_Ch_Frec_offset(self):
        return self.Ch_Frec_offset

    def set_Ch_Frec_offset(self, Ch_Frec_offset):
        self.Ch_Frec_offset = Ch_Frec_offset

    def get_Ch_Delay(self):
        return self.Ch_Delay

    def set_Ch_Delay(self, Ch_Delay):
        self.Ch_Delay = Ch_Delay


def main(top_block_cls=Lab_total, options=None):

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
