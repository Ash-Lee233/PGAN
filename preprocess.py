
""" preprocess """
import os
import argparse
import numpy as np

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="default name", add_help=False)

    parser.add_argument("--pre_result_path", type=str, default="",
                        help="out file path")
    parser.add_argument("--nimages", type=int, default="",
                        help="number of images")
    args_opt, _ = parser.parse_known_args()
    # initialize noise
    fixed_noise = np.random.randn(args_opt.nimages, 512).astype(np.float32)
    file_name = "wgan_bs" + str(args_opt.nimages) + ".bin"
    file_path = os.path.join(args_opt.pre_result_path, file_name)
    alpha = np.array(0.0).astype(np.float32)
    fixed_noise.tofile(file_path)
    file_path = os.path.join(args_opt.pre_result_path, "alpha.bin")
    alpha.tofile(file_path)
    print("*" * 20, "export bin files finished", "*" * 20)
