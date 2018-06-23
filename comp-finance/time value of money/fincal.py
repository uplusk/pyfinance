
def pvPerpetuity(c,rate):
    return c/rate

def pvPerpetuity_growth(c,rate,g):
    return c/(rate-g)

def pvPerpetuityDue(c,rate):
    return (c/rate)*(1+rate)

def pvPerpetuityDue_growth(c,rate):
    return (c/rate-g)*(1+rate-g)

def pvAnnuity(fv,n,rate,when=0):
    return fv/rate*(1-1/(1+rate)**n)*(1+ rate*when)

def pvAnnuity_growth(fv,n,rate,g,when=0):
    return fv/(rate-g)*(1-(1+g)**n/(1+rate)**n)*(1+ rate*when)

def fvAnnuity(pv,n,rate,when=0):
    return pv/rate*((1+rate)**n-1)*(1+ rate*when)

def fvAnnuity_growth(pv,n,rate,g,when=0):
    return pv/(rate-g)*((1+rate)**n-(1+g)**n)*(1+ rate*when)

