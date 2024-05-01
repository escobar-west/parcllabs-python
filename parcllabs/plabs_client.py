import json
import requests
from typing import Dict
from requests.exceptions import RequestException

from parcllabs import api_base

from parcllabs.services.investor_metrics import (
    InvestorMetricsHousingStockOwnership,
    InvesetorMetricsNewListingsForSaleRollingCounts,
    InvestorMetricsPurchaseToSaleRatio,
    InvestorMetricsHousingEventCounts,
)

from parcllabs.services.market_metrics import (
    MarketMetricsHousingEventPrices,
    MarketMetricsHousingStock,
    MarketMetricsHousingEventCounts,
)

from parcllabs.services.for_sale_market_metrics import (
    ForSaleMarketMetricsNewListingsRollingCounts,
)

from parcllabs.services.rental_market_metrics import (
    RentalMarketMetricsRentalUnitsConcentration,
    RentalMarketMetricsGrossYield,
)

from parcllabs.services.portfolio_metrics import PortfolioMetricsSFHousingStockOwnership
from parcllabs.services.search import SearchMarkets

class ParclLabsClient:
    def __init__(self, api_key: str):
        if api_key is None:
            raise ValueError("api_key is required")
        self.api_key = api_key
        self.api_url = api_base

        # top-level services: The client is responsible for creating instances of these services
        self.investor_metrics_housing_stock_ownership = (
            InvestorMetricsHousingStockOwnership(client=self)
        )
        self.investor_metrics_new_listings_for_sale_rolling_counts = (
            InvesetorMetricsNewListingsForSaleRollingCounts(client=self)
        )
        self.investor_metrics_purchase_to_sale_ratio = (
            InvestorMetricsPurchaseToSaleRatio(client=self)
        )
        self.investor_metrics_housing_event_counts = InvestorMetricsHousingEventCounts(
            client=self
        )
        self.market_metrics_housing_event_prices = MarketMetricsHousingEventPrices(
            client=self
        )
        self.market_metrics_housing_stock = MarketMetricsHousingStock(client=self)
        self.market_metrics_housing_event_counts = MarketMetricsHousingEventCounts(
            client=self
        )
        self.for_sale_market_metrics_new_listings_rolling_counts = (
            ForSaleMarketMetricsNewListingsRollingCounts(client=self)
        )
        self.rental_market_metrics_rental_units_concentration = (
            RentalMarketMetricsRentalUnitsConcentration(client=self)
        )
        self.rental_market_metrics_gross_yield = RentalMarketMetricsGrossYield(
            client=self
        )
        self.portfolio_metrics_sf_housing_stock_ownership = (
            PortfolioMetricsSFHousingStockOwnership(client=self)
        )
        self.search_markets = SearchMarkets(client=self)

    def get(self, url: str, params: dict = None):
        """
        Send a GET request to the specified URL with the given parameters.

        Args:
            url (str): The URL endpoint to request.
            params (dict, optional): The parameters to send in the query string.

        Returns:
            dict: The JSON response as a dictionary.
        """
        try:
            full_url = self.api_url + url
            headers = self._get_headers()
            response = requests.get(full_url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            try:
                error_details = response.json()
                error_message = error_details.get('detail', 'No detail provided by API')
            except json.JSONDecodeError:
                error_message = 'Failed to decode JSON error response'
            raise RequestException(f"{response.status_code} Error: {error_message}")
        except requests.exceptions.RequestException as err:
            raise RequestException(f"Request failed: {str(err)}")
        except Exception as e:
            raise RequestException(f"An unexpected error occurred: {str(e)}")

    def _get_headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"{self.api_key}",
            "Content-Type": "application/json",
        }
