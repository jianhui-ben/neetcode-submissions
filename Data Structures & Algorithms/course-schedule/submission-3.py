from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        create a directed graph, each vertice is a course
        and check the graph has a cycle

        we use a hashmap / adjacency map to represent the graph
        """
        graph = defaultdict(list)
        
        for prerequisite in prerequisites:
            course, prerequisite = prerequisite[0], prerequisite[1]
            graph[course].append(prerequisite)
        

        def canComplete(course, visited):
            if not len(graph[course]):
                return True
            if course in visited:
                return False
            
            visited.add(course)
            for prerequisite in graph[course]:
                if not canComplete(prerequisite, visited):
                    return False
            graph[course] = []
            return True
                    

        for course in range(numCourses):
            if not canComplete(course, set()):
                return False
        
        return True
        
        
        