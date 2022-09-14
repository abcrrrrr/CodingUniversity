# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buf4 = ["" for i in range(4)]
        self.nBuf4Remaining = 0
        self.nBuf4Read = 0
        self.isEndOfFile = False
        
    def read(self, buf: List[str], n: int) -> int:
        if self.isEndOfFile: 
            return 0
        buf = ["" for i in range(n)]
        iBuf = 0
        # read from saved buf4
        if self.nBuf4Remaining > 0:

            for i in range(self.nBuf4Read - self.nBuf4Remaining, self.nBuf4Read):
                buf[iBuf] = self.buf4[i]
                if iBuf == n-1:
                    break
                iBuf += 1
        if iBuf < n:
            # read new buf4
            self.nBuf4Read = read4(self.buf4)
            self.nBuf4Remaining = self.nBuf4Read
            if self.nBuf4Read == 0:
                self.isEndOfFile = True
                return iBuf
            for i in range(self.nBuf4Read):
                buf[iBuf] = self.buf4[i]
                
                self.nBuf4Remaining -= 1
                if iBuf == n-1:
                    break
                iBuf += 1
        return iBuf