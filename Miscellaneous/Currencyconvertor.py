'''
We will take the amount and currencies from the user.
Send the request to API and convert and show result.
'''
import requests
def req(cur_from, cur_to):
    host_url = "https://free.currconv.com"
    key = "ef0c42a1aba699dfbdbf"
    parameters =  f"/api/v7/convert?q={cur_from.upper()}_{cur_to.upper()}&compact=ultra&apiKey="
    url = host_url+parameters+key
    answer = requests.get(url)
    return answer.json()


def convert():
    amount = int(input("Enter Amount "))
    currency = input("Currency from ")
    currency_to = input("Currency to ")
    conv = req(currency,currency_to)
    key = list(conv.keys())
    final_ans = amount*conv[key[0]]
    print(" {} from {} to {} is {:.2f} ".format(amount, currency, currency_to, final_ans))

convert()

