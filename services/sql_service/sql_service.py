import allure


class SQLService:

    def __init__(self, connection):
        self.cursor = connection.cursor()

    @allure.step("Get firstname from DB")
    def get_first_name(self, email):
        query = f"SELECT Firstname FROM lc_customers WHERE Email='{email}'"
        return self.execute_query(query)[0][0]

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
