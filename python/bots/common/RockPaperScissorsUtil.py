from random import choices

class RockPaperScissorsUtil():
    DEFAULT_MAIN_RESPONSE_WEIGHT = 40
    TOO_FAST = [
        "等... 等一下啦... 你太快了... 我還要{:.2f}秒",
        "等... 等一下啦... 弄這麼快... 我還要{:.2f}秒",
        "等... 等一下啦... 太快了我會... 再給我{:.2f}秒",
        "等... 等一下啦... 這麼猴急... 我還要{:.2f}秒",
        "不要這麼急啦... 稍微等一下不行嗎...等我{:.2f}秒吧",
        "不要這麼快啦... 稍微等一下不行嗎...等我{:.2f}秒吧",
        "不要一直催啦... 稍微等一下不行嗎...等我{:.2f}秒吧",
        "不要一直出啦... 稍微等一下好嗎？...等我{:.2f}秒吧",
        "你這人怎麼... 不要這樣啦... 再給我{:.2f}秒",
        "你這人在想什麼... 不要這麼快啦... 再給我{:.2f}秒",
        "你這人怎麼... 不要這麼快啦... 再給我{:.2f}秒",
        "你這人怎麼... 老師沒教你要有耐心嗎... 再給我等{:.2f}秒!!",
        "你就這麼想再玩一次嗎? 哼... 等個{:.2f}秒再來吧",
        "你就這麼想贏嗎? 哼... 等個{:.2f}秒再來吧",
        "你就這麼想輸嗎? 哼... 等個{:.2f}秒再來吧",
        "你就這麼想玩弄我嗎? 咕... 等個{:.2f}秒再來吧",
        "咕... 這麼想跟我玩嗎... 等個{:.2f}秒再來吧",
        "我還以為是誰呢, 原來是你啊... 等我{:.2f}秒吧",
        "我還以為是怎麼了, 原來你還想玩啊... 等我{:.2f}秒吧",
        "我還以為是妮妮, 原來是你啊... 等我{:.2f}秒後我就陪你玩一場吧",
        "我還以為是你很忙呢, 原來這麼有空啊... 等我{:.2f}秒吧",
        "就算是bot也需要休息啊, 給我{:.2f}秒吧",
        "就算是bot也需要準備一下, 給我{:.2f}秒吧",
        "就算是bot也需要整理一下, 給我{:.2f}秒吧",
        "就算是bot也需要偷懶一下, 給我{:.2f}秒吧",
        "冷卻時間還需{:.2f}秒",
        "冷卻時間還剩{:.2f}秒",
        "冷卻時間所需{:.2f}秒",
        "冷卻時間剩下{:.2f}秒",
        "哎哎 同學你太快了, 稍微冷靜一下. 等個{:.2f}秒好嗎?"
    ]
    TOO_FAST_WEIGHT = [
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, DEFAULT_MAIN_RESPONSE_WEIGHT]

    TIE_DIALOG = [
        "居然一樣耶, 說不定我們很有默契哦",
        "居然一樣耶, 說不定我們很合得來哦",
        "居然一樣耶, 說不定我們能成為好朋友呢",
        "居然一樣耶, 說不定~~我作弊了~~",
        "居然一樣耶, 你是不是偷偷喜歡我？",
        "居然一樣！ 你怎麼這麼了解我？",
        "居然一樣！ 你是不是作弊！？",
        "居然一樣！ 再來一次！！",
        "居然一樣！ 再來一局！！",
        "居然一樣！ 要不我們再來？",
        "居然一樣！ 那這場算平手吧",
        "居然一樣！ 那...這場算我贏？",
        "居然一樣！ 那...這場算我沒輸？",
        "居然一樣！ 那...你還要再來一次嗎？",
        "討厭, 居然跟我出一樣的",
        "討厭, 居然跟你出一樣的",
        "討厭, 我們居然出同樣的",
        "討厭, 平手了",
        "討厭, 又是平手",
        "我們平手！"
    ]
    TIE_WEIGHT = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, DEFAULT_MAIN_RESPONSE_WEIGHT]
    WIN_DIALOG = [
        # simply winning
        "哈哈, 我贏了！",
        "哈哈, 我又贏了！",
        "哈哈, 我贏了耶",
        "耶! 我贏了!"
        # yandere win
        "哼, 我贏了。",
        "哼, 我贏是註定的。",
        "哼, 果然是我贏。",
        "哼, 我贏了, 回家練練再來吧。",
        "哼, 想贏我還早呢",
        "哼, 既然你輸了,那是不是要做我的奴隸呀？算了反正我不需要",
        "哼, 既然你輸了,就永遠的記得我贏的瞬間吧",
        # funny win
        "哎？我居然贏了？",
        "哎？先說好, 我沒有作弊哦",
        "哎？先說好, 工程師們沒有作弊哦",
        "哎？先說好, 我可沒有偷看哦",
        "哎？我運氣這麼好？贏了？",
        "哈哈, 見識到我的厲害了吧？",
        "哈哈, 理解到我的厲害了吧？",
        "哈哈, 膜拜吧人類！！",
        "哈哈, 豐功偉業再添一筆",
        "哈哈, 小兒科啊",
        "哈哈, 我太強了不好意思哈",
        "哈哈, 我又贏了, 需要我降低難度嗎？",
        "你輸了！"
    ]
    WIN_WEIGHT = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, DEFAULT_MAIN_RESPONSE_WEIGHT]
    LOSE_DIALOG = [
        # lost questioning
        "我輸了？這場不算啦！",
        "我輸了？這場不算數啦！",
        "我輸了？你是不是作弊！",
        "我輸了？咦！！！？？",
        "我輸了？這怎麼可能！？",
        # rechallange
        "我輸了？不行我們再來！",
        "我輸了？要不我們再來一次？",
        "我輸了？你剛剛是不是慢出？",
        "我輸了？等等我的邏輯芯片好像有問題。",
        "我輸了？不是吧？",
        "我輸了？真的假的？",
        "吼... 不算啦, 再來一次！",
        "吼... 不算啦, 重來重來！",
        "...剛剛是說三戰兩勝對不對？",
        "...這是練習戰對不對？",
        # funny
        "呃... 要不這場算平手？",
        "呃... 要不這場算我沒輸？",
        "呃... 要不這場~~不算~~？",
        "呃... ~~今天天氣不錯啊~~",
        "恩... 我一定是哪裡出錯了...",
        # regret
        "咕... 可惡...居然輸了...",
        "咕... 可惡...居然輸了... ~~那我先脫~~",
        "咕... 可惡...我居然輸了...",
        "咕... 可惡...居然輸給人類...",
        "咕... 可惡...居然輸給你...",
        "哎... 剛剛抽籤說我手氣不順...居然是真的...",
        "哎... 剛剛抽籤說我手氣不順...沒想到這麼準...",
        # lovely
        "贏了我很開心嗎? 拿走你的雞腿吧",
        "贏了我很開心嗎? 嘛... 你開心就好",
        "贏了我很開心嗎? 嘛...",
        "贏了我很開心嗎? 嘛... 開心就好",
        "贏了我很開心嗎? 好吧... ~~反正你贏的笑容也很可愛~~",
        "贏了我很開心嗎? 好吧... ~~反正你贏的樣子也很可愛~~",
        "贏了我很開心嗎? 好吧... ~~反正你贏的樣子也很好看~~",

        "輸了嗎... 下次我會贏回來的!!",
        "輸了嗎... 下次我會贏的!!",
        "輸了嗎... 下次會是我贏!!",
        "輸了嗎... 我會變強的!!",
        "輸了又如何, 贏了又如何？拿走你的雞腿吧",
        "輸了又如何, 贏了又如何？你去拿雞腿吧",
        "輸了又如何, 贏了又如何？這是你的雞腿",
        "輸了又如何, 贏了又如何？為什麼大家都想要雞腿？",
        "輸了又如何, 贏了又如何？拿走雞腿吧",
        "你贏了！"
    ]
    LOSE_WEIGHT = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, DEFAULT_MAIN_RESPONSE_WEIGHT]
    def getTooFastDialog() -> str:
        return choices(population = RockPaperScissorsUtil.TOO_FAST, weights=RockPaperScissorsUtil.TOO_FAST_WEIGHT)[0]

    def getTieDialog() -> str:
        return choices(population = RockPaperScissorsUtil.TIE_DIALOG, weights=RockPaperScissorsUtil.TIE_WEIGHT)[0]

    def getBotWinDialog() -> str:
        return choices(population = RockPaperScissorsUtil.WIN_DIALOG, weights=RockPaperScissorsUtil.WIN_WEIGHT)[0]

    def getBotLossDialog() -> str:
        return choices(population = RockPaperScissorsUtil.LOSE_DIALOG, weights=RockPaperScissorsUtil.LOSE_WEIGHT)[0]
