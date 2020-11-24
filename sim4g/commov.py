from math import sqrt
import argparse

def count_hex(area, radius, reuse):
    
    tri_area = radius*(radius*sqrt(3)/2)/2
    hex_area = 6*tri_area
    total_hex = area/hex_area
    total_clusters = total_hex//reuse

    return total_hex, total_clusters

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