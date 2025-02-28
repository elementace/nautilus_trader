# -------------------------------------------------------------------------------------------------
#  Copyright (C) 2015-2024 Nautech Systems Pty Ltd. All rights reserved.
#  https://nautechsystems.io
#
#  Licensed under the GNU Lesser General Public License Version 3.0 (the "License");
#  You may not use this file except in compliance with the License.
#  You may obtain a copy of the License at https://www.gnu.org/licenses/lgpl-3.0.en.html
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# -------------------------------------------------------------------------------------------------

from nautilus_trader.adapters.polymarket.common.constants import POLYMARKET_VENUE
from nautilus_trader.config import LiveDataClientConfig
from nautilus_trader.config import LiveExecClientConfig
from nautilus_trader.config import PositiveFloat
from nautilus_trader.config import PositiveInt
from nautilus_trader.model.identifiers import Venue


class PolymarketDataClientConfig(LiveDataClientConfig, frozen=True):
    """
    Configuration for ``PolymarketDataClient`` instances.

    Parameters
    ----------
    venue : Venue, default POLYMARKET_VENUE
        The venue for the client.
    private_key : str, optional
        The Polymarket private key.
        If ``None`` then will source the `POLYMARKET_PK` environment variable.
    signature_type : int, default 0 (EOA)
        The Polymarket signature type.
    funder : str, optional
        The Polymarket USDC wallet address.
        If ``None`` then will source the `POLYMARKET_FUNDER` environment variable.
    api_key : str, optional
        The Polymarket API public key.
        If ``None`` then will source the `POLYMARKET_API_KEY` environment variable.
    api_secret : str, optional
        The Polymarket API public key.
        If ``None`` then will source the `POLYMARKET_API_SECRET` environment variable.
    api_passphrase : str, optional
        The Polymarket API pass phrase.
        If ``None`` then will source the `POLYMARKET_API_PASSPHRASE` environment variable.
    base_url_http : str, optional
        The HTTP client custom endpoint override.
    base_url_ws : str, optional
        The WebSocket client custom endpoint override.
    ws_connection_delay_secs : PositiveInt, default 5
        The delay (seconds) prior to main websocket connection to allow initial subscriptions to arrive.
    update_instruments_interval_mins : PositiveInt, default 60
        The interval (minutes) between updating Polymarket instruments.

    """

    venue: Venue = POLYMARKET_VENUE
    private_key: str | None = None
    signature_type: int = 0
    funder: str | None = None
    api_key: str | None = None
    api_secret: str | None = None
    api_passphrase: str | None = None
    base_url_http: str | None = None
    base_url_ws: str | None = None
    ws_connection_delay_secs: PositiveInt = 5
    update_instrument_interval_mins: PositiveInt = 60


class PolymarketExecClientConfig(LiveExecClientConfig, frozen=True):
    """
    Configuration for ``PolymarketExecutionClient`` instances.

    Parameters
    ----------
    venue : Venue, default POLYMARKET_VENUE
        The venue for the client.
    private_key : str, optional
        The Polymarket private key.
        If ``None`` then will source the `POLYMARKET_PK` environment variable.
    signature_type : int, default 0 (EOA)
        The Polymarket signature type.
    funder : str, optional
        The Polymarket USDC wallet address.
        If ``None`` then will source the `POLYMARKET_FUNDER` environment variable.
    api_key : str, optional
        The Polymarket API public key.
        If ``None`` then will source the `POLYMARKET_API_KEY` environment variable.
    api_secret : str, optional
        The Polymarket API public key.
        If ``None`` then will source the `POLYMARKET_API_SECRET` environment variables.
    api_passphrase : str, optional
        The Polymarket API pass phrase.
        If ``None`` then will source the `POLYMARKET_API_PASSPHRASE` environment variable.
    base_url_http : str, optional
        The HTTP client custom endpoint override.
    base_url_ws : str, optional
        The WebSocket client custom endpoint override.
    max_retries : PositiveInt, optional
        The maximum number of times a submit or cancel order request will be retried.
    retry_delay : PositiveFloat, optional
        The delay (seconds) between retries.

    """

    venue: Venue = POLYMARKET_VENUE
    private_key: str | None = None
    signature_type: int = 0
    funder: str | None = None
    api_key: str | None = None
    api_secret: str | None = None
    api_passphrase: str | None = None
    base_url_http: str | None = None
    base_url_ws: str | None = None
    max_retries: PositiveInt | None = None
    retry_delay: PositiveFloat | None = None
