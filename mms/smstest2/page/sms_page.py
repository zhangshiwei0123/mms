from base.base_action import BaseAction
import page
class SmsPage(BaseAction):
    #初始化方法
    def __init__(self,driver):
        BaseAction.__init__(self,driver)
    #把要测试的整个业务分为多个函数实现
    #1点击新增短信按钮
    def click_add_new_sms(self):
        self.click_element(page.sms_add_btn)

    #2向接收着输入框里面输入内容
    def input_receive_sms_number(self,number):
        self.input_edit_content(page.sms_edit_receive_number,number)

    #3 实现发送短信功能
    def send_sms_content(self,content):
        #3.1 动态向发送框 输入了一个内容
        self.input_edit_content(page.sms_edit_send_content,content)
        #3.2 点击发送按钮
        self.click_element(page.sms_btn_send)

    #4.获取发送短信的列表
    def get_sms_send_lists(self):
        return self.find_elements(page.sms_send_lists)

