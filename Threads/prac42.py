# Threading

# Method 4 : Real World Example
import requests
import time
import concurrent.futures

# url of different images
img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

t1 = time.perf_counter()        # Start time

#for img_url in img_urls:
def download_image(img_url):  # instead of for loop used above
    img_bytes = requests.get(img_url).content   # gives the image content
    img_name = img_url.split('/')[3]       # splits and displays the content written in url after the 3rd "/"
    img_name = f'{img_name}.jpg'            # adds a ".jpg" tag to the image
    with open(img_name, 'wb') as img_file:  # opens the image file in write-binary mode
        img_file.write(img_bytes)       # wirtes the "image_byte" content in the image file
        print(f'{img_name} was downloaded...')



# the "map()" will go over the "download_image(image_url)"
# with each url in the "img_urls" list. But since we are using the
# "ThreadPoolExecutor()", it will download those images with a
# different thread for each one.
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)


t2 = time.perf_counter()        # Finish time

print(f'Finished in {t2-t1} seconds')