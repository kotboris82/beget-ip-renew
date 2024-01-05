import requests
import json

login = 'username'
password = 'api-password'

def change_domain_ip(domain):
    response = requests.get('https://api.myip.com')
    new_ip = json.loads(response.text)['ip']

    records = {
        'A': [
            {
                'priority': 10,
                'value': new_ip
            }
        ]
    }
    input_data = {
        'fqdn': domain,
        'records': records
    }

    params = {
        'login': login,
        'passwd': password,
        'input_format': 'json',
        'output_format': 'json',
        'input_data': json.dumps(input_data)
    }

    response = requests.get('https://api.beget.com/api/dns/changeRecords', params=params)

    if response.status_code == 200:
        result = json.loads(response.text)
        if result['status'] == 'success':
            print(f"IP адрес домена {domain} успешно изменен на {new_ip}")
        else:
            print(f"Ошибка при изменении IP адреса домена {domain}: {result['error_text']}")
    else:
        print(f"Ошибка при отправке запроса к API BeGet для домена {domain}: {response.status_code}")

domains = ['site.dev', '*.site.dev', 'www.site.dev'] // Массив доменов, которым обновляем A-записи

for domain in domains:
    change_domain_ip(domain)
