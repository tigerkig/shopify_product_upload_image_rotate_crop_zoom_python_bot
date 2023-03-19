from PIL import Image
import os
  
def main():
     # path of the folder containing the raw images
     inPath ="E:\\working\\Python\\shopify_product_upload_python_bot\\rotated_img"
     # path of the folder that will contain the modified image
     outPath ="E:\\working\\Python\\shopify_product_upload_python_bot\\croped_img"
     count = 0
     same_file_count = 1
     zoom = 1.5
     first_zoom = 1.2
     original_name= ''

     for imagePath in os.listdir(inPath):
          inputPath = os.path.join(inPath, imagePath)
          img = Image.open(inputPath)
          fileIndex = imagePath.split(' ')[0]

          if original_name == fileIndex:
               same_file_count += 1
          else:
               original_name = fileIndex
               same_file_count = 1

          if same_file_count <= 4:
               # img.save(os.path.join(outPath, f'{fileIndex}_{same_file_count}.jpg'))

               # if count % 2 == 0:
               image_1 = img.crop((((img.size[0]/2)-img.size[0]/(first_zoom*2)),((img.size[1]/2)-img.size[1]/(first_zoom*2)),((img.size[0]/2)+img.size[0]/(first_zoom*2)),((img.size[1]/2)+img.size[1]/(first_zoom*2))))
               image_1.save(os.path.join(outPath, f'{fileIndex}_{same_file_count}.jpg'))
               
               # else:
               image_2 = img.crop((((img.size[0]/2)-img.size[0]/(zoom*2)),((img.size[1]/4)-img.size[1]/(zoom*4)),((img.size[0]/1.5)+img.size[0]/(zoom*2)),((img.size[1]/2)+img.size[1]/(zoom*2))))
               
               same_file_count += 1
               image_2.save(os.path.join(outPath, f'{fileIndex}_{same_file_count}.jpg'))
          if count == 10:
               break
          count += 1

# Driver Function
if __name__ == '__main__':
     main()
