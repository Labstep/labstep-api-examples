import labstep
import schedule
import time
import smtplib
from prettytable import PrettyTable, ALL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

## Login to Labstep Workspace
user = labstep.authenticate('YOUR_USER_NAME','YOUR_API_KEY')
workspace = user.getWorkspace(13934)

def getNewOrderRequests():
  ## Get the latest order requests
  return workspace.getOrderRequests(status='new')

def getOrderRow(order):
  name = order.resource['name']
  resource = user.getResource(order.resource['id'])
  metadata = resource.getMetadata()
  account_number = "MY_ACCOUNT_NUMBER"
  vat_status = 'No'
  try:
    code = list(filter(lambda x: x.label =='Product Code',metadata))[0].value
  except:
    code = '?'
    print('Product Code not found for ',name)

  try:
    supplier = list(filter(lambda x: x.label == 'Supplier',metadata))[0].value
  except:
    supplier = '?'
    print('Supplier not found for ',name)
        
  return [name, code, supplier, account_number,vat_status]

def sendOrderEmail(new_orders):
  ## Authenticate imperial email
  MY_ADDRESS = 'MY_EMAIL_ADDRESS'
  MY_PASSWORD = 'MY_PASSWORD'
  SEND_TO = 'PROCURMENT_EMAIL_ADDRESS'

  s = smtplib.SMTP(host='smtp.office365.com', port=587)
  s.ehlo()
  s.starttls()
  s.login(MY_ADDRESS, MY_PASSWORD)
  ## Construct Email
  msg = MIMEMultipart()       
  msg['From']=MY_ADDRESS
  msg['To']=SEND_TO
  msg['Subject']="Order Request"
  template = Template('''
  <p>Dear XXXXX,</p>
  <p>Can you please order the following items from the accounts specified:</p>
  ${TABLE}
  <p>
  Thanks,
  <p>
  <p>XXXXXXX</p>
  ''')
  x = PrettyTable()
  x.border = True
  x.hrules = ALL
  x.vrules = ALL
  x.field_names = ["Name", "Code", "Supplier", "Account No.", 'VAT Free?']
  for order in new_orders:
    row = getOrderRow(order)
    x.add_row(row)
  table = x.get_html_string(format=True)
  body = template.substitute(TABLE=table)
  msg.attach(MIMEText(body, 'html'))
  ## Send message
  s.send_message(msg)
  print('Email Sent')
  s.quit()

def checkAndSend():
  new_orders = getNewOrderRequests()
  sendOrderEmail(new_orders)


schedule.every().day.at("10:30").do(checkAndSend)

while True:
  schedule.run_pending()
  time.sleep(60)
