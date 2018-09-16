from imapclient import IMAPClient
import pyzmail
server = IMAPClient('imap.gmail.com', use_uid=True)
server.login('17it142@sict.udn.vn', 'nguyenbaominhhoang')
print('Login successed!')
#server.list_folders()
select_info = server.select_folder('INBOX', readonly=True)
#print('There are %d message in your inbox' % select_info[b'EXISTS'])
UIDs = server.search(['SINCE', '15-Sep-2018'])
print(UIDs)
rawMessages = server.fetch(UIDs, ['BODY[]'])
#message = pyzmail.PyzMessage.factory(rawMessages[1074])
print(message.get_subject())
server.logout()
"""
messages = server.search(['FROM', 'Webmaster@manutd.com'])
for msgid, data in server.fetch(messages, ['ENVELOPE']).items():
	envelope = data[b'ENVELOPE']
	print('ID #%d: "%s" received %s' % (msgid, envelope.subject.decode(), envelope.date))
"""