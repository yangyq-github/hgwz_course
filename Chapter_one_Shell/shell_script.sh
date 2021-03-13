find_error_log() {
    #方法一：用grep 匹配，是整行匹配，所以正则表达式要格外严格
    less nginx.log | grep -E '(" 404 |" 500 )'
    #方法二：用awk，字段匹配
    awk '$12~/404|502/ {print $0}' trade.access.log
}

find_top_10() {
    #以下两种方法都可以
    awk '{print $1}' trade.access.log | sort | uniq -c | sort -nr | head -n 3
    awk '{print $1}' trade.access.log | sort | uniq -c | sort -n -k 1 | awk 'NR==10'
}

find_url_avg_time() {
    #统计一个URL的信息
    less trade.access.log | awk '$9~/^\/api\/v2\/realtime$/' | awk ' {sum+=$NF}END{print  "总的响应时间为:",sum  " 总的记录数为:",NR  "  平均值为:", sum/NR}'
    #统计所有URL的访问量

    less trade.access.log |
        awk '{print $9,$NF}' |
        sed -E 's#/api/v2/history\?symbol=BTCUSDT&resolution=([0-9])+&from=([0-9])+&to=([0-9])+#/api/v2/history#g' | sed -E 's#/api/v2/symbols\?symbol=[A-Z]+#/api/v2/symbols#g' | sed -E 's#/history\?symbol=XBTUSD&resolution=([0-9])+&from=([0-9])+&to=([0-9])+#/history#g' |
        sed -E 's#/api/v2/symbols\?symbol=[A-Z]+#/api/v2/symbols#g' |
        awk '{s[$1]+=$2;n[$1]+=1}END{for (k in s) print k,s[k]/n[k]}' |
        # sort -n -k2|less
        sort | uniq -c | sort -nr
}

perf_get() {
    #统计某个进程的性能，输出20s内某个进程的每秒的cpu和mem，并空出一行统计平均性能
    top -p26417 -n 20 -d 1 | grep --line-buffered 26417 | awk 'BEGIN{print "cup","mem";cpu_sum=0;mem_sum=0}{print $9,$10}{cup_sum+=$9;mem_sum+=$10}END{print "\n********\n"cup_sum/NR,mem_sum/NR}'
    #另外一种写法
    top -b -d 1 -n 20 | grep marketserver --line-buffered | awk '{print $0}{cup_sum+=$9;mem_sum+=$10}END{print "\n""cpu 平均值:",cup_sum/NR,"men 平均值:",mem_sum/NR}'
}

connection_summary() {
    #连接某个端口的ip分布情况：链接所有的端口和对应的tcp连接状态，找出他们的连接总数
    netstat -tn | awk 'NR>2 {print $4,$6}' | awk -F: '{print $2}' | sort | uniq -c | sort -nr | awk '{print $2,$3,$1}' | grep 3306
    # 加上 \t 输出格式
    netstat -tn | awk 'NR>2 {print $4,$6}' | awk -F: '{print $2}' | sort | uniq -c | sort -nr | awk '{print $2"\t",$3"\t",$1}'
}

#掷骰子:要求：100个人，每人一个骰子（6个点），掷骰子>3的点认为是通过的，否则淘汰。第一轮选出的人进入第二轮继续比赛，直至选出最终冠军

arrary=$(seq 1 100)
dian=$((RANDOM % 6)) #整数扩展。把里面的变量当作整数去处理

choujiang() {
    seq 1 100 | {
        all=()
        sub=()
        while read line; do
            all+=($line)
        done
        echo ${all[@]}

        while [[ ${#all[@]} -gt 1 ]]; do
            sub=("${all[@]}") #防止数组长度为0，提前备份
            for men in "${!all[@]}"; do
                [[ $((RANDOM % 6 + 1)) -le 3 ]] && unset all[$men]
            done
            echo ${all[@]}
            ((${#all[@]} == 0)) && all=("${sub[@]}") #如果数组长度为0，则复活上一轮
            echo "-------------"
        done
    }

}

#seq 1 100 | lucky
#seq 1 100 | xargs | lucky
lucky() {
    #需要给默认值，不然用于数组的时候，会默认有一个初始元素
    local all=() sub_temp=() sub=() index=0

    #多行模式支持选手名字带有空格
    while read line; do
        all+=("$line")
    done
    #单行的时候，默认空格区分每个选手
    ((${#all[@]} == 1)) && all=($all)
    #用于数据处理，不影响原来的all
    sub=("${all[@]}")

    while true; do
        echo "index=$index count=${#sub[@]} sub=${sub[@]}"
        ((index++))
        #用于复活上一轮的种子
        sub_temp=(${sub[@]})

        for i in "${!sub[@]}"; do
            ((RANDOM % 6 + 1 > 3)) || unset sub[$i]
        done

        ((${#sub[@]} == 1)) && {
            echo
            echo winner=${sub[@]}
            break
        }
        #复活上一轮
        ((${#sub[@]} == 0)) && { sub=(${sub_temp[@]}); }
    done
}
