def cyk(token, cnf):
    n = len(token)
    arr = [[set([]) for j in range(n)] for i in range(n)]
    for j in range(0, n):
      for lhs, rule in cnf.items():
        for rhs in rule:    
          if len(rhs) == 1 and rhs[0] == token[j]:
            arr[j][j].add(lhs)

      for i in range(j, -1, -1):     
        for k in range(i, j):  
          for lhs, rule in cnf.items():
            for rhs in rule:
              if len(rhs) == 2 and rhs[0] in arr[i][k] and rhs[1] in arr[k + 1][j]:
                arr[i][j].add(lhs)
    
    if 'S' in arr[0][n-1]:
        print("Compiled Successfully :)")
    else:
        print("Compile Failed :(")
      
if __name__ == "__main__":
  pass