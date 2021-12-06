
def numberToWords(num):
        if num == 0:
            return 'Zero'
        below20 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split(
            ' ')
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split(' ')
        ks = 'Thousand Million Billion'.split(' ')

        def words(num, idx=1):
            if num == 0:
                return []
            elif num < int(20):
                return [below20[num - 1]]
            elif num < 100:
                return [tens[num // 10 - 2]] + words(num % 10)
            elif num < 1000:
                return [below20[num // 100 - 1], 'Hundred'] + words(num % 100)
            elif num < 1000000: #thousands
                return words(num//1000)+[ks[0]]+words(num%1000)
            elif num < 1000000000: #millions
                return words(num//1000000)+[ks[1]]+words(num%1000000)     
            else: #billions
                return words(num//1000000000)+[ks[2]]+words(num%1000000000)

        return ' '.join(words(num, 0))

s = int(input("Enter the number:"))
Number = numberToWords(s)
print(Number) 