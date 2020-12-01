def main(summation: int) -> int:
    nums = set()
    with open('data.txt') as f:
        for line in f:
            num = int(line)
            for existing in nums:
                inverse = summation - num - existing
                if inverse in nums:
                    return num * inverse * existing
            nums.add(num)


if __name__ == '__main__':
    print(main(2020))
