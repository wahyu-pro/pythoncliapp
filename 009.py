import click,os.path
from selenium import webdriver
from time import sleepclass Screenshoot:
	"""docstring for Screenshoot"""
	@click.group()
	def screenshotGroup():
		"""welcome"""	@screenshotGroup.command("screenshoot")
	@click.option("--output", default="png")
	@click.argument("url", default="https://google.com")
	def screenshoot(output, url):
		driver = webdriver.Chrome("chromedriver.exe")
		driver.get(url)
		sleep(1)		filename = 'screenshot-001.'+output
		urutan = 1
		if os.path.exists(filename):
			try:
				filename = 'screenshot-00',urutan,".",output
				os.path.exists(filename)
				urutan += 1
			except Exception as e:
				driver.get_screenshot_as_file(filename)
				driver.quit()
		else:
			driver.get_screenshot_as_file(filename)
			driver.quit()
            
if __name__ == "__main__":
	Screenshoot.screenshotGroup()