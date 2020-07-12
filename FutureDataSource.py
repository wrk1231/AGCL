## Source: Tushare
## Basic functionality: construct consecutive future series https://mp.weixin.qq.com/s?__biz=MzI3Mjk5OTU1Ng==&mid=2247483896&idx=1&sn=3463f7da0cb219f10fa460337c41f952&scene=21#wechat_redirect
from datetime import datetime
from datetime import timedelta
import os
import tushare as ts
token = "517e5497cb2ced266feb20bd478a808d5b135e6c6367e899ac6b433f"
ts.set_token(token=token)