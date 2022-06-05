cc_list = """Ezra Koening <ekoeni@vpwk.com>, Rostam Batmanglij <rostam@vpwk.com>, Chris Tomnson <ctomson@vpwk.com>, Bobbi Baio <bbaio@vpwk.com"""

import re

obj = re.search(r"rostam", cc_list)
print(obj)

# 또는
obj = re.search(r"[RB]obb[i,y]", cc_list)
print(obj)

# 캐릭터세트
obj = re.search(r"[a-z]+", cc_list)
print(obj)

# 6자리
obj = re.search(r"[A-Za-z]{6}", cc_list)
print(obj)

# 와일드카드
obj = re.search(r"[RB]ob.[i,y]", cc_list)
print(obj)

# 주소프린트
obj = re.search(r"[A-Za-z]+@[a-z]+\.[a-z]+", cc_list)
print(obj)

# 캐릭터 클래스
matched = re.search(r"\w+@\w+\.\w+", cc_list)
print(matched)

# 그룹
matched = re.search(r"(\w+)@(\w+)\.(\w+)", cc_list)
print(matched)
print(matched.group(0))
print(matched.group(1))
print(matched.group(2))
print(matched.group(3))

# 네임드그룹
matched = re.search(r"(?P<name>\w+)@(?P<SLD>\w+)\.(?P<TLD>\w+)", cc_list)
print(
    f'Name : {matched.group("name")}\nSecondary Level Domain : {matched.group("SLD")}\nTop Level Domain : {matched.group("TLD")}'
)

# 찾기 반복자
matched = re.finditer(r"(?P<name>\w+)@(?P<SLD>\w+)\.(?P<TLD>\w+)", cc_list)
for m in matched:
    print(m.groupdict())

# 치환
user = re.sub(
    r"(?P<name>\w+)@(?P<SLD>\w+)\.(?P<TLD>\w+)", "\g<TLD>.\g<SLD>.\g<name>", cc_list
)
print(user)

# 컴파일링
regex = re.compile(r"(\w+)@(\w+)\.(\w+)")
print(regex.findall(cc_list))
