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
import sip
from b_Canal_AWGN_ff import b_Canal_AWGN_ff  # grc-generated hier_block
from b_Eye_Diagram_simple_f import b_Eye_Diagram_simple_f  # grc-generated hier_block
from b_PSD import b_PSD  # grc-generated hier_block
from b_PSD_advanced import b_PSD_advanced  # grc-generated hier_block
from b_binary_bipolar_source1_f import b_binary_bipolar_source1_f  # grc-generated hier_block
from b_eye_diagram2_f import b_eye_diagram2_f  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
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
        self.N = N = 256
        self.F_Resolucion = F_Resolucion = 200000
        self.Nlobf = Nlobf = 8
        self.B = B = N*F_Resolucion
        self.samp_rate = samp_rate = B
        self.Rb = Rb = B/Nlobf
        self.Sps = Sps = int(samp_rate/Rb)
        self.ntaps = ntaps = Sps*1
        self.W = W = Rb/2
        self.Fmax = Fmax = samp_rate/2
        self.samp_rate_T4 = samp_rate_T4 = samp_rate
        self.samp_rate_16 = samp_rate_16 = samp_rate/16
        self.run_stop = run_stop = True
        self.h = h = wform.rect(Sps)
        self.bits_afectados_por_ISI = bits_afectados_por_ISI = int(ntaps/Sps)-1
        self.Retardo_ojo_t = Retardo_ojo_t = 0
        self.Retardo_ojo = Retardo_ojo = 4
        self.Retardo_Timing = Retardo_Timing = 4
        self.No_dB = No_dB = -300
        self.Channel_BW_P4 = Channel_BW_P4 = W
        self.Channel_BW = Channel_BW = Fmax
        self.BW = BW = Fmax

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
        self.menu.addTab(self.menu_widget_1, 'P1')
        self.menu_widget_2 = Qt.QWidget()
        self.menu_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_2)
        self.menu_grid_layout_2 = Qt.QGridLayout()
        self.menu_layout_2.addLayout(self.menu_grid_layout_2)
        self.menu.addTab(self.menu_widget_2, 'P2')
        self.menu_widget_3 = Qt.QWidget()
        self.menu_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_3)
        self.menu_grid_layout_3 = Qt.QGridLayout()
        self.menu_layout_3.addLayout(self.menu_grid_layout_3)
        self.menu.addTab(self.menu_widget_3, 'P3')
        self.menu_widget_4 = Qt.QWidget()
        self.menu_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_4)
        self.menu_grid_layout_4 = Qt.QGridLayout()
        self.menu_layout_4.addLayout(self.menu_grid_layout_4)
        self.menu.addTab(self.menu_widget_4, 'P4a')
        self.menu_widget_5 = Qt.QWidget()
        self.menu_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_5)
        self.menu_grid_layout_5 = Qt.QGridLayout()
        self.menu_layout_5.addLayout(self.menu_grid_layout_5)
        self.menu.addTab(self.menu_widget_5, 'P4b')
        self.top_grid_layout.addWidget(self.menu, 2, 0, 1, 6)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Retardo_ojo_t_range = Range(0, Sps*2, 1, 0, 200)
        self._Retardo_ojo_t_win = RangeWidget(self._Retardo_ojo_t_range, self.set_Retardo_ojo_t, 'Center the Eye-Timing Diagramm', "counter", int)
        self.top_grid_layout.addWidget(self._Retardo_ojo_t_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._No_dB_range = Range(-300, 0, 300/100., -300, 200)
        self._No_dB_win = RangeWidget(self._No_dB_range, self.set_No_dB, 'No (dB)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._No_dB_win, 0, 4, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
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
        self.qtgui_number_sink_0_2_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_VERT,
            1
        )
        self.qtgui_number_sink_0_2_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_2_0_0_0.set_title("bits afectados por ISI")

        labels = ['bits_afectados_por_ISI', 'Fmax', 'F_resolucion', '', '',
            '', '', '', '', '']
        units = ['bits', 'Hz', 'Hz', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_2_0_0_0.set_min(i, -1)
            self.qtgui_number_sink_0_2_0_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_2_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_2_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_2_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_2_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_2_0_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_2_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_2_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_2_0_0_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_3.addWidget(self._qtgui_number_sink_0_2_0_0_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.menu_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_number_sink_0_2_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_VERT,
            1
        )
        self.qtgui_number_sink_0_2_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_2_0_0.set_title("Muestras por bit en T4")

        labels = ['Sps', 'Fmax', 'F_resolucion', '', '',
            '', '', '', '', '']
        units = ['muestras por bit', 'Hz', 'Hz', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_2_0_0.set_min(i, -1)
            self.qtgui_number_sink_0_2_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_2_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_2_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_2_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_2_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_2_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_2_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_2_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_2_0_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_2.addWidget(self._qtgui_number_sink_0_2_0_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.menu_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_number_sink_0_2_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_VERT,
            1
        )
        self.qtgui_number_sink_0_2_0.set_update_time(0.10)
        self.qtgui_number_sink_0_2_0.set_title("Muestras por segundo en T4")

        labels = ['samp_rate', 'Fmax', 'F_resolucion', '', '',
            '', '', '', '', '']
        units = ['MHz', 'Hz', 'Hz', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
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
        self.menu_grid_layout_1.addWidget(self._qtgui_number_sink_0_2_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.menu_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_1.setColumnStretch(c, 1)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(Sps, h)
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.b_eye_diagram2_f_0 = b_eye_diagram2_f(
            Delay=0,
            Nvol=10000,
            Sps=Sps,
            samp_rate=samp_rate,
        )
        self.b_binary_bipolar_source1_f_0 = b_binary_bipolar_source1_f(
            Am=1.,
        )
        self.b_PSD_advanced_0 = b_PSD_advanced(
            Ensayos=1000000,
            Resolution=0.5e6,
            Titulo='espectro',
            Ymax=1e-5,
            samp_rate=samp_rate,
        )

        self.menu_grid_layout_5.addWidget(self.b_PSD_advanced_0, 4, 0, 1, 1)
        for r in range(4, 5):
            self.menu_grid_layout_5.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_5.setColumnStretch(c, 1)
        self.b_PSD_0_0_0_0 = b_PSD(
            Ensayos=1000000,
            N=1024,
            Titulo='PSD in  R4 modificado',
            Ymax=1e-5,
            samp_rate_audio=samp_rate,
        )

        self.menu_grid_layout_5.addWidget(self.b_PSD_0_0_0_0, 3, 0, 1, 1)
        for r in range(3, 4):
            self.menu_grid_layout_5.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_5.setColumnStretch(c, 1)
        self.b_PSD_0_0_0 = b_PSD(
            Ensayos=1000000,
            N=1024,
            Titulo='PSD in  R4',
            Ymax=1e-5,
            samp_rate_audio=samp_rate,
        )

        self.menu_grid_layout_0.addWidget(self.b_PSD_0_0_0, 3, 0, 1, 1)
        for r in range(3, 4):
            self.menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_0.setColumnStretch(c, 1)
        self.b_Eye_Diagram_simple_f_0 = b_Eye_Diagram_simple_f(
            AlphaLineas=0.5,
            Delay_i=Retardo_ojo_t,
            GrosorLineas=20,
            N_eyes=2,
            Samprate=samp_rate,
            Sps=Sps,
            Title="Diagrama de ojo en R4 modificado",
            Ymax=2,
            Ymin=-2,
        )

        self.menu_grid_layout_4.addWidget(self.b_Eye_Diagram_simple_f_0, 0, 0, 1, 1)
        for r in range(0, 1):
            self.menu_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_4.setColumnStretch(c, 1)
        self.b_Canal_AWGN_ff_0_0 = b_Canal_AWGN_ff(
            BW=Channel_BW_P4,
            Ch_NodB=No_dB,
            Ch_Toffset=0,
            samp_rate=samp_rate,
        )
        self.b_Canal_AWGN_ff_0 = b_Canal_AWGN_ff(
            BW=Channel_BW,
            Ch_NodB=No_dB,
            Ch_Toffset=0,
            samp_rate=samp_rate,
        )
        self.analog_const_source_x_0_2_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, bits_afectados_por_ISI)
        self.analog_const_source_x_0_2_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, Sps)
        self.analog_const_source_x_0_2_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, samp_rate_T4/1e6)
        self._Retardo_ojo_range = Range(0, Sps*2, 1, 4, 200)
        self._Retardo_ojo_win = RangeWidget(self._Retardo_ojo_range, self.set_Retardo_ojo, 'Center the Eye by a delay', "counter", int)
        self.top_grid_layout.addWidget(self._Retardo_ojo_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Retardo_Timing_range = Range(0, Sps-1, 1, 4, 200)
        self._Retardo_Timing_win = RangeWidget(self._Retardo_Timing_range, self.set_Retardo_Timing, 'Timing', "counter_slider", int)
        self.top_grid_layout.addWidget(self._Retardo_Timing_win, 0, 3, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.E3TRadio_diezma_ff_0 = E3TRadio.diezma_ff(Sps, 2)
        self.E3TRadio_bipolar_decisor_ff_0 = E3TRadio.bipolar_decisor_ff()



        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_bipolar_decisor_ff_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.E3TRadio_diezma_ff_0, 0), (self.E3TRadio_bipolar_decisor_ff_0, 0))
        self.connect((self.analog_const_source_x_0_2_0, 0), (self.qtgui_number_sink_0_2_0, 0))
        self.connect((self.analog_const_source_x_0_2_0_0, 0), (self.qtgui_number_sink_0_2_0_0, 0))
        self.connect((self.analog_const_source_x_0_2_0_0_0, 0), (self.qtgui_number_sink_0_2_0_0_0, 0))
        self.connect((self.b_Canal_AWGN_ff_0, 0), (self.E3TRadio_diezma_ff_0, 0))
        self.connect((self.b_Canal_AWGN_ff_0, 0), (self.b_PSD_0_0_0, 0))
        self.connect((self.b_Canal_AWGN_ff_0_0, 0), (self.b_Eye_Diagram_simple_f_0, 0))
        self.connect((self.b_Canal_AWGN_ff_0_0, 0), (self.b_PSD_0_0_0_0, 0))
        self.connect((self.b_Canal_AWGN_ff_0_0, 0), (self.b_PSD_advanced_0, 0))
        self.connect((self.b_Canal_AWGN_ff_0_0, 0), (self.b_eye_diagram2_f_0, 0))
        self.connect((self.b_binary_bipolar_source1_f_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.b_Canal_AWGN_ff_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.b_Canal_AWGN_ff_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.set_B(self.N*self.F_Resolucion)

    def get_F_Resolucion(self):
        return self.F_Resolucion

    def set_F_Resolucion(self, F_Resolucion):
        self.F_Resolucion = F_Resolucion
        self.set_B(self.N*self.F_Resolucion)

    def get_Nlobf(self):
        return self.Nlobf

    def set_Nlobf(self, Nlobf):
        self.Nlobf = Nlobf
        self.set_Rb(self.B/self.Nlobf)

    def get_B(self):
        return self.B

    def set_B(self, B):
        self.B = B
        self.set_Rb(self.B/self.Nlobf)
        self.set_samp_rate(self.B)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_Fmax(self.samp_rate/2)
        self.set_Sps(int(self.samp_rate/self.Rb))
        self.set_samp_rate_16(self.samp_rate/16)
        self.set_samp_rate_T4(self.samp_rate)
        self.b_Canal_AWGN_ff_0.set_samp_rate(self.samp_rate)
        self.b_Canal_AWGN_ff_0_0.set_samp_rate(self.samp_rate)
        self.b_Eye_Diagram_simple_f_0.set_Samprate(self.samp_rate)
        self.b_PSD_0_0_0.set_samp_rate_audio(self.samp_rate)
        self.b_PSD_0_0_0_0.set_samp_rate_audio(self.samp_rate)
        self.b_PSD_advanced_0.set_samp_rate(self.samp_rate)
        self.b_eye_diagram2_f_0.set_samp_rate(self.samp_rate)

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.set_Sps(int(self.samp_rate/self.Rb))
        self.set_W(self.Rb/2)

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_bits_afectados_por_ISI(int(self.ntaps/self.Sps)-1)
        self.set_h(wform.rect(self.Sps))
        self.set_ntaps(self.Sps*1)
        self.analog_const_source_x_0_2_0_0.set_offset(self.Sps)
        self.b_Eye_Diagram_simple_f_0.set_Sps(self.Sps)
        self.b_eye_diagram2_f_0.set_Sps(self.Sps)

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_bits_afectados_por_ISI(int(self.ntaps/self.Sps)-1)

    def get_W(self):
        return self.W

    def set_W(self, W):
        self.W = W
        self.set_Channel_BW_P4(self.W)

    def get_Fmax(self):
        return self.Fmax

    def set_Fmax(self, Fmax):
        self.Fmax = Fmax
        self.set_BW(self.Fmax)
        self.set_Channel_BW(self.Fmax)

    def get_samp_rate_T4(self):
        return self.samp_rate_T4

    def set_samp_rate_T4(self, samp_rate_T4):
        self.samp_rate_T4 = samp_rate_T4
        self.analog_const_source_x_0_2_0.set_offset(self.samp_rate_T4/1e6)

    def get_samp_rate_16(self):
        return self.samp_rate_16

    def set_samp_rate_16(self, samp_rate_16):
        self.samp_rate_16 = samp_rate_16

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

    def get_bits_afectados_por_ISI(self):
        return self.bits_afectados_por_ISI

    def set_bits_afectados_por_ISI(self, bits_afectados_por_ISI):
        self.bits_afectados_por_ISI = bits_afectados_por_ISI
        self.analog_const_source_x_0_2_0_0_0.set_offset(self.bits_afectados_por_ISI)

    def get_Retardo_ojo_t(self):
        return self.Retardo_ojo_t

    def set_Retardo_ojo_t(self, Retardo_ojo_t):
        self.Retardo_ojo_t = Retardo_ojo_t
        self.b_Eye_Diagram_simple_f_0.set_Delay_i(self.Retardo_ojo_t)

    def get_Retardo_ojo(self):
        return self.Retardo_ojo

    def set_Retardo_ojo(self, Retardo_ojo):
        self.Retardo_ojo = Retardo_ojo

    def get_Retardo_Timing(self):
        return self.Retardo_Timing

    def set_Retardo_Timing(self, Retardo_Timing):
        self.Retardo_Timing = Retardo_Timing

    def get_No_dB(self):
        return self.No_dB

    def set_No_dB(self, No_dB):
        self.No_dB = No_dB
        self.b_Canal_AWGN_ff_0.set_Ch_NodB(self.No_dB)
        self.b_Canal_AWGN_ff_0_0.set_Ch_NodB(self.No_dB)

    def get_Channel_BW_P4(self):
        return self.Channel_BW_P4

    def set_Channel_BW_P4(self, Channel_BW_P4):
        self.Channel_BW_P4 = Channel_BW_P4
        self.b_Canal_AWGN_ff_0_0.set_BW(self.Channel_BW_P4)

    def get_Channel_BW(self):
        return self.Channel_BW

    def set_Channel_BW(self, Channel_BW):
        self.Channel_BW = Channel_BW
        self.b_Canal_AWGN_ff_0.set_BW(self.Channel_BW)

    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW



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
