class Solution(object):
    def getHappyString(self, n, k):
        out = [-1]*n
        self.k = k
        def find(l):
          if l==n:
            if self.k==1:
              return True
            else:
              self.k-=1
              return False
          for c in ['a', 'b', 'c']:
            if l==0 or out[l-1]!=c:
                out[l]=c
                if find(l+1):
                    return True
                out[l]=-1
          return False
        if find(0):
            return "".join(out)
        return ""