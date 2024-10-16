# LeetCode Problem: Number of Students Unable to Eat Lunch
# Problem Link: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

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
