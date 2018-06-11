import testlink
import os
print(os.environ['TESTLINK_API_PYTHON_SERVER_URL'])
print(os.environ['TESTLINK_API_PYTHON_DEVKEY'])
tls = testlink.TestLinkHelper().connect(testlink.TestlinkAPIClient)
tls.countProjects()
print(tls.getTestCase(None, testcaseexternalid='dpp-1'))
