from aiohttp import ClientSession
from Python_ARQ import ARQ

aiohttpsession = ClientSession()
ARQ_API_KEY = "YKYUHE-KEWVTL-HHSTVX-AZDKWX-ARQ"
ARQ_API_URL = "https://thearq.tech"
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)
