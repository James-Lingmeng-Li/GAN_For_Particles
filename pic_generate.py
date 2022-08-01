import cv2
import cv2
import numpy as np
from math import sqrt
import os
from random import randint
import random
from matplotlib import pyplot as plt
def get_picture_dir(file_dir):
    filelist = os.listdir(file_dir) #获取文件路径

    total_num=len(filelist)
    idx = randint(0,total_num)
    image_path=filelist[idx]
    return os.path.join(os.path.abspath(file_dir), image_path)
    # img=cv2.imread(picture_path)
    # cv2.imshow("img",img)
    # cv2.waitKey(0)

def get_obj(object_img):
    # obj_num=0
    # obj_total=5
    # obj_num < obj_total:
    # obj_dir=get_picture_dir(object_img)
    # obj_num+=1
    obj_num = randint(1,6)
    i=0
    obj_list=[]
    while i <obj_num:
        obj_list.append(get_picture_dir(object_img))
        i+=1
    return obj_list

def get_scale():
    scale=0
    while scale < 0.1 or scale > 0.5:
        scale = random.random()
    return scale

for i in range(10):
    object_img='.\\ven\\generated_particle'
    back_ground_folder = 'F:\image for Lingmeng\image'
    obj_list = get_obj(object_img)
    bg_dir=get_picture_dir(back_ground_folder)
    bg=cv2.imread(bg_dir)

    bg_name=os.path.split(bg_dir)
    # print(bg_name)
    name=bg_name[1]
    name=os.path.splitext(name)[0]
    name=name+'.txt'
    print(name)
    f = open(f"F:\\practise\\ven\\new_img\\{name}",'a')

    for obj_dir in obj_list:
        obj=cv2.imread(obj_dir)
        retry= False

        while retry!= True:
            try:
                scale=get_scale()
                print(scale)
                obj_edite = cv2.resize(obj, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)

                width, height, channels = bg.shape
                h = randint(1, 2000)
                w = randint(1, width)

                center = (h, w)
                print(h, w)
                mask = 255 * np.ones(obj_edite.shape, obj_edite.dtype)
                print(obj_edite.shape)
                print(bg.shape)

                cv2.namedWindow('findCorners', 0)
                cv2.resizeWindow('findCorners', 1000, 1000)  # 自己设定窗口图片的大小
                cv2.imshow("findCorners", obj_edite)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                obj_w, obj_h, obj_tunnel = obj_edite.shape

                print(obj_w)
                print(obj_h)

                f.write(str(obj_h) + ',' + str(obj_w) + ',' + str(center[0])+','+str(center[1]))
                f.write('\n')
                mixed_clone = cv2.seamlessClone(obj_edite, bg, mask, center, cv2.MIXED_CLONE)
                bg=mixed_clone
                # obj_dir = get_picture_dir(object_img)
                # obj=cv2.imread(obj_dir)
                # mixed_clone
                cv2.namedWindow('findCorners', 0)
                cv2.resizeWindow('findCorners', 1000, 1000)  # 自己设定窗口图片的大小
                cv2.imshow("findCorners", mixed_clone)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                retry=True

            except Exception as e:
                print(e)

    f.close()
    cv2.imwrite(f"F:\\practise\\ven\\new_img\\{bg_name[1]}",bg)

    # plt.savefig(f"F:\\practise\\ven\\new_img\\{bg_name[1]}",bbox_inches='tight', pad_inches=0.0)




