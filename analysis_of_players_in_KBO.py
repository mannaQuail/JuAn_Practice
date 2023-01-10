from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
name_list = ['김현준','구자욱','강민호','김상수','피렐라','김헌곤','김지찬','오재일','강한울','이원석','오선진','김태군','김재성','이재현'] #분석할 선수들의 이름

#dictionary와 변수들의 초기값 설정
data_list = {}
data_sum_list = {}
result = {}

driver = webdriver.Chrome('Users/LeeJuAn/chromedriver')
for name in name_list:
	count = 0

	#KBO 홈페이지 들어가기
	driver.get(url = "https://www.koreabaseball.com/Default.aspx")
	time.sleep(3)
	driver.find_element('xpath','//*[@id="lnb"]/li[4]/a').click()
	time.sleep(2)
	driver.find_element('xpath','//*[@id="cphContents_cphContents_cphContents_txtSearchPlayerName"]').send_keys(f'{name}')
	time.sleep(2)
	driver.find_element('xpath','//*[@id="cphContents_cphContents_cphContents_btnSearch"]').click()
	time.sleep(2)

	#동명이인 필터링
	html1 = driver.page_source
	soup1 = BeautifulSoup(html1, 'html.parser')

	for filter_person in soup1.find('table', class_="tEx").find('tbody').find_all('tr'):
		team_name = filter_person.find_all('td')
		team_name_check = team_name[2].get_text()
		if team_name_check=='삼성':
			break
		count+=1

	if count==0:
		driver.find_element('xpath','//*[@id="cphContents_cphContents_cphContents_udpRecord"]/div[2]/table/tbody/tr/td[2]/a').click()
	elif count==1:
		driver.find_element('xpath','//*[@id="cphContents_cphContents_cphContents_udpRecord"]/div[2]/table/tbody/tr[2]/td[2]/a').click()
	elif count==2:
		driver.find_element('xpath','//*[@id="cphContents_cphContents_cphContents_udpRecord"]/div[2]/table/tbody/tr[3]/td[2]/a').click()

	time.sleep(2)
	driver.find_element('xpath','//*[@id="contents"]/div[2]/div[1]/div[3]/ul/li[3]').click()
	time.sleep(2)
	driver.find_element('xpath','//*[@id="cphContents_cphContents_cphContents_ddlSeries"]').click()
	time.sleep(2)
	driver.find_element('xpath','//*[@id="cphContents_cphContents_cphContents_ddlSeries"]/option[1]').click()
	time.sleep(2)

	html = driver.page_source
	soup = BeautifulSoup(html, 'html.parser')

	#sum변수들의 초기화
	PA_sum = 0
	AB_sum = 0
	R_sum = 0
	H_sum = 0
	_2B_sum = 0
	_3B_sum = 0
	HR_sum = 0
	RBI_sum = 0
	SB_sum = 0
	CS_sum = 0
	BB_sum = 0
	HBP_sum = 0
	SO_sum = 0
	GDP_sum = 0

	# print(f'<{name} 선수 경기 일정>')
	data_list[name] = []
	for tb_class in soup.find_all('div', class_="tbl-type02 tbl-type02-pd0"):
		game = tb_class.find('tbody').find_all('tr')
		for line_1 in game:
			line = line_1.find_all('td')
			date= line[0].get_text()
			VS = line[1].get_text()
			AVG = line[2].get_text()
			PA = line[3].get_text()
			AB = line[4].get_text()
			R = line[5].get_text()
			H = line[6].get_text()
			_2B = line[7].get_text()
			_3B = line[8].get_text()
			HR = line[9].get_text()
			RBI = line[10].get_text()
			SB = line[11].get_text()
			CS = line[12].get_text()
			BB = line[13].get_text()
			HBP = line[14].get_text()
			SO = line[15].get_text()
			GDP = line[16].get_text()

			data_list[name].append([date, VS, AVG, PA, AB, R, H, _2B, _3B, HR, RBI, SB, CS, BB, HBP, SO, GDP])

			#데이터 합		
			PA_sum += int(PA)
			AB_sum += int(AB)
			R_sum += int(R)
			H_sum += int(H)
			_2B_sum += int(_2B)
			_3B_sum += int(_3B)
			HR_sum += int(HR)
			RBI_sum += int(RBI)
			SB_sum += int(SB)
			CS_sum += int(CS)
			BB_sum += int(BB)
			HBP_sum += int(HBP)
			SO_sum += int(SO)
			GDP_sum += int(GDP)
#                            0        1      2      3       4        5        6       7       8       9       10      11       12       13
	data_sum_list[name] = [PA_sum, AB_sum, R_sum, H_sum, _2B_sum, _3B_sum, HR_sum, RBI_sum, SB_sum, CS_sum, BB_sum, HBP_sum, SO_sum, GDP_sum]

	#각종 지표 계산
	wOBA = (data_sum_list[name][10]*0.69 + data_sum_list[name][11]*0.721 + data_sum_list[name][3]*0.884 + data_sum_list[name][4]*1.26 + data_sum_list[name][5]*1.599 + data_sum_list[name][6]*2.065 + data_sum_list[name][8]*0.2 + data_sum_list[name][9]*(-0.4))/PA_sum
	wRAA = (wOBA-0.331)*PA_sum/1.224	
	RAR = wRAA + 20*PA_sum/600
	WAR = RAR/10
	result[name] = [round(wOBA, 2), round(wRAA, 2), round(RAR, 2), round(WAR, 2)]

print("이름 :    wOBA   wRAR   RAR   WAR")
for keys in result.keys():
	print(f"{keys}: {result[keys]}")