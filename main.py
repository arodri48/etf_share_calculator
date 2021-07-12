from collections import defaultdict


def runner(total_amt: float, etf_val_filepath: str):
    # Step 1: Read in rows into dictionary
    etf_dict = defaultdict(list)
    with open(etf_val_filepath, 'r') as f:
        for line in f:
            line_split = line.rstrip('\n').split('\t')
            etf_dict[line_split[0]].append(float(line_split[1]))
            etf_dict[line_split[0]].append(float(line_split[2]))

    # Step 2: Carry out math to display results
    for key, val in etf_dict.items():
        num_shares = total_amt * val[1] / val[0]
        print(f"Shares of {key}: {num_shares:.2f}")


if __name__ == "__main__":
    runner(4018, 'etf_vals.txt')
