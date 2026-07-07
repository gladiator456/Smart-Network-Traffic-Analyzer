statistics={
    "TCP":0,
    "UDP":0,
    "ICMP":0,
    "OTHER":0
}

def update_statistics(protocol):

    if protocol in statistics:
        statistics[protocol]+=1
    else:
        statistics["OTHER"]+=1

    print("\nTraffic Statistics")

    for key,value in statistics.items():

        print(f"{key}: {value}")
