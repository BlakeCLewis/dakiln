class mypid():
    def __init__(self,Cpv,kc=6.0,kp=2.5,ki=0.5,kd=12.5,
                      win=30,imax=20,imin=-20,omax=100,omin=0):

        self.Kc = kc
        self.Kp = kp
        self.Ki = ki
        self.Kd = kd

        #time period in seconds
        self.tau = win

        #Iterm limits: (Imin <= Iterm <= Imax)
        #windup remediation
        self.Imax = imax
        self.Imin = imin
        self.Iterm = 0

        #output limit (Omin <= output <= Omax)
        #I am using % of window, so (0,100)
        self.Omin = omin
        self.Omax = omax

        #pervious error to compute Dterm
        self.laster = 0

        #what gets returned in manual mode
        #auto mode sets output so when switched to manual it will continue
        self.output = 0

        # false for manual overide mode
        self.auto = True

    def pid(self, Csp, Cpv, Cex):

        if self.auto :
            er = Csp-Cpv
         
            #steady state loss (inside C - outide C) * Kc, Cterm ~= 6/100C
            Cterm = self.Kc * (Cpv-Cex) / 100
         
            # P time desired change
            Pterm = self.Kp * er * 60 / self.tau
         
            #add last error rate * Ki to the sum
            self.Iterm += self.Ki * er * 60 / self.tau
            if self.Iterm < self.Imin:
                self.Iterm = self.Imin
            elif self.Iterm > self.Imax:
                self.Iterm = self.Imax
         
            #(delta error rate) * Kd
            Dterm = self.Kd * (er - laster) * 60 / self.tau
            self.laster = er
         
            op = (Cterm + Pterm + self.Iterm + Dterm)
         
            if op < Omin:
                op = Omin
            elif op > self.Omax:
                op = self.Omax

            self.output = op
            #dataout(Cterm,Pterm,self.Iterm,Dterm,op)

            print(str(Cterm) +'+'+ str(Pterm) +
                 '+'+ str(self.Iterm) +'+'+ str(Dterm) +'='+ str(op))
        else
            print(str(self.output)) 

        return(self.output/100 * self.tau)

    #setters
    def auto(Cpv, Cex):
        self.Iterm = self.output - (self.Kc * (Cpv - Cex))
        self.laster = 0
        self.auto=True

    def manual():
        self.auto=False

    def setKc(self, Kacie):
        self.Kc=Kacie

    def setKp(self, Kpee):
        self.Kp=Kpee

    def setKi(self, Kai):
        self.Ki=Kai

    def setKd(self, Kadee):
        self.Kd=Kadee

    def setImin(self, hymin):
        self.Imin=hymin

    def setImax(self, eyemax):
        self.Imax=eyemax

    def setOmax(self, ohmin):
        self.Omin=ohmin

    def setOmax(self, ohmax):
        self.Omax=ohmax

    def settau(self, bod):
        self.tau=bod

    def setI(self, eye):
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

    def gettau(self):
        return self.tau

    def getIterm(self):
        return self.Iterm

    def getauto(self):
        return self.auto
