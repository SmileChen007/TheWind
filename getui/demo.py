﻿# -*- coding: utf-8 -*-
from array import array
__author__ = 'wei'


from igt_push import *
from igetui.template import *
from igetui.template.igt_base_template import *
from igetui.template.igt_transmission_template import *
from igetui.template.igt_link_template import *
from igetui.template.igt_notification_template import *
from igetui.template.igt_notypopload_template import *
from igetui.template.igt_apn_template import *
from igetui.igt_message import *
from igetui.igt_target import *
from igetui.template import *
from BatchImpl import *
from payload.APNPayload import *
from igetui.utils.AppConditions import *

# toList接口每个用户返回用户状态开关,true：打开 false：关闭
os.environ['needDetails'] = 'true'
APPKEY = "Kto8WpxyJC9EyKudBNxXX9"
APPID = "KyvIrznoRb89u7JQx2WUu8"
MASTERSECRET = "6Q0UtrZztj8RSfU5d4gkX8"
CID = "48d89bc6956d4a451f30e11255684098"
HOST = 'http://sdk.open.api.igexin.com/apiex.htm'
Alias = '请输入别名'
DEVICETOKEN = ""


def pushAPN():

    push = IGeTui(HOST, APPKEY, MASTERSECRET)
    message = IGtSingleMessage()

    
# APN简单推送
    template = APNTemplate()
    apn = APNPayload()
    alertMsg = SimpleAlertMsg()
    alertMsg.alertMsg = ""
    apn.alertMsg = alertMsg
    apn.badge = 2
    apn.sound = ""
    apn.addCustomMsg("payload", "payload")
#     apn.contentAvailable=1
#     apn.category="ACTIONABLE"
    template.setApnInfo(apn)
    
# APN高级推送
#     template = APNTemplate()
#     apnpayload = APNPayload()
#     应用icon上显示的数字
#     apnpayload.badge = 4
#     通知铃声文件名
#     apnpayload.sound = "sound"
#     apnpayload.addCustomMsg("payload", "payload")
#     推送直接带有透传数据
#     apnpayload.contentAvailable = 1
#     在客户端通知栏触发特定的action和button显示
#     apnpayload.category = "ACTIONABLE"
#         
#         
#     alertMsg = DictionaryAlertMsg()
#     通知文本消息字符串
#     alertMsg.body = 'body'
#     (用于多语言支持）指定执行按钮所使用的Localizable.strings
#     alertMsg.actionLocKey = 'actionLockey'
#     (用于多语言支持）指定Localizable.strings文件中相应的key
#     alertMsg.locKey = 'lockey'
#     如果loc-key中使用的占位符，则在loc-args中指定各参数
#     alertMsg.locArgs=['locArgs']
#     指定启动界面图片名
#     alertMsg.launchImage = 'launchImage'
#     # IOS8.2以上版本支持
#     alertMsg.title = 'Title'
#     对于标题, 如果loc-key中使用的占位符，则在loc-args中指定各参数
#     alertMsg.titleLocArgs = ['TitleLocArg']
#     (用于多语言支持）对于标题指定执行按钮所使用的Localizable.strings
#     alertMsg.titleLocKey = 'TitleLocKey'
#     apnpayload.alertMsg=alertMsg
#     template.setApnInfo(apnpayload)

    # 单个用户推送接口
    message.data = template
    ret = push.pushAPNMessageToSingle(APPID, DEVICETOKEN, message)
    print message
    print ret

    # 多个用户推送接口
#     message = IGtListMessage()
#     message.data = template
#     contentId = push.getAPNContentId(APPID, message)
#     deviceTokenList = []
#     deviceTokenList.append(DEVICETOKEN)
#     ret = push.pushAPNMessageToList(APPID, contentId, deviceTokenList)
#     print ret

def pushMessageToSingle():
    push = IGeTui(HOST, APPKEY, MASTERSECRET)
    # 消息模版：
    # 1.TransmissionTemplate:透传功能模板
    # 2.LinkTemplate:通知打开链接功能模板
    # 3.NotificationTemplate：通知透传功能模板
    # 4.NotyPopLoadTemplate：通知弹框下载功能模板

    template = NotificationTemplateDemo()
    # template = LinkTemplateDemo()
    # template = TransmissionTemplateDemo()
    # template = NotyPopLoadTemplateDemo()
	
    message = IGtSingleMessage()
    #是否离线推送
    message.isOffline = True
    #离线有效时间
    message.offlineExpireTime = 1000 * 3600 * 12
    message.data = template
    # 推送的网络类型：(0:不限;1:wifi;2:4G/3G/2G)
    # message.pushNetWorkType = 2

    target = Target()
    target.appId = APPID
    target.clientId = CID

    try:
        ret = push.pushMessageToSingle(message, target)
        print ret
    except RequestException, e:
        requstId = e.getRequestId()
        ret = push.pushMessageToSingle(message, target, requstId)
        print ret

def pushMessageToSingleBatch():
    push = IGeTui(HOST, APPKEY, MASTERSECRET)
    batch = BatchImpl(APPKEY, push)
    
    # 消息模版：
    # 1.TransmissionTemplate:透传功能模板
    # 2.LinkTemplate:通知打开链接功能模板
    # 3.NotificationTemplate：通知透传功能模板
    # 4.NotyPopLoadTemplate：通知弹框下载功能模板

    templateNoti = NotificationTemplateDemo()
    templateLink = LinkTemplateDemo()
    # template = TransmissionTemplateDemo()
    # template = NotyPopLoadTemplateDemo()
    
    messageNoti = IGtSingleMessage()
    messageNoti.isOffline = True
    messageNoti.offlineExpireTime = 1000 * 3600 * 12
    messageNoti.data = templateNoti
#     message.pushNetWorkType = 1

    targetNoti = Target()
    targetNoti.appId = APPID
    targetNoti.clientId = CID

    batch.add(messageNoti, targetNoti)
    
    messageLink = IGtSingleMessage()
    messageLink.isOffline = True
    messageLink.offlineExpireTime = 1000 * 3600 * 12
    messageLink.data = templateLink
#     message.pushNetWorkType = 1

    targetLink = Target()
    targetLink.appId = APPID
    targetLink.clientId = CID

    batch.add(messageLink, targetLink)
    try:
        ret = batch.submit()
        print ret
    except Exception, e:
        ret=batch.retry()
        print ret


def pushMessageToList():
    push = IGeTui(HOST, APPKEY, MASTERSECRET)

    # 消息模版： 
    # 1.TransmissionTemplate:透传功能模板  
    # 2.LinkTemplate:通知打开链接功能模板  
    # 3.NotificationTemplate：通知透传功能模板  
    # 4.NotyPopLoadTemplate：通知弹框下载功能模板

    template = NotificationTemplateDemo()
    # template = LinkTemplateDemo()
    # template = TransmissionTemplateDemo()
    # template = NotyPopLoadTemplateDemo()

    message = IGtListMessage()
    message.data = template
    message.isOffline = True
    message.offlineExpireTime = 1000 * 3600 * 12
    message.pushNetWorkType = 0

    target1 = Target()
    target1.appId = APPID
    target1.clientId = CID
    #target1.alias = Alias
    arr = []
    
    arr.append(target1)
    contentId = push.getContentId(message, 'ToList_任务别名_可为空')
    ret = push.pushMessageToList(contentId, arr)
    print ret


def pushMessageToApp():
    push = IGeTui(HOST, APPKEY, MASTERSECRET)

    # 消息模版： 
    # 1.TransmissionTemplate:透传功能模板  
    # 2.LinkTemplate:通知打开链接功能模板  
    # 3.NotificationTemplate：通知透传功能模板  
    # 4.NotyPopLoadTemplate：通知弹框下载功能模板

    template = NotificationTemplateDemo()
    # template = LinkTemplateDemo()
    # template = TransmissionTemplateDemo()
    # template = NotyPopLoadTemplateDemo()

    message = IGtAppMessage()
    message.data = template
    message.isOffline = True
    message.offlineExpireTime = 1000 * 3600 * 12
    message.appIdList.extend([APPID])

    conditions = AppConditions()
    phoneType = ['ANDROID']
    tags = ['dddd', 'ceshi2']
    conditions.addCondition('phoneType', phoneType, OptType.OR)
    conditions.addCondition(AppConditions.TAG, tags, OptType.AND)
    message.setConditions(conditions)
    # message.phoneTypeList.extend(["ANDROID", "IOS"])
    # message.provinceList.extend(["浙江", "上海"])
    # message.tagList.extend(["开心"])
    # message.pushNetWorkType = 1
    # 控速推送(条/秒)
    # message.setSpeed(10)

    ret = push.pushMessageToApp(message, 'toApp_任务别名_可为空')
    # print message.getSpeed()
    print ret

# 通知透传模板动作内容
def NotificationTemplateDemo():
    template = NotificationTemplate()
    template.appId = APPID
    template.appKey = APPKEY
    template.transmissionType = 1
    template.transmissionContent = u"请填入透传内容"
    template.title = u"测试"
    template.text = u"测试通知"
    template.logo = "ic_launcher.png"
    template.logoURL = ""
    template.isRing = True
    template.isVibrate = True
    template.isClearable = True
    # begin = "2015-03-04 17:40:22"
    # end = "2015-03-04 17:47:24"
    # template.setDuration(begin, end)
    return template

# 通知链接模板动作内容
def LinkTemplateDemo():
    template = LinkTemplate()
    template.appId = APPID
    template.appKey = APPKEY
    template.title = u"请填入通知标题"
    template.text = u"请填入通知内容"
    template.logo = ""
    template.url = "http://www.baidu.com"
    template.transmissionType = 1
    template.transmissionContent = ''
    template.isRing = True
    template.isVibrate = True
    template.isClearable = True
    return template

# 透传模板动作内容
def TransmissionTemplateDemo():
    template = TransmissionTemplate()
    template.transmissionType = 1
    template.appId = APPID
    template.appKey = APPKEY
    template.transmissionContent = '请填入透传内容'
    # iOS 推送需要的PushInfo字段 前三项必填，后四项可以填空字符串
    # template.setPushInfo(actionLocKey, badge, message, sound, payload, locKey, locArgs, launchImage)
#     template.setPushInfo("", 0, "", "com.gexin.ios.silence", "", "", "", "")

# APN简单推送
    alertMsg = SimpleAlertMsg()
    alertMsg.alertMsg = ""
    apn = APNPayload()
    apn.alertMsg = alertMsg
    apn.badge = 2
#     apn.sound = ""
    apn.addCustomMsg("payload", "payload")
#     apn.contentAvailable=1
#     apn.category="ACTIONABLE"
    template.setApnInfo(apn)

    # APN高级推送
#     apnpayload = APNPayload()
#     apnpayload.badge = 4
#     apnpayload.sound = "com.gexin.ios.silence"
#     apnpayload.addCustomMsg("payload", "payload")
#     apnpayload.contentAvailable = 1
#     apnpayload.category = "ACTIONABLE"
#     alertMsg = DictionaryAlertMsg()
#     alertMsg.body = 'body'
#     alertMsg.actionLocKey = 'actionLockey'
#     alertMsg.locKey = 'lockey'
#     alertMsg.locArgs=['locArgs']
#     alertMsg.launchImage = 'launchImage'
#     # IOS8.2以上版本支持
#     alertMsg.title = 'Title'
#     alertMsg.titleLocArgs = ['TitleLocArg']
#     alertMsg.titleLocKey = 'TitleLocKey'
#     apnpayload.alertMsg=alertMsg
#     template.setApnInfo(apnpayload)
    
    
    return template

# 通知弹框下载模板动作内容
def NotyPopLoadTemplateDemo():
    template = NotyPopLoadTemplate()
    template.appId = APPID
    template.appKey = APPKEY
    template.notyIcon = "icon.png"
    template.logoUrl = ""
    template.notyTitle = u"通知弹框下载功能标题"
    template.notyContent = u"通知弹框下载功能内容"
    template.isRing = True
    template.isVibrate = True
    template.isClearable = True

    template.popTitle = u"弹框标题"
    template.popContent = u"弹框内容"
    template.popImage = ""
    template.popButton1 = u"下载"
    template.popButton2 = u"取消"

    template.loadIcon = "file://icon.png"
    template.loadTitle = u"下载内容"
    template.loadUrl = "http://gdown.baidu.com/data/wisegame/c95836e06c224f51/weixinxinqing_5.apk"
    template.isAutoInstall = True
    template.isActive = False
    return template

# 获取用户状态
def getUserStatus():
    push = IGeTui(HOST, APPKEY, MASTERSECRET)
    print push.getClientIdStatus(APPID, CID)

# 任务停止功能
def stopTask():
    push = IGeTui(HOST, APPKEY, MASTERSECRET)
    print push.stop("OSA-0226_50RYYPFmos9eQEHZrkAf27")
 
# 根据ClientID设置标签功能
def setTag():
    push = IGeTui(HOST, APPKEY, MASTERSECRET)
    tagList = ['标签1', '标签2', '......']
    print push.setClientTag(APPID, CID, tagList)

# 根据taskId返回推送结果
def getPushResultTest():
    push = IGeTui(HOST, APPKEY, MASTERSECRET)
    #返回根据任务tasdkId返回数据
#     print push.getPushResult("OSA-0304_LUNiKF8n6i8PXgvqARRUp8")
    #返回用户推送结果信息
#     print push.queryAppPushDataByDate(APPID, "20150525")
    #返回用户注册结果信息
    print push.queryAppUserDataByDate(APPID,"20150525")
    

# 根据ClientID查询标签
def getUserTagsTest():
    push = IGeTui(HOST, APPKEY, MASTERSECRET)
    dictz = push.getUserTags(APPID, CID)
    for key in dictz:
	print key + ":" + dictz[key].decode("utf-8")        

    #
    # 服务端支持三个接口推送
    # 1.PushMessageToSingle接口：支持对单个用户进行推送
    # 2.PushMessageToList接口：支持对多个用户进行推送，建议为50个用户
    # 3.pushMessageToApp接口：对单个应用下的所有用户进行推送，可根据省份，标签，机型过滤推送
    #
def queryAppPushDataByDate():
    push = IGeTui(HOST, APPKEY, MASTERSECRET)
    res = push.queryAppPushDataByDate(APPID,"20150910")
    print(res)

def queryAppUserDataByDate():
    push = IGeTui(HOST, APPKEY, MASTERSECRET)
    res = push.queryAppUserDataByDate(APPID,"20150910")
    print(res)

def getPersonaTagsDemo():
    push = IGeTui(HOST, APPKEY, MASTERSECRET)
    res = push.getPersonaTags(APPID)
    print(json.dumps(res).decode("unicode_escape").encode("utf-8"))
    for result in res["tags"]:
        print(result["desc"])

# queryAppPushDataByDate()
# queryAppUserDataByDate()
pushMessageToSingle()
# pushMessageToSingleBatch()
# pushMessageToList()
# pushMessageToApp()

# IOS简化版推送接口
# pushAPN()

# 获取用户状态接口
# getUserStatus()

# 任务停止功能接口
# stopTask()

# 通过服务端设置用户标签
# setTag()

# 根据TaskID返回任务推送结果功能
# getPushResultTest()

# 根据ClientID查询标签功能
# getUserTagsTest()

#获取appid可以操作的用户属性
# getPersonaTagsDemo()
