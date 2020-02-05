import sys


def reg(filename):
    i = 0
    with open('./cips.txt', 'r') as row:
        i+=1
        regu =[]
        for line in row.readlines():
            (OrderId, Status, Paydate, ChannelId, BankCode, BankId, total, MoneyId) = line.replace("\n", "").split(",")
            regu.append(
                {'OrderId': OrderId,
                 'Status': Status,
                 'Paydate': Paydate,
                 'ChannelId': ChannelId,
                 'BankCode': BankCode,
                 'BankId': BankId,
                 'total': total,
                 'MoneyId': MoneyId
                 }
            )
    return regu


