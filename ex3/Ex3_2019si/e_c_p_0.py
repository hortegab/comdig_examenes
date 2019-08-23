import numpy as np
from gnuradio import gr

class blk(gr.sync_block):  
    """Autor: Homero Ortega. Permite obtener la fase de una senal compleja. A diferencia de otros bloques de gnuradio, este entrega valores positivos de fase entre 0 y 2pi. M es el numero de posibles fases discretas que trae la senal"""
    def __init__(self,M=4):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='Complex to Phase',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.float32]
        )
	self.M=M
	self.p2=2.*np.pi
	self.p_margen=self.p2/(M*2.)

    def work(self, input_items, output_items):
	fases=np.angle(input_items[0]) # tiene valores negativos
	fases=(fases+self.p_margen +self.p2)% self.p2-self.p_margen
        output_items[0][:] = fases
        return len(output_items[0])
