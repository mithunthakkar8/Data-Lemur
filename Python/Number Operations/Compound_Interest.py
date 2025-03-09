import math
def compound_interest(principal, rate, contribution, years):
    final_amount = principal
    for _ in range(years):
      final_amount += final_amount * rate/100
      final_amount += contribution
    
    final_amount = round(final_amount,2)
    
    return final_amount
