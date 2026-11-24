import time

import pyautogui as pa
import pydirectinput as p

def herb_search(*args):
    # 以字符串列表形式逐步接受草药

    search_region = {
        (2560, 1440):(118, 468, 183, 1160),
        (1920, 1080):(92, 352, 134, 870),
    }

    region = search_region.get((p.size()[0], p.size()[1]))
    if region is None:
        print('对不起，该脚本目前仅支持以下分辨率：')
        for index in search_region.keys():
            print(f'   {index[0]}x{index[1]}   ')
        raise OSError

    p.press('i')
    time.sleep(0.5)

    for s in args:
        # 尝试查找新鲜草药
        try:
            location = pa.locateOnScreen(
                ''.join(('./data/icons/', s, '.TIF')),
                confidence=0.7,
                region=region
            )
        except pa.ImageNotFoundException:
            location = None
            # 尝试查找干草药
            try:
                location_dried = pa.locateOnScreen(
                    ''.join(('./data/icons/dried_', s, '.TIF')),
                    confidence=0.7,
                    region=region
                )
            except pa.ImageNotFoundException, OSError:
                location_dried = None

        # 优先使用新鲜草药
        if location is not None:
            point = pa.center(location)
            p.click(point.x, point.y)
            time.sleep(0.1)
            p.press('e')
            time.sleep(0.5)

        elif location_dried is not None:
            point = pa.center(location_dried)
            p.click(point.x, point.y)
            time.sleep(0.1)
            p.press('e')
            time.sleep(0.5)
        else:
            print(f'在材料里没有找到{s}')
            raise pa.ImageNotFoundException

    time.sleep(0.5)
    p.press('esc')
    time.sleep(0.5)