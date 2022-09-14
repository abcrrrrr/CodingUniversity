# The read4 API is already defined for you.
# @param buf4, List[str]
# @return an integer
# def read4(buf4):

class Solution(object):

    def __init__(self):
        # Buffer for read4()
        self.buf4 = ['' for i in range(4)]
    
        # Number of items in Buff4 yet to be added to buffer
        self.buf4Remaining = 0
        
        # Number of characters readh previous
        self.prevCharsRead = 0

        # Have we read all that is in the file ?
        self.endOfFile = False

    def read(self, buf, n):
        """
        :type buf: List[str]
        :type n: int
        :rtype: int
        """
        
        # No characters being read
        if n <= 0:
            return 0
        
        # Number of characters copied
        charactersCopied = 0
        
        # Number of characters read as part of read4()
        charactersRead = 4
        
        
        # First take un read characters from previoous read4() as part of previous read(), if any
        for i in range(self.prevCharsRead - self.buf4Remaining, self.prevCharsRead):
            
            # Copy character
            buf[charactersCopied] = self.buf4[i]
            charactersCopied += 1
            
            # Update remaining buffer, make sure it wont go below 0
            if self.buf4Remaining - 1 >= 0:
                self.buf4Remaining = self.buf4Remaining - 1
            else:
                self.buf4Remaining  = 0

            
            # Check if we hit the required count
            if charactersCopied == n:
                return charactersCopied
            
        # If we have we have exhausted un read charactes from previous fetch of read4()ra
        # and is also at the end of file then we just return it
        if self.endOfFile:
            return charactersCopied
        
        # At this point we have used any remaining characters
        # That were previously fetched
        while charactersRead == 4:
            charactersRead = read4(self.buf4)
            
            # If number of characters read is < 4, it is end of file
            if charactersRead < 4:
                self.endOfFile = True

            for i in range(charactersRead):
                buf[charactersCopied] = self.buf4[i]
                charactersCopied +=1
                
                if charactersCopied == n:
                    # Update chars unread (or remaining) form current fetch of read4()
                    self.buf4Remaining = charactersRead - i - 1
                    self.prevCharsRead = charactersRead
                    return charactersCopied
        

        # Return the count of characters read
        return charactersCopied
        