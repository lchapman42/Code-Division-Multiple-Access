#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: luke
# GNU Radio version: 3.10.5.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation



from gnuradio import qtgui

class CDM_Test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
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

        self.settings = Qt.QSettings("GNU Radio", "CDM_Test")

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
        self.samp_rate = samp_rate = 1e6
        self.psk8 = psk8 = digital.constellation_8psk().base()
        self.norm_factor = norm_factor = 1/4
        self.key_length = key_length = 8
        self.bpsk = bpsk = digital.constellation_bpsk().base()

        ##################################################
        # Blocks
        ##################################################

        self.digital_constellation_encoder_bc_1_0_0 = digital.constellation_encoder_bc(bpsk)
        self.digital_constellation_encoder_bc_1_0 = digital.constellation_encoder_bc(bpsk)
        self.digital_constellation_encoder_bc_1 = digital.constellation_encoder_bc(bpsk)
        self.digital_constellation_encoder_bc_0_1 = digital.constellation_encoder_bc(psk8)
        self.digital_constellation_encoder_bc_0_0 = digital.constellation_encoder_bc(psk8)
        self.digital_constellation_encoder_bc_0 = digital.constellation_encoder_bc(psk8)
        self.digital_constellation_decoder_cb_0_1 = digital.constellation_decoder_cb(psk8)
        self.digital_constellation_decoder_cb_0_0 = digital.constellation_decoder_cb(psk8)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(psk8)
        self.blocks_vector_source_x_0_0_0 = blocks.vector_source_b((0, 0, 1, 1, 0, 0, 1, 1), True, 1, [])
        self.blocks_vector_source_x_0_0 = blocks.vector_source_b((0, 1, 0, 1, 0, 1, 0, 1), True, 1, [])
        self.blocks_vector_source_x_0 = blocks.vector_source_b((0, 0, 0, 0, 0, 0, 0, 0), True, 1, [])
        self.blocks_unpack_k_bits_bb_0_0_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_unpack_k_bits_bb_0_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_throttle_0_2 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_throttle_0_1 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_throttle_0_0_0_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_throttle_0_0_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_repeat_0_0_0 = blocks.repeat(gr.sizeof_gr_complex*1, key_length)
        self.blocks_repeat_0_0 = blocks.repeat(gr.sizeof_gr_complex*1, key_length)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_gr_complex*1, key_length)
        self.blocks_pack_k_bits_bb_0_0_0_0 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0_0_0 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0_0 = blocks.pack_k_bits_bb(8)
        self.blocks_multiply_xx_0_2 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_cc(norm_factor)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_cc(norm_factor)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(norm_factor)
        self.blocks_integrate_xx_0_1 = blocks.integrate_cc(key_length, 1)
        self.blocks_integrate_xx_0_0 = blocks.integrate_cc(key_length, 1)
        self.blocks_integrate_xx_0 = blocks.integrate_cc(key_length, 1)
        self.blocks_file_source_1_1 = blocks.file_source(gr.sizeof_char*1, '/home/luke/Workspace/GNURadio/Code_Division_Multiplexing/input2.txt', False, 0, 0)
        self.blocks_file_source_1_1.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_1_0 = blocks.file_source(gr.sizeof_char*1, '/home/luke/Workspace/GNURadio/Code_Division_Multiplexing/input3.txt', False, 0, 0)
        self.blocks_file_source_1_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_1 = blocks.file_source(gr.sizeof_char*1, '/home/luke/Workspace/GNURadio/Code_Division_Multiplexing/input.txt', False, 0, 0)
        self.blocks_file_source_1.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_1 = blocks.file_sink(gr.sizeof_char*1, '/home/luke/Workspace/GNURadio/Code_Division_Multiplexing/output3.txt', False)
        self.blocks_file_sink_0_1.set_unbuffered(True)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, '/home/luke/Workspace/GNURadio/Code_Division_Multiplexing/output2.txt', False)
        self.blocks_file_sink_0_0.set_unbuffered(True)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/luke/Workspace/GNURadio/Code_Division_Multiplexing/output.txt', False)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.blocks_add_xx_0 = blocks.add_vcc(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_0_1, 1))
        self.connect((self.blocks_file_source_1, 0), (self.blocks_unpack_k_bits_bb_0_0, 0))
        self.connect((self.blocks_file_source_1_0, 0), (self.blocks_unpack_k_bits_bb_0_0_0, 0))
        self.connect((self.blocks_file_source_1_1, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_integrate_xx_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_integrate_xx_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_integrate_xx_0_1, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.digital_constellation_decoder_cb_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.digital_constellation_decoder_cb_0_1, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_integrate_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.blocks_integrate_xx_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_1, 0), (self.blocks_integrate_xx_0_1, 0))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_2, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_pack_k_bits_bb_0_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0_0_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0_0_0_0, 0), (self.blocks_file_sink_0_1, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.blocks_repeat_0_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_repeat_0_0_0, 0), (self.blocks_multiply_xx_0_2, 0))
        self.connect((self.blocks_throttle_0, 0), (self.digital_constellation_encoder_bc_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.digital_constellation_encoder_bc_1, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.digital_constellation_encoder_bc_1_0, 0))
        self.connect((self.blocks_throttle_0_0_0_0, 0), (self.digital_constellation_encoder_bc_1_0_0, 0))
        self.connect((self.blocks_throttle_0_1, 0), (self.digital_constellation_encoder_bc_0_0, 0))
        self.connect((self.blocks_throttle_0_2, 0), (self.digital_constellation_encoder_bc_0_1, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_throttle_0_1, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0_0_0, 0), (self.blocks_throttle_0_2, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.blocks_throttle_0_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_0_0, 0), (self.blocks_throttle_0_0_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blocks_pack_k_bits_bb_0_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0, 0), (self.blocks_pack_k_bits_bb_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_1, 0), (self.blocks_pack_k_bits_bb_0_0_0_0, 0))
        self.connect((self.digital_constellation_encoder_bc_0, 0), (self.blocks_repeat_0_0, 0))
        self.connect((self.digital_constellation_encoder_bc_0_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.digital_constellation_encoder_bc_0_1, 0), (self.blocks_repeat_0_0_0, 0))
        self.connect((self.digital_constellation_encoder_bc_1, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.digital_constellation_encoder_bc_1, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.digital_constellation_encoder_bc_1_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.digital_constellation_encoder_bc_1_0, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.digital_constellation_encoder_bc_1_0_0, 0), (self.blocks_multiply_xx_0_0_1, 0))
        self.connect((self.digital_constellation_encoder_bc_1_0_0, 0), (self.blocks_multiply_xx_0_2, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "CDM_Test")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_2.set_sample_rate(self.samp_rate)

    def get_psk8(self):
        return self.psk8

    def set_psk8(self, psk8):
        self.psk8 = psk8

    def get_norm_factor(self):
        return self.norm_factor

    def set_norm_factor(self, norm_factor):
        self.norm_factor = norm_factor
        self.blocks_multiply_const_vxx_0.set_k(self.norm_factor)
        self.blocks_multiply_const_vxx_0_0.set_k(self.norm_factor)
        self.blocks_multiply_const_vxx_0_0_0.set_k(self.norm_factor)

    def get_key_length(self):
        return self.key_length

    def set_key_length(self, key_length):
        self.key_length = key_length
        self.blocks_repeat_0.set_interpolation(self.key_length)
        self.blocks_repeat_0_0.set_interpolation(self.key_length)
        self.blocks_repeat_0_0_0.set_interpolation(self.key_length)

    def get_bpsk(self):
        return self.bpsk

    def set_bpsk(self, bpsk):
        self.bpsk = bpsk




def main(top_block_cls=CDM_Test, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
