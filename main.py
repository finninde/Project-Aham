from optimizer import Optimizer



if __name__ == "__main__":
   opt = Optimizer(elementer=[7,5,8,1,4,3,2,9,11,50,17,22,34,11,5,99,1,42,24])
   # print ([7,5,8,1,4,3,2,9,11,50,17,22,34,11,5,99,1,42,24])
   print(opt.solveSA())
   print(opt.solve()) 
