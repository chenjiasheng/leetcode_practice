# 专业级

## 题目一 生产线消耗电容速度

### 题目描述
电容对于终端来说是原材料当中的易耗品，现把仓库中的电容分成 N 份，第 i 份有 parts[i] 个电容。假如：

生产线要消耗完一份电容，才能开始消耗下一份；
生产线每分钟可消耗 K  个；如果某一份的电容数量小于 K 个，则生产线在这一分钟内消耗完这份电容后，剩余时间就会空闲，直到下一分钟开始消耗下一份。
距离下批电容上线前有 lengthTime 分钟，请计算在下批电容上线前，消耗完当前所有电容的最小速度 K（个/分钟，K 为整数）。

### 测试用例
+ 用例1
```txt
输入: parts = [3,6,7,11], lengthTime = 8
输出: 4
解释: 假如速度是 4 个/分钟的话：第 1 份 parts[0] 消耗 1 分钟，第 2 份 parts[1] 消耗 2 分钟，第 3 份 parts[2] 消耗 2 分钟，第 4 份 parts[3] 消耗 3 分钟，合计 8 分钟，符合要求。如果速度是 3 个/分钟的话，则需要 10 分钟，超过时间（8）要求；如果是 5 个/分钟的话，也是在 8 分钟内消耗完、满足时间要求，但是比 4 个/分钟速度快，不是最小速度。
```

+ 提示
```txt
1 <= parts.length <= 10^4
parts.length <= lengthTime <= 10^9
1 <= parts[i] <= 10^9
```

### 函数原型
> 【Java】
```txt
class Solution {
    public int minConsumingSpeed(int[] parts, int lengthTime) {
    }
}
```

> 【C++】
```c++

```

### 参考
[该题目已案例开放](http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=5962563)

# 专业级

## 题目一 高铁选座

### 题目描述
在某趟高铁列车上，每个车厢内共有 rows 行座位，每行/列座位的序号和分布如示例 1 的图示。
注："ABC DF"，"C" 与 "D" 间的空格表示车厢内的过道，列名仅由 "A"、"B"、"C"、"D"、"F"表示，并且都是大写。
列表 seats 中保存了此车厢已被购买的座位。若列表为空，表示该车厢内的座位还未被购买，且每个座位只能被购买一次。
根据 seats 显示的售卖情况，请问可以订到多少对（2 张）同一行相邻的座位（"C" 和 "D" 跨过道不相邻）。

### 测试用例
+ 用例1
```txt
输入：rows = 4, seats = ["3A","4F","3B"]
输出：6
解释：还剩 6 个双人座供 6 对旅客选择，下图为情况之一
```

+ 提示
```txt
注：此图仅展示一种选择情况，若第一排过道左侧选择 1B 和 1C（二四排同理）也是满足选择条件的。限制：
•       1 <= rows <= 10^9（非列车现实场景）
•       0 <= seats.length <= 10^5，座位编号类似 "999999A" 表示 999999 行 A 列。保证用例都是合法的数字和字母。
```

### 函数原型
> 【Java】
```txt
public class Solution1 {
    public int numSeats(int rows, String[] seats) {
        
    }
}
```

> 【C++】
```c++

```

### 参考
[该题目已案例开放](http://3ms.huawei.com/km/groups/3803117/blogs/details/9892189)

# 工作级
## 题目二 设计通讯录
### 题目描述 
请你设计一个简易通讯录系统，实现以下功能：
- Add(String name, String number)- 增加联系人：名字为 name，联系号码为 number，若已经存在不作处理；
- Update(String name, String number)- 更新联系人信息：若系统中已存在联系人 name，则将此联系人的联系号码更新为 number，并返回其更新前的联系号码；若系统中不存在此联系人，则不作处理并返回 "No such person"；
- Delete(String name)- 删除联系人：若系统中已存在联系人 name，则在系统中删除此联系人记录、并返回其联系号码；若系统中不存在此联系人，则返回 "No such person"；
- Prefix(String s)- 过滤联系人：把名字前缀为 s的联系人过滤出来（区分大小写），并把记录按照名字的字典序返回，形如 [["Abby","12321"],["Alice","1-22442"]...]。

1、用例保证：
•       name 中仅包含小写字母、大写字母与空格
•       number 中仅包含数字与 "-"

2、答题要求：系统中的联系人字母大小写敏感

### 示例

+ 示例1：
```txt
输入：
["PhoneSystem","add","add","update","prefix","delete","add","add","update","prefix"]
[[],["Herry","123"],["Merry","456"],["Merry","789"],["Me"],["Merry"],["Herry","234"],["Henry","2564"],["Merry","111"],["He"]]
输出：[null,null,null,"456",[["Merry","789"]],"789",null,null,"No such person",[["Henry","2564"],["Herry","123"]]]

解释：
PhoneSystem p = PhoneSystem()
p.Add("Herry","123")    // 在系统中添加姓名为 "Herry" 的联系方式 "123"
p.Add("Merry","456")    // 在系统中添加姓名为 "Merry" 的联系方式 "456"
p.Update("Merry","789") // 将系统中姓名为 "Merry" 的联系方式更新为 "789"，返回更新前的联系方式 "456"
p.Prefix("Me")          // 将系统中前缀为 "Me" 的联系人姓名及联系方式按联系人姓名的字典序返回 ["Merry","789"]
p.Delete("Merry")       // 删除系统中姓名为 "Merry" 的联系人及其联系方式，并返回其联系方式 "789"
p.Add("Herry","234")    // 系统中已存在姓名为 "Herry" 的联系方式，不作处理
p.Add("Henry","2564")   // 在系统中添加姓名为 "Henry" 的联系方式 "2564"
p.Update("Merry","111") // 系统中不存在姓名为 "Merry" 的联系人，返回 "No such person"
p.Prefix("He")          // 系统中前缀为 "He" 的联系人姓名及联系方式按联系人姓名的字典序返回 [["Henry","2564"],["Herry","123"]]
注：输出中的 null 表示此对应函数无输出（其中：C的构造函数有返回值，但是也是无需输出）

```
+ 提示
```txt
提示：
•      1 <= Add,Update,Prefix,Delete 所有操作数 <= 1000
•      1 <= name.length, number.length <= 20
•      字典序：指按照单词出现在字典的顺序进行排序的方法。先按照第一个字母以 a、b、c......z 的顺序排列，如果第一个字母一样，那么比较第二个、第三个乃至后面的字母。如果比到最后两个单词不一样长（比如 sigh 和 sight），那么把短者排在前。初始化及调用参考（以 C 为例，其他语言参考）：

/*
 * Your PhoneSystem struct will be instantiated and called as such:
 * PhoneSystem* obj = PhoneSystemCreate();
 * PhoneSystemAdd(obj, name, number);
 * char* param_2 = PhoneSystemUpdate(obj, name, number);
 * char* param_3 = PhoneSystemDelete(obj, name);
 * char*** param_4 = PhoneSystemPrefix(obj, s, retSize, retColSize);
 * PhoneSystemFree(obj);
*/

 答题要求：结果可信和过程可信同样重要，您编写的代码需要符合可信的要求（包括通用编码规范、安全编码规范和圈复杂度）。
```
### 函数原型

> 【Java】
```java
    PhoneSystem() {
    }

    public void add(String name, String number) {
    }

    public String update(String name, String number) {
    }

    public String delete(String name) {
    }

    public List<List<String>> prefix(String s) {
    }
```

> 【C++】

```c++
class PhoneSystem {
public:
    PhoneSystem() {}
  
    void Add(string name, string number)
    {
    }
  
    string Update(string name, string number)
    {
    }
  
    string Delete(string name)
    {
    }
  
    vector<vector<string>> Prefix(string s)
    {
    }
};
```

### 参考
[该题目已案例开放](http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=4796311&pid=50665291#p50665291)

# 专业级

## 题目一 电话号码转换

### 题目描述
某语音翻译软件，需要实现如下中英文电话号码转换功能：
若输入的是英文数字单词或Double组成的电话号码，则输出对应的中文数字单词；
若输入为中文数字单词组成的电话号码，则输出对应的英文数字单词。
若输入不合法，则输出字符串ERROR。
中文数字、英文数字分别见下表：
中文数字单词：Yi Er San Si Wu Liu Qi Ba Jiu Ling
英文数字单词：One Two Three Four Five Six Seven Eight Nine Zero

说明：
输入若存在Double，其后必须跟随英文数字单词，代表两个该数字。如输入DoubleSix，代表 SixSix；
输入保证要么全中文，要么全英文（含Double），并且每个单词都是合法的英文数字单词/中文数字单词/Double；
输入不合法的场景，仅为Double后跟随的不是英文数字单词。如DoubleLiu 非法。
解答要求时间限制：1000ms, 内存限制：256MB

输入
一行仅由大小写字母组成的字符串，非空且长度不大于500

输出
一个字符串，表示转换后的电话号码；若输入不合法，输出ERROR。
### 测试用例
+ 用例1
```txt
输入样例 1 
SixOneThreeOneDoubleZero

输出样例 1
LiuYiSanYiLingLing
```
+ 用例2
```txt
输入样例 2 
YiLingSanSanJiu

输出样例 2
OneZeroThreeThreeNine
```
+ 用例3
```txt
输入样例 3 
DoubleLiu

输出样例 3
ERROR
```

### 函数原型
> 【Java】
```java
public class Solution {
    public String translate(String input) {
    }
}
```

> 【C++】

```c++
class Solution {
public:
    // 待实现函数，在此函数中填入答题代码
    string Translate(const string &input)
    {
    }
};
```

### 参考
[该题目已案例开放](http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=4849555)


# 专业级

## 题目一 招标系统

### 题目描述
请你设计一个招标系统，需要实现以下几个功能：
AddTender(int userId, int projectId, int price) - 将投标方 userId 对项目 projectId 的投标金额 price 录入系统；若系统中已存在 userId 对项目 projectId 的投标金额，则不作处理。
UpdateTender(int userId, int projectId, int price) - 若系统中存在投标方 userId 对项目 projectId 的投标金额，则将该金额更新为 price，并返回更新前的投标金额；否则请返回 -1。
RemoveTender(int userId, int projectId) - 若系统中存在投标方 userId 对项目 projectId 的投标金额，删除该投标记录，返回被删除的投标金额；否则返回 -1
QueryTender(int projectId, int price) - 查询并返回系统中项目 projectId 的投标记录中，投标金额大于 price 且最接近 price 的投标方 userId；
若有多个投标方投标金额相同，比较投标方最后一次投标时间，返回投标时间最早的投标方 userId；（AddTender 和 UpdateTender 都是投标）
若不存在符合要求的投标记录，请返回 -1；

### 测试用例
+ 用例1
```txt
输入：
["TenderSystem","addTender","addTender","addTender","updateTender","updateTender","removeTender","removeTender","addTender","addTender","addTender","queryTender","queryTender"]
[[],[1,1,10],[2,2,20],[2,2,30],[1,1,40],[1,3,40],[1,1],[1,3],[1,2,20],[3,2,10],[4,2,40],[2,15],[5,10]]

输出：[null,null,null,null,10,-1,40,-1,null,null,null,2,-1]
```
+ 用例2
```txt
输入：["TenderSystem","addTender","addTender","updateTender","queryTender"]
[[],[1,1,10],[2,1,20],[1,1,20],[1,10]]

输出：[null,null,null,10,2]

解释：
TenderSystem t = TenderSystem()
t.AddTender(1,1,10) // 在系统中添加 userId 为 1，projectId 为 1 的投标金额 10
t.AddTender(2,1,20) // 在系统中添加 userId 为 2，projectId 为 1 的投标金额 20
t.UpdateTender(1,1,20) // 在系统中将 userId 为 1，projectId 为 1 的投标金额更新为 20，并返回更新前的金额 10
t.QueryTender(1,10) // 查询系统中 projectId 为 1，投标金额大于 10 且最接近 10 的 userId，1 与 2 均符合条件，由于 userId 1 更新时间晚（虽然 userId 1先做了首次投标，但是取其最后一次更新投标的时间来进行比较），因此返回最早录入系统的 userId 2
```
+ 提示
```txt
提示：
1 <= userId <= 10^4
1 <= projectId <= 10^6
1 <= price <= 10^8
addTender、updateTender、removeTender、queryTender 累计操作数 <= 1000
```
### 函数原型
> 【Java】
```java
class TenderSystem {
    public TenderSystem() {

    }

    public void addTender(int userId, int projectId, int price) {
    }

    public int updateTender(int userId, int projectId, int price) {
    }

    public int removeTender(int userId, int projectId) {
    }

    public int queryTender(int projectId, int price) {
    }
}
```

> 【C++】

```c++
class TenderSystem {
public:
    TenderSystem() {
    }

    void AddTender(int userId, int projectId, int price)
    {
    }

    int UpdateTender(int userId, int projectId, int price)
    {
    }

    int RemoveTender(int userId, int projectId)
    {
    }

    int QueryTender(int projectId, int price)
    {
    }
};
```

### 参考
[该题目已案例开放](http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=4962327)


# 专业级

## 题目二 自动售货系统

### 题目描述
模拟实现一个简单的自动售货系统。
商品名称和价格如下：
设定单次购买流程为：先把投币存入系统的存钱盒内，系统再进行后续处理：
如果可以购买成功，则提供一个所购买商品，同时按钱币找零总张数最少的原则进行找零。
如果因为投币不足、商品数量不足、存钱盒内钱币不足，导致购物失败，则退回所投入的钱币。
注：1）存钱盒里面的钱币只有四种面额：1元，2元，5元，10元。2）一次购买只能买一个该商品。
现给定系统初始信息及系列购买行为，请输出最后一次购买商品的结果（成功或失败），以及找零或退币的数量组合。

解答要求时间限制：1000ms, 内存限制：64MB

输入
第一行是系统初始化商品的数量，格式为：A1数量-A2数量-A3数量-A4数量-A5数量-A6数量
第二行是存钱盒里面钱币的数量，格式为：1元张数-2元张数-5元张数-10元张数
第三行是整数 N ，表示有N次购买操作，取值范围 [1,5]
接下来 N 行是按照先后顺序购买商品的系列操作，格式为：商品名称 1元张数-2元张数-5元张数-10元张数，表示要购买的商品以及投入的钱币。

输出
最后一次购买商品的结果，以及找零或退币的数量组合，格式为：购买结果 1元张数-2元张数-5元张数-10元张数

购买结果: 成功为T，失败为F
购买结果、找零或退币的数量之间使用单空格分隔，各钱币数量之间使用-分割

### 测试用例
+ 用例1
```txt
输入样例 1
0-5-4-3-2-1
0-5-2-0
1
A1 0-1-0-0

输出样例 1
F 0-1-0-0
```
+ 用例2
```txt
输入样例 2
6-5-4-3-2-1
0-5-2-0
3
A1 0-0-0-1
A1 0-0-0-1
A2 0-0-0-2

输出样例 2
T 0-1-1-1
```

+ 提示
```txt
提示
样例1解释：投入2元购买A1商品，但A1商品不足，购买失败，退回投入的钱。
样例2解释：
第一次购买成功后，售货机中的钱分别为 0-1-2-1 （1个2元，2个5元，1个10元）
第二次购买，没法找零8元，购买失败，退回投入的钱。
第三次购买：投入20元购买A2（价格3元），购买成功，找回17元。
```

### 函数原型
> 【Java】
```java
public class Solution {
    // 待实现函数，在此函数中填入答题代码
   private String purchaseResult(Map<String, Product> goods, Money moneyBox, BuyItem[] buyItems) {
    }
    /**
     * main入口由OJ平台调用
     */
    public static void main(String[] args) {
        Scanner cin = new Scanner(System.in, StandardCharsets.UTF_8.name());
        String goodsNum = cin.nextLine();
        String moneys = cin.nextLine();
        int count = Integer.parseInt(cin.nextLine());
        BuyItem[] buyItems = new BuyItem[count];
        for (int i = 0; i < count; i++) {
            BuyItem buyItem = new BuyItem(cin.nextLine());
            buyItems[i] = buyItem;
        }
        Product product = new Product();
        Money moneyBox = new Money(moneys);
        Map<String, Product> goods = product.initProduct(goodsNum);
        cin.close();
        System.out.println(purchaseResult(goods, moneyBox, buyItems));
   	 }
    /**
     * 商品
     *
     * @since 2020-08-28
     */
    static class Product {
        int price = -1;

        int nums = -1;

        Product() {
        }

        Product(int price, int nums) {
            this.price = price;
            this.nums = nums;
        }

        private Map<String, Product> initProduct(String input) {
            Map<String, Product> maps = new HashMap<>();
            String[] strs = input.split("-");
            int[] temp = Arrays.stream(strs).mapToInt(Integer::parseInt).toArray();
            maps.put("A1", new Product(2, temp[0]));
            maps.put("A2", new Product(3, temp[1]));
            maps.put("A3", new Product(4, temp[2]));
            maps.put("A4", new Product(5, temp[3]));
            maps.put("A5", new Product(8, temp[4]));
            maps.put("A6", new Product(6, temp[5]));
            return maps;
        }
    }

    /**
     * 钱数
     *
     * @since 2020-08-28
     */
    static class Money {
        int[] money = null;

        Money() {
            this.money = new int[4];
        }

        Money(String input) {
            String[] strs = input.split("-");
            this.money = Arrays.stream(strs).mapToInt(Integer::parseInt).toArray();
        }
    }

    /**
     * 购买商品数据
     *
     * @since 2020-08-28
     */
    static class BuyItem {
        Money money;

        String goodsName = null;

        String moneyString;

        BuyItem(String input) {
            this.goodsName = input.split(" ")[0];
            this.money = new Money(input.split(" ")[1]);
            this.moneyString = input.split(" ")[1];
        }
    }
}
```

> 【C++】
```c++
class Solution {
public:
    // 待实现函数，在此函数中填入答题代码
    pair<bool, vector<int>> PurchaseResult(const vector<int>& goods, const vector<int>& coins,
        vector<pair<string, vector<int>>> &buyItems)
    {
    }
};
```

### 参考
[该题目已案例开放](http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=4970555)
[该题目已案例开放](http://3ms.huawei.com/km/groups/3803117/blogs/details/8891395)


# 专业级

## 题目一 速记内容复原
### 题目描述 
有一种速记方式，针对重复内容有一套独特的缩写规则：

重复的部分会被以 "(重复内容)<重复次数>" 形式记录，并且可能存在嵌套缩写关系。不重复的部分按照原样记录。
现给一个符合此速记方式的字符串 records，请以字符串形式返回复原后的内容。
注： records 仅由小写字母、数字及<, >, (, )组成。
### 示例
+ 用例1
```txt
示例 1：
输入：records = "abc(d)<2>e"
输出："abcdde"
解释：字符串中出现 "(d)<2>"，表示 "d" 重复出现 2 次，因此返回复原后的内容 "abcdde"。

```
+ 用例2
```txt
输入：records = "a(b(c)<3>d)<2>e"
输出："abcccdbcccde"
解释：字符串中出现 "a(b(c)<3>d)<2>"，其中 "(c)<3>" 表示 "c" 出现 3 次，复原为 "ccc"；"(bcccd)<2>" 表示 "bcccd" 重复出现 2 次，复原为 "bcccdbcccd"。最终返回复原后内容 "abcccdbcccde"
```

+ 提示
```txt
1 <= records.length <= 200
2 <= 重复次数 <= 10
题目保证返回结果字符串长度小于等于 10^4
输入保证合法，确保括号与尖括号成对出现
嵌套深度不超过 13
```

### 函数原型

【Java】
```txt
class Solution {
    public String unzipString(String records) {
        
    }
}
```

【C++】
```txt
class Solution {
public:
    string UnzipString(string records)
    {
    }
}
``` 
[该题目已案例开放](http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=4999053)


## 题目二 道路植树

### 题目描述
云服务平台新上线一个绿化规划服务，园林部门用其帮助规划种树任务：在某个笔直的路段栽种 num 棵树。
假定该路段规划设计图上的坐标自 0 开始，二维数组 areas 按照坐标升序以 [起点坐标，终点坐标] 记录了规划绿化区间，且区间互不相交。树木只能栽种在绿化区间内，且在不同的整数坐标位置上。

尽量稀疏种植，每种种植方案中相邻两棵树的间距最小的记为 minDistance，其中 minDistance 最大的则为最佳种植方案，请返回 minDisatance 最大可能是多少。若无法在 areas 给出的规划绿化区间内完成种树任务，请返回 -1。

### 测试用例
+ 用例1
```txt
输入：num = 5, areas = [[1,3],[5,6],[8,9],[10,11]]
输出：2
解释：起点坐标为 0，终点坐标为 11（最后一个区间的终点坐标），合计 12 个坐标点。最佳种植方案有：[1,3,5,8,10],[1,3,5,8,11],[1,3,5,9,11],[1,3,6,8,10],[1,3,6,8,11],[1,3,6,9,11]，最小间距的最大值为 2。
```

+ 提示
```txt
限制：
1 <= areas.length <= 1000
2 <= num <= 1000
0 <= areas[i][0] <= areas[i][1] <= 10^7
```

### 函数原型
> 【Java】
```txt
public class Solution2 {
    public int distanceBetweenTree(int num, int[][] areas) {

    }
}
```

> 【C++】
```c++
class Solution {
public:
    int DistanceBetweenTree(int num, const vector>& areas)
    {
    }
};
```

### 参考
[该题目已案例开放](http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=5962563)

# 专业级 删除整个目录

## 题目一 名称

### 题目描述
我们定义一种目录结构字符串(类似Windows的tree/f的输出内容)，用它来表达目录树的结构，如图所示：
A                                     
|-B                           
|-|-C                          
|-|-D                          
|-|-E                          
|-|-|-F                          
|-lib32    
目录结构字符串的输入仅含数字、字母和|-，其中：|- 表示子目录的层次符号；字母或数字表示目录名。
某目录的子目录的顺序以输入先后顺序为准。
某目录的多个子目录不能同名，如果出现多个，则只保留第一个，后续的输入忽略。
无对应的父目录，属于异常情况，直接忽略。          
给定一个目录结构字符串，请按先后顺序删除所有目录，并依次输出删除的目录名称：

如果是叶子目录，直接删除。
如果某目录含有子目录，则需要先删除其子目录。
如上图所示的输出为C D F E B lib32 A

解答要求时间限制：1000ms, 内存限制：64MB  

输入
首行是一个整数 n，表示目录结构字符串的行数，取值范围 [1, 50)
接下来n行，每行字符串表示一个待处理的目录，目录名长度为[1,10]，整行字符串长度为 [1,100]。
用例保证，有且仅有一个根目录。

输出
字符串序列，表示依次删除的目录，目录之间以单空格分隔。          
### 测试用例
+ 用例1
```txt
输入样例 1 
10
|-B
A
|-B
|-|-C
|-|-D
|-|-D
|-|-|-|-D
|-|-E
|-|-|-F
|-lib32

输出样例 1
C D F E B lib32 A
```

+ 提示
```txt
样例1解释：
|-B     //非顶层目录，并且它前面无对应的父目录，该行输入被忽略
A     //A为顶层目录
|-B     //B为第二层，它所跟随的上一层目录为A，因此B为A的子目录
|-|-C     //C为第三层，它紧跟的上一层目录为B，因此其父目录为B。
|-|-D     //D为第三层，它紧跟的上一层目录为B，因此其父目录为B，它和C为兄弟关系。
|-|-D     //D为第三层，与先输入的第三层目录D同名，该行输入被忽略。
|-|-|-|-D   //D为第五层，前面没有第四层目录，因此无对应的父目录，该行输入被忽略。
|-|-E      //E为第三层，它紧跟的上一层目录为B，因此其父目录为B，它和C、D为兄弟关系。
|-|-|-F      //它紧跟的上一层目录为E，因此其父目录为E。
|-lib32     //它紧跟的上一层目录为A，因此其父目录为A。
按先后顺序删除时：A有子目录B、lib32，先删除B时，其子目录C、D、E需要被先删除，C、D无子目录直接被删除，E有子目录F则先删除F。以此类推，最终输出为 C D F E B lib32 A
```

### 函数原型
> 【Java】
```txt
public class Solution {
    private static String delAllDirectorys(String[] dirTreeLines) {
    }
	private static void traverseTree(Deque<Node> nodeStack, List<String> queue) {
    }
}
```

> 【C++】

```c++
class TenderSystem {
public:
    int GetLevelName(string &line, string &name)
    {
    }
    
    void InsertNode(Node *root, int level, string &name)
    {
    }
    
    void Traverse(Node *root)
    {
    }
};
```

### 参考
[该题目已案例开放](http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=5034005#)


# 专业级

## 题目一 路由表最长匹配

### 题目描述
路由表最长匹配是IP(v4) 路由器的最基本的功能之一：当路由器收到一个IP数据包时，会将数据包的目的IP地址与本地路由表进行匹配：

格式：目的IP地址为dstIP，路由表中每条路由为entryIP/掩码长度m，如 10.166.50.0/23。 注：所有IP地址以点分十进制字符串表示。
匹配规则：
如果 entryIP 和 dstIP 的二进制表示的前 m 个bit相同，则说明该条路由是匹配的。注：10.166.50.0的二进制表示如下：
0.0.0.0/0是默认路由，它与任何目的IP地址都是匹配的，m 值为 0 。
所有匹配的路由中，m 最大的即为“最长匹配”。
现给出目的IP地址和本地路由表，请输出最长匹配的路由；如果有多条，则按给出的先后顺序输出最先的；如果没有匹配的，输出字符串empty。

解答要求时间限制：1000ms, 内存限制：64MB

输入
第一行是目的IP地址，点分十进制表示的字符串。
第二行一个整数 n，表示路由表中的路由数量，取值范围为 [1, 10000]。
接下来 n 行表示 n 条路由，其中掩码长度 m 的取值范围为[0, 32]，m 值为 0 仅存在于路由 0.0.0.0/0 。

输出
最长匹配的路由，格式同输入；如果没有则输出字符串empty。
### 测试用例
+ 用例1
```txt
输入样例1 
192.168.0.3
6
10.166.50.0/23
192.0.0.0/8
10.255.255.255/32
192.168.0.1/24
127.0.0.0/8
192.168.0.0/24

输出样例 1
192.168.0.1/24
```

+ 提示
```txt
提示
样例1解释：如下图所示，先按匹配的长度，再按输入先后顺序，结果为192.168.0.1/24

```

### 函数原型
> 【Java】
```txt
public class Solution {
    private String routerSearch(String dstIp, String[][] ipTable) {
    }
}
```

> 【C++】
```c++
class Solution {
public:
    // 待实现函数，在此函数中填入答题代码;
    string RouterSearch(const string &dstIp, const vector<string> &ipTable)
    {
    }
};

```

### 参考
[该题目已案例开放](http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=5050307#)

# 专业级

## 题目一 备忘录设计系统

### 题目描述
请设计一个备忘录系统，要求有以下功能：

addEvent(int startDate, String content, int num, int period) – 自日期 startDate 开始（startDate 包含在内），添加 num 个以 period 为间隔周期待办事项 content。例如若命令为 addEvent(0,"a",4,2)，表示于日期 0，2，4，6 分别添加待办事项 "a"。
返回本次操作共计新增待办事项的数量。若部分日期上已存在该事项，无论该事项是否设置为已完成，这些日期不需添加该事项。

finishEvent(int date, String content) – 将日期 date 上的 content 事项设置为已完成。
若该日期上不存在此事项，或该日期上此事项已完成，返回 false；
若设置操作完成，则返回 true。

removeEvent(int date, String content) – 移除日期 date 上的 content 事项。
若该日期上不存在此事项，返回 false；
若移除操作完成，则返回 true。

queryTodo(int startDate, int endDate) – 查询从 startDate 到 endDate（起止日期均包含在内）这段日期内所有的未完成的 content 事项，并将查询到的事项以字符串形式按日期升序记于数组后返回，若查询到相同日期的多条待办事项，则将其按字典序排列。
### 测试用例
+ 用例1
```txt
输入：["MemoSystem","addEvent","queryTodo","finishEvent","removeEvent"]
[[],[2,"eat a burger",2,3],[0,5],[2,"eat a burger"],[2,"eat a burger"]]
输出：[null,2,["eat a burger","eat a burger"],true,true]

解释：
MemoSystem ms = MemoSystem();
ms.addEvent(2,"eat a burger",2,3); // 自日期 2 开始，添加 2 个间隔周期为 3 的待办事项 "eat a burger"，即在日期 2、5 添加该待办事项。本次操作共新添加了 2 个待办事项，返回 2
ms.queryTodo(0,5); //查询自日期 0 至日期 5 的所有未完成的事项，返回数组 ["eat a burger","eat a burger"]
ms.finishEvent(2,"eat a burger"); // 将系统中日期为 2 的待办事项 "eat a burger" 设置为已完成，返回 true
ms.removeEvent(2,"eat a burger"); // 移除系统中日期为 2 的事项 "eat a burger"，返回 true
注：输出中的 null 表示此对应函数无输出（其中：C 的构造函数有返回值，但是也是无需输出）
```

+ 用例2
```txt
输入：
["MemoSystem","addEvent","addEvent","removeEvent","finishEvent","addEvent","addEvent","queryTodo","queryTodo","finishEvent","addEvent"]
[[],[2,"save files",1,1],[2,"eat a burger",1,1],[2,"drink water"],[1,"drink water"],[0,"eat a burger",5,2],[2,"save files",1,1],[0,4],[10,11],[2,"eat a burger"],[2,"eat a burger",1,1]]
输出：[null,1,1,false,false,4,0,["eat a burger","eat a burger","save files","eat a burger"],[],true,0]

解释：
MemoSystem ms = MemoSystem();
第 3 个命令 ms.addEvent(2,"eat a burger",1,1); // 同一个日期可以增加不同的待办事项，本次操作共新添加了 1 个待办事项，返回 1
第 6 个命令 ms.addEvent(0,"eat a burger",5,2); // 自日期 0 开始，添加 5 个间隔周期为 2 的待办事项 "eat a burger"，即在日期 0，2，4，6，8 添加该待办事项。由于日期 2 的记录中已存在该事项，因此本次操作共新添加了 4 个待办事项，返回 4
第 8 个命令 ms.queryTodo(0,4); // 查询自日期 0 至日期 4 的所有未完成的事项，按日期返回，其中日期 2 的待办事项需按字典序排列，返回数组 ["eat a burger","eat a burger","save files","eat a burger"]
第 9 个命令 ms.queryTodo(10,11); // 查询自日期 10 至日期 11 的所有未完成的事项，返回空数组 []

注：输出中的 null 表示此对应函数无输出（其中：C 的构造函数有返回值，但是也是无需输出）
```

+ 提示
```txt
1 <= addEvent,finishEvent,removeEvent,queryTodo 总操作数 <= 1000
0 <= startDate <= endDate <= 1000
0 < num, period, 0 <= startDate + (num - 1) * period <= 1000
1 <= content.length <= 20 ，仅包含小写字母、大写字母与空格
0 <= date <= 1000
queryTodo 函数对于 Java/Js/Python/Go 语言，如果返回的记录为空，则返回空数组
```

### 函数原型
> 【Java】
```java
public class MemoSystem {
    public MemoSystem() {
        
    }
    
    public int addEvent(int startDate, String content, int num, int period) {
        
    }
    
    public boolean finishEvent(int date, String content) {
        
    }
    
    public boolean removeEvent(int date, String content) {
        
    }
    
    public String[] queryTodo(int startDate, int endDate) {
        
    }
}
```

> 【C++】
```c++
class MemoSystem {
public:
    MemoSystem() {}

    int AddEvent(int startDate, string content, int num, int period)
    {
    }

    bool FinishEvent(int date, string content)
    {
    }

    bool RemoveEvent(int date, string content)
    {
    }

    vector<string> QueryTodo(int startDate, int endDate)
    {
    }
};
```

### 参考
[该题目已案例开放](http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=5093713)

# 专业级

## 题目一 服务器组的均匀拆分

### 题目描述
某客户的核心网服务器组成了一个pool，假定使用一个二叉树表示pool里面的服务器，每个结点的值表示对应服务器的处理能力。
由于业务发展，需要将该pool拆分成两个处理能力相等的pool。即去掉树上的一条边，将其均匀拆成两棵子树（两子树的结点值之和相等）。

现给出数组A表示的二叉树结构，如果该二叉树可以均匀拆分，请找到拆分出的新子树的根结点，输出该节点在数组A中的下标（用例保证结果的唯一性）；如果不能均匀拆分，输出 -1。

输入
第一行：一个整数 N，表示数组 A 的长度，取值范围 [1, 10000]。
第二行：一个长度为 N 的整数数组 A，表示二叉树的结构，以一种层序方式给出各节点的值：
首个值是根节点的值。
-1表示空节点，不是树上的有效节点，且它的子节点不再给出。
数组元素的取值范围 [0, 10^9]。

输出
一个整数，表示新子树的根结点在数组A的下标；或者 -1 。
### 测试用例
+ 用例1
```txt
输入样例 1
7
9 13 12 -1 -1 2 8

输出样例 1
2
```
+ 用例2
```txt
输入样例 2
10
7 8 10 4 -1 -1 3 1 -1 2

输出样例 2
-1
```

+ 提示
```txt
样例1：
9 13 12 -1 -1 2 8
表示如下的二叉树结构：9是根节点；第二层分别为13和12；第三层为-1 -1 2 8，其中-1 和 -1表示节点 13 无子节点，2 和 8 是节点 12 的左右子节点。
    9
   / \
 13  12
     / \
    2   8
可拆为：
    9             
   /
  13    
 和
     12
     / \
    2   8
新子树的根结点在数组A中的下标为2。

样例2：
7 8 10 4 -1 -1 3 1 -1 2
表示如下的二叉树状结构：节点8的右子节点是空节点，该空节点的子节点不用在数组中给出；节点10的左子节点是空节点，该空节点的子节点也未在数组中给出。
      7
     / \
    8  10
   /     \
  4       3
 /       /
1       2
原树无法按要求拆分，直接输出-1。
```

### 函数原型
> 【Java】
```txt
public class Solution {
    // 待实现函数，在此函数中填入答题代码
    private static int splitEqualTree(int[] tree) {
    }
}
```

> 【C++】
```c++
class Solution {
public:
    // 待实现函数，在此函数中填入答题代码
    int SplitEqualTreeAndOutputNewRoot(const vector<int>& tree)
    {
    }
};
```

### 参考
[该题目已案例开放](http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=5126557)


# 专业级

## 题目一 任务规划

### 题目描述
任务列表 tasks 中有 N 个任务，任务编号 Ni​ 的值范围为 [0, N-1]。

由于存在资源竞争，某些任务间存在两两互斥关系，并记录在二维数组 mutexPairs 中，该二维数组元素为 [Ni​, Nj​]，其中 Ni​，Nj​ 为互斥的两个任务编号。

现在需要对任务列表 tasks 进行切割分组。要求：

存在互斥关系的任务不能分在同一组
单个任务也可以单独一组
一个任务可能和多个任务互斥
请判断 最少 可以将任务列表 tasks 切割 成几组？（即：切割后的小组是原列表的 连续子数组）
### 测试用例
+ 用例1
```txt
输入：tasks = [1,4,2,3,0], mutexPairs = []
输出：1

解释：无互斥关系，所有任务可分在同一组。
```

+ 用例2
```txt
输入：tasks = [1,3,2,4,6,5,0], mutexPairs = [[1,3],[4,5]]
输出：3

解释：任务1，3 不能被分在同一组；4，5 不能被分在同一组，所以最终只能将任务列表分成3组。例如，[1],[3,2,4,6],[5,0] 为其中一种分法；[1],[3,2,4],[6,5,0] 为另一种分法。
注意：切割后的小组是原列表的连续子数组。
```

+ 用例3
```txt
输入：tasks = [0,1,2,3,4,5], mutexPairs = [[1,3],[3,5]]
输出：3

解释：最少分成 3 组。例如，[0,1,2],[3,4],[5] 为其中一种分法。
```

+ 提示
```txt
1 <= tasks.length <= 10^5
0 <= mutexPairs.length <= 1000 且 mutexPairs[i].length == 2
0 <= mutexPairs[i][0] < mutexPairs[i][1] < tasks.length
```

### 函数原型
> 【Java】
```txt
public class Solution {
    public int divideGroup(int[] tasks, int[][] mutexPairs) {
    }
}
```

> 【C++】
```c++
class Solution {
public:
    int DivideGroup(const vector<int>& tasks, const vector<vector<int>>& mutexPairs) {
    }
};
```

### 参考
[该题目已案例开放](http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=5170675)


# 专业级

## 题目二 结果对比
### 题目描述
终端某产品的车间工人位置分布视作一个矩阵，记为二维数组 scores，scores[row][col] 代表此位置工人的 11 月的完成件数。
每位工人都想计算同行同列中一共有多少人比自己完成的件数多，最后把计算结果记录在一个新的二维数组的对应位置上，并返回该二维数组。

### 示例

**示例1：**
```txt
输入：scores = [[10,20],[30,10]]
输出：[[2,0],[0,2]]
解释：
与 scores[0][0] 同行的元素中 scores[0][1] 比它大，与 scores[0][0] 同列的元素中 scores[1][0]比它大，同行同列合计2个人；
与 scores[0][1] 同行同列的两个元素都不比它大；
与 scores[1][0] 同行同列的两个元素都不比它大；
与 scores[1][1] 同行同列的两个元素都比它大。
注：返回的数组和 scores 的行、列数相等。

```
**示例2：**
```txt
输入：scores = [[10,20,30],[30,15,10]]
输出：[[3,1,0],[0,2,3]]
解释：
与 scores[0][0] 同行同列的三个元素都比它大；
与 scores[0][1] 同行同列的三个元素中 score[0][2] 比它大；
与 scores[0][2] 同行同列的三个元素都不比它大；
与 scores[1][0] 同行同列的三个元素都不比它大；
与 scores[1][1] 同行同列的三个元素中 score[1][0]、score[0][1] 比它大；
与 scores[1][2] 同行同列的三个元素都比它大；
```
提示：
1 <= scores.length, scores[row].length <= 500
0 <= scores[row][col] <= 10^4

请注意，该题有性能要求，暴力解法的用例通过率不高
### 函数原型

【Java】
```java
class Solution {
    public int[][] cmpScores(int[][] scores) {
        
    }
}
```

【C++】
```txt
class Solution {
public:
    vector<vector<int>> CmpScores(const vector<vector<int>> &scores)
    {
    }
}
``` 
[该题目已案例开放](http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=5180955#)


# 专业级

## 题目一 数字字符串插入

### 题目描述
已知有一个数字字符串 score，现再给你一个数字字符串 digit ，你可将 digit 整体插入到 score 的任意位置（含开头和结尾），形成一个新的数字字符串。
请问所有形成的新数字字符串中能表示的最大数值是多少？并返回这个字符串。

约束：
score 仅含数字字符 0-9，其表示的数值大于 0，并且无前缀0；
digit 仅含数字字符 0-9，其表示的数值大于等于 0，可以有前缀0，如 "099"。
### 测试用例
+ 用例1
```txt
输入：
score = "523"
digit = "4"

输出: "5423"

解释：4523、5423、5243、5234 为所有插入后的数值，其中 5423 为最大数值。
```

+ 用例2
```txt
输入:
score = "6121"
digit = "0"

输出: "61210"

解释：06121、60121、61021、61201、61210 为所有插入后的数值，其中 61210 为最大数值。
```

+ 用例3
```txt
输入：
score = "735"
digit = "76"

输出："77635"

解释：76735、77635、73765、73576 为所有插入后的数值，其中 77635 为最大数值。
```

+ 提示
```txt
1 <= score.length <= 10^6
1 <= digit.length <= 20
```

### 函数原型
> 【Java】
```txt
class Solution {
    public String insertDigit(String score, String digit) {
    }
};
```

> 【C++】
```c++
lass Solution {
public:
    string InsertDigit(string score, string digit)
    {
    }
};
```

### 参考
[该题目已案例开放](http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=5270171)


# 专业级

## 题目一

### 题目描述
某系统中有一空间连续的内存，被划分成多个大小相同的内存块。内存的使用状态记录在字符串 memory 中，每个内存块的状态用字符 x 或 . 表示，其中：

. 表示该内存块空闲；
x 表示该内存块被使用，x 为小写字母。
现在可释放其中 最多 cnt 个内存块（即字符串中的 x 变成 .），以获得一块空间连续的、且 最长的 空闲内存，请计算并返回该最长空闲内存的内存块数量。

### 测试用例
```txt
示例 1：
输入：
memory = "..x..x..xx..."
cnt = 2

输出：8

解释：
..x..x..xx...
|---8---|
将 memory[2] 与 memory[5] 的内存块释放，可获得从 memory[0] 到 memory[7]、长度为 8 的连续空闲内存；
将 memory[5] 与 memory[8] 的内存块释放，可获得从 memory[3] 到 memory[8]、长度为 6 的连续空闲内存；
将 memory[8] 与 memory[9] 的内存块释放，可获得从 memory[6] 到 memory[12]、长度为 7 的连续空闲内存；
其他释放方式获得的连续空闲内存都小于 8；
因此返回 8。
```

```txt
示例 2：

输入：
memory = "....x."
cnt = 3
输出：6

示例 3：

输入：
memory = "xx.x..xx....x..."
cnt = 0

输出：4

提示：0 <= cnt <= memory.length <= 10^5
```

### 函数原型

【Java】

```java
class Solution {
    public int getMaxFreeMemoryLen(String memory, int cnt) {
    }
}
```

【C++】

```c++
class Solution {
public:
    int GetMaxFreeMemoryLen(string memory, int cnt)
    {
    }
};
```

### 参考

[该题目已案例开放](http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=5433691#)

## 题目二

### 题目描述
#设计通讯录
请你设计一个简易通讯录系统，实现以下功能：
- Add(String name, String number)- 增加联系人：名字为 name，联系号码为 number，若已经存在不作处理；
- Update(String name, String number)- 更新联系人信息：若系统中已存在联系人 name，则将此联系人的联系号码更新为 number，并返回其更新前的联系号码；若系统中不存在此联系人，则不作处理并返回 "No such person"；
- Delete(String name)- 删除联系人：若系统中已存在联系人 name，则在系统中删除此联系人记录、并返回其联系号码；若系统中不存在此联系人，则返回 "No such person"；
- Prefix(String s)- 过滤联系人：把名字前缀为 s的联系人过滤出来（区分大小写），并把记录按照名字的字典序返回，形如 [["Abby","12321"],["Alice","1-22442"]...]。

1、用例保证：
•       name 中仅包含小写字母、大写字母与空格
•       number 中仅包含数字与 "-"

2、答题要求：系统中的联系人字母大小写敏感

### 示例

**示例1：**

```txt
输入：
["PhoneSystem","add","add","update","prefix","delete","add","add","update","prefix"]
[[],["Herry","123"],["Merry","456"],["Merry","789"],["Me"],["Merry"],["Herry","234"],["Henry","2564"],["Merry","111"],["He"]]
输出：[null,null,null,"456",[["Merry","789"]],"789",null,null,"No such person",[["Henry","2564"],["Herry","123"]]]

解释：
PhoneSystem p = PhoneSystem()
p.Add("Herry","123")    // 在系统中添加姓名为 "Herry" 的联系方式 "123"
p.Add("Merry","456")    // 在系统中添加姓名为 "Merry" 的联系方式 "456"
p.Update("Merry","789") // 将系统中姓名为 "Merry" 的联系方式更新为 "789"，返回更新前的联系方式 "456"
p.Prefix("Me")          // 将系统中前缀为 "Me" 的联系人姓名及联系方式按联系人姓名的字典序返回 ["Merry","789"]
p.Delete("Merry")       // 删除系统中姓名为 "Merry" 的联系人及其联系方式，并返回其联系方式 "789"
p.Add("Herry","234")    // 系统中已存在姓名为 "Herry" 的联系方式，不作处理
p.Add("Henry","2564")   // 在系统中添加姓名为 "Henry" 的联系方式 "2564"
p.Update("Merry","111") // 系统中不存在姓名为 "Merry" 的联系人，返回 "No such person"
p.Prefix("He")          // 系统中前缀为 "He" 的联系人姓名及联系方式按联系人姓名的字典序返回 [["Henry","2564"],["Herry","123"]]
注：输出中的 null 表示此对应函数无输出（其中：C的构造函数有返回值，但是也是无需输出）

提示：
•      1 <= Add,Update,Prefix,Delete 所有操作数 <= 1000
•      1 <= name.length, number.length <= 20
•      字典序：指按照单词出现在字典的顺序进行排序的方法。先按照第一个字母以 a、b、c......z 的顺序排列，如果第一个字母一样，那么比较第二个、第三个乃至后面的字母。如果比到最后两个单词不一样长（比如 sigh 和 sight），那么把短者排在前。初始化及调用参考（以 C 为例，其他语言参考）：


/*
 * Your PhoneSystem struct will be instantiated and called as such:
 * PhoneSystem* obj = PhoneSystemCreate();
 * PhoneSystemAdd(obj, name, number);
 * char* param_2 = PhoneSystemUpdate(obj, name, number);
 * char* param_3 = PhoneSystemDelete(obj, name);
 * char*** param_4 = PhoneSystemPrefix(obj, s, retSize, retColSize);
 * PhoneSystemFree(obj);
*/

 答题要求：结果可信和过程可信同样重要，您编写的代码需要符合可信的要求（包括通用编码规范、安全编码规范和圈复杂度）。

```

### 函数原型

【Java】

```java

```


## 题目三 整理仓库

### 题目描述
管理员需要整理所有货箱，要求如下：

将若干 位置连续 的货箱堆起，从左至右整理成三堆，每一堆至少有一个货箱；

三堆货箱重量满足条件：左边一堆货箱重量 <= 中间一堆货箱重量 <= 右边一堆货箱重量。

请返回管理员共有多少种满足要求的整理方案；如果无可行方案，返回 0。

注意：答案需要以 1e9 + 7 (1000000007) 为底取余，如：计算初始结果为：1000000008，则取余后返回 1。

### 测试用例
+ 用例1
```txt
示例 1：

输入：boxes = [1,1,2,1,4]
输出：5
解释：有五种整理方法：
整理成 [1,1,7]，7 = boxes[2] + boxes[3] + boxes[4] = 2 + 1 + 4，由右侧 3 个货箱堆成一堆；
整理成 [1,3,5]；
整理成 [1,4,4]；
整理成 [2,2,5]；
整理成 [2,3,4]。
```

+ 提示
```txt
限制：
3 <= boxes.length <= 10^6
1 <= boxes[i] <= 10^6
```

### 函数原型
> 【Java】
```txt
public class Solution3 {
    public int arrangeBoxes(int[] boxes) {
    }
}
```

> 【C++】
```c++
class Solution {
public:
    int ArrangeBoxes(const vector<int>& boxes)
    {
    }
};
```

### 参考
[该题目已案例开放](http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=5962563)

# 专业级

## 题目二 字符串编码校验

### 题目描述
有一种校验码机制，用于数据传输中的数据完整性检查，规则如下：

- 在字符串中插入一些数字作为校验码，每个数字之后跟随对应个数的字符；
- 要求有校验码（校验码大于零并且无前导零），并且正确匹配、无歧义：
如，"helloworld" 在插入校验码之后可以为 "5hello5world"，即 5 + "hello" + 5 + "world"；

但是，有些字符串在进行校验时会产生歧义，比如 "109something" 可以校验为 10 + "9something" 或者 1 + "0" + 9 + "something"，故这类编码方式是有歧义的。

现给出一个字符串 encodedString，请判断这个字符串是否符合上述规则：

- 如果是，则返回去掉校验码后的字符串长度；
- 如果不是，则返回 -1。
### 测试用例
```txt
示例 1：
输入：encodedString = "9computer012"
输出：10
解释：只可以解析为 9 + "computer0" + 1 + "2"，可以正确匹配（校验码与随后字符个数相同）且无歧义。返回去掉校验码后的字符串 "computer02" 的长度 10。
```

```txt
示例 2：
输入：encodedString = "118computer1a"
输出：-1
解释：可以解析为 11 + "8computer1a" 或 1 + "1" + 8 + "computer" + 1 + "a"，有两种解析方式，所以有歧义。
```

```txt
示例 3：
输入：encodedString = "1a02hw"
输出：-1
解释：0 不能作为校验码，02 也不能作为校验码，因此返回 -1。
```

```txt
提示：
1 <= encodedString.length <= 10^3
encodedString 仅由小写字母[a~z]和数字[0~9]构成
```
### 函数原型

【Java】

```java
class Solution {
    public int getLength(String encodedString) {
        }
    }
```

【C++】

```c++
class Solution {
public:
    int GetLength(string encodedString) {
    }
}
```

### 参考

[该题目已案例开放](http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=5536685)


# 专业级

## 题目二

### 题目描述
HC 大会门票数量有限，组织者在前台派发门票，并把每轮派发门票的时间点按时间先后顺序记录在数组 distribute 中。每轮有num张门票供派发，具体派发规则如下：

每位同事在派发时间点之前（含派发时间点）到达才可以领票；
先到先得，一人一票，本轮余票作废；
若有多人同时到达但余票不足，则余票随机分配；
本轮没有拿到票的人将等待下一轮派发，直到拿到票或所有门票派发完毕。
每位同事预计到达前台的时间按时间先后顺序记录在数组 arrive 中。

 

假设你也想参加 HC 大会，请问你最晚什么时间去前台保证可以拿到票？
### 测试用例
```txt
示例 1：
输入：distribute = [11,20], num = 2, arrive = [11,12,15,15,15]
输出：14

解释：
第 1 轮派发时间点为 11，时间点 11 及之前到达的同事有 1 人，抢到第一轮供应的第一张票，余票作废；
第 2 轮派发时间点为 20，时间点 12 到达的同事先到先得、先抢到第二轮供应的第一张票，剩余一张；之后在时间点 15 到达 3 人，如果你在时间点 15 到达则是 4 人抢一张票，不保证一定能拿到票，所以必须早于时间点 15 赶到，即最晚能抢到的时间点是 14。
```

```txt
示例 2：
输入：distribute = [13,20], num = 3, arrive = [11,11,11,12,16,16,17,18]
输出：15

解释：
第 1 轮派发时间点为 13，时间点 11 到达的三位同事，抢到第一轮供应的三张票，时间点 12 到达的同事继续排队等待下一轮派发；
第 2 轮派发时间点为 20，时间点 12 到达（上轮未领到票）的同事先到先得、先抢到第二轮供应的第一张票，剩余两张，如果时间点 16 到达，就会和另外两个同事共 3 人同时抢两张票，不能保证一定拿到票，所以必须早于时间点 16 赶到，即最晚能抢到的时间点是 15。
```

```txt
提示：

1 <= distribute.length <= 10^3，distribute 是升序的（无重复）
1 < distribute[i] <= 10^5，每个distribute[i]的值代表一个时间点
1 <= num <= 100，num 代表每轮派发门票数，固定大小
1 < arrive.length <= 10^5，arrive 是升序的（可能存在相同的时间点）
1 <= arrive[i] <= 10^5，每个arrive[i]的值代表一个时间点
```
### 函数原型

【Java】

```java
class Solution {
    public int latestTime(int[] distribute, int num, int[] arrive) {
        }
    }
```

【C++】

```c++
class Solution {
public:
    int LatestTime(const vector<int> &distribute, int num, const vector<int> &arrive) {
    }
}
```

### 参考

[该题目已案例开放](http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=5667167)

# 专业级

## 题目一

### 题目描述

请你设计一个租房系统。支持以下几个函数

1. 向系统中加入房号为id的房子:`boolean addRoom(int id, int area, int price, int rooms, int[] address)`

`id`:房间编号，`area`：房间面积，`price`：房间租金，`rooms`：房间对应数量，`address`:房间平面坐标(x坐标，y坐标；长度为2)

执行addRoom操作：

- 若租房系统中已经存在房号为id的房间，则更新该房间的信息为新加入的信息，同时返回false
- 若租房系统中已经不存在房号为id的房间，则更新该房间的信息为新加入的信息，同时返回true


2. 从系统中移除房号为id的房子:`boolean deleteRoom(int id)`

- 若租房系统中已经存在房号为id的房间，则将该房间从系统移除，返回`true`
- 若租房系统中不存在房号为id的房间，返回`false`

3. 查询满足指定规则的房间:`int[] queryRoom(int area, int price, int rooms, int[] address, int[][] orderBy)`

查询规则：

找出当前租房系统中房间面积大于等于`area`，租金小于等于`price`，房间数量等于`rooms`的房间，将这些房间按照`orderBy`指定的规则进行升序或者降序排列。

`orderBy`的每一个元素为(`parameter`,`order`)，其中`parameter`可能取值为`1`（按照面积排序），`2`(按照租金排序)，`3`(曼哈顿距离排序)

`order`可能的取值`1`（升序排列），`-1`（降序排列）。

曼哈顿距离：|x1-x2|+|y1-y2|

例如：orderBy=\[\[3,1\],\[2,-1\]\]表示先按照曼哈顿距离升序排序，排序后，如果距离相同，再按照租金降序排序。

### 测试用例

**输入：**

```txt
["RentingSystem","addRoom","addRoom","queryRoom","deleteRoom"]
[[],[3,24,200,2,[0,1]],[1,10,400,2,[1,0]],[1,400,2,[1,1],[[3,1],[2,-1]]],[3]]
```

**输出：**

```txt
[null,true,true,[1,3],true]
```

### 函数原型

【Java】

```java
public class RentingSystem{
    public RentingSystem() {

    }

    public boolean addRoom(int id, int area, int price, int rooms, int[] address) {

    }

    public boolean deleteRoom(int id) {

    }

    public int[] queryRoom(int area, int price, int rooms, int[] address, int[][] orderBy) {

    }
}
```

【C++】

```c++
class RentingSystem {

public:

    RentingSystem()
    {

    }

    bool AddRoom(int id, int area, int price, int rooms, const vector<int>& address)
    {

    }

    bool DeleteRoom(int id)
    {

    }

    vector<int> QueryRoom(int area, int price, int rooms, const vector<int>& address, const vector<vector<int>>& orderBy)
    {
    
    }
}
```

### 参考

[该题目已案例开放](http://3ms.huawei.com/km/groups/3803117/blogs/details/10397189)

## 题目二

### 题目描述

给你一个二叉树，每个节点有一个值（可能重复），现在对这个二叉树进行标记，从根节点到叶子节点组成的路径里，如果存在一个节点，使得由该节点分割的上游路径和下游路径上节点的值的和相等，则标记该节点。

求这个二叉树没有被标记的节点的值的总和。

### 示例

**示例1：**

```txt
          4
         /
       [1]
      /  \
    [4]   4
   /   \
  2    [1]
 /       \
3         9
```

如上图所示，方括号为被标记的节点，节点所在的路径的两部分的和刚好相等，最终结果为 4 + 4 + 2 + 3 + 9 = 22

### 函数原型

【Java】

```java
/*
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public int bisectTreePath(TreeNode root) {
}
```
[该题目参考](http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=5750895)

## 题目三

### 题目描述

有一个 `M*N` 的矩形，矩形的每个点放置着数量不等的传感器，将边为`cnt`的正方形视为一个区域，找出包含传感器数量最多的区域，返回部署的传感器数量的类型的个数。

### 示例

```txt
|1|1|5|
|2|1|1|
|4|1|3|
```

`cnt` = 2，可以组成以下几个区域：

```txt
a. |1|1|  b. |1|5|  c. |2|1|  d. |1|1|
   |2|1|     |1|1|     |4|1|     |1|3|
```

其中，包含传感器的总数量，a=5，b=8，c=8，d=6，b和c是最多的。

在b和c中部署的传感器数量的类型有 1,2,4,5，总共4种，所以返回4。


再例如如下数组

```txt
|3|2|2|3|1|
|4|2|3|3|0|
|3|3|2|1|1|
|3|3|4|3|1|
```

cnt = 2，返回结果3

### 函数原型

【Java】

```java
public int sensorsNumCategory(int[][] sensors, int cnt) {

}
```

# 入门级

## 题目1

给一串由`数字`、`空格（" "）`和`横线`组成的字符串，要求只保留数字，并且将结果要求每三数字一组，最后不能剩余1个。
  
解释： `n%3`的可能结果为0，1, 2，对于余数为1的要转化为3*（n-1）+ 2 +2；

例如:

`3  33-3` 四个数字格式化后的结果为：`33-33`;
`987456412`格式化的结果为：`987-456-412`;
`9874564122`格式化的结果为：`987-456-41-22`;
`98745641223`格式化的结果为：`987-456-412-23`。



# 工作级

## 题目1

### 题目描述
给一串由`数字`、`空格（" "）`和`横线`组成的字符串，要求只保留数字，并且将结果要求每三数字一组，最后不能剩余1个。
  
解释： `n%3`的可能结果为0，1, 2，对于余数为1的要转化为3*（n-1）+ 2 +2；

例如:

`3  33-3` 四个数字格式化后的结果为：`33-33`;
`987456412`格式化的结果为：`987-456-412`;
`9874564122`格式化的结果为：`987-456-41-22`;
`98745641223`格式化的结果为：`987-456-412-23`。


## 题目2

### 题目描述
给出一个整数数组nums[]，数组中nums[i]表示第i天的工作量，给定一个时间长度period天，要求对每一天的进行计分，计分规则如下。

从当前天开始，统计period天内的总工作量total，不足period天的，不计入分数

当总工作量total小于minNum时，总分数-1；

当总工作量total大于maxNum时，总分数+1；

其他情况，分数不变；请计算总得分。

例如：

整数数组[6, 7, 15, 8, 10, 9, 9]，period为1，minNum为8，maxNum为10，则总得分-1。


## 题目三

### 题目描述

请你设计一个租房系统。支持以下几个函数

1. 向系统中加入房号为id的房子:`boolean addRoom(int id, int area, int price, int rooms, int[] address)`

`id`:房间编号，`area`：房间面积，`price`：房间租金，`rooms`：房间对应数量，`address`:房间平面坐标(x坐标，y坐标；长度为2)

执行addRoom操作：

- 若租房系统中已经存在房号为id的房间，则更新该房间的信息为新加入的信息，同时返回false
- 若租房系统中已经不存在房号为id的房间，则更新该房间的信息为新加入的信息，同时返回true


2. 从系统中移除房号为id的房子:`boolean deleteRoom(int id)`

- 若租房系统中已经存在房号为id的房间，则将该房间从系统移除，返回`true`
- 若租房系统中不存在房号为id的房间，返回`false`

3. 查询满足指定规则的房间:`int[] queryRoom(int area, int price, int rooms, int[] address, int[][] orderBy)`

查询规则：

找出当前租房系统中房间面积大于等于`area`，租金小于等于`price`，房间数量等于`rooms`的房间，将这些房间按照`orderBy`指定的规则进行升序或者降序排列。

`orderBy`的每一个元素为(`parameter`,`order`)，其中`parameter`可能取值为`1`（按照面积排序），`2`(按照租金排序)，`3`(曼哈顿距离排序)

`order`可能的取值`1`（升序排列），`-1`（降序排列）。

曼哈顿距离：|x1-x2|+|y1-y2|

例如：orderBy=\[\[3,1\],\[2,-1\]\]表示先按照曼哈顿距离升序排序，排序后，如果距离相同，再按照租金降序排序。

### 测试用例

**输入：**

```txt
["RentingSystem","addRoom","addRoom","queryRoom","deleteRoom"]
[[],[3,24,200,2,[0,1]],[1,10,400,2,[1,0]],[1,400,2,[1,1],[[3,1],[2,-1]]],[3]]
```

**输出：**

```txt
[null,true,true,[1,3],true]
```

### 函数原型

【Java】

```java
public class RentingSystem{
    public RentingSystem() {

    }

    public boolean addRoom(int id, int area, int price, int rooms, int[] address) {

    }

    public boolean deleteRoom(int id) {

    }

    public int[] queryRoom(int area, int price, int rooms, int[] address, int[][] orderBy) {

    }
}
```

### 参考

[该题目已案例开放](http://3ms.huawei.com/km/groups/3803117/blogs/details/10397189)

# 专业级

## 题目一

### 题目描述

设计一个音乐播放器，完成音乐播放器的基本功能：

1. create一个音乐播放器，入参为歌曲容量；

2. 加入一首歌曲，入参为音乐播放器的指针和music_id，具体规则如下：

    * 如果播放器中已经存在该music_id，返回-1，否则如下；
    * 如果音乐播放器容量未满，则将music_id对应的歌曲加入到播放器中，返回0；

    * 如果音乐播放器容量已满，则删除播放次数最少的一首歌曲，再将music_id对应的歌曲加入到播放器中，返回删除的music_id，删除的规则如下：
        * 如果最少播放记录为0，则删除加入播放器时间最早的歌曲删除；
        * 如果最少播放记录不为0，则删除首次播放时间最早的歌曲。
3. 播放一首歌曲，入参为音乐播放器的指针和music_id，如果播放器中未存在该music_id，则返回false；否则返回true；

4. 删除一首歌曲，入参为音乐播放器的指针和music_id，如果播放器中未存在该music_id，则返回false；否则删除该歌曲，并返回true；

5. destroy音乐播放器，入参为音乐播放器的指针。

### 测试用例

### 函数原型

* Java

``` java
class MusicPlayer {
    public MusicPlayer(int capacity) {
        ...
    }
    public int addMusic(int musicId) {
        ...
    }
    public boolean playMusic(int musicId) {
        ...
    }

    public boolean deleteMusic(int musicId) {
        ...
    }

}
```


### 参考

* [参考1](http://3ms.huawei.com/km/blogs/details/10436409)
* [参考2](http://3ms.huawei.com/km/blogs/details/10437607)

## 题目二

### 题目描述 地铁闸机

某地铁站有一个闸机，同一时刻只允许一名乘客进站或出站，一个乘客通过闸机需要 1 秒钟。
* 如果在同一时刻，一个乘客要进站，另一个乘客要出站，按如下规则进出站：
* 如果上一秒，闸机没有被使用（即使更早被使用过），那么进站的乘客优先通过；
* 如果上一秒，闸机有乘客进站，那么进站的乘客优先；如果上一秒，闸机有乘客出站，那么出站的乘客优先。

现有一群乘客要通过这个闸机，乘客的到达时刻记录于数组 `arrTime` 中（升序，可能有重复值），下标表示乘客的编号；

乘客的进出站方向记录于`direction`中（0 表示出站，1 表示进站）。

请按乘客的编号顺序依次返回每个乘客实际通过闸机的时刻。

注意：若多人同时进站，按 `arrTime` 中下标从小到大顺序通过闸机；若多人同时出站，也按此处理。

### 示例
* 示例 1
```
输入：arrTime = [0,0,1,5] direction = [0,1,1,0]
输出：[2,0,1,5]
解释：在 0 时刻，乘客 0（出站）和 乘客1（进站）想要通过闸机。由于闸机上一秒没有被使用，所以乘客 1 优先进站，乘客 0 等待下一时刻；
在 1 时刻，乘客 2（进站）到达闸机，和乘客 0（出站）都要通过闸机。由于上一秒闸机有乘客进站，所以乘客 2 优先进站，乘客 0 继续等待下一时刻；
在 2 时刻，乘客 0 通过闸机；
在 5 时刻，乘客 3 通过闸机。
```
* 示例 2
```
输入：arrTime = [2,2,2,2,3,3,5,5,20,20] direction = [0,1,1,0,0,1,1,0,0,1]
输出：[6,2,3,7,8,4,5,9,21,20]
解释：在 2 时刻，乘客 0 和 乘客3 同时出站，乘客 1 和 乘客2 同时进站。由于闸机上一秒没有被使用，进站优先，且下标小的乘客 1 优先通过闸机；
在 20 时刻，乘客 8 要出站，乘客 9 要进站。由于闸机上一秒没有被使用（之前被使用过），所以乘客 9 优先通过闸机。
```

提示：
 0 < arrTime.length == direction.length <= 10^5，arrTime[i] 和 direction[i] 分别表示第 i 个乘客的到达时刻和进出站方向
 0 <= arrTime[i] <= arrTime[i+1] < 10^9
 direction[i] 仅为 0 或 1
答题要求：您编写的代码需要符合 CleanCode 的要求（包括通用编码规范、安全编码规范和圈复杂度）。

### 函数原型

[该题目已案例开放](http://3ms.huawei.com/km/groups/3803117/blogs/details/10473629?l=zh-cn)


#Java
``` java
class Solution {
    public int[] getTimes(int[] arrTime, int[] direction) {
		...
	}
}
```

#C++
``` C++
class Solution {
public:
	vector<int> GetTimes(const vector<int>& arrTime, const vector<int>& dirction) {
	
	}
}

```

# 专业级

## 题目一：基站信号地图

### 题目描述

1. 视一片区域为一个 rows * cols 的矩阵（行列编号皆从 1 开始），初始有一批基站分布在某些单元格内（位置无重复）。现对这片区域进行改造，涉及两种操作：
    • add：在单元格[row,col]中添加一个基站，若该单元格已经存在基站，则不做任何动作。
    • delete：清除单元格[row,col]及**周边范围**（上、下、左、右、对角的相邻单元格）中的基站。

    假设每个基站的信号覆盖范围为上、下、左、右、对角的相邻单元格；每存在一个基站，覆盖范围内的每个单元格的信号强度增加 1 。

    改造完成后，请统计最终矩阵各单元格（不含基站位置）的信号强度之和。

**输入**

- 首行两个整数rows cols，表示矩阵的行数和列数，取值范围均为[1,100]。
- 第二行是一个整数 baseStationCnt，表示初始基站的个数，取值范围[0,100];
  接下来 baseStationCnt 行，每行输入一个基站的位置，格式为row col，row的取值范围 [1,rows]，col的取值范围 [1,cols]；输入保证初始基站位置无重复。
- 然后一行是一个整数 cmdCnt，表示改造操作的个数，取值范围：[0,100]。
  接下来 cmdCnt 行，每行一个操作，格式为操作 row col，操作仅为add或delete, row的取值范围 [1,rows]，col的取值范围 [1,cols]。

**输出**

一个整数，表示最终矩阵各单元格（不含基站位置）的信号强度之和。

### 示例

- 示例 1

```
输入：
4 6
3
2 2
3 3
4 4
3
delete 4 3
add 1 2
delete 2 5
输出：11
解释：
入下图所示，左边矩阵表示初始基站的分布（*表示基站）
delete 4 3 操作：清除单元格[4,3]周边范围内的两个基站
add 1 2    操作：在单元格[1,2]中添加基站
delete 2 5 操作：单元格[2,5]周边范围内没有基站，因此该操作不改变矩阵内的基站。
最后存在2个基站，如下图右边矩阵所示：绿框表示基站[1,2]的信号覆盖范围，蓝框表示基站[2,2]的信号覆盖范围。 最终矩阵每个单元格（不含基站位置）的信号强度为图中数字，和为11。
```

![20210618P1](../../图库/20210618P1.png)

### 函数原型

* Java

``` java
class Main {
    private static int getMatrixSum(int rows, int cols, int[][] baseStations, Command[] commands) {
        ...
    }

}
```

* [该题目已案例开放](http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id=5892477))

## 题目二

### 题目描述  订单系统

请设计一个订单系统，接收用户的订单并发货。 流程：接收用户的订单，记录用户id，和用户订购的货物id；发货**按照订货顺序**进行，最后返回未发货数最大的用户的id。
* 可以重复订购相同商品
* 输出最多商品未发货的消费者customerId，如果商品未发货值相同，取值小的customerId作为输出；如果不存在未发货返回-1；

**输入**

- 第一行是int，表示系统命令的个数
- ORDER=customerId:goods[] 
- DELIVER=goods 
- ORDER表示一个消费者(customerId)定购了一些商品goods[]，可以重复订购同一件商品
- DELIVER 表示商户已发货商品goods[]

**输出**

一个整数，表示未发货数最大的用户的customerId

### 示例
* 示例 1
```
输入：
5
ORDER=90:1 3 6 8
ORDER=80:5 7
DELIVER=3 5
ORDER=70:10
DELIVER=6 7
输出：90
解释：
```

### 参考

- [参考一](http://3ms.huawei.com/km/blogs/details/10500095)

## 题目三

### 题目描述   社区送菜

有N志愿者，M个社区，第i个社区有X[i]个家庭，现志愿者需要给社区送菜，每个社区只能由一个志愿者送菜，送菜时间为该社区的家庭数；每个志愿者在送菜期间只能送一段编号连续的社区，如社区1，2，3，社区1,2,4则不符合要求；N个志愿者可以并行送菜。问最少送菜时间？

**输入**

- N  志愿者数量
- M 社区数量
- X 各个社区的家庭数量数组

- ### **数据范围**

  1<N<100000

  1<M<100000

  1<X[i]<10000

**输出**

一个整数，最少送菜时间

### 示例

- 示例 1

```
输入：
2
3
40 10 20
输出：40
解释：第一个志愿者送第一一个社区时间为40；第二个志愿者送第二、三个社区，时间为30，两个志愿者同时开始送菜，则最小送菜时间为40
```

### 参考

- [参考一](http://3ms.huawei.com/km/blogs/details/10500095)


# 专业级

## 题目一： 计算展厅人数

MWCS展共有N个展厅，每个展厅的报名人数记于数nums,因疫情原因，所有展厅参展总人数上线为cnt,若报名人数大于cnt，则需要限制展厅入场的人数为limit，需要根据输入，计算出limit，限制规则如下：

如果报名总人数少于cnt，则全部可以入场，返回-1；

如果报名总人数大于cnt，则需要设定limit，超过limit的报名人数的展厅，需要将入场人数限制为limit;其余未达到limit的展厅的报名人，全部可以入场。

**输入**

int，每个展厅的报名人数

int ，最大限制人数

**输出**

int, 需要限制每个展厅最多入场人数

**示例一**：

输入：

1,4,2,5,5,1,6
13 
输出：2 

**解释**：

因为1 + 4 + 2 + 5 + 5 + 1 + 6 > 13；而 1 + 2 + 2 + 2 + 2 + 1 + 2 = 12 < 13，所以展厅最大人数为 2

**用例二**：

输入：

1,1
1
输出：0

### 函数原型

- Java

```java
class ManageTourists   {
   public int manageTourists(int[] nums, int cnt) {
    
    }
}
```

- C++

```c++
class ManageTourists {
public:
   int manageTourists(int[] nums, int cnt)
    {

    }
};
```

- python

```python
class DataMachineSystem:

    def manageTourists(self, nums, cnt):

```





## 题目二：数据设备系统设计

### 题目描述

1. 现有一套由若干个设备组成的系统 ，每个设备既能产生、也能发送和接收数据，系统保证每个设备新产生数据的编号全局唯一。请实现如下功能：
-  DataMachineSystem(int num) - 初始化系统的设备数量为 num（编号 1~num）。
-  transferData(int machineA, int machineB, int dataId)- 设备 machineA 点到点发送编号为dataId的数据给设备 machineB 。若machineB已经有此数据，则不接收并返回 0；否则接收该数据，machineA、machineB 都会留存数据 dataId，并返回 1。
    o    注：若machineA没有该数据，表示系统中也无此数据，则自己产生编号为dataId的数据再发送。
- transferDataToAll(int machine, int dataId)- 设备 machine 群发编号为 dataId 的数据给所有设备。已经有此数据的设备不会接收，请返回发送后接收了此数据的设备数量。发送后，machine 和接收到此数据的设备都会留存数据 dataId。
    o    注：若 machine 没有该数据，表示系统中也无此数据，则自己产生编号为 dataId 的数据再发送。
- queryContribution(int machine)- 查询设备 machine 的贡献量 。贡献量的计算规则如下：
    o    对于每个接收到数据的设备，其发送方都增加贡献量 10；注意对于群发，发送方增加贡献量为 接收到此数据的设备数量 * 10；
    o    贡献会传递：如果发送方的数据来源于另一设备，那么该设备的贡献量也增加 10；贡献继续传递，直至数据的产生方。
    如：已知A、B、C、D 四台设备，对同一数据依次做如下 3 次数据发送操作：
    A->B：A发送数据给B；此时，A 增加了 10 贡献量；
    B->C：B再发送同一数据给C；此时，B、A 都增加 10 贡献量；
    C->D：C再发送同一数据给D；此时，C、B、A 都增加 10 贡献量；
    最后，A、B、C 分别增加了 30、20、10 贡献量。

**输入**
- ["DataMachineSystem","transferData","transferDataToAll","queryContribution"]
[[3],[1,2,17],[2,29],[2]]

**输出**
[null,1,2,20]

![20210809P1](../../图库/20210809P1.png)
**解释**
DataMachineSystem obj = DataMachineSystem(3); // 一共有 3 个设备完成初始化；
obj.transferData(1, 2, 17); // 设备 1 当前无数据17，会产生数据 17 并发送此数据给设备2；由于设备 2 无此数据，所以会接收此数据，返回 1。同时发送设备 1 的贡献量增加 10；
obj.transferDataToAll(2, 29); // 设备 2 当前无数据29，会产生数据 29 并群发此数据。由于设备 1 和 3 都没有数据 29，会接收此数据，所以返回接收设备数为 2。同时发送设备 2 的贡献量增加 20；
obj.queryContribution(2); // 设备 2 的贡献量累计是 20。
注：输出中的 null 表示此对应函数无输出（其中：C 的构造函数有返回值，但是也是无需输出）

**输入2**：
["DataMachineSystem","transferData","transferData","transferData","queryContribution","transferData","transferDataToAll","queryContribution","transferData","queryContribution","queryContribution","queryContribution"]
[[4],[1,2,15],[2,3,15],[3,4,15],[1],[2,4,37],[2,37],[2],[3,4,37],[1],[3],[4]]

**输出2**：[null,1,1,1,30,1,2,50,0,30,10,0]

![20210809P2](../../图库/20210809P2.png)
**解释2**：
DataMachineSystem obj = DataMachineSystem(4); // 初始化，一共有 4 个设备
obj.transferData(1, 2, 15); // 返回 1
obj.transferData(2, 3, 15); // 返回 1，2的贡献量为10，...
obj.transferData(3, 4, 15); // 返回 1，2的贡献量增加10，...
obj.queryContribution(1); // 返回 30
obj.transferData(2, 4, 37); // 返回 1，2的贡献量增加10，...
obj.transferDataToAll(2, 37); // 设备 2 群发数据 37。由于设备 4 已有数据 37，所以发给设备1 和 3，返回接收设备数为 2。同时，2 的贡献量增加 20，累计 50
obj.queryContribution(2); // 返回 50
obj.transferData(3, 4, 37); // 由于设备 4 已有数据 37，返回 0
obj.queryContribution(1); // 返回 30
obj.queryContribution(3); // 返回 10
obj.queryContribution(4); // 返回 0
注：输出中的 null 表示此对应函数无输出（其中：C 的构造函数有返回值，但是也是无需输出）

### 提示：

·         1 <= transferData, transferDataToAll 累计操作数 <= 1000

·         1 <= queryContribution 累计操作数 <= 10^5

·         2 <= num <= 1000

·         1 <= machineA, machineB, machine <= num

1 <= dataId <= 1000



### 函数原型

* Java

``` java
class DataMachineSystem  {
    public DataMachineSystem(int num) {
    
    }
    
    public int transferData(int machineA, int machineB, int dataId) {
        
    }
    
    public int transferDataToAll(int machine, int dataId) {
        
    }
    
    public int queryContribution(int machine) {
        
    }

}
```
* C++
``` c++
class DataMachineSystem {
public:
    explicit DataMachineSystem(int num)
    {

    }
    
    int TransferData(int machineA, int machineB, int dataId)
    {

    }
    
    int transferDataToAll(int machine, int dataId)
    {

    }
    
    int queryContribution(int machine) 
    {
        
    }

};
```
* python
``` python
class DataMachineSystem:

    def transfer_data(self, machine_a, machine_b, data_id):
 
    def transfer_data_to_all(self, machine, data_id):
        
    def transferDataToAll(self, machine, dataId):
       
    def queryContribution(self, machine):
        

```

* [该题目已案例开放](http://3ms.huawei.com/km/groups/3803117/blogs/details/10742427))


## 题目三

### 题目描述   演出成本

某社团有2\*num个团队，编号为0—(2\*num - 1)。有一次大型演出，需要两个团队一起出节目，两个团队出节目有一个成本。大型演出规定，社团里的所有团队都需要出演，并只能出演一次，我们取出演的所有节目总成本最高的成本，叫做昂贵成本，设计算法计算最低的昂贵成本。

**输入**

- 一个二维数组[ [x,y,N], [...]...[...] ]，每个数组[x,y,N]表示社团编号为x和y的团队共同演出成本为N.

**输出**

一个整数，最小昂贵成本

### 示例

- 示例 1

```
num = 2
program = [[0,1,250],[0,3,10],[1,2,25],[1,3,80],[2,3,90]]
输出：25
解释：主办方可选择的 num 个节目的方案有两个：
方案一：
program 中下标为 0 的节目，由社团 0 和社团 1 合作演出，成本为 250；
program 中下标为 4 的节目，由社团 2 和社团 3 合作演出，成本为 90；
「昂贵成本」为 250。
方案二：
program 中下标为 1 的节目，由社团 0 和社团 3 合作演出，成本为 10；
program 中下标为 2 的节目，由社团 1 和社团 2 合作演出，成本为 25；
「昂贵成本」为 25。
两个方案中「昂贵成本」最小的是方案二，因此返回25。
```
### 示例

- 示例 2
```
输入：
num = 3
program = [[0,4,41],[2,5,35],[1,3,49]]
输出：49

提示：
1 <= num <= 8
num <= program.length <= 500
0 <= program[i][0] < program[i][1] < 2*num
2 <= program[i][2] <= 1000
答题要求：您编写的代码需要符合 CleanCode 的要求（包括通用编码规范、安全编码规范和圈复杂度）。
```

### 参考

### 函数原型

- Java

```java
class Main  {
    public int cooperativePerformance(int num, int[][] program) {
    
    }
}
```

- C++

```c++
class Main {
public:
    int  CooperativePerformance(int num, int[][] program)
    {

    }
};
```

- python

```python
class Main:
    def CooperativePerformance(self, num, program):
        pass
```
