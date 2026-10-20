"""Paint out the polo chest logo and the fake chip-bag lettering on every frame up to the cut.

Logo: tracked as the small navy/black blob near its last position (navy reads B >= R, which
separates it from skin); inpainted with a dilated mask. Bag: tracked by template matching,
then red lettering pixels inside the bag box are inpainted.
"""
import pathlib, sys
import cv2
import numpy as np

HERE = pathlib.Path(__file__).parent
FR, OUT = HERE/"fr", HERE/"clean"
OUT.mkdir(exist_ok=True)
CUT = 168                       # last frame kept (1-based file index)
QA = [1, 30, 60, 90, 120, 150, 168]

def find_logo(img, pos, r=22):
    x0, y0 = max(0, pos[0]-r), max(0, pos[1]-r)
    win = img[y0:pos[1]+r, x0:pos[0]+r].astype(int)
    b, g, rr = win[..., 0], win[..., 1], win[..., 2]
    gray = (b+g+rr)/3
    m = ((gray < 62) & (rr < 75)).astype(np.uint8)
    n, lab, st, cen = cv2.connectedComponentsWithStats(m, 8)
    best = None
    for i in range(1, n):
        a = st[i, cv2.CC_STAT_AREA]
        if 3 <= a <= 160:
            cx, cy = cen[i][0]+x0, cen[i][1]+y0
            d = (cx-pos[0])**2+(cy-pos[1])**2
            if best is None or d < best[0]:
                best = (d, i, (int(cx), int(cy)))
    if best is None:
        return None, None
    full = np.zeros(img.shape[:2], np.uint8)
    full[y0:y0+lab.shape[0], x0:x0+lab.shape[1]][lab == best[1]] = 255
    return best[2], full

def main():
    first = cv2.imread(str(FR/"0001.png"))
    # seed positions read off the full-res QA crops
    logo = (424, 632)
    p, _ = find_logo(first, logo, r=16)
    if p is None:
        sys.exit("logo not found in frame 1")
    logo = p
    bag_box = [292, 770, 84, 104]          # x, y, w, h around the chip bag in frame 1
    tmpl = first[bag_box[1]:bag_box[1]+bag_box[3], bag_box[0]:bag_box[0]+bag_box[2]].copy()
    misses = 0
    for n in range(1, CUT+1):
        img = cv2.imread(str(FR/f"{n:04d}.png"))
        mask = np.zeros(img.shape[:2], np.uint8)
        # ---- logo ----
        p, m = find_logo(img, logo)
        if p is not None:
            logo = p
            mask |= cv2.dilate(m, np.ones((7, 7), np.uint8), iterations=1)
        else:
            misses += 1
        # ---- bag ----
        x, y, w, h = bag_box
        sx0, sy0 = max(0, x-40), max(0, y-40)
        search = img[sy0:y+h+40, sx0:x+w+40]
        if search.shape[0] >= h and search.shape[1] >= w:
            res = cv2.matchTemplate(search, tmpl, cv2.TM_CCOEFF_NORMED)
            _, score, _, loc = cv2.minMaxLoc(res)
            if score > 0.45:
                bag_box = [sx0+loc[0], sy0+loc[1], w, h]
                x, y = bag_box[0], bag_box[1]
                tmpl = img[y:y+h, x:x+w].copy()
        roi = img[y:y+h, x:x+w].astype(int)
        b, g, r = roi[..., 0], roi[..., 1], roi[..., 2]
        letters = ((r > 105) & (g < 105) & (r-g > 60)).astype(np.uint8)*255
        letters = cv2.dilate(letters, np.ones((3, 3), np.uint8), iterations=1)
        mask[y:y+h, x:x+w] |= letters
        if mask.any():
            img = cv2.inpaint(img, mask, 5, cv2.INPAINT_TELEA)
        cv2.imwrite(str(OUT/f"{n:04d}.png"), img)
        if n in QA:
            cv2.imwrite(str(HERE/f"qa_{n:04d}.png"), img[540:960, 220:520])
    print("done, logo misses:", misses)

if __name__ == "__main__":
    main()
