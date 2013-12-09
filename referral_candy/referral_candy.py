import hashlib
import requests
import time

_DEFAULT_API_URL = 'https://my.referralcandy.com/api/v1/'
_API_METHODS = {
    'get' : ['verify', 'referrals', 'referrer', 'contacts'],
    'post': ['purchase', 'referral', 'signup', 'invite']
}

class ReferralCandy:
    def __init__(self, access_id, secret_key):
        self.access_id = access_id
        self.secret_key = secret_key

    def _add_signature_to(self, params):
        params.update({'accessID': self.access_id, 'timestamp': int(time.time())})
        params.update({'signature': self._signature(params)})
        return params

    def _signature(self, params):
        collected_params = ''.join(('%s=%s' % (k,v)) for k, v in sorted(params.iteritems()))
        return hashlib.md5(self.secret_key + collected_params).hexdigest()

def define_endpoint_fn(verb, ep):
    def endpoint_fn(self, params=None):
        if params is None:
            params = {}
        http_method_fn = getattr(requests, verb)
        return http_method_fn("%s%s.json" % (_DEFAULT_API_URL, ep),
                               params=self._add_signature_to(params))
    setattr(ReferralCandy, ep, endpoint_fn)

for verb, endpoints in _API_METHODS.iteritems():
    for ep in endpoints:
        define_endpoint_fn(verb, ep)
