import json


class BusCompany:

    def __init__(self, data):
        self.raw_data = json.loads(data)
        self.structure = {
            'bus_id': {'type': int, 'required': True},
            'stop_id': {'type': int, 'required': True},
            'stop_name': {'type': str, 'required': True},
            'next_stop': {'type': int, 'required': True},
            'stop_type': {'type': 'char', 'required': False},
            'a_time': {'type': str, 'required': True},
        }
        self.errors = dict.fromkeys(self.structure, 0)

    def count_errors(self):
        for record in self.raw_data:
            for key, value in record.items():
                correct_type = self.structure[key]['type']
                required = self.structure[key]['required']
                if any([value != "" and not self.type_ok(correct_type, value),
                        not self.required_filled(required, value)]):
                    self.errors[key] += 1

    def type_ok(self, correct_type, value):
        if correct_type == 'char':
            is_char = (type(value) is str and len(value) == 1)
            return is_char
        return type(value) is correct_type

    def required_filled(self, required, value):
        return required and value != "" or not required

    def error_report(self):
        print(f'Type and required field validation: {sum(self.errors.values())} errors')
        print(*[f'{key}: {value}' for key, value in self.errors.items()], sep='\n')


easy_rider = BusCompany(input())
easy_rider.count_errors()
easy_rider.error_report()