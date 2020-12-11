#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: labcomunicaciones2_2020
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
import E3TRadio
import e_VCO_fase_fc_0
import math
from gnuradio import qtgui

class e_VCO_Fase_Parcialgrc(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
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

        self.settings = Qt.QSettings("GNU Radio", "e_VCO_Fase_Parcialgrc")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.M = M = 4
        self.Rb = Rb = 100
        self.BpS = BpS = int(math.log(M,2))
        self.Sps = Sps = 64*BpS
        self.Rs = Rs = Rb/BpS
        self.samp_rate = samp_rate = Rs*Sps
        self.run_stop = run_stop = True
        self.Tupdate = Tupdate = 1./Rb
        self.P = P = 0.
        self.Ar = Ar = 0.08
        self.A = A = 1.

        ##################################################
        # Blocks
        ##################################################
        self._P_range = Range(-2.*math.pi, 2.*math.pi, (4.*math.pi)/360., 0., 200)
        self._P_win = RangeWidget(self._P_range, self.set_P, 'Fase', "counter_slider", float)
        self.top_grid_layout.addWidget(self._P_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Ar_range = Range(0, 4., (4.)/50., 0.08, 200)
        self._Ar_win = RangeWidget(self._Ar_range, self.set_Ar, 'Ruido', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Ar_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._A_range = Range(-1.5, 1.5, (1.5)/100., 1., 200)
        self._A_win = RangeWidget(self._A_range, self.set_A, 'A', "counter_slider", float)
        self.top_grid_layout.addWidget(self._A_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        _run_stop_check_box = Qt.QCheckBox('Inicial/Parar')
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.items())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_0_0_0 = qtgui.time_sink_f(
            1024, #size
            (samp_rate), #samp_rate
            "Comparacion de mensaje y EC", #name
            3 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0_0.set_update_time(Tupdate)
        self.qtgui_time_sink_x_0_0_0_0_0.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_0_0_0_0.set_y_label('Amplitud', 'volts')

        self.qtgui_time_sink_x_0_0_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_stem_plot(False)


        labels = ['Mensaje', 'BPSK parte real', 'BPSK parte Imaginaria', '', '',
            '', '', '', '', '']
        widths = [3, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_0_win, 4, 1, 1, 2)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_0_0 = qtgui.time_sink_f(
            1024, #size
            (samp_rate), #samp_rate
            "Nivel de Amplitud", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0.set_update_time(Tupdate)
        self.qtgui_time_sink_x_0_0_0_0.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_0_0_0.set_y_label('Amplitud', 'volts')

        self.qtgui_time_sink_x_0_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_stem_plot(False)


        labels = ['.', '', '', '', '',
            '', '', '', '', '']
        widths = [3, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_win, 3, 0, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
            int(1024/Sps), #size
            (samp_rate), #samp_rate
            "Nivel de Fase. M-PAM", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(Tupdate)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-2*math.pi, 2*math.pi)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Fase', 'radianes')

        self.qtgui_time_sink_x_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(True)


        labels = ['.', '', '', '', '',
            '', '', '', '', '']
        widths = [3, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [0, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_win, 3, 1, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_1 = qtgui.const_sink_c(
            4000, #size
            "CONSTELACION", #name
            1 #number of inputs
        )
        self.qtgui_const_sink_x_1.set_update_time(0.10)
        self.qtgui_const_sink_x_1.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_1.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1.enable_autoscale(False)
        self.qtgui_const_sink_x_1.enable_grid(False)
        self.qtgui_const_sink_x_1.enable_axis_labels(True)


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

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_1_win = sip.wrapinstance(self.qtgui_const_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_1_win, 4, 0, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.e_VCO_fase_fc_0 = e_VCO_fase_fc_0.blk()
        self.blocks_vector_source_x_0 = blocks.vector_source_b((0,1,0,1,0,1,0,1), True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(BpS, gr.GR_MSB_FIRST)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff((2*math.pi)/M+P)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_char_to_float_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.analog_noise_source_x_1 = analog.noise_source_c(analog.GR_GAUSSIAN, Ar, 0)
        self.analog_const_source_x_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, A)
        self.E3TRadio_zero_order_hold2_cc_0 = E3TRadio.zero_order_hold2_cc(Sps)
        self.E3TRadio_Zero_Order_Hold_0 = E3TRadio.Zero_Order_Hold(int(Sps/BpS))



        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_Zero_Order_Hold_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 0))
        self.connect((self.E3TRadio_zero_order_hold2_cc_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.analog_const_source_x_0_0_0, 0), (self.e_VCO_fase_fc_0, 1))
        self.connect((self.analog_const_source_x_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 0))
        self.connect((self.analog_noise_source_x_1, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_char_to_float_1, 0), (self.E3TRadio_Zero_Order_Hold_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.qtgui_time_sink_x_0_0_0_0_0, 2))
        self.connect((self.blocks_complex_to_float_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.e_VCO_fase_fc_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_const_sink_x_1, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_char_to_float_1, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.e_VCO_fase_fc_0, 0), (self.E3TRadio_zero_order_hold2_cc_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "e_VCO_Fase_Parcialgrc")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_BpS(int(math.log(self.M,2)))
        self.blocks_multiply_const_vxx_0.set_k((2*math.pi)/self.M+self.P)

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.set_Rs(self.Rb/self.BpS)
        self.set_Tupdate(1./self.Rb)

    def get_BpS(self):
        return self.BpS

    def set_BpS(self, BpS):
        self.BpS = BpS
        self.set_Rs(self.Rb/self.BpS)
        self.set_Sps(64*self.BpS)
        self.E3TRadio_Zero_Order_Hold_0.set_retardo(int(self.Sps/self.BpS))

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_samp_rate(self.Rs*self.Sps)
        self.E3TRadio_Zero_Order_Hold_0.set_retardo(int(self.Sps/self.BpS))
        self.E3TRadio_zero_order_hold2_cc_0.set_retardo(self.Sps)

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.set_samp_rate(self.Rs*self.Sps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate((self.samp_rate))
        self.qtgui_time_sink_x_0_0_0_0.set_samp_rate((self.samp_rate))
        self.qtgui_time_sink_x_0_0_0_0_0.set_samp_rate((self.samp_rate))

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        self._run_stop_callback(self.run_stop)

    def get_Tupdate(self):
        return self.Tupdate

    def set_Tupdate(self, Tupdate):
        self.Tupdate = Tupdate
        self.qtgui_time_sink_x_0_0_0.set_update_time(self.Tupdate)
        self.qtgui_time_sink_x_0_0_0_0.set_update_time(self.Tupdate)
        self.qtgui_time_sink_x_0_0_0_0_0.set_update_time(self.Tupdate)

    def get_P(self):
        return self.P

    def set_P(self, P):
        self.P = P
        self.blocks_multiply_const_vxx_0.set_k((2*math.pi)/self.M+self.P)

    def get_Ar(self):
        return self.Ar

    def set_Ar(self, Ar):
        self.Ar = Ar
        self.analog_noise_source_x_1.set_amplitude(self.Ar)

    def get_A(self):
        return self.A

    def set_A(self, A):
        self.A = A
        self.analog_const_source_x_0_0_0.set_offset(self.A)



def main(top_block_cls=e_VCO_Fase_Parcialgrc, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
