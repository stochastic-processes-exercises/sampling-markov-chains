try:
    from AutoFeedback.funcchecks import check_func 
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func

from AutoFeedback.randomclass import randomvar
import unittest
from main import *

class helper : 
    def check_mean( n, probs, start ) :
        m = 0
        for i in range(n) : m = m + markov_move( probs, start ) 
        return m / n

class UnitTests(unittest.TestCase) :
    def test_variable(self) : 
       inputs, variables = [], []
       
       mat1 = np.array([[0.3,0.5,0.2],[0.3,0.4,0.3],[0.2,0.5,0.3]])
       for j in range(3) : 
           exp = np.dot( mat1[j,:], myvars )
           var = var = np.dot( mat1[j,:], myvars*myvars ) - exp*exp
           for i in range(10): 
               inputs.append((mat1,j,))
               myvar = randomvar( exp, variance=var, vmin=0, vmax=2, isinteger=True )
               variables.append( myvar )
       mat2 = np.array([[1,0,0,0,0],[1/3,1/3,1/3,0,0],[0,0.5,0,0.5,0],[0,0.5,0,0,0.5],[0,0,0,0,1]])
       for j in range(3) : 
           exp = np.dot( mat2[j,:], myvars )
           var = var = np.dot( mat2[j,:], myvars*myvars ) - exp*exp
           for i in range(10): 
               inputs.append((mat2,j,))
               myvar = randomvar( exp, variance=var, vmin=0, vmax=2, isinteger=True )
               variables.append( myvar ) 

       assert( check_func("markov_move", inputs, variables ) )

    def test_mean(self) : 
       inputs, variables = [], []
       mat1 = np.array([[0.3,0.5,0.2],[0.3,0.4,0.3],[0.2,0.5,0.3]])
       for j in range(3) : 
           exp = np.dot( mat1[j,:], myvars )
           var = var = np.dot( mat1[j,:], myvars*myvars ) - exp*exp
           for i in range(5):  
               nmean = (i+1)*10
               inputs.append((nmean,mat1,j))
               myvar = randomvar( exp, variance=var/nmean, vmin=0, vmax=4, isinteger=False )
               variables.append( myvar )

       assert( check_func("check_mean", inputs, variables, modname=helper ) )
