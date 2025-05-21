from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

"""
    The Class preparing_dataset.py.
    The preparing_dataset.py class is responsible for preparing the dataset for analysis.
    @Author Bruno Tanabe
    @CreatedAt 2025-04-23
"""


class PreparingDataset:

    def __init__(self):
        try:
            self.df_churn = (
                pd.read_csv(str(BASE_DIR) + "/data/churn_customers.csv")
                .merge(
                    pd.read_csv(str(BASE_DIR) + "/data/churn_services.csv"), on="customerID"
                )
                .merge(
                    pd.read_csv(str(BASE_DIR) + "/data/churn_contracts.csv"),
                    on="customerID",
                )
            )

            self.df_churn["TotalCharges"] = pd.to_numeric(
                self.df_churn["TotalCharges"], errors="coerce"
            )

            self.df_churn.columns = [
                "customer_id",
                "gender",
                "senior_citizen",
                "partner",
                "dependents",
                "phone_service",
                "multiple_lines",
                "internet_service",
                "online_security",
                "online_backup",
                "device_protection",
                "tech_support",
                "streaming_tv",
                "streaming_movies",
                "tenure",
                "contract",
                "paperless_billing",
                "payment_method",
                "monthly_charges",
                "total_charges",
                "churn",
            ]

        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except pd.errors.EmptyDataError as e:
            print(f"Empty data error: {e}")
        except pd.errors.ParserError as e:
            print(f"Parser error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

            
            
