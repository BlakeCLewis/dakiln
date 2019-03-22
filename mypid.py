class mypid():
    def __init__(self,Cpv,kc=6.0,kp=2.5,ki=0.5,kd=12.5,
                      win=30,imin=-20,imax=20,omin=0,omax=100):

        #time period in seconds
        self._tau = win

        # to minimize math in the pid loop scale the constants

        #Kc is the required output to maintain temp per 100C
        self._Kc = kc / 100

        #time is constant, unless we change it
        self._Kp = kp * 60 / win 
        self._Ki = ki * 60 / win
        self._Kd = kd * 60 / win

        #_Iterm limits: (_Imin <= _Iterm <= _Imax)
        #windup remediation
        self._Imax = imax
        self._Imin = imin
        self._Iterm = 0

        #output limit (_Omin <= output <= _Omax)
        #% of window, (0,100)
        self._Omin = omin
        self._Omax = omax

        #pervious error to compute Dterm
        self._laster = 0

        #what gets returned in manual mode
        #auto mode sets output so when switched to manual it will continue
        self._output = 0

        # false for manual overide mode
        self._auto = True

    def pid(self, Csp, Cpv, Cex):

        if self.auto :
            er = Csp-Cpv
         
            #steady state loss (inside C - outide C) * _Kc
            # heat loss is proportional to temp differitial
            Cterm = self._Kc * (Cpv-Cex)
         
            # P time desired change
            # to enable change in tau without blowing chunks
            # 'delta t' need to be include in the calculation
            Pterm = self._Kp * er
         
            #add last error rate * _Ki to the sum
            self._Iterm += self._Ki * er
            if self._Iterm < self._Imin:
                self._Iterm = self._Imin
            elif self._Iterm > self._Imax:
                self._Iterm = self._Imax
         
            #(delta error rate) * _Kd
            Dterm = self._Kd * (er - _laster)
            self._laster = er
         
            op = (Cterm + Pterm + self._Iterm + Dterm)
         
            if op < _Omin:
                op = _Omin
            elif op > self._Omax:
                op = self._Omax

            self._output = op
            #dataout(Cterm,Pterm,self._Iterm,Dterm,op)

            print(str(Cterm) +'+'+ str(Pterm) +
                 '+'+ str(self._Iterm) +'+'+ str(Dterm) +'='+ str(op))
        else
            print(str(self._output))
            #if in manual mode do nothing and return unchange output
        return(self._output * self._tau /100)

    #setters
    def auto(Cpv, Cex):
        """ switch to auto in a smooth operation
            set Iterm to maintain current output
            zero laster so Dterm does not contribute
            requires internal and external temps
        """
        self._Iterm = self._output - (self._Kc * (Cpv - Cex))
        self._laster = 0
        self.auto=True

    def manual(op):
        """"pause pid calculation
            set output = op
        """
        self._output = op
        self.auto = False

    def set_Kc(self, Kacie):
        self._Kc = Kacie / 100

    def set_Kp(self, Kpee):
        self._Kp = Kpee * 60 / self.tau

    def set_Ki(self, Kai):
        self._Ki = Kai * 60 / self.tau

    def set_Kd(self, Kadee):
        self._Kd = Kadee * 60 / self.tau

    def set_Imin(self, eyemin):
        self._Imin = eyemin

    def set_Imax(self, eyemax):
        self._Imax = eyemax

    def set_Omin(self, ohmin):
        self._Omin = ohmin

    def set_Omax(self, ohmax):
        self._Omax = ohmax

    def set_tau(self, bod):
        self._Kp *= self._tau / bod
        self._Ki *= self._tau / bod
        self._Kd *= self._tau / bod
        self._tau = bod

    #getters 
    def get_Kc(self):
        return self._Kc * 100

    def get_Kp(self):
        return self._Kp * self._tau / 60

    def get_Ki(self):
        return self._Ki * self._tau / 60

    def get_Kd(self):
        return self._Kd * self._tau / 60

    def get_Imin(self):
        return self._Imin

    def get_Imax(self):
        return self._Imax

    def get_Omax(self):
        return self._Omax

    def get_tau(self):
        return self._tau

    def get_Iterm(self):
        return self._Iterm

    def is_auto(self):
        return self._auto
