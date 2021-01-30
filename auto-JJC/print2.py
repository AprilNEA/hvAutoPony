import pyautogui
import cv2
import numpyasnpfromPIL import ImageGrab

#截屏，同时提前准备一张屏幕上会出现的小图bd.png
im=ImageGrab.grab()
im.save('screen.png','png')

#加载原始RGB图像
img_rgb= cv2.imread("screen.png")

#创建一个原始图像的灰度版本，所有操作在灰度版本中处理，然后在RGB图像中使用相同坐标还原
img_gray=cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

#加载将要搜索的图像模板
template= cv2.imread('.png',0)

#使用matchTemplate对原始灰度图像和图像模板进行匹配
res=cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

#设定阈值,0.7应该可以
threshold= 0.999#res大于99.9%loc= np.where( res >=threshold)

#得到原图像中的坐标for pt in zip(*loc[::-1]):
print(pt[0],pt[1])

#pyautogui.click(pt[0],pt[1])break#cv2.destroyAllWindows()
print("the end")