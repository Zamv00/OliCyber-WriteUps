from PIL import Image
import numpy as np

file1 = "challenge.png"
file2 = "whoami.png"
output_path = "xor_result.png"


img1 = np.array(Image.open(file1).convert("RGB"))
img2 = np.array(Image.open(file2).convert("RGB"))


xor_img = np.bitwise_xor(img1, img2)

result = Image.fromarray(xor_img)
result.save(output_path)

output_path
#ptm{y0u_r34lly_7r4c3d_m3}