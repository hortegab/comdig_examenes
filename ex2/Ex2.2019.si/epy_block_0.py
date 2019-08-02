"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
from eyediagram.demo_data import demo_data
from eyediagram.mpl import eyediagram
import matplotlib.pyplot as plt









class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, example_param=1.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Embedded Python Block',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.example_param = example_param

    def work(self, input_items, output_items):
        """example: multiply with constant"""

	#Generamos senal de ejemplo  
	num_symbols = 1000
	samples_per_symbol = 24
	y = demo_data(num_symbols, samples_per_symbol)

	#Llamamos el modulo que instalamos
	eyediagram(y, 2*samples_per_symbol, offset=16, cmap=plt.cm.coolwarm)

	#Graficamos
	#plt.plot(y)
	plt.show()

        output_items[0][:] = input_items[0] * self.example_param
        return len(output_items[0])
