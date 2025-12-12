class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        # 1) Sort events: first by int(timestamp), then OFFLINE before MESSAGE
        events.sort(key=lambda e: (int(e[1]), 0 if e[0] == "OFFLINE" else 1))
        
        ans = [0] * numberOfUsers
        # online_t[i] = time when user i becomes back online (initially 0 so online at all times >=0)
        online_t = [0] * numberOfUsers
        all_lazy = 0  # count of "ALL" mentions to add at end
        
        for etype, ts, data in events:
            t = int(ts)
            
            if etype == "OFFLINE":
                # user goes offline; comes back online after t+60
                uid = int(data)
                online_t[uid] = t + 60
            
            else:  # "MESSAGE"
                # ALL: count but defer adding later
                if data == "ALL":
                    all_lazy += 1
                
                # HERE: only count currently online users
                elif data == "HERE":
                    for i in range(numberOfUsers):
                        if online_t[i] <= t:
                            ans[i] += 1
                
                # specific ids like "id0 id3 id3"
                else:
                    parts = data.split()
                    for p in parts:
                        uid = int(p[2:])  # strip "id"
                        ans[uid] += 1
        
        # finally apply ALL mentions to all users
        if all_lazy:
            for i in range(numberOfUsers):
                ans[i] += all_lazy
        
        return ans
