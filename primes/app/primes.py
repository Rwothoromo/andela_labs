class Primes(object):
    def is_prime(self, number):
        i = 1
        count = 0

        if number == 1 or number == 0:
            return False

        while i <= number:
            if number%i == 0:
                count += 1

                if count > 2:
                    return False
            i += 1

        if count == 2:
            return True
        return False

    def primes(self, number_limit):
        prime_list = []

        if not isinstance(number_limit, int):
            raise TypeError("Value must be integer.")

        if number_limit < 0:
            raise ValueError("Value must be positive.")

        for i in range(number_limit+1):
            if self.is_prime(i):
                prime_list.append(i)

        return prime_list
