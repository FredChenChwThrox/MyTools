import argparse
import pprint


def _strip_extra_line_of_file(input_file, output_file):
    with open(input_file, 'rb') as in_f:
        with open(output_file, 'wb') as out_f:
            last_is_empty = False
            while True:
                line = in_f.readline()

                if not line:
                    break

                striped_line = line.rstrip(b'\n')

                if striped_line:
                    out_f.write(striped_line + b'\n')
                    last_is_empty = False
                else:
                    if not last_is_empty:
                        last_is_empty = True
                    else:
                        out_f.write(b'\n')
                        last_is_empty = False


def _handle_cmd_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=str
                       , dest='in_file_path'
                       , help='Please help to specify a input file to process')
    parser.add_argument('-o', type=str
                       , dest='out_file_path'
                       , help='Please help to specify an output file to process')

    args = parser.parse_args()

    return args


def main():
    args = _handle_cmd_args()
    if args.in_file_path and args.out_file_path:
        _strip_extra_line_of_file(args.in_file_path, args.out_file_path)
    else:
        pprint.pprint("paraments is invalid")


if __name__ == '__main__':
    main()
