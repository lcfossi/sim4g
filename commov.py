from math import sqrt, log10, pow
from matplotlib import pyplot as plt

import argparse

def count_hex(area, radius, reuse):
    
    tri_area = radius*(radius*sqrt(3)/2)/2
    hex_area = 6*tri_area
    total_hex = area/hex_area
    total_clusters = total_hex//reuse

    return total_hex, total_clusters

def link_budget(pot_tx, pot_rx, snr, Md, Gt, Pt):
    Lmax = pot_tx - pot_rx + Gt - Pt - snr - Md
    return Lmax

def max_radius(max_loss, freq, hb, hm):
    x = 44.9 - 6.55*hb
    a = (1.11*log10(freq) - 0.7)*hm - 1.56*log10(freq) - 0.8
    log_R_max = (max_loss - 69.55 - 26.16*log10(freq) + 13.82*log10(hb) + a)/x
    R_max = pow(10, log_R_max)
    
    return R_max

def max_throughput(bw, bpsimb):
    t_simb = 0.00001
    subcarries = bw*60
    throughput = t_simb*subcarries*bpsimb

    return throughput

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Input arguments")
    parser.add_argument('--bandwidth', '-b', 
                        type=float,
                        help="Channel bandwidth to work on. It must be 1.4, 3, 5, 10, 15 or 20 [MHz]. Default = 20",
                        default=20)
    parser.add_argument('--reuse', '-r',
                        type=int,
                        help="Valid frequency reuse factor. Default = 7",
                        default=7)
    
    inputs = parser.parse_args()