class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ''
        for i in s:
            if i == ' ':
                res += '%20'
            else:
                res += i
        return res


双指针移动+计数

这个方法的思路是:
首先遍历一次字符串s来统计有多少个空格
假设有m个空格,我们需要填充的%20占用三个字符位置,所以需要额外开辟出2*m个空间
将开辟出的空间链接到原字符串的后面,新的字符串命名为s_new设置两个指针p1和p2,
初始时p1指向原字符串s的末尾,p2指向s_new的末尾
p1指针向前移动,当p1指向的字符不是空格时,将p1指向的字符复制到p2指向的位置,并都向前移动一位
当p1指向的字符是空格时,p1向前移动一格,这时应该插入%20,所以p2向前移动三格,并在这三格中插入%,2,0
时间复杂度O(n),空间复杂度O(n+2m)

代码
class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_len = len(s)
        space_count = 0
        for i in s:
            if i == ' ':
                space_count += 1
        s_len += 2 * space_count
        new_array = [' '] * s_len
        j = 0
        for i in range(len(s)):
            if s[i] == ' ':
                new_array[j] = '%'
                new_array[j+1] = '2'
                new_array[j+2] = '0'
                j += 3
            else:
                new_array[j] = s[i]
                j += 1
        return ''.join(new_array)
