class InputValidator:
    MIN_AREA = 1000
    MAX_AREA = 10000
    MIN_BEDROOMS = 1
    MAX_BEDROOMS = 6
    MIN_AGE = 1
    MAX_AGE = 100

    def get_input(self, value_name):
        min_value = self.__getattribute__('MIN_' + value_name)
        max_value = self.__getattribute__('MAX_' + value_name)

        input_value = 0
        while input_value < min_value or input_value > max_value:
            input_text = "Please enter {0} of home ({1}-{2}): "
            input_value = input(input_text.format(value_name.lower(), min_value, max_value))
            try:
                input_value = int(input_value)
            except ValueError:
                input_value = 0

        return input_value
