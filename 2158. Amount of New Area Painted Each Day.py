class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        # keep a record of painted walls : intervals
        # when new paint everyday -> compare if has overlap with painted
            # overlap -> should deduct overlap point in new_paint_count today. update boundary
            # not overlap -> insert into painted
        
        painted = []
        result = []
        for start, end in paint:
            new_start = start
            new_end = end
            new_painted = []
            overlap = 0

            for p_start, p_end in painted:
                # detect overlap
                if p_end < new_start or p_start > new_end : # no overlap    
                    new_painted.append([p_start, p_end])
                else:  # has overlap
                    new_start = min(new_start, p_start)
                    new_end = max(new_end, p_end)
                    overlap += min(p_end, end) - max(p_start, start)

            result.append(end - start - overlap)
            new_painted.append([new_start, new_end])
            painted = new_painted.copy()
        return result
            