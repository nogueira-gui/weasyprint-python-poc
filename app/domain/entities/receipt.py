class Receipt:
    def __init__(self, amount: float, date: str, payment_method: str):
        self.amount = amount
        self.date = date
        self.payment_method = payment_method

    def validate_amount(self):
        if not isinstance(self.amount, float) or self.amount <= 0:
            raise ValueError("Amount must be a positive float value")

    def validate_date(self):
        #valide o formato da data e se está correto dd/mm/yyyy
        if not isinstance(self.date, str) or len(self.date) != 10:
            raise ValueError("Date must be a string in the format dd/mm/yyyy")

    def validate_payment_method(self):
        if not isinstance(self.payment_method, str) or len(self.payment_method) == 0:
            raise ValueError("payment method must be a non-empty string")

    def validate(self):
        self.validate_amount()
        self.validate_date()
        self.validate_payment_method()