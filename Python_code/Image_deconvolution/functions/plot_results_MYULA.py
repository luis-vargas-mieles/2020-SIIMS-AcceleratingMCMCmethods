import matplotlib.pyplot as plt

def plot_results_MYULA(Y,X,meanSamples,logPiTrace,mseValues):

    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica"]})

    'exec(%matplotlib inline)'

    # 1. PLOT ORIGINAL, OBSERVATIONS AND ESTIMATES

    # Plot the original image
    plt.figure(figsize=(16,8))
    plt.subplot(231)
    plt.gray()
    plt.imshow(X)
    plt.title("Original image")

    # Plot the noisy observation
    plt.subplot(232)
    plt.gray()
    plt.imshow(Y)
    plt.title("Blurred and noisy observation")

    # Plot the MMSE of x
    plt.subplot(233)
    plt.gray()
    plt.imshow(meanSamples)
    plt.title("MMSE estimate of $x$")
    
    # Plot the \log\pi trace of the samples
    plt.subplot(234)
    plt.plot(logPiTrace)
    plt.xscale('log')
    plt.xlabel('number of gradient evaluations')
    plt.ylabel('$\log\pi(X_n)$')
    plt.title('$\log\pi$ trace of $X_n$')
    
    # % Plot the evolution of the MSE in stationarity
    plt.subplot(235)
    plt.plot(mseValues)
    plt.xlabel('number of gradient evaluations')
    plt.ylabel('MSE')
    plt.title('Evolution of MSE in stationarity')

    # to show all the plots
    plt.show()