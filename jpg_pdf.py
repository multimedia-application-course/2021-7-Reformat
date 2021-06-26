import os

import fitz  # pip install PyMuPDF


def pic2pdf(img_path, save_path):
    doc = fitz.Document()
    imgdoc = fitz.Document(img_path)  # 打开图片
    pdfbytes = imgdoc.convert_to_pdf()  # 使用图片创建单页的 PDF
    imgpdf = fitz.Document("pdf", pdfbytes)
    doc.insert_pdf(imgpdf)  # 将当前页插入文档
    doc.save(save_path)  # 保存pdf文件
    doc.close()


def pdf2jpg(pdf_path, save_path):
    doc = fitz.open(pdf_path)
    # 每个尺寸的缩放系数为2，生成分辨率提高四倍的图像
    zoom_x = 2.0
    zoom_y = 2.0
    if doc.page_count > 1:
        for pg in range(doc.page_count):
            page = doc[pg]
            trans = fitz.Matrix(zoom_x, zoom_y).prerotate(0)
            pm = page.getPixmap(matrix=trans, alpha=False)
            pm.writePNG('%s(%d).jpg' % (save_path[:-4], pg + 1))
    else:
        trans = fitz.Matrix(zoom_x, zoom_y).prerotate(0)
        pm = doc[0].getPixmap(matrix=trans, alpha=False)
        pm.writePNG(save_path)
    doc.close()


if __name__ == '__main__':
    pic2pdf('path', 'save_path')
    pdf2jpg('path', 'save_path')
