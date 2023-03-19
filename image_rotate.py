from PIL import Image
import os
  
def main():
     # path of the folder containing the raw images
     inPath ="E:\\working\\Python\\shopify_product_upload_python_bot\\source"
     
     # path of the folder that will contain the modified image
     outPath ="E:\\working\\Python\\shopify_product_upload_python_bot\\rotated_img"
     # count = 0
     for imagePath in os.listdir(inPath):
          # imagePath contains name of the image 
          inputPath = os.path.join(inPath, imagePath)
     
          # inputPath contains the full directory name
          img = Image.open(inputPath)
     
          fullOutPath = os.path.join(outPath, imagePath)
          # fullOutPath contains the path of the output
          # image that needs to be generated
          img.rotate(270, expand=True).save(fullOutPath)
          # count += 1
          # if count == 8: 
          #      break
          print(fullOutPath)
  
# Driver Function
if __name__ == '__main__':
     main()