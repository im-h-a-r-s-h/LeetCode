# LeetCode Problem: Number of Students Unable to Eat Lunch
# Problem Link: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/



# Approach 1: Using a queue and stack to simulate the lunch process
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n=len(students)
        count=0
        while((len(students)!=0 or len(sandwiches)!=0) and count<len(students)):
            if(students[0]==sandwiches[0]):
                students.pop(0)
                sandwiches.pop(0)
                count=0
            else:
                students.append(students.pop(0))
                count+=1
        return len(students)

# Approach 2: Count students who prefer each sandwich type
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        d={0:0,1:0}
        for i in students:
            if i in d:
                d[i]+=1
        cnt=0
        for i in sandwiches:
            if d[i] > 0:
                d[i] -= 1
            else:
                break
        return d[0] + d[1]

