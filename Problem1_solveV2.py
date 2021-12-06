
def numberToWords( num):
        if num == 0:
            return 'Zero'
        below19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split(
            ' ')
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split(' ')
        ks = 'Thousand Million Billion'.split(' ')

        def words(num, idx=1):
            if num == 0:
                return []
            elif num < int(20):
                return [below19[num - 1]]
            elif num < 100:
                return [tens[num // 10 - 2]] + words(num % 10)
            elif num < 1000:
                return [below19[num // 100 - 1], 'Hundred'] + words(num % 100)
            else:
                m, r = divmod(num, 1000)
                space = [] if m % 1000 == 0 else [ks[idx]]
                return words(m, idx + 1) + space + words(r, idx)

        return ' '.join(words(num, 0))

s = int(input("Enter the number:"))
Number = numberToWords(s)
print(Number) 