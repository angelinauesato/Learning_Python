from codigo.bytebank import Employee
import pytest
from pytest import mark
# pytest --markers

class TestClass:
    # Given-When_Then or AAA (Arrange-Act-Assert)
    def test_when_age_is_13_09_2000_returns_22(self):
        input_data = '13/09/2000'
        output_data = 22

        employee_test = Employee('Test', input_data, 1111)

        # When: action
        result = employee_test.age()

        # Then: result
        assert result == output_data

    def test_when_full_name_Lucas_Vallares_returns_Vallares(self):
        input_data = ' Lucas Vallares '
        output_data = 'Vallares'

        employee = Employee(input_data, '11/11/2000', 1111)

        result = employee.last_name()

        assert result == output_data

    # @mark.skip
    def test_when_decrease_salary_directors_100000_returns_90000(self):
        input_data = 100000
        name = 'Pedro Higa'
        output_data = 90000

        employee = Employee(name, '11/11/2000', input_data)
        employee.decrease_salary()
        result = employee.salary

        assert result == output_data

    @mark.calc_bonus
    def test_when_calc_bonus_salary_1000_return_100(self):
        input_data = 1000
        output_data = 100

        employee = Employee('test', '11/11/2000', input_data)
        result = employee.calc_bonus()

        assert result == output_data

    @mark.calc_bonus
    def test_when_calc_bonus_salary_1000000_return_exception(self):
        with pytest.raises(Exception):
            input_data = 1000000

            employee = Employee('test', '11/11/2000', input_data)
            result = employee.calc_bonus()

            assert result

    def test_when_returns_str(self):
        input_data_name, dob, salary = 'Test', '13/03/2000', 1000
        output_data = 'Employee(Test, 13/03/2000, 1000)'

        employee = Employee(input_data_name, dob, salary)
        result = employee.__str__()

        assert result == output_data