n = int(input())
for _ in range(n):
    day, month = input().split()
    day = int(day)
    if month == 'Dec':
        astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
    elif month == 'Jan':
        astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
    elif month == 'Feb':
        astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
    elif month == 'Mar':
        astro_sign = 'Pisces' if (day < 21) else 'Aries'
    elif month == 'Apr':
        astro_sign = 'Aries' if (day < 20) else 'Taurus'
    elif month == 'May':
        astro_sign = 'Taurus' if (day < 21) else 'Gemini'
    elif month == 'Jun':
        astro_sign = 'Gemini' if (day < 21) else 'Cancer'
    elif month == 'Jul':
        astro_sign = 'Cancer' if (day < 23) else 'Leo'
    elif month == 'Aug':
        astro_sign = 'Leo' if (day < 23) else 'Virgo'
    elif month == 'Sep':
        astro_sign = 'Virgo' if (day < 23) else 'Libra'
    elif month == 'Oct':
        astro_sign = 'Libra' if (day < 23) else 'Scorpio'
    elif month == 'Nov':
        astro_sign = 'scorpio' if (day < 22) else 'Sagittarius'
    print(astro_sign)