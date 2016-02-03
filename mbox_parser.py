import mailbox
import csv

writer = csv.writer(open("clean_mail.csv", "wb"))
writer.writerow(["subject", "from", "to", "date", "body"])
for message in mailbox.mbox('Spam.mbox'):
	writer.writerow([message['subject'], message['from'], message['to'], message['date'], message.get_payload()])
