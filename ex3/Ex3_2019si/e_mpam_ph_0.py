import numpy as np
from gnuradio import gr

class blk(gr.sync_block):  
#    """Traduce M_PAM a valores de fase"""
    def __init__(self,M=4):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='M_PAM to Phase',   # will show up in GRC
            in_sig=[np.int8],
            out_sig=[np.float32]
        )
	self.M=M
	self.p2=2.*np.pi

    def work(self, input_items, output_items):
	#fases=input_items[0]*self.p2/self.M

        output_items[0][:] = input_items[0]*self.p2/self.M
        return len(output_items[0])
