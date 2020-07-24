#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Top Block
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

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from b_Canal_AWGN_ff import b_Canal_AWGN_ff  # grc-generated hier_block
from b_PSD import b_PSD  # grc-generated hier_block
from b_binary_bipolar_source_f import b_binary_bipolar_source_f  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
import E3TRadio
import math
import numpy
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
        self.Sps = Sps = 4
        self.ntaps = ntaps = Sps*8
        self.Tntaps = Tntaps = 0.1e-3
        self.samp_rate = samp_rate = (ntaps-2)/Tntaps
        self.Rb = Rb = samp_rate/Sps
        self.W = W = Rb/2
        self.Rolloff = Rolloff = 0.1
        self.N = N = 1024
        self.senal_p2 = senal_p2 = numpy.concatenate(([1],[0]*(int(ntaps/Sps)-1)))
        self.run_stop = run_stop = True
        self.h = h = wform.rcos(Sps,ntaps,Rolloff)
        self.bits_afectados_por_ISI = bits_afectados_por_ISI = ntaps/Sps-1
        self.Samp_rate_T4 = Samp_rate_T4 = Rb
        self.No_dB = No_dB = -60
        self.Fmax = Fmax = samp_rate/2
        self.F_Resolucion = F_Resolucion = samp_rate/N
        self.Channel_BW = Channel_BW = samp_rate/2.
        self.BW = BW = W*(1+Rolloff)

        ##################################################
        # Blocks
        ##################################################
        self.menu = Qt.QTabWidget()
        self.menu_widget_0 = Qt.QWidget()
        self.menu_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_0)
        self.menu_grid_layout_0 = Qt.QGridLayout()
        self.menu_layout_0.addLayout(self.menu_grid_layout_0)
        self.menu.addTab(self.menu_widget_0, 'Datos de Entrada')
        self.menu_widget_1 = Qt.QWidget()
        self.menu_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_1)
        self.menu_grid_layout_1 = Qt.QGridLayout()
        self.menu_layout_1.addLayout(self.menu_grid_layout_1)
        self.menu.addTab(self.menu_widget_1, 'P1. Bits afectados')
        self.menu_widget_2 = Qt.QWidget()
        self.menu_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_2)
        self.menu_grid_layout_2 = Qt.QGridLayout()
        self.menu_layout_2.addLayout(self.menu_grid_layout_2)
        self.menu.addTab(self.menu_widget_2, 'P2. Frec en T4')
        self.menu_widget_3 = Qt.QWidget()
        self.menu_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_3)
        self.menu_grid_layout_3 = Qt.QGridLayout()
        self.menu_layout_3.addLayout(self.menu_grid_layout_3)
        self.menu.addTab(self.menu_widget_3, 'P3.PSD')
        self.top_grid_layout.addWidget(self.menu, 2, 0, 1, 2)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._No_dB_range = Range(-300, 0, 300/100., -60, 200)
        self._No_dB_win = RangeWidget(self._No_dB_range, self.set_No_dB, 'No (dB)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._No_dB_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Channel_BW_range = Range(0., samp_rate/2., (samp_rate/2)/100., samp_rate/2., 200)
        self._Channel_BW_win = RangeWidget(self._Channel_BW_range, self.set_Channel_BW, 'Channel_BW', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Channel_BW_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        _run_stop_check_box = Qt.QCheckBox('Pause')
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
        self.qtgui_time_sink_x_0_1_0 = qtgui.time_sink_f(
            ntaps, #size
            samp_rate, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1_0.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_1_0.set_y_label('output of  waveform filter', "")

        self.qtgui_time_sink_x_0_1_0.enable_tags(True)
        self.qtgui_time_sink_x_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1_0.enable_grid(False)
        self.qtgui_time_sink_x_0_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1_0.enable_stem_plot(False)


        labels = ['', 'Info Received', '', '', '',
            '', '', '', '', '']
        widths = [1, 2, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_1_0_win, 2, 0, 1, 2)
        for r in range(2, 3):
            self.menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 2):
            self.menu_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_f(
            int(ntaps/Sps), #size
            Rb, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_1.set_y_label('input of the waveform filter', "")

        self.qtgui_time_sink_x_0_1.enable_tags(True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1.enable_stem_plot(True)


        labels = ['', 'Info Received', '', '', '',
            '', '', '', '', '']
        widths = [2, 2, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_1_win, 1, 0, 1, 2)
        for r in range(1, 2):
            self.menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 2):
            self.menu_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_number_sink_0_2_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_VERT,
            3
        )
        self.qtgui_number_sink_0_2_0.set_update_time(0.10)
        self.qtgui_number_sink_0_2_0.set_title("Parámetros de la PSD")

        labels = ['BW', 'Fmax', 'F_resolucion', '', '',
            '', '', '', '', '']
        units = ['Hz', 'Hz', 'Hz', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(3):
            self.qtgui_number_sink_0_2_0.set_min(i, -1)
            self.qtgui_number_sink_0_2_0.set_max(i, 1)
            self.qtgui_number_sink_0_2_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_2_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_2_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_2_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_2_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_2_0.enable_autoscale(False)
        self._qtgui_number_sink_0_2_0_win = sip.wrapinstance(self.qtgui_number_sink_0_2_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_3.addWidget(self._qtgui_number_sink_0_2_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.menu_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_number_sink_0_2 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_2.set_update_time(0.10)
        self.qtgui_number_sink_0_2.set_title("")

        labels = ['Bits afectados por cada bit', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_2.set_min(i, -1)
            self.qtgui_number_sink_0_2.set_max(i, 1)
            self.qtgui_number_sink_0_2.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_2.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_2.set_label(i, labels[i])
            self.qtgui_number_sink_0_2.set_unit(i, units[i])
            self.qtgui_number_sink_0_2.set_factor(i, factor[i])

        self.qtgui_number_sink_0_2.enable_autoscale(False)
        self._qtgui_number_sink_0_2_win = sip.wrapinstance(self.qtgui_number_sink_0_2.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_1.addWidget(self._qtgui_number_sink_0_2_win, 1, 0, 1, 2)
        for r in range(1, 2):
            self.menu_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 2):
            self.menu_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")

        labels = ['La frecuencia de muestreo en T4', '', '', '', '',
            '', '', '', '', '']
        units = ['Hz', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_2.addWidget(self._qtgui_number_sink_0_win, 1, 0, 1, 2)
        for r in range(1, 2):
            self.menu_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 2):
            self.menu_grid_layout_2.setColumnStretch(c, 1)
        self.interp_fir_filter_xxx_0_0 = filter.interp_fir_filter_fff(Sps, h)
        self.interp_fir_filter_xxx_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(Sps, h)
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_vector_source_x_0_0 = blocks.vector_source_f(senal_p2, True, 1, [])
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(1.)
        self.blocks_delay_0_1_0 = blocks.delay(gr.sizeof_float*1, int((ntaps/Sps)/2))
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_float*1, 0)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.b_binary_bipolar_source_f_0 = b_binary_bipolar_source_f(
            Am=1.,
            Spb=1,
        )
        self.b_PSD_0_0_0 = b_PSD(
            Ensayos=1000000,
            N=1024,
            Titulo='PSD in  R3',
            Ymax=1e-5,
            samp_rate_audio=samp_rate,
        )

        self.menu_grid_layout_3.addWidget(self.b_PSD_0_0_0, 3, 0, 1, 1)
        for r in range(3, 4):
            self.menu_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_3.setColumnStretch(c, 1)
        self.b_Canal_AWGN_ff_0 = b_Canal_AWGN_ff(
            BW=Channel_BW,
            Ch_NodB=No_dB,
            Ch_Toffset=0,
            samp_rate=samp_rate,
        )
        self.analog_const_source_x_0_2_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, Fmax)
        self.analog_const_source_x_0_2_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, BW)
        self.analog_const_source_x_0_2 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, bits_afectados_por_ISI)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, F_Resolucion)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, Rb)
        self.E3TRadio_unipolar_to_bipolar_ff_0 = E3TRadio.unipolar_to_bipolar_ff(1.)
        self.E3TRadio_diezma_ff_0 = E3TRadio.diezma_ff(Sps, 2)
        self.E3TRadio_decisor_fb_0 = E3TRadio.decisor_fb(0.)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_decisor_fb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.E3TRadio_diezma_ff_0, 0), (self.E3TRadio_decisor_fb_0, 0))
        self.connect((self.E3TRadio_unipolar_to_bipolar_ff_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.analog_const_source_x_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.analog_const_source_x_0_0, 0), (self.qtgui_number_sink_0_2_0, 2))
        self.connect((self.analog_const_source_x_0_2, 0), (self.qtgui_number_sink_0_2, 0))
        self.connect((self.analog_const_source_x_0_2_0, 0), (self.qtgui_number_sink_0_2_0, 0))
        self.connect((self.analog_const_source_x_0_2_1, 0), (self.qtgui_number_sink_0_2_0, 1))
        self.connect((self.b_Canal_AWGN_ff_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.b_binary_bipolar_source_f_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.E3TRadio_unipolar_to_bipolar_ff_0, 0))
        self.connect((self.blocks_delay_0_1, 0), (self.qtgui_time_sink_x_0_1_0, 0))
        self.connect((self.blocks_delay_0_1_0, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.E3TRadio_diezma_ff_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.b_PSD_0_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.blocks_delay_0_1_0, 0))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.interp_fir_filter_xxx_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.b_Canal_AWGN_ff_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.blocks_delay_0_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_Rb(self.samp_rate/self.Sps)
        self.set_bits_afectados_por_ISI(self.ntaps/self.Sps-1)
        self.set_h(wform.rcos(self.Sps,self.ntaps,self.Rolloff))
        self.set_ntaps(self.Sps*8)
        self.set_senal_p2(numpy.concatenate(([1],[0]*(int(self.ntaps/self.Sps)-1))))
        self.blocks_delay_0_1_0.set_dly(int((self.ntaps/self.Sps)/2))

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_bits_afectados_por_ISI(self.ntaps/self.Sps-1)
        self.set_h(wform.rcos(self.Sps,self.ntaps,self.Rolloff))
        self.set_samp_rate((self.ntaps-2)/self.Tntaps)
        self.set_senal_p2(numpy.concatenate(([1],[0]*(int(self.ntaps/self.Sps)-1))))
        self.blocks_delay_0_1_0.set_dly(int((self.ntaps/self.Sps)/2))

    def get_Tntaps(self):
        return self.Tntaps

    def set_Tntaps(self, Tntaps):
        self.Tntaps = Tntaps
        self.set_samp_rate((self.ntaps-2)/self.Tntaps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_Channel_BW(self.samp_rate/2.)
        self.set_F_Resolucion(self.samp_rate/self.N)
        self.set_Fmax(self.samp_rate/2)
        self.set_Rb(self.samp_rate/self.Sps)
        self.b_Canal_AWGN_ff_0.set_samp_rate(self.samp_rate)
        self.b_PSD_0_0_0.set_samp_rate_audio(self.samp_rate)
        self.qtgui_time_sink_x_0_1_0.set_samp_rate(self.samp_rate)

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.set_Samp_rate_T4(self.Rb)
        self.set_W(self.Rb/2)
        self.analog_const_source_x_0.set_offset(self.Rb)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.Rb)

    def get_W(self):
        return self.W

    def set_W(self, W):
        self.W = W
        self.set_BW(self.W*(1+self.Rolloff))

    def get_Rolloff(self):
        return self.Rolloff

    def set_Rolloff(self, Rolloff):
        self.Rolloff = Rolloff
        self.set_BW(self.W*(1+self.Rolloff))
        self.set_h(wform.rcos(self.Sps,self.ntaps,self.Rolloff))

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.set_F_Resolucion(self.samp_rate/self.N)

    def get_senal_p2(self):
        return self.senal_p2

    def set_senal_p2(self, senal_p2):
        self.senal_p2 = senal_p2
        self.blocks_vector_source_x_0_0.set_data(self.senal_p2, [])

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
        self.interp_fir_filter_xxx_0.set_taps(self.h)
        self.interp_fir_filter_xxx_0_0.set_taps(self.h)

    def get_bits_afectados_por_ISI(self):
        return self.bits_afectados_por_ISI

    def set_bits_afectados_por_ISI(self, bits_afectados_por_ISI):
        self.bits_afectados_por_ISI = bits_afectados_por_ISI
        self.analog_const_source_x_0_2.set_offset(self.bits_afectados_por_ISI)

    def get_Samp_rate_T4(self):
        return self.Samp_rate_T4

    def set_Samp_rate_T4(self, Samp_rate_T4):
        self.Samp_rate_T4 = Samp_rate_T4

    def get_No_dB(self):
        return self.No_dB

    def set_No_dB(self, No_dB):
        self.No_dB = No_dB
        self.b_Canal_AWGN_ff_0.set_Ch_NodB(self.No_dB)

    def get_Fmax(self):
        return self.Fmax

    def set_Fmax(self, Fmax):
        self.Fmax = Fmax
        self.analog_const_source_x_0_2_1.set_offset(self.Fmax)

    def get_F_Resolucion(self):
        return self.F_Resolucion

    def set_F_Resolucion(self, F_Resolucion):
        self.F_Resolucion = F_Resolucion
        self.analog_const_source_x_0_0.set_offset(self.F_Resolucion)

    def get_Channel_BW(self):
        return self.Channel_BW

    def set_Channel_BW(self, Channel_BW):
        self.Channel_BW = Channel_BW
        self.b_Canal_AWGN_ff_0.set_BW(self.Channel_BW)

    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW
        self.analog_const_source_x_0_2_0.set_offset(self.BW)



def main(top_block_cls=top_block, options=None):

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
