#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Lab Total
# Generated: Wed Mar 20 08:37:15 2019
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
from b_PSD_VRMS_c import b_PSD_VRMS_c  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import numpy
import sip
import wform  # embedded python module
from gnuradio import qtgui


class Lab_total(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Lab Total")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Lab Total")
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

        self.settings = Qt.QSettings("GNU Radio", "Lab_total")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 6250000
        self.rolloff = rolloff = 0.35
        self.ntaps = ntaps = 64
        self.const = const = (digital.constellation_bpsk(), digital.constellation_qpsk(), digital.constellation_8psk(), digital.qam.qam_constellation(16))
        self.Sps = Sps = 4
        self.Const_ID = Const_ID = 3
        self.run_stop = run_stop = True
        self.hrc = hrc = wform.rcos(Sps,ntaps,rolloff)
        self.Rs = Rs = samp_rate/Sps
        self.Rb = Rb = samp_rate
        self.M = M = len(const[Const_ID].points())
        self.Fc = Fc = 80000000

        ##################################################
        # Blocks
        ##################################################
        self.pestana = Qt.QTabWidget()
        self.pestana_widget_0 = Qt.QWidget()
        self.pestana_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_0)
        self.pestana_grid_layout_0 = Qt.QGridLayout()
        self.pestana_layout_0.addLayout(self.pestana_grid_layout_0)
        self.pestana.addTab(self.pestana_widget_0, 'Datos')
        self.top_grid_layout.addWidget(self.pestana)
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
        self.qtgui_time_sink_x_0_0_0_0_0_1 = qtgui.time_sink_f(
        	ntaps, #size
        	samp_rate, #samp_rate
        	"Punto 4. Salida del Bloque Raiz Coseno. Parte Imaginaria", #name
        	5 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0_0_1.set_y_axis(-3.5, 3.5)

        self.qtgui_time_sink_x_0_0_0_0_0_1.set_y_label('RC Filter Poly', "")

        self.qtgui_time_sink_x_0_0_0_0_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0_0_1.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_0_0_0_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0_0_0_1.disable_legend()

        labels = ['simbolo1', 'simbolo2', 'simbolo3', 'simbolo4', 'Suma',
                  '', '', '', '', '']
        widths = [3, 3, 3, 3, 5,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, 0, 0, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(5):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_0_1.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_0_0_0_0_1_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.pestana_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.pestana_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_0_0_0 = qtgui.time_sink_f(
        	ntaps, #size
        	samp_rate, #samp_rate
        	"Punto 4. Salida del Bloque Raiz Coseno. Parte Real", #name
        	5 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0_0.set_y_axis(-3.5, 3.5)

        self.qtgui_time_sink_x_0_0_0_0_0.set_y_label('RC Filter Poly', "")

        self.qtgui_time_sink_x_0_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0_0_0.disable_legend()

        labels = ['simbolo1', 'simbolo2', 'simbolo3', 'simbolo4', 'Suma',
                  '', '', '', '', '']
        widths = [3, 3, 3, 3, 5,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, 0, 0, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(5):
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
        self.pestana_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_0_0_0_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.pestana_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.pestana_grid_layout_0.setColumnStretch(c, 1)
        self.interp_fir_filter_xxx_0_0_0_0 = filter.interp_fir_filter_ccc(Sps, (hrc))
        self.interp_fir_filter_xxx_0_0_0_0.declare_sample_delay(0)
        self.digital_chunks_to_symbols_xx = digital.chunks_to_symbols_bc((const[Const_ID].points()), 1)
        self.blocks_vector_source_x_0_1_1 = blocks.vector_source_f(1*hrc, True, 1, [])
        self.blocks_vector_source_x_0_1_0_1 = blocks.vector_source_f(1*hrc, True, 1, [])
        self.blocks_vector_source_x_0_1_0_0_1 = blocks.vector_source_f(-3*hrc, True, 1, [])
        self.blocks_vector_source_x_0_1_0_0_0_0 = blocks.vector_source_f(-1*hrc, True, 1, [])
        self.blocks_vector_source_x_0_1_0_0_0 = blocks.vector_source_f(-1*hrc, True, 1, [])
        self.blocks_vector_source_x_0_1_0_0 = blocks.vector_source_f(-3*hrc, True, 1, [])
        self.blocks_vector_source_x_0_1_0 = blocks.vector_source_f(1*hrc, True, 1, [])
        self.blocks_vector_source_x_0_1 = blocks.vector_source_f(1*hrc, True, 1, [])
        self.blocks_throttle_0_0_0_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_0_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_delay_0_0_1 = blocks.delay(gr.sizeof_float*1, 0)
        self.blocks_delay_0_0_0_1 = blocks.delay(gr.sizeof_float*1, Sps)
        self.blocks_delay_0_0_0_0_1 = blocks.delay(gr.sizeof_float*1, Sps*2)
        self.blocks_delay_0_0_0_0_0_0 = blocks.delay(gr.sizeof_float*1, Sps*3)
        self.blocks_delay_0_0_0_0_0 = blocks.delay(gr.sizeof_float*1, Sps*3)
        self.blocks_delay_0_0_0_0 = blocks.delay(gr.sizeof_float*1, Sps*2)
        self.blocks_delay_0_0_0 = blocks.delay(gr.sizeof_float*1, Sps)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, 0)
        self.blocks_add_xx_0_0 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.b_PSD_VRMS_c_0 = b_PSD_VRMS_c(
            Ensayos=1000000,
            Fc=Fc,
            N=1024,
            Titulo="Punto 3. La PSD",
            samp_rate_audio=samp_rate,
        )
        self.pestana_grid_layout_0.addWidget(self.b_PSD_VRMS_c_0, 0, 0, 1, 1)
        for r in range(0, 1):
            self.pestana_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.pestana_grid_layout_0.setColumnStretch(c, 1)
        self.analog_random_source_x = blocks.vector_source_b(map(int, numpy.random.randint(0, M, 10000000)), True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x, 0), (self.digital_chunks_to_symbols_xx, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 4))
        self.connect((self.blocks_add_xx_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0_1, 4))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_throttle_0_0_0_0, 0))
        self.connect((self.blocks_delay_0_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_delay_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 1))
        self.connect((self.blocks_delay_0_0_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_delay_0_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 2))
        self.connect((self.blocks_delay_0_0_0_0_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_delay_0_0_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 3))
        self.connect((self.blocks_delay_0_0_0_0_0_0, 0), (self.blocks_add_xx_0_0, 3))
        self.connect((self.blocks_delay_0_0_0_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0_1, 3))
        self.connect((self.blocks_delay_0_0_0_0_1, 0), (self.blocks_add_xx_0_0, 2))
        self.connect((self.blocks_delay_0_0_0_0_1, 0), (self.qtgui_time_sink_x_0_0_0_0_0_1, 2))
        self.connect((self.blocks_delay_0_0_0_1, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.blocks_delay_0_0_0_1, 0), (self.qtgui_time_sink_x_0_0_0_0_0_1, 1))
        self.connect((self.blocks_delay_0_0_1, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.blocks_delay_0_0_1, 0), (self.blocks_throttle_0_0_0_0_0, 0))
        self.connect((self.blocks_throttle_0_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 0))
        self.connect((self.blocks_throttle_0_0_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0_1, 0))
        self.connect((self.blocks_vector_source_x_0_1, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_1_0, 0), (self.blocks_delay_0_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_1_0_0, 0), (self.blocks_delay_0_0_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_1_0_0_0, 0), (self.blocks_delay_0_0_0_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_1_0_0_0_0, 0), (self.blocks_delay_0_0_0_0_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_1_0_0_1, 0), (self.blocks_delay_0_0_0_0_1, 0))
        self.connect((self.blocks_vector_source_x_0_1_0_1, 0), (self.blocks_delay_0_0_0_1, 0))
        self.connect((self.blocks_vector_source_x_0_1_1, 0), (self.blocks_delay_0_0_1, 0))
        self.connect((self.digital_chunks_to_symbols_xx, 0), (self.interp_fir_filter_xxx_0_0_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0_0_0, 0), (self.b_PSD_VRMS_c_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Lab_total")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0_0_0_0_0_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0_0_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0_0_0_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_0_0.set_sample_rate(self.samp_rate)
        self.b_PSD_VRMS_c_0.set_samp_rate_audio(self.samp_rate)
        self.set_Rs(self.samp_rate/self.Sps)
        self.set_Rb(self.samp_rate)

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff
        self.set_hrc(wform.rcos(self.Sps,self.ntaps,self.rolloff))

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_hrc(wform.rcos(self.Sps,self.ntaps,self.rolloff))

    def get_const(self):
        return self.const

    def set_const(self, const):
        self.const = const
        self.set_M(len(self.const[self.Const_ID].points()))
        self.digital_chunks_to_symbols_xx.set_symbol_table((self.const[self.Const_ID].points()))

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_hrc(wform.rcos(self.Sps,self.ntaps,self.rolloff))
        self.blocks_delay_0_0_0_1.set_dly(self.Sps)
        self.blocks_delay_0_0_0_0_1.set_dly(self.Sps*2)
        self.blocks_delay_0_0_0_0_0_0.set_dly(self.Sps*3)
        self.blocks_delay_0_0_0_0_0.set_dly(self.Sps*3)
        self.blocks_delay_0_0_0_0.set_dly(self.Sps*2)
        self.blocks_delay_0_0_0.set_dly(self.Sps)
        self.set_Rs(self.samp_rate/self.Sps)

    def get_Const_ID(self):
        return self.Const_ID

    def set_Const_ID(self, Const_ID):
        self.Const_ID = Const_ID
        self.set_M(len(self.const[self.Const_ID].points()))
        self.digital_chunks_to_symbols_xx.set_symbol_table((self.const[self.Const_ID].points()))

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        self._run_stop_callback(self.run_stop)
        if self.run_stop: self.start()
        else: self.stop(); self.wait()

    def get_hrc(self):
        return self.hrc

    def set_hrc(self, hrc):
        self.hrc = hrc
        self.interp_fir_filter_xxx_0_0_0_0.set_taps((self.hrc))
        self.blocks_vector_source_x_0_1_1.set_data(1*self.hrc, [])
        self.blocks_vector_source_x_0_1_0_1.set_data(1*self.hrc, [])
        self.blocks_vector_source_x_0_1_0_0_1.set_data(-3*self.hrc, [])
        self.blocks_vector_source_x_0_1_0_0_0_0.set_data(-1*self.hrc, [])
        self.blocks_vector_source_x_0_1_0_0_0.set_data(-1*self.hrc, [])
        self.blocks_vector_source_x_0_1_0_0.set_data(-3*self.hrc, [])
        self.blocks_vector_source_x_0_1_0.set_data(1*self.hrc, [])
        self.blocks_vector_source_x_0_1.set_data(1*self.hrc, [])

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc
        self.b_PSD_VRMS_c_0.set_Fc(self.Fc)


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
