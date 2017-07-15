import urllib
import urllib2

import cookielib

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
	'stuid':'531227',
	'pwd':'145014'
})

loginUrl = 'http://cjcx.jlu.edu.cn/score/userLogin.php?reason=logout'

result = opener.open(loginUrl,postdata)

cookie.save(ignore_discard=True, ignore_expires=True)

gradeUrl = 'http://cjcx.jlu.edu.cn/score/index.php#f=score.studScoreSearch&p=fix'

result = opener.open(gradeUrl)
print result.read()