def pow(r,n):
    if n==1:
        return r
    else:
        return r * pow(r,n-1)
print(pow(2,5))