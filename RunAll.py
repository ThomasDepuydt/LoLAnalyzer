# All script can be called from here

import multiprocessing

import ConfigUpdater
import DataDownloader
import DataExtractor
import Networks
import RoleUpdater
import DataProcessing
import DataShuffling
import Learner
import BestPicks
import Modes


# Running options
cpu = min(multiprocessing.cpu_count() - 1, 1)  # The number of cpu the scripts will use.
shuffling_files = 37  # prime number to maximize spreading. Take a prime higher to the number of data files (e.g. If you have 32 data files, take 37)
restore = False  # leave this to False, or your model will overfit the data (it will recognize the game and not learn why the game is won/loss)

# Mode and Network
# Look at Modes.py and Networks.py to see the list of available modes/networks
# Feel free to build/tune your own networks
# BUT, keep in mind that more complex networks require more data and take more time to train.
mode = Modes.ABOTJMCS_Mode()
network = Networks.DenseUniform(mode=mode, n_hidden_layers=3, NN=256, dropout=0.2, batch_size=1000, report=10)

# Scripts to execute, comment useless ones
# In particular, if you just want to run the app, comment all but 'BestPicks'
to_execute = [
    # 'ConfigUpdater',
    # 'DataDownloader',  # run on multiple cpu
    'DataExtractor',
    'RoleUpdater',
    'DataProcessing',  # run on multiple cpu
    'DataShuffling',
    'Learner',  # run on gpu
    'BestPicks',
]


if __name__ == '__main__':
    if 'ConfigUpdater' in to_execute:
        ConfigUpdater.run()
    if 'DataDownloader' in to_execute:
        DataDownloader.run(mode)
    if 'DataExtractor' in to_execute:
        DataExtractor.run(mode)
    if 'RoleUpdater' in to_execute:
        RoleUpdater.run(mode)
    if 'DataProcessing' in to_execute:
        DataProcessing.run(mode, cpu)
    if 'DataShuffling' in to_execute:
        DataShuffling.run(mode, shuffling_files)
    if 'Learner' in to_execute:
        Learner.run(mode, network, restore)
    if 'BestPicks' in to_execute:
        BestPicks.run(mode, network)