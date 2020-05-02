# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
# 示例:
#
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# 说明：
#
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。

# 解法一
# 最通用的一种解法，对于每个字符串，比较它们的每个字符出现的个数是否相等，
# 相等的话就把它们放在一个 list 中去，作为一个类别。最外层写一个 for 循环然后一一比较就可以，还可以用一个等大的布尔型数组来记录当前字符串是否已经加入的了 list 。比较两个字符串的字符出现的次数可以用一个 HashMap，具体看代码吧。

# public List<List<String>> groupAnagrams(String[] strs) {
#     List<List<String>> ans = new ArrayList<>();
#     boolean[] used = new boolean[strs.length];
#     for (int i = 0; i < strs.length; i++) {
#         List<String> temp = null;
#         if (!used[i]) {
#             temp = new ArrayList<String>();
#             temp.add(strs[i]);
#             //两两比较判断字符串是否符合
#             for (int j = i + 1; j < strs.length; j++) {
#                 if (equals(strs[i], strs[j])) {
#                     used[j] = true;
#                     temp.add(strs[j]);
#                 }
#             }
#         }
#         if (temp != null) {
#             ans.add(temp);
#
#         }
#     }
#     return ans;
#
# }
#
# private boolean equals(String string1, String string2) {
#     Map<Character, Integer> hash = new HashMap<>();
#     //记录第一个字符串每个字符出现的次数，进行累加
#     for (int i = 0; i < string1.length(); i++) {
#         if (hash.containsKey(string1.charAt(i))) {
#             hash.put(string1.charAt(i), hash.get(string1.charAt(i)) + 1);
#         } else {
#             hash.put(string1.charAt(i), 1);
#         }
#     }
#      //记录第一个字符串每个字符出现的次数，将之前的每次减 1
#     for (int i = 0; i < string2.length(); i++) {
#         if (hash.containsKey(string2.charAt(i))) {
#             hash.put(string2.charAt(i), hash.get(string2.charAt(i)) - 1);
#         } else {
#             return false;
#         }
#     }
#     //判断每个字符的次数是不是 0 ，不是的话直接返回 false
#     Set<Character> set = hash.keySet();
#     for (char c : set) {
#         if (hash.get(c) != 0) {
#             return false;
#         }
#     }
#     return true;
# }
#
# #解法2
# public List<List<String>> groupAnagrams(String[] strs) {
#     HashMap<String, List<String>> hash = new HashMap<>();
#     for (int i = 0; i < strs.length; i++) {
#         char[] s_arr = strs[i].toCharArray();
#         //排序
#         Arrays.sort(s_arr);
#         //映射到 key
#         String key = String.valueOf(s_arr);
#         //添加到对应的类中
#         if (hash.containsKey(key)) {
#             hash.get(key).add(strs[i]);
#         } else {
#             List<String> temp = new ArrayList<String>();
#             temp.add(strs[i]);
#             hash.put(key, temp);
#         }
#
#     }
#     return new ArrayList<List<String>>(hash.values());
# }


from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dic = {}
        for s in strs:
            keys = "".join(sorted(s))
            if keys not in dic:
                dic[keys] = [s]
            else:
                dic[keys].append(s)
        return list(dic.values())
