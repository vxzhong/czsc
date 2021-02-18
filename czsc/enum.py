# coding: utf-8

from enum import Enum

class Mark(Enum):
    D = "底分型"
    G = "顶分型"

class Direction(Enum):
    Up = "向上"
    Down = "向下"

class Freq(Enum):
    F1 = "1分钟"
    F5 = "5分钟"
    F15 = "15分钟"
    F30 = "30分钟"
    F60 = "60分钟"
    D = "日线"
    W = "周线"
    M = "月线"

class Signals(Enum):
    Other = "其他"

    # 信号值编码规则：
    # 笔数：X3 - 三笔信号；X5 - 五笔信号；X7 - 七笔信号；X9 - 九笔信号；
    # 多空：L - 多头信号；S - 空头信号；
    # 顺序：L/S 后面跟的 A-F 表示信号顺序
    # 数字：0-10表示信号变种，0是基础型
    # 组合规则：笔数_多空_顺序_数字；如 X5LA0 表示五笔多头信号A0
    # ============================================================================================

    # 三笔形态信号
    X3LA0 = "X3LA0~向下不重合"
    X3LB0 = "X3LB0~向下奔走型中枢"
    X3LC0 = "X3LC0~向下三角收敛中枢"
    X3LD0 = "X3LD0~向下三角扩张中枢"
    X3LE0 = "X3LE0~向下盘背中枢"
    X3LF0 = "X3LF0~向下无背中枢"

    X3SA0 = "X3SA0~向上不重合"
    X3SB0 = "X3SB0~向上奔走型中枢"
    X3SC0 = "X3SC0~向上三角收敛中枢"
    X3SD0 = "X3SD0~向上三角扩张中枢"
    X3SE0 = "X3SE0~向上盘背中枢"
    X3SF0 = "X3SF0~向上无背中枢"

    # 五笔形态信号
    # 具体描述：https://blog.csdn.net/baidu_25764509/article/details/113639353
    X5LA0 = "X5LA0~aAb式底背弛"
    X5LB0 = "X5LB0~三买"
    X5LC0 = "X5LC0~类趋势底背驰"
    X5LD0 = "X5LD0~向下三角扩张中枢"
    X5LE0 = "X5LE0~向下三角收敛中枢"
    X5LF0 = "X5LF0~大级别底分"

    X5SA0 = "X5SA0~aAb式顶背驰"
    X5SB0 = "X5SB0~三卖"
    X5SC0 = "X5SC0~类趋势顶背驰"
    X5SD0 = "X5SD0~向上三角扩张中枢"
    X5SE0 = "X5SE0~向上三角收敛中枢"
    X5SF0 = "X5SF0~大级别顶分"

    # 七笔多头信号
    # 具体描述：https://blog.csdn.net/baidu_25764509/article/details/113649988
    X7LA0 = "X7LA0~aAbcd式底背弛"
    X7LB0 = "X7LB0~abcAd式底背弛"
    X7LC0 = "X7LC0~aAb式底背弛"
    X7LD0 = "X7LD0~类趋势底背弛"
    X7LE0 = "X7LE0~BaA式右侧底"
    X7LF0 = "X7LF0~类趋势底背弛强反弹后不创新低"

    X7SA0 = "X7SA0~aAbcd式顶背驰"
    X7SB0 = "X7SB0~abcAd式顶背驰"
    X7SC0 = "X7SC0~aAb式顶背驰"
    X7SD0 = "X7SD0~类趋势顶背驰"
    X7SE0 = "X7SE0~BaA式右侧顶"
    X7SF0 = "X7SF0~类趋势顶背驰强反弹后不创新高"

    # 九笔多头信号
    X9LA0 = "X9LA0~aAbBc式向下趋势底背弛"
    X9LB0 = "X9LB0~aAb式底背弛"
    X9LC0 = "X9LC0~aAbcd式底背弛"

    X9SA0 = "X9SA0~aAbBc式向上趋势顶背驰"
    X9SB0 = "X9SB0~aAb式顶背弛"
    X9SC0 = "X9SC0~aAbcd式顶背弛"


class Factors(Enum):
    Other = "其他"
    DEV = "DEV~开发中的因子"

    # 因子值编码规则：
    # D - 日线；F30 - 30分钟; F5 - 5分钟;
    # L - 多头信号标记；S - 空头信号标记；
    # A - 右侧转折标记；B - 左侧转折标记；C - 右侧中继标记；D - 左侧中继标记；
    # 最后的数字为因子的编写顺序，仅用于区分不同因子
    # 组合规则为 级别_多空_左右_数字
    # ============================================================================================
    # 日线因子
    # ============================================================================================
    # 日线向下笔转折右侧因子 DLA
    DLA1 = "DLA1~日线第N笔超强底分&5分钟近七笔为BaA式右侧底"

    DLA2 = "DLA2~30分钟三买"
    DLA2a = "DLA2a~30分钟三买&30分钟最近一个向上笔创新高"

    DLA3 = "DLA3~15分钟三买"
    DLA3a = "DLA3a~15分钟三买&15分钟最近一个向上笔创新高"
    DLA4 = "DLA4~15分钟近七笔为BaA式右侧底"

    DLA5 = "DLA5~60分钟三买"
    DLA5a = "DLA5a~60分钟三买&60分钟最近一个向上笔创新高"

    # 日线向下笔转折左侧因子 DLB
    DLB1 = "DLB1~30分钟近五笔为底背弛"
    DLB2 = "DLB2~30分钟近七笔为底背弛"

    DLB3 = "DLB3~30分钟近九笔为底背弛"
    DLB3a = "DLB3a~30分钟近九笔为aAbBc式底背弛"

    DLB4 = "DLB4~60分钟近五笔为底背弛"
    DLB5 = "DLB5~60分钟近七笔为底背弛"

    DLB6 = "DLB6~60分钟近九笔为底背弛"
    DLB6a = "DLB6a~60分钟近九笔为aAbBc式底背弛"

    DLB7 = "DLB7~15分钟近五笔为底背弛"
    DLB8 = "DLB8~15分钟近七笔为底背弛"

    DLB9 = "DLB9~15分钟近九笔为底背弛"
    DLB9a = "DLB9a~15分钟近九笔为aAbBc式底背弛"

    # 日线向上笔中继右侧因子
    DLC1 = "DLC1~5分钟近七笔为底背弛&1分钟近五笔为大级别底分"

    # 日线向上笔中继左侧因子
    DLD1 = "DLD1~5分钟近七笔为底背弛&1分钟近五笔为大级别底分"

    # 日线向上笔转折右侧因子
    DSA1 = "DSA1~30分钟近五笔为三卖"

    # 日线向上笔转折左侧因子
    DSB1 = "DSB1~30分钟近七笔为顶背弛"

    # 日线向下笔中继右侧因子
    DSC1 = "DSC1~30分钟近五笔为大级别顶分"

    # 日线向下笔中继左侧因子
    DSD1 = "DSD1~5分钟近五笔为aAb式顶背驰"

    # ============================================================================================
    # 30分钟因子
    # ============================================================================================
    # 30分钟向下笔转折右侧因子 F30LA
    F30LA1 = "F30LA1~5分钟近七笔为BaA式右侧底"
    F30LA2 = "F30LA2~15分钟近七笔为BaA式右侧底"
    F30LA3 = "F30LA3~1分钟近七笔为BaA式右侧底"
    F30LA4 = "F30LA4~5分钟三买"
    F30LA5 = "F30LA5~15分钟三买"
    F30LA6 = "F30LA6~1分钟三买"

    # 30分钟向下笔转折左侧因子 F30LB
    F30LB1 = "F30LB1~5分钟倒1的七笔为底背弛"

    # 30分钟向上笔中继右侧因子
    F30LC1 = "F30LC1~"

    # 30分钟向上笔中继左侧因子
    F30LD1 = "F30LD1~"





