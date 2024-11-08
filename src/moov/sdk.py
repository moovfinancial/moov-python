"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, HttpClient
from .sdkconfiguration import SDKConfiguration
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
import httpx
from moov import models, utils
from moov._hooks import SDKHooks
from moov.access_token import AccessToken
from moov.accounts import Accounts
from moov.analytics import Analytics
from moov.application_sdk import ApplicationSDK
from moov.avatars import Avatars
from moov.bank_accounts import BankAccounts
from moov.branding_sdk import BrandingSDK
from moov.capabilities import Capabilities
from moov.card_issuing import CardIssuing
from moov.cards import Cards
from moov.checkout_sdk import CheckoutSDK
from moov.connections import Connections
from moov.devices import Devices
from moov.disputes import Disputes
from moov.email_password import EmailPassword
from moov.end_to_end_encryption import EndToEndEncryption
from moov.enriched_address import EnrichedAddress
from moov.enriched_profile import EnrichedProfile
from moov.files import Files
from moov.industries_sdk import IndustriesSDK
from moov.institutions import Institutions
from moov.invites import Invites
from moov.issuing_transactions import IssuingTransactions
from moov.moov_internal import MoovInternal
from moov.onboarding import Onboarding
from moov.open_id_connect import OpenIDConnect
from moov.payment_methods import PaymentMethods
from moov.ping import Ping
from moov.representatives import Representatives
from moov.roles import Roles
from moov.schedules import Schedules
from moov.session_sdk import SessionSDK
from moov.signup_sdk import SignupSDK
from moov.sweeps import Sweeps
from moov.transfers import Transfers
from moov.types import OptionalNullable, UNSET
from moov.underwriting_sdk import UnderwritingSDK
from moov.users import Users
from moov.verification_sdk import VerificationSDK
from moov.wallet_transactions import WalletTransactions
from moov.wallets import Wallets
from moov.webhooks import Webhooks
from typing import Any, Callable, Dict, Optional, Union


class Moov(BaseSDK):
    r"""Moov API: Moov is a platform that enables developers to integrate all aspects of money movement with ease and speed. The Moov API makes it simple for platforms to send, receive, and store money. Our API is based upon REST principles, returns JSON responses, and uses standard HTTP response codes. To learn more about how Moov works at a high level, read our [concepts](https://docs.moov.io/guides/get-started/glossary/) guide."""

    signup: SignupSDK
    r"""How to sign a user up via app.moov.io"""
    email_password: EmailPassword
    r"""Authentication via using a email and password."""
    open_id_connect: OpenIDConnect
    r"""Details on Moov's open id connect implementation"""
    verification: VerificationSDK
    access_token: AccessToken
    r"""When making requests to Moov from a browser, you can use OAuth with JSON Web Tokens (JWT).

    Our authentication flow follows the OAuth 2.0 standard. With this endpoint, you'll [create an access token](/api/authentication/access-tokens/) that you will pass along with API requests or when initializing Moov.js. To generate an authentication token, you’ll need to specify [scopes](https://docs.moov.io/guides/developer-tools/scopes/) that enable the token to use a specific set of API endpoints. <br><br> If a scope is required, it will be listed in the description of the endpoint.

    """
    session: SessionSDK
    devices: Devices
    invites: Invites
    accounts: Accounts
    r"""[Accounts](https://docs.moov.io/guides/accounts/) represent a legal entity (either a business or an individual) in Moov. You can create an account for yourself or set up accounts for others, requesting different [capabilities](https://docs.moov.io/guides/accounts/capabilities/) depending on what you need to be able to do with that account. You can retrieve an account to get details on the business or individual account holder, such as an email address or employer identification number (EIN).

    Based on the type of account and its requested capabilities, we have certain [verification requirements](https://docs.moov.io/guides/accounts/identity-verification/). To see what capabilities that account has, you can use the [GET capability endpoint](https://docs.moov.io/api/moov-accounts/capabilities/get/).

    When you sign up for the Moov Dashboard, you will have a **facilitator account** which can be used to facilitate money movement between other accounts. A facilitator account will not show up in your list of accounts and cannot be created via API. To update your facilitator account information, use the settings page of the Moov Dashboard.

    You can disconnect an account within the account's settings in the Moov Dashboard. This action cannot be undone. When an account is disconnected, the account's history and wallet is retained, but transfers cannot be submitted, and no actions can be taken on the account. See the [Dashboard](https://docs.moov.io/guides/dashboard/accounts/#disconnect-accounts) guide for more information. It is not possible to permanently delete an account.

    """
    onboarding: Onboarding
    r"""<b>Coming soon -</b> Invite organizations to onboard with Moov. Create an invitation containing a unique link that allows the recipient to provide data necessary to fulfill capability requirements, agree to pricing, and accept Moov's terms.

    You can create and send an onboarding link directly from the Moov Dashboard. See our [documentation](https://docs.moov.io/guides/accounts/hosted-onboarding/) for details.

    """
    moov_internal: MoovInternal
    representatives: Representatives
    r"""We think of a representative as an individual who can take major actions on behalf of a business. A representative can be the business owner, or anyone who owns 25% or more of the business. Some examples of representatives are the CEO, CFO, COO, or president. We require all business accounts to have valid information for at least one representative. Moov accounts must have verified business representatives before a business account can send funds, collect money from other accounts, or store funds in a wallet. To learn more, read our guide on [business representatives](https://docs.moov.io/guides/accounts/business-representatives/).

    """
    users: Users
    r"""Users are lightweight objects that handle signing in to our app.moov.io

    """
    roles: Roles
    application: ApplicationSDK
    r"""An application allows an account to connect to other accounts and gain access to their information and move money on their behalf.

    """
    connections: Connections
    r"""A connection forms a relationship between two accounts, allowing them to transact with each other. When you create an account for someone else, your account automatically has a connection with the account you've just created."""
    wallets: Wallets
    r"""A [Moov wallet](https://docs.moov.io/guides/wallet/) can serve as a funding source as you accumulate funds. You can also use the Moov wallet to:
    - Pre-fund transfers for faster payouts
    - Transfer funds between Moov wallets for instantly available funds

    <em> If you've requested the `send-funds` or `collect-funds` capability, the `wallet` capability will be automatically requested as well. Read more on the [data requirements for wallets here](https://docs.moov.io/guides/accounts/capabilities/#wallet).</em>

    """
    wallet_transactions: WalletTransactions
    r"""Wallet transactions provide insight into funds that move in and out of an account’s wallet. For each Moov transfer, we create a corresponding transaction that represents how that initial source impacted a wallet. Read more about [wallet transactions](https://docs.moov.io/guides/wallets/transactions).

    """
    sweeps: Sweeps
    transfers: Transfers
    r"""A [transfer](https://docs.moov.io/guides/money-movement/) is the movement of money between Moov accounts, from source to destination. You can initiate a transfer to another Moov account as long as there is a linked and verified payment method.

    With Moov, you can also implement transfer groups, allowing you to associate multiple transfers together and run them sequentially. To learn more, read our guide on [transfer groups](https://docs.moov.io/guides/money-movement/transfer-groups/#transfer-statuses).

    You can simulate various RTP, push to card, ACH, and declined transfer scenarios in test mode. See our [test mode](https://docs.moov.io/guides/get-started/test-mode/#transfers) guide for more information.

    """
    schedules: Schedules
    r"""Set up future transfers through scheduling.

    """
    bank_accounts: BankAccounts
    r"""To transfer money with Moov, you’ll need to link a bank account to your Moov account, then verify that account. You can link a bank account to a Moov account by providing the bank account number, routing number, and Moov account ID.

    We require micro-deposit verification to reduce the risk of fraud or unauthorized activity. You can verify a bank account by initiating [micro-deposits](https://docs.moov.io/guides/sources/bank-accounts/#micro-deposit-verification), sending two small credit transfers to the bank account you want to confirm. Note that there is no way to initiate a micro-deposit from your bank of choice.

    You can simulate bank account payment methods in test mode. See our [test mode](https://docs.moov.io/guides/get-started/test-mode/#bank-accounts) guide for more information.

    Alternatively, you can link and verify a bank account in one step through an instant account verification token from a third party provider like [Plaid](https://docs.moov.io/guides/sources/bank-accounts/verification/plaid/) or [MX](https://docs.moov.io/guides/sources/bank-accounts/verification/mx/). Bank accounts can have the following statuses: `new`, `pending`, `verified`, `verificationFailed`, `errored`. Learn more by reading our guide on [bank accounts](https://docs.moov.io/guides/sources/bank-accounts/).

    """
    cards: Cards
    r"""You can link credit or debit cards to Moov accounts. You can use a card as a source for making transfers, which charges the card. To link a card to a Moov account and avoid some of the burden of PCI compliance, use the [card link Moov Drop](https://docs.moov.io/moovjs/drops/card-link). You cannot add a card via the Dashboard. If you're linking a card via API, you must provide Moov with a copy of your PCI attestation of compliance. When testing cards, use the designated [card numbers for test mode](https://docs.moov.io/guides/set-up-your-account/test-mode/#card-acceptance). You must contact Moov before going live in production with cards. Read our guide on [cards](https://docs.moov.io/guides/sources/cards/) for more information."""
    card_issuing: CardIssuing
    r"""A Moov wallet can serve as a funding source for issuing virtual cards. Note that we currently only issue Visa cards. Virtual cards can then be used to spend funds from the wallet.

    <em> The `card-issuing` and `wallet` capabilities are required to be enabled before any card issuing functionality is available. Moov is in a private beta with select customers for card issuing.</em>

    """
    issuing_transactions: IssuingTransactions
    disputes: Disputes
    r"""A [dispute](https://docs.moov.io/guides/money-movement/cards/disputes/) is a situation where a cardholder formally questions a transaction on their account with their card issuer. This could be for a number of reasons ranging from billing errors to fraudulent activity or dissatisfactory goods/services. If the dispute is recognized as legitimate, the issuer will reverse the payment (otherwise known as a chargeback).

    You can simulate disputes, including winning or losing a dispute, in test mode. See our [test mode](https://docs.moov.io/guides/get-started/test-mode/#disputes) guide for more information.

    """
    files: Files
    r"""Files can be used for a multitude of different use cases including but not limited to, individual identity verification and business underwriting. You may need to provide documentation to enable capabilities or to keep capabilities enabled for an account. The maximum file size is 10MB. Each account is allowed a maximum of 50 files. Acceptable file types include csv, jpg, pdf, and png. To learn about uploading files in the Moov Dashboard, read our [file upload guide](https://docs.moov.io/guides/dashboard/accounts/#file-upload).

    """
    underwriting: UnderwritingSDK
    r"""[Underwriting](https://docs.moov.io/guides/accounts/underwriting) is a tool Moov uses to understand a business’s profile before allowing them to collect funds on our platform. This profile includes information like a description of the company or the merchant’s business model, the industry they operate in, and transaction volume. Through underwriting, we can understand and prevent unnecessary financial risk for Moov and those transacting on our platform. Note that underwriting can be instant, but in some cases make take around 2 business days before approval.

    """
    payment_methods: PaymentMethods
    r"""[Payment methods](https://docs.moov.io/guides/money-movement/payment-methods/) represent all of the ways an account can move funds to another Moov account. Payment methods are generated programmatically when a card or bank account is added or the status is updated e.g., `ach-debit-fund` will be added as a payment method once the bank account is verified.

    <em>RTP® and Push to Card are not yet generally available on Moov. Contact us for more information.</em>

    """
    capabilities: Capabilities
    r"""Capabilities determine what a Moov account can do. Each capability has specific [requirements](https://docs.moov.io/guides/accounts/capabilities/requirements/), depending on risk and compliance standards associated with different account activities. For example, there are more information requirements for a business that wants to charge other accounts than for an individual who simply wants to receive funds.

    When you request a capability, we list the information requirements for that capability. Once you submit the required information, we need to verify the data. Because of this, a requested capability may not immediately become active. Note, if an account requests and is approved for `send-funds` or `collect-funds`, the `wallet` capability is automatically enabled as well. For more detailed information on capabilities and capability IDs, read our [capabilities guide](https://docs.moov.io/guides/accounts/capabilities/).

    """
    industries: IndustriesSDK
    r"""Information about industries and their merchant codes.

    """
    institutions: Institutions
    r"""Lookup ACH and wire participating financial institutions. We recommend using this endpoint when an end-user enters a routing number to confirm their bank or credit union.

    """
    avatars: Avatars
    r"""You can retrieve an account's profile image. This is especially useful if you'd like to use the profile image for a corresponding account in your own product.

    """
    enriched_address: EnrichedAddress
    r"""Search for valid addresses using a partial or full address.

    """
    enriched_profile: EnrichedProfile
    r"""By supplying an email address, you can retrieve a profile with enriched data fields. This service is offered in collaboration with Clearbit.

    """
    webhooks: Webhooks
    ping: Ping
    analytics: Analytics
    r"""You can retrieve helpful at-a-glance information about your account by getting metrics on categories such as new accounts, transfer counts, and transfer volume over different time periods.

    """
    end_to_end_encryption: EndToEndEncryption
    r"""Allows for the passing of secure authentication data through an unverified proxies.

    """
    checkout: CheckoutSDK
    r"""<b>Coming soon -</b> Hosted checkout.

    """
    branding: BrandingSDK

    def __init__(
        self,
        gateway_auth: Optional[
            Union[Optional[str], Callable[[], Optional[str]]]
        ] = None,
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

        :param gateway_auth: The gateway_auth required for authentication
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

        security: Any = None
        if callable(gateway_auth):
            security = lambda: models.Security(gateway_auth=gateway_auth())  # pylint: disable=unnecessary-lambda-assignment
        else:
            security = models.Security(gateway_auth=gateway_auth)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        BaseSDK.__init__(
            self,
            SDKConfiguration(
                client=client,
                async_client=async_client,
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

        self._init_sdks()

    def _init_sdks(self):
        self.signup = SignupSDK(self.sdk_configuration)
        self.email_password = EmailPassword(self.sdk_configuration)
        self.open_id_connect = OpenIDConnect(self.sdk_configuration)
        self.verification = VerificationSDK(self.sdk_configuration)
        self.access_token = AccessToken(self.sdk_configuration)
        self.session = SessionSDK(self.sdk_configuration)
        self.devices = Devices(self.sdk_configuration)
        self.invites = Invites(self.sdk_configuration)
        self.accounts = Accounts(self.sdk_configuration)
        self.onboarding = Onboarding(self.sdk_configuration)
        self.moov_internal = MoovInternal(self.sdk_configuration)
        self.representatives = Representatives(self.sdk_configuration)
        self.users = Users(self.sdk_configuration)
        self.roles = Roles(self.sdk_configuration)
        self.application = ApplicationSDK(self.sdk_configuration)
        self.connections = Connections(self.sdk_configuration)
        self.wallets = Wallets(self.sdk_configuration)
        self.wallet_transactions = WalletTransactions(self.sdk_configuration)
        self.sweeps = Sweeps(self.sdk_configuration)
        self.transfers = Transfers(self.sdk_configuration)
        self.schedules = Schedules(self.sdk_configuration)
        self.bank_accounts = BankAccounts(self.sdk_configuration)
        self.cards = Cards(self.sdk_configuration)
        self.card_issuing = CardIssuing(self.sdk_configuration)
        self.issuing_transactions = IssuingTransactions(self.sdk_configuration)
        self.disputes = Disputes(self.sdk_configuration)
        self.files = Files(self.sdk_configuration)
        self.underwriting = UnderwritingSDK(self.sdk_configuration)
        self.payment_methods = PaymentMethods(self.sdk_configuration)
        self.capabilities = Capabilities(self.sdk_configuration)
        self.industries = IndustriesSDK(self.sdk_configuration)
        self.institutions = Institutions(self.sdk_configuration)
        self.avatars = Avatars(self.sdk_configuration)
        self.enriched_address = EnrichedAddress(self.sdk_configuration)
        self.enriched_profile = EnrichedProfile(self.sdk_configuration)
        self.webhooks = Webhooks(self.sdk_configuration)
        self.ping = Ping(self.sdk_configuration)
        self.analytics = Analytics(self.sdk_configuration)
        self.end_to_end_encryption = EndToEndEncryption(self.sdk_configuration)
        self.checkout = CheckoutSDK(self.sdk_configuration)
        self.branding = BrandingSDK(self.sdk_configuration)
