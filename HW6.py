def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:

     if len(assignment) == len(self.variables):
         return assignment


     unassigned: List[V] = [v for v in self.variables if v not in assignment]

    
     first: V = unassigned[0]
     for value in self.domains[first]:
         local_assignment = assignment.copy()
         local_assignment[first] = value
         # if we're still consistent, we recurse (continue)
         if self.consistent(first, local_assignment):
             result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment)
             # if we didn't find the result, we will end up backtracking
             if result is not None:
                 return result
     return None
