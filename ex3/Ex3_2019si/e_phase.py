import numpy as np
from gnuradio import gr

class blk(gr.sync_block):  
#    """Traduce fases a valores de M_PAM y aplica decisor mediante redondeo"""
    def __init__(self,M=4):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='phase to M_PAM',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.int8]
        )
	self.M=M
	self.p2=2.*np.pi

    def work(self, input_items, output_items):
	mpam_con_ruido=input_items[0]*self.M/self.p2
	mpam_sin_ruido=np.round(mpam_con_ruido)

        output_items[0][:] = mpam_sin_ruido.astype(np.int8)
        return len(output_items[0])
