import win32com.client
#message.Delete()
str_body=""
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)
BlYo = inbox.Folders.Item("BlueYonder")

messages = inbox.Items
alerts = BlYo.Items

message = messages.GetLast()
alert=alerts.GetLast()

str_body=message.body
str_alert=alert.Body

str_alert=str.replace(str_alert,'Usuario: ','')
str_alert=str.replace(str_alert,'   Saludos ','')
str_alert=str.replace(str_alert,'La Orden  ', '{"orden":')
str_alert=str.replace(str_alert,' tiene un error en la secuencia: ',', "secuencia":')
str_alert=str.replace(str_alert,'" - "','","linea":"')
str_alert=str.replace(str_alert,'Event failed to be logged -- 9945: ',',"mensaje":"' )

if( 'Sequence' in str_alert ):
    str_alert= str.replace(str_alert,').',')."}')
else : str_alert= str.replace(str_alert,'_id','_id"}')

while str_alert[len(str_alert)-1] != '}':
    str_alert=str_alert[:-1]

print('ALERT: \n'+ str_alert )

tmp01="123456"
print(tmp01[:-1])
print(tmp01[len(tmp01)-1])

while tmp01[len(tmp01)-1] != '3':
    tmp01=tmp01[:-1]

print('ALERT: \n'+ str_alert )

