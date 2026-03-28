import unittest
import sys
import types

import auto_scheduler

fake_curl_cffi = types.ModuleType("curl_cffi")
fake_curl_cffi.requests = types.SimpleNamespace()
sys.modules.setdefault("curl_cffi", fake_curl_cffi)

import ncs_register


class ProxyNormalizationTests(unittest.TestCase):
    def test_ncs_register_default_proxy_is_disabled(self):
        self.assertEqual(ncs_register._normalize_proxy_value(""), "")
        self.assertEqual(ncs_register._normalize_proxy_value("填入您自己的代理地址"), "")
        self.assertEqual(ncs_register._normalize_proxy_value("direct"), "")

    def test_auto_scheduler_placeholder_proxy_is_disabled(self):
        self.assertEqual(auto_scheduler._normalize_proxy_value(""), "")
        self.assertEqual(auto_scheduler._normalize_proxy_value("填写你的代理"), "")
        self.assertEqual(auto_scheduler._normalize_proxy_value("http://127.0.0.1:7890"), "http://127.0.0.1:7890")


if __name__ == "__main__":
    unittest.main()
