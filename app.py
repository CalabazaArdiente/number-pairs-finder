import argparse  #Interface argument management

def find_number_pairs(nums, target_sum):
    if not nums:
        raise ValueError("Input list cannot be empty.")

    if target_sum < min(nums):
        raise ValueError("Target sum is not achievable with the given list.")

    complements = {}
    pairs = []

    for num in nums:
        complement = target_sum - num
        if complement in complements:
            pairs.append((num, complement))
        complements[num] = complement
    
    if not pairs:
        raise ValueError("Target sum is not achievable with the given list.")

    return pairs


def main():
    parser = argparse.ArgumentParser(description="Find pairs of integers that sum a given sum value.")
    parser.add_argument("nums", type=str, help="Comma-separated list of integers")
    parser.add_argument("target_sum", type=int, help="Target sum")

    args = parser.parse_args()
    nums = [int(num) for num in args.nums.split(",")]

    try:
        pairs = find_number_pairs(nums, args.target_sum)
        for pair in pairs:
            print("+", pair[0], ",", pair[1])
    except ValueError as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
