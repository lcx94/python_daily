# -*- coding: utf-8 -*-
"""
---------------------------------
File Name: trans
Description: 截屏快速翻译
Author: Liu Changxin
date: 2020/4/3
---------------------------------
Change Activity:
2020/4/3
"""
import tkinter.messagebox
from tkinter import *

import pytesseract
from PIL import Image, ImageGrab
from googletrans import Translator


def translate():
    # 从剪切板获取图片，保存到本地
    img = ImageGrab.grabclipboard()
    if img and isinstance(img, Image.Image):
        img_result = './img/temp.png'
        img.save(img_result)

        # OCR
        content_eng = pytesseract.image_to_string(Image.open(img_result), lang='eng')
        print(content_eng)

        # 翻译
        translator = Translator(service_urls=['translate.google.cn'])
        content_chinese = translator.translate(content_eng, src='en', dest='zh-cn').text

        # 显示
        root = Tk()
        root.withdraw()
        tkinter.messagebox.showinfo('翻译结果', content_chinese)


if __name__ == '__main__':
    translate()
