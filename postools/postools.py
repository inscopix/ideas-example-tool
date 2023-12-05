import isx
import matplotlib.pyplot as plt
import numpy as np


def plot_trace_status(cell_set_file: list[str]) -> None:
    """simple dummy function that plots the mean and
    standard deviation of every trace in a cellset file"""

    out_file_name = "fig.png"

    cellset = isx.CellSet.read(cell_set_file[0])

    trace_means = []
    trace_stds = []
    for i in range(cellset.num_cells):
        trace = cellset.get_cell_trace_data(i)
        trace_means.append(np.nanmean(trace))
        trace_stds.append(np.nanstd(trace))

    fig, ax = plt.subplots(figsize=(5, 5))
    plt.scatter(trace_means, trace_stds)
    fig.savefig(out_file_name, dpi=300)


def dummy_func():
    """this function does nothing"""
    pass
