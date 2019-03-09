class mypid():
    def __init__(self,Cpv,kc=6.0,kp=3.0,ki=3.0,kd=3.0,window=30,imax=40,imin=-40,omax=1):

        #initialize Csps to current kiln temp set up 0 error
        self.sp = []
        self.sp.append(Cpv)
        self.sp.append(Cpv)
 
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
        self.er = []
        self.er.append(0)
        self.er.append(0)
        #new Csp n, time period is not over
        #er[0] is n-1, error from last window
        #er[1] is n-2, error from window before last

    def pid(self, Csp, Cpv, Cex):
        self.sp.insert(0, Csp)
        self.sp.pop()
        self.er.insert(0, self.sp[1]-Cpv)
        self.er.pop()

        #steady state loss (outide C - inside C) * Kc, Cterm ~= 6/100C
        Cterm = self.Kc * (Cpv-Cex) / 100

        # P time desired change
        Pterm = self.Kp * (Csp-Cpv) * self.Win / 60

        #add last error rate * Ki to the sum
        self.Iterm += self.Ki * self.er[0] * self.Win / 60
        if self.Iterm < self.Imin:
            self.Iterm = self.Imin
        elif self.Iterm > self.Imax:
            self.Iterm = self.Imax

        #(delta error rate) * Kd
        Dterm = self.Kd * (self.er[0] - self.er[1]) * self.Win / 60
        output = (Cterm + Pterm + self.Iterm + Dterm) / 100
        print(str(Cterm) +'+'+ str(Pterm) +'+' + str(self.Iterm) +'+' + str(Dterm))
        if output < 0:
            output = 0
        elif output > self.Omax:
            output = self.Omax
        return(output * self.Win)

    #setters, I believe in changing one thing at a time
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
