# 导入pillow库
import PIL.Image as Image


# 将透明的像素转化为白色
def alphabg2white_PIL(img):
    img = img.convert('RGBA')
    sp = img.size
    width = sp[0]
    height = sp[1]
    for yh in range(height):
        for xw in range(width):
            dot = (xw, yh)
            color_d = img.getpixel(dot)
            if color_d[3] == 0:
                color_d = (255, 255, 255, 255)
                img.putpixel(dot, color_d)
    return img


# 函数PNG_JPG：用于将png转化为jpg格式
def png2jpg(path, save_path):
    # 读取图像
    pic = Image.open(path)
    # 将图片透明像素转化为白色
    pic = alphabg2white_PIL(pic)

    # 转换格式
    try:
        # 如果此时颜色模式为RGBA时，则将图片格式转化为RGB
        if len(pic.split()) == 4:
            red, green, blue, alpha = pic.split()
            pic = Image.merge("RGB", (red, green, blue))
            pic.convert('RGB').save(save_path, quality=95)
        # 其他颜色模式转化为RGB格式
        else:
            pic.convert('RGB').save(save_path, quality=95)

    # 如果报错，则输出出错误提示
    except Exception as problem:
        print("转换格式失败", problem)


def jpg2png(path, save_path):
    # 将jpg转换为png
    image = Image.open(path)
    image.save(save_path)


if __name__ == '__main__':
    jpg2png('path', 'save_path')
    png2jpg('path', 'save_path')
