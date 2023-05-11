#1.def-color,shape,draw 
#2.trackbar in color to adject 
import cv2
import numpy as np 
import color as c 
import shape as sh 
bins=256

def callback(x):
    pass
cv2.namedWindow('frame')
cv2.createTrackbar('ih','frame',116,255,callback)
cv2.createTrackbar('is','frame',63,255,callback)
cv2.createTrackbar('iv','frame',0,255,callback)
cv2.createTrackbar('hh','frame',143,255,callback)
cv2.createTrackbar('hs','frame',255,255,callback)
cv2.createTrackbar('hv','frame',255,255,callback)
def enchancement(frame):
    b, g, r = cv2.split(frame)
    b = frame[:, :, 0]//2
    g = frame[:, :, 1]//2
    r = frame[:, :, 2]
    b_flattened = b.flatten()
    b_hist = np.zeros(bins)
    for pix in b:
        b_hist[pix] += 1
    cum_sum = np.cumsum(b_hist)
    norm = (cum_sum - cum_sum.min()) * 255
    # normalization of the pixel values
    n_ = cum_sum.max() - cum_sum.min()
    uniform_norm = norm / n_
    uniform_norm = uniform_norm.astype('int')

    # flat histogram
    b_eq = uniform_norm[b_flattened]
    # reshaping the flattened matrix to its original shape
    b_eq = np.reshape(a=b_eq, newshape=b.shape)
    b_eq=np.uint8(b_eq)
    g_flattened = g.flatten()
    g_hist = np.zeros(bins)
    for pix in g:
        g_hist[pix] += 1
    
    cum_sum = np.cumsum(g_hist) 
    norm = (cum_sum - cum_sum.min()) * 255
    # normalization of the pixel values
    n_ = cum_sum.max() - cum_sum.min()
    uniform_norm = norm / n_
    uniform_norm = uniform_norm.astype('int')

    # flat histogram
    g_eq = uniform_norm[g_flattened]
    # reshaping the flattened matrix to its original shape
    g_eq = np.reshape(a=g_eq, newshape=g.shape)
    g_eq=np.uint8(g_eq)
    
    r_flattened = r.flatten()
    r_hist = np.zeros(bins)
    for pix in r:
        r_hist[pix] += 1
    cum_sum = np.cumsum(r_hist)
    norm = (cum_sum - cum_sum.min()) * 255
    # normalization of the pixel values
    n_ = cum_sum.max() - cum_sum.min()
    uniform_norm = norm / n_
    uniform_norm = uniform_norm.astype('int')

    # flat histogram
    r_eq = uniform_norm[r_flattened]
    # reshaping the flattened matrix to its original shape
    r_eq = np.reshape(a=r_eq, newshape=r.shape)
    r_eq=np.uint8(r_eq)
    image_eq=cv2.merge((b_eq,g_eq,r_eq))
    return image_eq

if __name__ == "__main__":
    cap=cv2.VideoCapture(0)
    #frame=cv2.imread(r'C:\AUV\turkey\codes\images\2.png')
    #frame=cv2.resize(frame,(520,520))
    while True:
       _,frame=cap.read()
       frame=enchancement(frame)
       frame=cv2.resize(frame,(520,520))
       cv2.imshow('initial',frame)
       c.capture(frame)
       k=cv2.waitKey(1)
       if k==27:
        break
    #cap.release()
    cv2.destroyAllWindows()    


