from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter
import os

from PIL import Image
import PyPDF2
import img2pdf

#First of all,we convert all the Pictures into 1 pdf

images_list = []
pdf_list = []

PicToPdf_name = "PicToPdf.pdf"

def get_Pic_dir():
    for every_file in os.listdir():
    
        if every_file.endswith(".jpg") or every_file.endswith(".png") or every_file.endswith(".bmp"):
        
            images_list.append(os.path.abspath(every_file))
            
def sort_image():
    images_list.sort()

def convert_Pic_To_Pdf():

    get_Pic_dir()
    sort_image()

    pdfContent = img2pdf.convert(images_list)
        
    with open(PicToPdf_name, "wb") as PicToPdf_out:
        PicToPdf_out.write(pdfContent)
    PicToPdf_out.close()


def GetFileName(dir_path):
    file_list = [os.path.join(dirpath, filesname) \
                 for dirpath, dirs, files in os.walk(dir_path) \
                 for filesname in files]
                 
    for every_f in file_list:
        if every_f.endswith(".pdf"):
            pdf_list.append(every_f)
                 
    return pdf_list
    
    
    
def MergePDF(dir_path, file_name):
    # 实例化写入对象
    output = PdfWriter()
    outputPages = 0
    # 调用上一个函数获取全部文件的绝对路径
    file_list = GetFileName(dir_path)

    for pdf_file in file_list:
        print("文件：%s" % pdf_file.split('\\')[-1], end=' ')

        # 读取PDF文件
        input = PdfReader(open(pdf_file, "rb"))
        # 获得源PDF文件中页面总数
        pageCount = len(input.pages)
        outputPages += pageCount
        print("页数：%d" % pageCount)
        # 分别将page添加到输出output中
        for iPage in range(pageCount):
            output.add_page(input.pages[iPage])
            
    print("\n合并后的总页数:%d" % outputPages)
    # 写入到目标PDF文件
    print("PDF文件正在合并，请稍等......")
    with open(os.path.join(dir_path, file_name), "wb") as outputfile:
        # 注意这里的写法和正常的上下文文件写入是相反的
        output.write(outputfile)
    outputfile.close()
        
    print("PDF文件合并完成")


if __name__ == '__main__':

    pdfpath = r'D:\Work\2023\pdf_code'

    name_final = 'PDF_4DX.pdf'
    
    convert_Pic_To_Pdf()
        
    GetFileName(pdfpath)

    MergePDF(pdfpath, name_final)