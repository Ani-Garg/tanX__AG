import unittest
import pandas as pd

class TestOrders(unittest.TestCase):

    def setUp(self):
      
        self.df = pd.DataFrame({
            'order_id': [1, 2, 3, 4, 5],
            'customer_id': [101, 102, 103, 101, 104],
            'order_date': pd.to_datetime(['2023-01-01', '2023-01-15', '2023-02-01', '2023-02-15', '2023-03-01']),
            'product_id': [201, 202, 203, 201, 204],
            'product_name': ['Product A', 'Product B', 'Product C', 'Product A', 'Product D'],
            'product_price': [10.0, 20.0, 30.0, 10.0, 40.0],
            'quantity': [1, 2, 3, 4, 5]
        })

    def test_monthly_revenue(self):
        result = compute_monthly_revenue(self.df)
        expected = pd.Series([30.0, 100.0, 200.0], index=pd.PeriodIndex(['2023-01', '2023-02', '2023-03'], freq='M'))
        pd.testing.assert_series_equal(result, expected)

    def test_product_revenue(self):
        result = compute_product_revenue(self.df)
        expected = pd.Series([50.0, 40.0, 90.0, 200.0], index=['Product A', 'Product B', 'Product C', 'Product D'])
        pd.testing.assert_series_equal(result, expected)

    def test_customer_revenue(self):
        result = compute_customer_revenue(self.df)
        expected = pd.Series([50.0, 40.0, 90.0, 200.0], index=[101, 102, 103, 104])
        pd.testing.assert_series_equal(result, expected)

    def test_top_10_customers(self):
        result = identify_top_10_customers(self.df)
        expected = pd.Series([200.0, 90.0, 50.0, 40.0], index=[104, 103, 101, 102])
        pd.testing.assert_series_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
