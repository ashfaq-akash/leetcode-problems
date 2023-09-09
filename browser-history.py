class BrowserHistory:

    def __init__(self, homepage: str):
        self.history=[homepage]
        self.curr_length=0
        

    def visit(self, url: str) -> None:
        #It keeps all the history up to and including the current page 
        # and removes everything after that.
        self.history=self.history[:self.curr_length+1]
        self.history.append(url)
        self.curr_length +=1
        

    def back(self, steps: int) -> str:
        #find the value between 0 index and steps
        self.curr_length=max(0,self.curr_length-steps)
        return self.history[self.curr_length]
        

    def forward(self, steps: int) -> str:
        #find the value with in index range i.e. (len(self.history)-1)
        self.curr_length=min(len(self.history)-1,self.curr_length+steps)
        return self.history[self.curr_length]