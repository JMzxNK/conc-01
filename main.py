import sys


def main(filename):
    i = 0
    with open(filename, 'r') as row:
        i+=1
        for line in row.readlines():
            (OrderId, Status, Paydate, ChannelId, BankCode, BankId, total, MoneyId) = line.replace("\n", "").split(",")
            regu = act_pag(OrderId, Status, Paydate, ChannelId, BankCode, BankId, total, MoneyId)
            print(regu)


def act_pag(OrderId, Status, Paydate, ChannelId, BankCode, BankId, total, MoneyId):

    conc = "UPDATE PagoEfectivo.OrdenPago  \
            SET IdEstado = "+Status+",  \
            FechaCancelacion = '"+Paydate+"',  \
            FechaActualizacion = GETDATE()  \
            WHERE IdOrdenPago = "+OrderId+"; \
            INSERT INTO PagoEfectivo.Movimiento (IdOrdenPago, IdMoneda, IdTipoMovimiento, IdMedioPago, Monto, \
            FechaMovimiento, FechaCreacion, FechaActualizacion,IdAperturaOrigen,IdTipoOrigenCancelacion, \
            CodigoCanal,CodigoBanco,IdBanco) VALUES ( \
            "+OrderId+","+MoneyId+",34,2,"+total+","+Paydate+",GETDATE(),GETDATE(),4,1, \
            "+ChannelId+","+BankCode+","+BankId+");)"
    return conc


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Debe ingresar archivo de datos")
        exit(-1)

    filename = sys.argv[1]
    main(filename)
