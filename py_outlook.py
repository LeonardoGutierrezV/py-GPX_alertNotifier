import win32com.client

str_body=""
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)
messages = inbox.Items
message = messages.GetLast()

str_body=message.body
str_body=str.replace(str_body,'Usuario: ','')
str_body=str.replace(str_body,'   Saludos ','')
str_body=str.replace(str_body,'La Orden  ', '"orden":')
str_body=str.replace(str_body,' tiene un error en la secuencia: ',', "secuencia":')
str_body=str.replace(str_body,'" - "','","linea":"')
str_body=str.replace(str_body,'Event failed to be logged -- 9945: ',',"mensaje":"' )

if( 'Sequence' in str_body ):
    str_body= str.replace(str_body,').',')."}')
else : str_body= str.replace(str_body,'_id','_id"}')
print('R01: \n'+ str_body)

tmp01="123456"
print(tmp01[:-1])
print(tmp01[len(tmp01)-1])

#if tmp01[len(tmp01)-1] != '5':  tmp01=tmp01[:-1]

while tmp01[len(tmp01)-1] != '3':
    tmp01=tmp01[:-1]

print(tmp01)

#print("str_body"[: len("str_body")-1 ])
#print( str_body[:len(str_body)-1])
'''
while str_body[:len(str_body)-1] != '}':
    str_body[:len(str_body)-1]
    print( str_body)
'''
#print('R02: \n'+ str_body)