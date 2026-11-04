from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        create a directed graph, each vertice is a course
        and check the graph has a cycle

        we use a hashmap to represent the graph
        """
        visited = set()
        graph = defaultdict(list)
        
        for prerequisite in prerequisites:
            second_class, first_class = prerequisite[0], prerequisite[1]
            graph[second_class].append(first_class)
        
        def finish_course(course, cur_path):
            if course in cur_path:
                return False
            if course in visited:
                return True

            cur_path.add(course)
            for previous_course in graph[course]:
                if not finish_course(previous_course, cur_path):
                    return False
            cur_path.remove(course)
            visited.add(course)
            return True


        for course in range(numCourses):
            if not finish_course(course, set()):
                return False
        
        return True
        