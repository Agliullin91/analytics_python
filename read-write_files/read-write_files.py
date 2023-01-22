import re


def file_to_dict(filename):
    result_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            purchase = line.strip()
            key = purchase.split(',')[0].split(':')[1].strip()
            value = purchase.split(',')[1].split(':')[1].strip()
            result_dict[re.sub(r'"', '', key)] = re.sub(r'"}?', '', value)
    return result_dict


def visit_log(log, purchase_dict):
    result_file = open('funnel.csv', 'w', encoding='utf-8')
    with open(log, 'r') as log_file:
        for line in log_file:
            if purchase_dict.get(line.split(',')[0]) is not None:
                new_line = f"{line.strip()},{purchase_dict.get(line.split(',')[0])}\n"
                result_file.write(new_line)
    result_file.close()


if __name__ == "__main__":
    visit_log('visit_log.csv', file_to_dict('purchase_log.txt'))

