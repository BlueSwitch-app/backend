import cloudinary
import cloudinary.uploader
def upload_image(image_path):
# Configuration       
    cloudinary.config( 
    cloud_name = "dkjlygxse", 
    api_key = "111946664427639", 
    api_secret = "iYwxs47jmdPmb-xCGtJfWKtg-F8", # Click 'View API Keys' above to copy your API secret
    secure=True
)

# Upload an image
    upload_result = cloudinary.uploader.upload(image_path,
                                           public_id="shoes")
    return(upload_result["secure_url"])