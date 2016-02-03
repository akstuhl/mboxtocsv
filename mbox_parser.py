import mailbox
import csv

writer = csv.writer(open("clean_mail.csv", "wb"))
writer.writerow(["subject", "from", "to", "date", "body"])
for message in mailbox.mbox('Spam.mbox'):
	payload = message.get_payload()
	if message.is_multipart():
		payload = message.get_payload(0).get_payload()
	writer.writerow([message['subject'], message['from'], message['to'], message['date'], payload])
