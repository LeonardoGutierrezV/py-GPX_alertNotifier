import win32com.client

str_body=""
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)
messages = inbox.Items
message = messages.GetLast()

str_body=message.body
print(message.SenderName )
print(message.subject)
str_body= str.replace( str.replace(str_body,'Usuario: ',''), '   ','')
print(str_body)