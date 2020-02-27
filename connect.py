import pyodbc
import sqlalchemy as sl
import pandas as pd


# def read(conn):
#     print("Read")
#     cursor = conn.cursor()
#     cursor.execute('select idordenpago from BDPagoEfectivoReplicaCore.PagoEfectivo.OrdenPago where IdOrdenPago in (23423182)')
#
#
# connection = pyodbc.connect("Driver = {ODBC Driver 17 for SQL Server};"
#                             "Server = nat04.orbis.pe,3401;"
#                             "username = usr_cgomez;"
#                             "password = cgomez2015;"
#                             "Trusted_Connection = yes;")
#

engine = sl.create_engine('mssql+pyodbc://usr_cgomez:cgomez2015@nat04.orbis.pe:3401/BDPagoEfectivoReplicaCore?'
                          'driver=FreeTDS?Trusted_Connection=yes')
# conn = engine.connect()
#
# result = engine.execute('select idOrdenpago,idServicio,Total,FechaCancelacion'
#                         ' from PagoEfectivo.OrdenPago where IdOrdenPago in (23423182)')
# for row in result:
#     print(row)
#
# result.close()


sq = pd.read_sql_query('select idOrdenpago,idServicio,Total,FechaCancelacion '
                       'from PagoEfectivo.OrdenPago where IdOrdenPago in (23423182)', engine)
df = pd.DataFrame(sq, columns=['idOrdenpago', 'idServicio', 'Total', 'FechaCancelacion'])
print(df)

# cnn = pyodbc.connect('DRIVER=FreeTDS;SERVER=nat04.orbis.pe;PORT=3401;DATABASE=BDPagoEfectivoReplicaCore;
# UID=usr_cgomez;PWD=cgomez2015')
# cursor = cnn.cursor()
# for row in cursor.execute("select idOrdenpago,idServicio,Total,FechaCancelacion from
# BDPagoEfectivoReplicaCore.PagoEfectivo.OrdenPago where IdOrdenPago in (23423182)"):
#    print(row)
