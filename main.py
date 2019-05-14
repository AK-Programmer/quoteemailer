import getQuote
from emailing import send_quote

final_message = getQuote.grabQuote(getQuote.importData(), getQuote.chooseQuote())
print(final_message)
send_quote(final_message)
