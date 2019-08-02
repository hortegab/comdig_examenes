#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Aug  2 04:42:25 2019
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
from b_Canal_AWGN_ff import b_Canal_AWGN_ff  # grc-generated hier_block
from b_Eye_Diagram_simple import b_Eye_Diagram_simple  # grc-generated hier_block
from b_PSD import b_PSD  # grc-generated hier_block
from b_binary_bipolar_source_f import b_binary_bipolar_source_f  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import eyediagram
import math
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
        self.h = h = (1,1,1,1,1,1)
        self.Sps = Sps = len(h)
        self.Rb = Rb = 12000
        self.samp_rate_data = samp_rate_data = Rb*Sps
        self.run_stop = run_stop = True
        self.W = W = Rb/2
        self.BWdata = BWdata = samp_rate_data/2
        self.Ab = Ab = 1.

        ##################################################
        # Blocks
        ##################################################
        self.menu = Qt.QTabWidget()
        self.menu_widget_0 = Qt.QWidget()
        self.menu_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_0)
        self.menu_grid_layout_0 = Qt.QGridLayout()
        self.menu_layout_0.addLayout(self.menu_grid_layout_0)
        self.menu.addTab(self.menu_widget_0, 'P3 a)')
        self.menu_widget_1 = Qt.QWidget()
        self.menu_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_1)
        self.menu_grid_layout_1 = Qt.QGridLayout()
        self.menu_layout_1.addLayout(self.menu_grid_layout_1)
        self.menu.addTab(self.menu_widget_1, 'P3 b)')
        self.menu_widget_2 = Qt.QWidget()
        self.menu_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_2)
        self.menu_grid_layout_2 = Qt.QGridLayout()
        self.menu_layout_2.addLayout(self.menu_grid_layout_2)
        self.menu.addTab(self.menu_widget_2, 'P3 c)')
        self.top_grid_layout.addWidget(self.menu, 2, 0, 1, 2)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
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
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_VERT,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")

        labels = ['Ancho de Banda', '', '', '', '',
                  '', '', '', '', '']
        units = ['kHz', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, 0)
            self.qtgui_number_sink_0.set_max(i, samp_rate_data/1000)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_1.addWidget(self._qtgui_number_sink_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.menu_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_1.setColumnStretch(c, 1)
        self.interp_fir_filter_xxx_0_0 = filter.interp_fir_filter_fff(1, (h))
        self.interp_fir_filter_xxx_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(Sps, (h))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((1./Sps, ))
        self.b_binary_bipolar_source_f_0 = b_binary_bipolar_source_f(
            Am=1.,
            Spb=1,
        )
        self.b_PSD_0_0_0 = b_PSD(
            Ensayos=1000000,
            N=1024,
            Titulo='espectro R3',
            Ymax=3e-7,
            samp_rate_audio=samp_rate_data,
        )
        self.menu_grid_layout_2.addWidget(self.b_PSD_0_0_0, 1, 0, 1, 1)
        for r in range(1, 2):
            self.menu_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_2.setColumnStretch(c, 1)
        self.b_Eye_Diagram_simple_0 = b_Eye_Diagram_simple(
            AlphaLineas=0.5,
            Delay_i=4,
            GrosorLineas=20,
            N_eyes=2,
            Samprate=samp_rate_data,
            Sps=Sps,
            Title="Eye Diagramm",
            Ymax=2,
            Ymin=-2,
        )
        self.menu_grid_layout_0.addWidget(self.b_Eye_Diagram_simple_0, 0, 0, 1, 1)
        for r in range(0, 1):
            self.menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_0.setColumnStretch(c, 1)
        self.b_Canal_AWGN_ff_0 = b_Canal_AWGN_ff(
            BW=samp_rate_data/2,
            Ch_NodB=-45,
            Ch_Toffset=0,
            samp_rate=samp_rate_data,
        )
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, BWdata/1000)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.b_Canal_AWGN_ff_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.b_binary_bipolar_source_f_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.b_PSD_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.interp_fir_filter_xxx_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.b_Canal_AWGN_ff_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.b_Eye_Diagram_simple_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.blocks_null_sink_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_h(self):
        return self.h

    def set_h(self, h):
        self.h = h
        self.set_Sps(len(self.h))
        self.interp_fir_filter_xxx_0_0.set_taps((self.h))
        self.interp_fir_filter_xxx_0.set_taps((self.h))

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_samp_rate_data(self.Rb*self.Sps)
        self.blocks_multiply_const_vxx_0.set_k((1./self.Sps, ))
        self.b_Eye_Diagram_simple_0.set_Sps(self.Sps)

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.set_samp_rate_data(self.Rb*self.Sps)
        self.set_W(self.Rb/2)

    def get_samp_rate_data(self):
        return self.samp_rate_data

    def set_samp_rate_data(self, samp_rate_data):
        self.samp_rate_data = samp_rate_data
        self.set_BWdata(self.samp_rate_data/2)
        self.b_PSD_0_0_0.set_samp_rate_audio(self.samp_rate_data)
        self.b_Eye_Diagram_simple_0.set_Samprate(self.samp_rate_data)
        self.b_Canal_AWGN_ff_0.set_BW(self.samp_rate_data/2)
        self.b_Canal_AWGN_ff_0.set_samp_rate(self.samp_rate_data)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_W(self):
        return self.W

    def set_W(self, W):
        self.W = W

    def get_BWdata(self):
        return self.BWdata

    def set_BWdata(self, BWdata):
        self.BWdata = BWdata
        self.analog_const_source_x_0.set_offset(self.BWdata/1000)

    def get_Ab(self):
        return self.Ab

    def set_Ab(self, Ab):
        self.Ab = Ab


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
