"""Turn owner photos into a game-cover illustration look: painterly smoothing (cv2.stylization), colour quantization,
clean ink outlines (Canny on a smoothed image) and boosted contrast/saturation. The sunset grade is applied in the
flyer with a soft-light gradient so the photos stay true to the real equipment."""
import cv2, numpy as np
def art(src, dst, width=1400, k=18, sat=1.35, con=1.18):
    im = cv2.imread(src); h, w = im.shape[:2]; im = cv2.resize(im, (width, int(h*width/w)), interpolation=cv2.INTER_AREA)
    st = cv2.stylization(im, sigma_s=70, sigma_r=0.38)
    Z = st.reshape(-1, 3).astype(np.float32)
    _, lab, cen = cv2.kmeans(Z, k, None, (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0), 2, cv2.KMEANS_PP_CENTERS)
    q = cen.astype(np.uint8)[lab.flatten()].reshape(st.shape)
    g = cv2.cvtColor(cv2.bilateralFilter(im, 9, 80, 80), cv2.COLOR_BGR2GRAY); g = cv2.GaussianBlur(g, (5, 5), 0)
    e = cv2.Canny(g, 40, 110); e = cv2.dilate(e, np.ones((2, 2), np.uint8), 1)
    n, labs, stats, _ = cv2.connectedComponentsWithStats(e, 8)              # drop speckle edges (floor grain)
    keep = np.zeros_like(e); 
    for i in range(1, n):
        if stats[i, cv2.CC_STAT_AREA] >= 60: keep[labs == i] = 255
    out = q.copy(); out[keep > 0] = (25, 12, 20)
    hsv = cv2.cvtColor(out, cv2.COLOR_BGR2HSV).astype(np.float32); hsv[..., 1] = np.clip(hsv[..., 1]*sat, 0, 255)
    out = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)
    out = cv2.convertScaleAbs(out, alpha=con, beta=-10)
    cv2.imwrite(dst, out, [cv2.IMWRITE_JPEG_QUALITY, 94])
if __name__ == '__main__':
    art('gta/src_chairs.jpg', 'gta/art_chairs.jpg', 1500)
    art('gta/src_tables.jpg', 'gta/art_tables.jpg', 1100, sat=1.5)
    print('ok')
