from parshuffle import *

if __name__ == '__main__':

    args = params.parse_args()
    shuffle_file(args.input_file, args.output_file)
