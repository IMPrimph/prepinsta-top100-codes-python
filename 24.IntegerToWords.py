num = int(input('Enter a number: '))
lev1 = "Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split(
    " ")
lev2 = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split(" ")
lev3 = "Hundred"
lev4 = "Thousand Million Billion".split(" ")

curr = num
res = []
commas = 0
n = None
words = None

while curr:
    n = curr % 1000
    curr = curr // 1000

    words = []

    if(n > 99):
        words.append(lev1[n // 100])
        words.append(lev3)
        n = n % 100

    if n > 19:
        words.append(lev2[n // 10 - 2])
        n = n % 10
    if n > 0:
        words.append(lev1[n])

    if len(words) > 0:
        if commas > 0:
            words.append(lev4[commas - 1])
        res.append(" ".join(words))
    commas += 1

print(" ".join(res[::-1]))
