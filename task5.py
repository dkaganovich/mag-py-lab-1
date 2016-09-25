# -*- coding: UTF-8 -*-


def main():
    nums = ("no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten")
    format_str0 = "%s green %s hanging on the wall,"
    format_str1 = "%s one green bottle should accidentally fall,"
    format_str2 = "There’ll be %s green %s hanging on the wall."
    for i in xrange(10, 0, -1):
        for _ in xrange(2):
            print format_str0 % (nums[i].capitalize(), "bottles" if i > 1 else "bottle")
        print format_str1 % ("And if" if i > 1 else "If that")
        print format_str2 % (nums[i - 1], "bottles" if i != 2 else "bottle")


if __name__ == "__main__":
    main()
