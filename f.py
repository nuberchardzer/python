def get_summ(one, two, delimiter='&'):
    gf = f'{one}{delimiter}{two}'
    return gf

print(get_summ('hnydymjgmjd', ',oril,ku,dy,y,')) # Learn&python
print(get_summ('Learn', 'python', delimiter='!!!'))
print(get_summ(123, 456)) # 123&456