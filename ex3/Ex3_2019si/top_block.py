#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Aug 21 05:27:02 2019
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
from b_Canal_AWGN import b_Canal_AWGN  # grc-generated hier_block
from b_Eye_Diagram_c import b_Eye_Diagram_c  # grc-generated hier_block
from b_PCM_Encoder_Bb import b_PCM_Encoder_Bb  # grc-generated hier_block
from b_PSD_c import b_PSD_c  # grc-generated hier_block
from b_sampler_cc import b_sampler_cc  # grc-generated hier_block
from b_u_M_PAM_bb import b_u_M_PAM_bb  # grc-generated hier_block
from b_u_de_M_PAM_bb import b_u_de_M_PAM_bb  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import e_VCO_fase_fc_0
import e_c_p
import e_mpam_ph
import e_phase
import math
import pmt
import sip
import wform  # embedded python module
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 390625
        self.samp_rate_data = samp_rate_data = samp_rate
        self.Sps = Sps = 8
        self.M = M = 8
        self.code1 = code1 = '010110011011101100010101011111101001001110001011010001101010001'
        self.Rs = Rs = samp_rate_data/Sps
        self.BpS = BpS = int(math.log(M,2))
        self.payload = payload = 128
        self.Rollof = Rollof = 0.5
        self.Rb = Rb = Rs*BpS
        self.NBpCode = NBpCode = len(code1)/8+10.
        self.run_stop = run_stop = True
        self.h = h = wform.rrcos(Sps,  Sps*32, Rollof)
        self.Rbi = Rbi = Rb/(1+NBpCode/payload)
        self.Delay_mpam = Delay_mpam = 36
        self.Delay = Delay = 6

        ##################################################
        # Blocks
        ##################################################
        self.Menu = Qt.QTabWidget()
        self.Menu_widget_0 = Qt.QWidget()
        self.Menu_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_0)
        self.Menu_grid_layout_0 = Qt.QGridLayout()
        self.Menu_layout_0.addLayout(self.Menu_grid_layout_0)
        self.Menu.addTab(self.Menu_widget_0, 'Info')
        self.Menu_widget_1 = Qt.QWidget()
        self.Menu_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_1)
        self.Menu_grid_layout_1 = Qt.QGridLayout()
        self.Menu_layout_1.addLayout(self.Menu_grid_layout_1)
        self.Menu.addTab(self.Menu_widget_1, 'Modulacion')
        self.Menu_widget_2 = Qt.QWidget()
        self.Menu_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_2)
        self.Menu_grid_layout_2 = Qt.QGridLayout()
        self.Menu_layout_2.addLayout(self.Menu_grid_layout_2)
        self.Menu.addTab(self.Menu_widget_2, 'Canal')
        self.top_grid_layout.addWidget(self.Menu, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Delay_mpam_range = Range(0, 256, 1, 36, 200)
        self._Delay_mpam_win = RangeWidget(self._Delay_mpam_range, self.set_Delay_mpam, 'Retraso a T3', "counter_slider", int)
        self.Menu_grid_layout_0.addWidget(self._Delay_mpam_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.Menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_0.setColumnStretch(c, 1)
        self._Delay_range = Range(0, Sps-1, 1, 6, 200)
        self._Delay_win = RangeWidget(self._Delay_range, self.set_Delay, 'Timing (Clock Recovery)', "counter_slider", int)
        self.top_grid_layout.addWidget(self._Delay_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        _run_stop_check_box = Qt.QCheckBox('Inicial/Parar')
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.iteritems())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_3 = qtgui.time_sink_f(
        	1024, #size
        	Rb, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_3.set_update_time(0.10)
        self.qtgui_time_sink_x_3.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_3.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_3.enable_tags(-1, True)
        self.qtgui_time_sink_x_3.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_3.enable_autoscale(False)
        self.qtgui_time_sink_x_3.enable_grid(False)
        self.qtgui_time_sink_x_3.enable_axis_labels(True)
        self.qtgui_time_sink_x_3.enable_control_panel(False)
        self.qtgui_time_sink_x_3.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_3.disable_legend()

        labels = ['T3', 'R3', '', '', '',
                  '', '', '', '', '']
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

        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_3.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_3.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_3.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_3.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_3.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_3.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_3.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_3_win = sip.wrapinstance(self.qtgui_time_sink_x_3.pyqwidget(), Qt.QWidget)
        self.Menu_grid_layout_0.addWidget(self._qtgui_time_sink_x_3_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.Menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
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
        self.Menu_grid_layout_1.addWidget(self._qtgui_const_sink_x_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.Menu_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_1.setColumnStretch(c, 1)
        self.interp_fir_filter_xxx_1_0 = filter.interp_fir_filter_ccc(1, (h))
        self.interp_fir_filter_xxx_1_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_1 = filter.interp_fir_filter_ccc(Sps, (h))
        self.interp_fir_filter_xxx_1.declare_sample_delay(0)
        self.e_phase = e_phase.blk(M=M)
        self.e_mpam_ph = e_mpam_ph.blk(M=M)
        self.e_c_p = e_c_p.blk(M=M)
        self.e_VCO_fase_fc_0 = e_VCO_fase_fc_0.blk()
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((1./Sps, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/uis-e3t/MisGits/comdig_examenes/ex3/Ex3_2019si/enviado.txt', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/uis-e3t/MisGits/comdig_examenes/ex3/Ex3_2019si/recibido.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, Delay_mpam)
        self.blocks_char_to_float_3_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_3 = blocks.char_to_float(1, 1)
        self.blks2_packet_decoder_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code=code1,
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0.recv_pkt(ok, payload),
        	),
        )
        self.b_u_de_M_PAM_bb_0 = b_u_de_M_PAM_bb(
            M=M,
        )
        self.b_u_M_PAM_bb_0 = b_u_M_PAM_bb(
            M=M,
        )
        self.b_sampler_cc_0 = b_sampler_cc(
            DelayDiez=Delay,
            Sps=Sps,
        )
        self.b_PSD_c_0 = b_PSD_c(
            Ensayos=1000000,
            Fc=10000,
            N=1024,
            Titulo="PSD",
            Ymax=6e-6,
            samp_rate_audio=samp_rate_data,
        )
        self.Menu_grid_layout_2.addWidget(self.b_PSD_c_0, 1, 0, 1, 1)
        for r in range(1, 2):
            self.Menu_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_2.setColumnStretch(c, 1)
        self.b_PCM_Encoder_Bb_0 = b_PCM_Encoder_Bb(
            code=code1,
            payload=payload,
        )
        self.b_Eye_Diagram_c_0 = b_Eye_Diagram_c(
            AlphaLineas=0.5,
            Delay_i=0,
            GrosorLineas=20,
            N_eyes=2,
            Samprate=samp_rate_data,
            Sps=Sps,
            Title="Eye Diagramm",
            Ymax=2,
            Ymin=-2,
        )
        self.Menu_grid_layout_2.addWidget(self.b_Eye_Diagram_c_0, 0, 0, 1, 1)
        for r in range(0, 1):
            self.Menu_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_2.setColumnStretch(c, 1)
        self.b_Canal_AWGN_0 = b_Canal_AWGN(
            BW=samp_rate_data/2,
            Ch_NodB=-65,
            Ch_Toffset=0,
            samp_rate=samp_rate_data,
        )
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1.)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.e_VCO_fase_fc_0, 1))
        self.connect((self.b_Canal_AWGN_0, 0), (self.interp_fir_filter_xxx_1_0, 0))
        self.connect((self.b_PCM_Encoder_Bb_0, 0), (self.b_u_M_PAM_bb_0, 0))
        self.connect((self.b_sampler_cc_0, 0), (self.b_Eye_Diagram_c_0, 1))
        self.connect((self.b_sampler_cc_0, 1), (self.e_c_p, 0))
        self.connect((self.b_sampler_cc_0, 1), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.b_u_M_PAM_bb_0, 0), (self.blocks_char_to_float_3, 0))
        self.connect((self.b_u_M_PAM_bb_0, 0), (self.e_mpam_ph, 0))
        self.connect((self.b_u_de_M_PAM_bb_0, 0), (self.blks2_packet_decoder_0, 0))
        self.connect((self.blks2_packet_decoder_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_char_to_float_3, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_char_to_float_3_0, 0), (self.qtgui_time_sink_x_3, 1))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_3, 0))
        self.connect((self.blocks_file_source_0, 0), (self.b_PCM_Encoder_Bb_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.b_Eye_Diagram_c_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.b_sampler_cc_0, 0))
        self.connect((self.e_VCO_fase_fc_0, 0), (self.interp_fir_filter_xxx_1, 0))
        self.connect((self.e_c_p, 0), (self.e_phase, 0))
        self.connect((self.e_mpam_ph, 0), (self.e_VCO_fase_fc_0, 0))
        self.connect((self.e_phase, 0), (self.b_u_de_M_PAM_bb_0, 0))
        self.connect((self.e_phase, 0), (self.blocks_char_to_float_3_0, 0))
        self.connect((self.interp_fir_filter_xxx_1, 0), (self.b_Canal_AWGN_0, 0))
        self.connect((self.interp_fir_filter_xxx_1, 0), (self.b_PSD_c_0, 0))
        self.connect((self.interp_fir_filter_xxx_1_0, 0), (self.blocks_multiply_const_vxx_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samp_rate_data(self.samp_rate)

    def get_samp_rate_data(self):
        return self.samp_rate_data

    def set_samp_rate_data(self, samp_rate_data):
        self.samp_rate_data = samp_rate_data
        self.b_PSD_c_0.set_samp_rate_audio(self.samp_rate_data)
        self.b_Eye_Diagram_c_0.set_Samprate(self.samp_rate_data)
        self.b_Canal_AWGN_0.set_BW(self.samp_rate_data/2)
        self.b_Canal_AWGN_0.set_samp_rate(self.samp_rate_data)
        self.set_Rs(self.samp_rate_data/self.Sps)

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_h(wform.rrcos(self.Sps,  self.Sps*32, self.Rollof))
        self.blocks_multiply_const_vxx_1.set_k((1./self.Sps, ))
        self.b_sampler_cc_0.set_Sps(self.Sps)
        self.b_Eye_Diagram_c_0.set_Sps(self.Sps)
        self.set_Rs(self.samp_rate_data/self.Sps)

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.e_phase.M = self.M
        self.e_mpam_ph.M = self.M
        self.e_c_p.M = self.M
        self.b_u_de_M_PAM_bb_0.set_M(self.M)
        self.b_u_M_PAM_bb_0.set_M(self.M)
        self.set_BpS(int(math.log(self.M,2)))

    def get_code1(self):
        return self.code1

    def set_code1(self, code1):
        self.code1 = code1
        self.b_PCM_Encoder_Bb_0.set_code(self.code1)
        self.set_NBpCode(len(self.code1)/8+10.)

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.set_Rb(self.Rs*self.BpS)

    def get_BpS(self):
        return self.BpS

    def set_BpS(self, BpS):
        self.BpS = BpS
        self.set_Rb(self.Rs*self.BpS)

    def get_payload(self):
        return self.payload

    def set_payload(self, payload):
        self.payload = payload
        self.b_PCM_Encoder_Bb_0.set_payload(self.payload)
        self.set_Rbi(self.Rb/(1+self.NBpCode/self.payload))

    def get_Rollof(self):
        return self.Rollof

    def set_Rollof(self, Rollof):
        self.Rollof = Rollof
        self.set_h(wform.rrcos(self.Sps,  self.Sps*32, self.Rollof))

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.qtgui_time_sink_x_3.set_samp_rate(self.Rb)
        self.set_Rbi(self.Rb/(1+self.NBpCode/self.payload))

    def get_NBpCode(self):
        return self.NBpCode

    def set_NBpCode(self, NBpCode):
        self.NBpCode = NBpCode
        self.set_Rbi(self.Rb/(1+self.NBpCode/self.payload))

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_h(self):
        return self.h

    def set_h(self, h):
        self.h = h
        self.interp_fir_filter_xxx_1_0.set_taps((self.h))
        self.interp_fir_filter_xxx_1.set_taps((self.h))

    def get_Rbi(self):
        return self.Rbi

    def set_Rbi(self, Rbi):
        self.Rbi = Rbi

    def get_Delay_mpam(self):
        return self.Delay_mpam

    def set_Delay_mpam(self, Delay_mpam):
        self.Delay_mpam = Delay_mpam
        self.blocks_delay_0.set_dly(self.Delay_mpam)

    def get_Delay(self):
        return self.Delay

    def set_Delay(self, Delay):
        self.Delay = Delay
        self.b_sampler_cc_0.set_DelayDiez(self.Delay)


def main(top_block_cls=top_block, options=None):

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
