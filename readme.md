# 數據結構

##      什麼是數據結構:

            1.數據

                輸入到電腦中並且能被電腦識別，存儲和處理的符號總稱。媽的蛋幹
            
            2.數據結構
           
               數據結構指的是數據元素及數據元素之間的相互關係,或組織數據的形式。

##     數據之間的結構關係。

             1.邏輯結構。

                表示數據之間的抽象關係(如鄰接關係、從屬關係等),按每個元素可能具有的直接前趨數和
                直接後繼數將邏輯結構分為"線性結構"和"非線性結構"兩大類。

             2.存儲結構。

                邏輯結構在計算機中的具體實現方法,分為順序存儲方法、
                連結存儲方法、索引存儲方法、散列存儲方法。
                
             3.邏輯結構
    
               1.特點:

            　　-只是描述數據結構中數據元素之間的聯繫規律
            　　-是從具體問題中抽象的數據模型，是獨立於計算機存儲的(與計算機無關)
    
     2.邏輯結構分類

        -線性結構

                一對一。
                線性結構是N個數據元素的有序集合。
                
                集合中必存在唯一的一個"第一個元素"
                集合中必存在唯一的一個"最後的元素"
                除最後元素外，每個元素均有唯一的"前驅"與"後繼"

        -樹形結構(層次結構)

                樹形結構指的是數據元素之間存著一對多的樹形關係的
                數據結構，是一類重要的非線性樹聚結構。
                
                在樹聚結構中，樹根結點沒有前驅節點，其餘每個結點
                有且只有一個前驅結點。葉子結點沒有後續結點，
                其餘每個結點的後續結點樹可以是一個或是多個。

        圖形結構

                圖是一種比較複雜的樹聚結構，再圖結構中任意兩個元素之間都可能有關係，
                也就是說這是一種多對多的關係。
    
##     3.存儲結構

        1.特點:

                是數據的邏輯結構在計算機存儲中的映象(或表示)
                存儲結構是通過計算機程序來實現，因為是依賴於具體的計算機語言。

        2.存儲結構分類

                -順序存儲 

                        順序存儲(Sequential Storage):
                        將數據結構中各元素按照其邏輯順序存放於存儲器一片連續的存儲空間。

                        優點:緊密排列，收尋速度快。
                        缺點:無法從中間插入數據。
                        例如:list，tuple，str

                -鏈式存儲

                        鏈式存儲(Linked Storage):
                        將數據結構中各元素分布到存儲器的不同點，用記錄下一個節點位置的方式。
                        建立他們之間的關係，由此得到的存儲結構為鏈式存儲結構。

                        優點:不是緊密排列的關係，所以可以在任何一點插入數據。
                        缺點:查找速度慢

                索引存儲:

                        索引存儲(Index Storage):
                        在存儲數據的同時，建立一個附加的索引表，及索引存儲結構 = 數據文件 + 索引表。

##    4.線性表
    
           定義:
                線性表的定義是描述其邏輯結構，而通常會在線性表上進形的查找，插入，刪除等操作。
                線性表作為一種基本的數據結構類形，在計算機存儲器中的映象(或表示)，
                一般有兩種形式:

                        一種是:順序映像
                        一種是:鏈式映像
           
           線性表的順序存儲

                1.定義:

                        將線性表 L=(a0,a1........an-1)中的各元素依次存儲於計算機一片連續的存儲空間，
                        這樣機制表示為線性表的順序存儲結構。

                2.特點:

                        1.邏輯上相鄰的元素(a1,+ai+1),其存儲位置也是相鄰的。 
                        2.存儲密度高，方便對數據的遍立查找。
                        3.對表的插入和刪除等運算的效率較差。
                
                3.程式實現:

                        list存放於一片單一連續的記憶體，故可借助於列表型來描述線性表的順序存儲結構，
                        而且列表本身就提供了豐富的接口滿足這種數據結構的運算。
        
###          線性表的鏈式存儲


               1.定義:

                        將線性表 L = (a0,a1.......,an-1)中各元素分布在存儲器的不同存儲快，稱為結點，
                        每個結點(尾節點除外)中都持有一個指向下一個節點的引用，所以所得到的存儲
                        結構為鏈表結構。

                2.特點:

                        -邏輯上相鄰的元素ai,ai+1，其存儲位置也不一定相鄰。
                        -存儲稀疏，不必開闢整塊存儲空間
                        -對表的插入和刪除等運算效率較高
                        -邏輯結構複查，不利於遍立。


        
        隊列:

                1.定義:

                        隊列是限制在兩端進行插入操作和刪除操作的線性表，
                        允許進行存入操作的一端稱為:"隊尾"
                        允許進行刪除操作的一端稱為:"隊頭"
                
                2.特稱:

                        -隊列只能在隊頭和隊尾進行數據操作
                        -隊列的模型具有 "先進先出" 或 "後進後出" 的規律

                3.隊列的代碼:

                        -隊列的操作有入隊，出隊，判斷隊列的空滿等操作。


練習:

        1. 對鍊表進行畫圖整理
        2. 創建兩個鍊表，鍊表當中的值均為有序值(從小到大)
           將兩個鍊表合併成一個，合併後要求值為有序值。
           
           例如:
                鏈表1 : 1,2,3,4,7,9
                鍊表2:  4,5,6,8

                合併後的鍊表:1,2,3,4,5,6,7,8,9

作業:

        1.熟悉markdown標籤規則。之後都會用這個，所以要熟悉
          會編寫基本的markdown文檔
        
        2.熟悉第二階段重點代碼 一定要了解未來找data的時候會用。

        3.編寫作業

                編寫一個接口程式，獲取一段文字，判斷文字中括弧是否正確，如果正確輸入正確，如果不正確則指出出錯的地方。

                "Next, install the Python 3 interpreter on your computer. This is the program that reads Python programs and carries out their instructions; you need it before you can do any Python programming. Mac and Linux distributions may include an outdated version of Python (Python 2), but you should install an updated one (Python 3). See BeginnersGuide/Download for instructions to download the correct version of Python."

# 樹形結構

##      基礎概念

###             1.一個節點的子樹的個數稱為該節點的度數，一棵樹的度數是指該樹中節點的最大度數。

###             2.度數為零的的節點稱為樹葉或終端節點，度數不為零的節點稱為分支節點，除根節點外的分支節點稱為內部節點。

###             3.一個節點的子樹之根節點稱為該節點的子節點，該節點稱為他們的父節點，

>>>>>>> david_dev






