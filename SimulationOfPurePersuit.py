import numpy as np
import matplotlib.pyplot as plt


def main():
    vf = 50
    xf,yf = np.random.randint(-500,500,2)
    xb,yb = np.random.randint(-500,500,2)

    minDist = int(input("Enter minimum distance to caught Bomber : "))
    #print(type(minDist))
    maxDist = 900

    fx = []
    fy = []
    bx = []
    by = []

    fx.append(xf)
    fy.append(yf)
    bx.append(xb)
    by.append(yb)

    cnt = 0
    while(True):
        dist = np.sqrt((xb-xf)**2 + (yb-yf)**2)
        print(dist)
        cnt += 1
        if dist<minDist:
            print("The Bomber is caught at step : "+str(cnt))
            flag = True
            break
        elif dist>=maxDist:
            print("The Bomber escaped away at step : "+str(cnt))
            flag = False
            break
        else:
            cosA,sinA = (xb - xf)/dist, (yb-yf)/dist
            xf = xf + vf * cosA
            yf = yf + vf * sinA
            xb,yb = np.random.randint(-500,500,2)

            fx.append(xf)
            fy.append(yf)
            bx.append(xb)
            by.append(yb)

    #plt.scatter(fx,fy)
    #plt.scatter(bx,by)
    plt.plot(bx,by)
    plt.plot(fx,fy)
    
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.title('Fighter vs Bomber \n  Bomber '+('caught ' if flag == True else 'escaped' )+ ' at step '+ str(cnt))
    plt.legend(['Bomber','Fighter'])
    plt.show()


main()