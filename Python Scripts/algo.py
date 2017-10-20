
OrigBal = StartBalance
outstandingDebt = agingBal = CurrBal = EndBalance

for row in rows_qryAgingByClient:
    if period != 5:
        if transactino_code!=-4 and Amount < 0:
            outstandingDebt -= Amount
            p += Amount
        
        if outstandingDebt > 0:
            p += outstandingDebt
            break
        
        agingBal -= Amount

        if agingBal > 0:
            p += CurrBal- (p1+p2+p3+p4)
            break