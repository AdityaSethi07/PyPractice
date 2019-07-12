from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

class AmazonBot:
	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.bot=webdriver.Chrome()
		
	def login(self):
		bot=self.bot
		bot.get('https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
		time.sleep(5)
		email = bot.find_element_by_id('ap_email')
		email.clear()
		email.send_keys(self.username)
		email.send_keys(Keys.RETURN)
		time.sleep(5)
		password = bot.find_element_by_id('ap_password')
		password.clear()
		password.send_keys(self.password)
		password.send_keys(Keys.RETURN)
		time.sleep(5)

	def open_product(self,product_link):
		bot=self.bot
		bot.get(product_link)

	def place_order(self):
		bot=self.bot
		action=ActionChains(bot)
		order = bot.find_element_by_id('buy-now-button')
		action.move_to_element(order).perform()
		order.click()

	def payment(self):
		bot = self.bot
		action = ActionChains(bot)
		

		time.sleep(10) # select payment method manually (you can decrease time, if payment method is already selected by default)
		
		
		next_= bot.find_element_by_name('ppw-widgetEvent:SetPaymentPlanSelectContinueEvent')
		action.move_to_element(next_).perform()
		next_.click()
		

b=AmazonBot('username@email.com','password')
b.login()
time.sleep(20) #enter OTP if asked for (time is in seconds, can be increased or decreased as per requirement)
#time.sleep(5)  # if OTP not required, change to this one

#ENTER PRODUCT LINK HERE
b.open_product('https://www.amazon.in/gp/product/B07NR79B1X/ref=s9_acss_bw_cg_CG2_3a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-3&pf_rd_r=A9V87C8DQGRXGVD030AB&pf_rd_t=101&pf_rd_p=3f52a0d7-1135-45b5-90e7-981cf5284d82&pf_rd_i=1389401031')
time.sleep(5)
b.place_order()
time.sleep(5)
b.payment()
