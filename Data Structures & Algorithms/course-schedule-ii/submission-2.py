class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        create a directed graph, each vertice is a course
        and check the graph has a cycle

        we use a hashmap / adjacency map to represent the graph

        we need to track visited as well the takenCourse
        """
        graph = defaultdict(list)
        
        for prerequisite in prerequisites:
            course, prerequisite = prerequisite[0], prerequisite[1]
            graph[course].append(prerequisite)
        taken_courses = []
        taken_courses_set = set()

        def canComplete(course, visited, taken_courses):
            if not len(graph[course]):
                if course not in taken_courses_set:
                    taken_courses.append(course)
                    taken_courses_set.add(course)
                return True
            if course in visited:
                return False
            
            visited.add(course)
            for prerequisite in graph[course]:
                if not canComplete(prerequisite, visited, taken_courses):
                    return False
            graph[course] = []
            if course not in taken_courses_set:
                taken_courses.append(course)
                taken_courses_set.add(course)
            return True
        
        for course in range(numCourses):
            if not canComplete(course, set(), taken_courses):
                return []
        
        return taken_courses