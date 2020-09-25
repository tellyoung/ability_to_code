def restoreIpAddresses(s):
    def func(remain, choose):
        print(choose, remain)
        if len(choose) == 4 and not remain:
            res.append(choose.copy())
            return

        if not remain or len(choose) == 4:
            return

        if len(remain) >= 3 and len(choose) < 4 and int(remain[:3]) <= 255 and remain[0] != '0':
            choose.append(remain[:3])
            func(remain[3:], choose)
            choose.pop(-1)

        if len(remain) >= 2 and len(choose) < 4 and remain[0] != '0':
            choose.append(remain[:2])
            func(remain[2:], choose)
            choose.pop(-1)

        if len(remain) >= 1 and len(choose) < 4:
            choose.append(remain[:1])
            func(remain[1:], choose)
            choose.pop(-1)

    res = []
    func(s, [])
    print(res)
    return res

restoreIpAddresses("25525511135")