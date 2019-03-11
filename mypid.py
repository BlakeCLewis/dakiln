class mypid():
    def __init__(self,Cpv,kc=6.0,kp=2.5,ki=0.5,kd=12.5,window=30,imax=20,imin=-20,omax=100):

        #initialize Csps to current kiln temp set up 0 error
        self.sp = Cpv
 
        #sp[0] is current Csp
        #sp[1] is previous Csp

        self.Kc = kc
        self.Kp = kp
        self.Ki = ki
        self.Kd = kd

        #time period in seconds
        self.Win = window

        #Iterm limits: (Imin <= Iterm <= Imax)
        self.Imax = imax
        self.Imin = imin
        self.Iterm = 0

        #output limit (0 <= output <= Omax)
        self.Omax = omax

        #intialize errors
        self.lastErrr = 0

    def pid(self, Csp, Cpv, Cex):
        er = Csp-Cpv

        #steady state loss (inside C - outide C) * Kc, Cterm ~= 6/100C
        Cterm = self.Kc * (Cpv-Cex) / 100

        # P time desired change
        Pterm = self.Kp * er * 60 / self.Win

        #add last error rate * Ki to the sum
        self.Iterm += self.Ki * er * 60 / self.Win
        if self.Iterm < self.Imin:
            self.Iterm = self.Imin
        elif self.Iterm > self.Imax:
            self.Iterm = self.Imax

        #(delta error rate) * Kd
        Dterm = self.Kd * (er - laster) * 60 / self.Win
        self.laster = er

        output = (Cterm + Pterm + self.Iterm + Dterm)
        print(str(Cterm) +'+'+ str(Pterm) +'+' + str(self.Iterm) +'+' + str(Dterm))
        if output < 0:
            output = 0
        elif output > self.Omax:
            output = self.Omax
        return(output/100 * self.Win)

    def setKc(self,Kacie):
        self.Kc=Kacie

    def setKp(self,Kpee):
        self.Kp=Kpee

    def setKi(self,Kai):
        self.Ki=Kai

    def setKd(self,Kadee):
        self.Kd=Kadee

    def setImin(self,hymin):
        self.Imin=hymin

    def setImax(self,eyemax):
        self.Imax=eyemax

    def setOmax(self,ohmax):
        self.Omax=ohmax

    def setWin(self,bod):
        self.Win=bod

    def setI(self,eye):
        self.Iterm = eye

    #getters
    def getKc(self):
        return self.Kc

    def getKp(self):
        return self.Kp

    def getKi(self):
        return self.Ki

    def getKd(self):
        return self.Kd

    def getImin(self):
        return self.Imin

    def getImax(self):
        return self.Imax

    def getOmax(self):
        return self.Omax

    def getWin(self):
        return self.Win

    def getIterm(self):
        return self.Iterm
