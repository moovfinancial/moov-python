"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, ClientOwner, HttpClient, close_clients
from .sdkconfiguration import SDKConfiguration
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
import httpx
from moovio_sdk import utils
from moovio_sdk._hooks import SDKHooks
from moovio_sdk.accounts import Accounts
from moovio_sdk.adjustments import Adjustments
from moovio_sdk.apple_pay import ApplePay
from moovio_sdk.authentication import Authentication
from moovio_sdk.avatars import Avatars
from moovio_sdk.bank_accounts import BankAccounts
from moovio_sdk.branding import Branding
from moovio_sdk.capabilities import Capabilities
from moovio_sdk.card_issuing import CardIssuing
from moovio_sdk.cards import Cards
from moovio_sdk.disputes import Disputes
from moovio_sdk.end_to_end_encryption import EndToEndEncryption
from moovio_sdk.enriched_address import EnrichedAddress
from moovio_sdk.enriched_profile import EnrichedProfile
from moovio_sdk.fee_plans import FeePlans
from moovio_sdk.files import Files
from moovio_sdk.industries import Industries
from moovio_sdk.institutions import Institutions
from moovio_sdk.issuing_transactions import IssuingTransactions
from moovio_sdk.models import components, internal
from moovio_sdk.onboarding import Onboarding
from moovio_sdk.payment_links import PaymentLinks
from moovio_sdk.payment_methods import PaymentMethods
from moovio_sdk.ping import Ping
from moovio_sdk.representatives import Representatives
from moovio_sdk.scheduling import Scheduling
from moovio_sdk.sweeps import Sweeps
from moovio_sdk.terminal_applications import TerminalApplications
from moovio_sdk.transfers import Transfers
from moovio_sdk.types import OptionalNullable, UNSET
from moovio_sdk.underwriting import Underwriting
from moovio_sdk.wallet_transactions import WalletTransactions
from moovio_sdk.wallets import Wallets
from typing import Callable, Dict, Optional, Union, cast
import weakref


class Moov(BaseSDK):
    r"""Moov API: Moov is a platform that enables developers to integrate all aspects of money movement with ease and speed.
    The Moov API makes it simple for platforms to send, receive, and store money. Our API is based upon REST
    principles, returns JSON responses, and uses standard HTTP response codes. To learn more about how Moov
    works at a high level, read our [concepts](https://docs.moov.io/guides/get-started/glossary/) guide.
    """

    accounts: Accounts
    adjustments: Adjustments
    apple_pay: ApplePay
    bank_accounts: BankAccounts
    branding: Branding
    capabilities: Capabilities
    cards: Cards
    disputes: Disputes
    fee_plans: FeePlans
    files: Files
    payment_links: PaymentLinks
    payment_methods: PaymentMethods
    representatives: Representatives
    scheduling: Scheduling
    sweeps: Sweeps
    transfers: Transfers
    underwriting: Underwriting
    wallets: Wallets
    wallet_transactions: WalletTransactions
    avatars: Avatars
    end_to_end_encryption: EndToEndEncryption
    enriched_address: EnrichedAddress
    enriched_profile: EnrichedProfile
    industries: Industries
    institutions: Institutions
    issuing_transactions: IssuingTransactions
    card_issuing: CardIssuing
    authentication: Authentication
    onboarding: Onboarding
    ping: Ping
    terminal_applications: TerminalApplications

    def __init__(
        self,
        security: Optional[
            Union[components.Security, Callable[[], components.Security]]
        ] = None,
        x_moov_version: Optional[str] = None,
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param security: The security details required for authentication
        :param x_moov_version: Configures the x_moov_version parameter for all supported operations
        :param server_idx: The index of the server to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        if client is None:
            client = httpx.Client()

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        if async_client is None:
            async_client = httpx.AsyncClient()

        if debug_logger is None:
            debug_logger = get_default_logger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        _globals = internal.Globals(
            x_moov_version=utils.get_global_from_env(
                x_moov_version, "MOOV_X_MOOV_VERSION", str
            ),
        )

        BaseSDK.__init__(
            self,
            SDKConfiguration(
                client=client,
                async_client=async_client,
                globals=_globals,
                security=security,
                server_url=server_url,
                server_idx=server_idx,
                retry_config=retry_config,
                timeout_ms=timeout_ms,
                debug_logger=debug_logger,
            ),
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(
            current_server_url, self.sdk_configuration.client
        )
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        weakref.finalize(
            self,
            close_clients,
            cast(ClientOwner, self.sdk_configuration),
            self.sdk_configuration.client,
            self.sdk_configuration.async_client,
        )

        self._init_sdks()

    def _init_sdks(self):
        self.accounts = Accounts(self.sdk_configuration)
        self.adjustments = Adjustments(self.sdk_configuration)
        self.apple_pay = ApplePay(self.sdk_configuration)
        self.bank_accounts = BankAccounts(self.sdk_configuration)
        self.branding = Branding(self.sdk_configuration)
        self.capabilities = Capabilities(self.sdk_configuration)
        self.cards = Cards(self.sdk_configuration)
        self.disputes = Disputes(self.sdk_configuration)
        self.fee_plans = FeePlans(self.sdk_configuration)
        self.files = Files(self.sdk_configuration)
        self.payment_links = PaymentLinks(self.sdk_configuration)
        self.payment_methods = PaymentMethods(self.sdk_configuration)
        self.representatives = Representatives(self.sdk_configuration)
        self.scheduling = Scheduling(self.sdk_configuration)
        self.sweeps = Sweeps(self.sdk_configuration)
        self.transfers = Transfers(self.sdk_configuration)
        self.underwriting = Underwriting(self.sdk_configuration)
        self.wallets = Wallets(self.sdk_configuration)
        self.wallet_transactions = WalletTransactions(self.sdk_configuration)
        self.avatars = Avatars(self.sdk_configuration)
        self.end_to_end_encryption = EndToEndEncryption(self.sdk_configuration)
        self.enriched_address = EnrichedAddress(self.sdk_configuration)
        self.enriched_profile = EnrichedProfile(self.sdk_configuration)
        self.industries = Industries(self.sdk_configuration)
        self.institutions = Institutions(self.sdk_configuration)
        self.issuing_transactions = IssuingTransactions(self.sdk_configuration)
        self.card_issuing = CardIssuing(self.sdk_configuration)
        self.authentication = Authentication(self.sdk_configuration)
        self.onboarding = Onboarding(self.sdk_configuration)
        self.ping = Ping(self.sdk_configuration)
        self.terminal_applications = TerminalApplications(self.sdk_configuration)

    def __enter__(self):
        return self

    async def __aenter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.sdk_configuration.client is not None:
            self.sdk_configuration.client.close()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.sdk_configuration.async_client is not None:
            await self.sdk_configuration.async_client.aclose()
