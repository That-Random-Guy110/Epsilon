def parse_int(string):
    numbers = {"ten":10, "eleven":11, "twelve":12, "thirteen":13, 
    "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17,
    "eighteen":18, "nineteen":19, "twenty":20, "thirty":30, "forty":40,
    "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninty":90,
    "one":1, "two":2, "three":3, "four":4,"five":5, "six":6, "seven":7,
    "eight":8, "nine":9, "hundred":100, "thousand":1000, "million":1000000}
    powers = [1000, 1000000]
    new_nums = []
    full_nums = []
    string = string.replace("-", " ").split(" ")
    for i in string:
        new_nums.append(numbers.get(i))
    if len(new_nums) == 1:
        return new_nums[0]
    test = []
    for i in new_nums:
        if i in powers:
            full_nums.append(test)
            full_nums.append(i)
            test = []
        else:
            if i == 100:
                multi = sum(test) * 100
                full_nums.append(multi)
                test = []
            else:
                test.append(i)
    full_nums.append(test)
    print (new_nums)
    print (full_nums)
    full_nums = [sum(x) if isinstance(x, list) else x for x in full_nums]
    if 1000 and 10000 and 100000 and 1000000 not in full_nums:
        return sum(full_nums)
    return full_nums