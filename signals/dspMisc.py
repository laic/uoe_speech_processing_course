import sys
import matplotlib.pyplot as plt
import numpy as np

import cmath
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
plt.style.use('ggplot')

## Plot a waveform in time
def plot_waveform(time_steps, amplitudes, title="time vs amplitude", ylim=(-2,2), figsize=(16,4)):
    fig, timedom = plt.subplots(figsize=(16, 4))
    timedom.scatter(time_steps, amplitudes, color='magenta')
    timedom.plot(time_steps, amplitudes, color='magenta')
    timedom.set_xlabel("time (s)")
    timedom.set_ylabel("Amplitude")
    timedom.set_title(title)
    timedom.set_ylim(-2,2)
    
    return fig, timedom


## Plot a magnitude spectrum
def plot_mag_spectrum(output_frequencies, magnitudes,  title='Magnitude spectrum', figsize=(14,4)):
    fig, fdom = plt.subplots(figsize=figsize)
    fdom.stem(output_frequencies, magnitudes, 'b', use_line_collection=True) 
    fdom.set_xlabel('Freq (Hz)')
    fdom.set_ylabel('Magnitude')
    fdom.set_title(title)
    return fig, fdom

## Zoom in on a magnitude spectrum plot
def zoom_mag_spectrum(output_frequencies, magnitudes, center, window=50, title='Magnitude spectrum', figsize=(14,4)):
    fig, fdom = plt.subplots(figsize=figsize)
    fdom.stem(output_frequencies, magnitudes, 'b', use_line_collection=True) 
    fdom.set_xlabel('Freq (Hz)')
    fdom.set_ylabel('Magnitude')
    fdom.set_title(title)
    fdom.set_xlim((center-window, center+window))
    
    return fig, fdom

## A function that returns the complex numbers corresponding to the sine wave
## from time t=Tmin to Tmax, given a sample time of t_step and a desired 
## frequency (freq)

def gen_phasor_vals_freq(Tmin=0, Tmax=10, t_step=0.23, freq=None):
    # Tmin, Tmax : seconds
    # c_s : cycles/sample
    # theta_s = radians/sample
    # freq = cycles/sec -> 2*pi*f radians/sec
    # 2*pi*f * tmax radians in Tmax seconds 
    
    tsteps = np.arange(Tmin, Tmax, t_step)
    if freq != None:
        rads_per_sec = 2*np.pi*freq
        theta_s = t_step*rads_per_sec
        thetas = np.arange(Tmin*rads_per_sec, Tmax*rads_per_sec, theta_s)
    else: 
        thetas = np.arange(Tmin, Tmax, t_step)

    ## A sequence of complex numbers with r=1, theta=t, for t in ts
    zs = np.exp(1j*thetas)
 
    ## For convenience we return the theta values and time steps as well
    return zs, thetas, tsteps


def plot_phasor_and_sinusoid_static(As, Bs, thetas, xlim=(0,7), ylim=(-2,2), R=1):
    
    fig, (phasor, sinusoid) = plt.subplots(1, 2, gridspec_kw={'width_ratios': [4, 7]}, figsize=(15,5))
    phasor.set(xlim=ylim, ylim=ylim)

    ## plot the phasor: these are our complex zs values, i.e. e^(j*theta)
    ## Since we set the magnitude to r=1, all these points sit nicely on the unit circle

    ## Add in some axes lines
    phasor.plot(ylim, [0,0], color='grey')
    phasor.plot([0,0],ylim, color='grey')

    ## Plot the unit circle in grey just to check 
    circle1 = plt.Circle((0, 0), R, color='grey',fill=False)
    phasor.add_artist(circle1)

    ## plot our complex numbers (rectangular coordinates)
    phasor.scatter(As, Bs)

    ## Some labels for the left hand plot
    phasor.set_xlabel("Real Component")
    phasor.set_ylabel("Imaginary Component")


    ## plot the sinusoid on the right: sin(theta)
    ## The x-axis represents our theta values (think of this as time)
    ## The y-axis is sin(theta)
    sinusoid.set(xlim=xlim, ylim=ylim)
    sinusoid.plot(thetas, R*np.sin(thetas), color='grey')
    sinusoid.plot(thetas, Bs, 'o')

    #print(R)
    ## Some labels for the right hand plot
    sinusoid.set_ylabel("Amplitude")
    sinusoid.set_xlabel("Time ($t$ radians = $t$ seconds) ")
    
    return fig, phasor, sinusoid


def plot_phasor_and_sinusoid(R=1, theta_min=0, theta_max=7, theta_step=0.23):
    
    thetas = np.arange(theta_min, theta_max, theta_step)
    ## Generate sequence of complex numbers with r=1, theta=theta, for theta in thetas
    
    zs = R*np.exp(1j*thetas)
    
    As = np.real(zs)
    Bs = np.imag(zs)
    
    #print(As.shape, Bs.shape, thetas.shape)
    
    fig, phasor, sinusoid = plot_phasor_and_sinusoid_static(As, Bs, thetas, xlim=(theta_min, theta_max), R=R)
    
    n_samples = As.shape[0]
    
    A = np.array(As).reshape(n_samples, 1)
    B = np.array(Bs).reshape(n_samples, 1)

    zeros = np.zeros(n_samples).reshape(n_samples, 1)
    A = np.concatenate([zeros, A], axis=1)
    B = np.concatenate([zeros, B], axis=1)    
    
    ## Some initialization
    line = phasor.plot([], [], color='b', lw=3)[0]
    point = phasor.plot([], [], 'o', color='b',  markersize=10)[0]
    sin_t = sinusoid.plot([], [], 'o', color='b', markersize=10)[0]

    ## Set axes lables
    phasor.set_xlabel("Real Component")
    phasor.set_ylabel("Imaginary Component")
    sinusoid.set_xlabel("Time ($t$ radians = $t$ seconds) ")
    sinusoid.set_ylabel("Amplitude")


    ## Do the animation!
    def anim_sinusoid(i):
        t = thetas[i]
        line.set_data(A[i, :], B[i,:])
        point.set_data(A[i, 1], B[i,1])
        sin_t.set_data(t, B[i, 1])

    anim = FuncAnimation(
        fig, lambda x: anim_sinusoid(x), interval=600, frames=n_samples)
 
    return anim


def create_phasor_sinusoid_bkg(Tmin, Tmax, ymax=2, plot_phasor=True, plot_real=False, plot_imag=True, color='grey'): 
    
    fig_width=15
    if plot_real and plot_phasor:
        fig_height = 15
    else: 
        fig_height = 4.5
    
  
    fig = plt.figure(figsize=(fig_width,fig_height))
    
    phasor, rproj, iproj = None, None, None
    
    if plot_phasor and plot_real:

        gs = fig.add_gridspec(3, 3)
        phasor = fig.add_subplot(gs[0, 0])
        phasor.set(xlim=(-ymax, ymax), ylim=(-ymax, ymax))
        phasor.plot([-ymax,ymax], [0,0], color=color)
        phasor.plot([0,0],[-ymax,ymax], color=color)
        circle1 = plt.Circle((0, 0), 1, color=color,fill=False)
        phasor.add_artist(circle1)

        rproj = fig.add_subplot(gs[1:, 0])
        rproj.set(ylim=(Tmax+0.1, Tmin-0.1), xlim=(-ymax, ymax))
        rproj.plot([0,0], [Tmin-1, Tmax+1], color=color)


        if plot_imag:
            iproj = fig.add_subplot(gs[0, 1:])  
            iproj.set(xlim=(Tmin-0.1, Tmax+0.1), ylim=(-ymax, ymax))
            iproj.plot([Tmin-1,Tmax+1], [0,0], color=color)

    elif plot_phasor and not plot_real:
        gs = fig.add_gridspec(1, 3)
        phasor = fig.add_subplot(gs[0, 0])
        phasor.set(xlim=(-ymax, ymax), ylim=(-ymax, ymax))
        phasor.plot([-ymax,ymax], [0,0], color=color)
        phasor.plot([0,0],[-ymax,ymax], color=color)
        circle1 = plt.Circle((0, 0), 1, color=color,fill=False)
        phasor.add_artist(circle1)

        if plot_imag:
            iproj = fig.add_subplot(gs[0, 1:])  
            iproj.set(xlim=(Tmin-0.1, Tmax+0.1), ylim=(-ymax, ymax))
            iproj.plot([Tmin-1, Tmax+1], [0,0], color=color)


    elif not plot_phasor and plot_real and plot_imag:
            gs = fig.add_gridspec(1, 2)

            rproj = fig.add_subplot(gs[0, 0])
            rproj.set(xlim=(Tmin-0.1, Tmax+0.1), ylim=(-ymax, ymax))
            rproj.plot([Tmin-1,Tmax+1], [0,0], color=color)

            iproj = fig.add_subplot(gs[0, 1])  
            iproj.set(xlim=(Tmin-0.1, Tmax+0.1), ylim=(-ymax, ymax))
            iproj.plot([Tmin-1,Tmax+1], [0,0], color=color)


    else: 
        print(plot_phasor, plot_real_, plot_imag)

    return fig, phasor, iproj, rproj



def get_phasor_animation(X, Y, tsteps, phasor, iproj, rproj, fig, Xlist=None, Ylist=None, params=None):
    line = phasor.plot([], [], color='b', lw=3)[0]
    lines = []
    circles = []
    phasor_points = []

    if params: 
        for l in range(len(params)):
            lines.append(phasor.plot([], [], color='C'+str(l), lw=3)[0])
            circles.append(plt.Circle((0, 0), params[l][0], color='C'+str(l), fill=False, lw=1))
            phasor.add_patch(circles[-1])
            phasor_points.append(phasor.plot([], [], 'o', color='C0')[0])


    else:
        lines.append(phasor.plot([], [], color='C0', lw=3)[0])
        circles.append(plt.Circle((0, 0), 1, color='grey', fill=False, lw=1))
        phasor.add_patch(circles[-1])
        phasor_points.append(phasor.plot([], [], 'o', color='C0')[0])

    ## Set up sinusoid animation
    imag_t, real_t = None, None
    if iproj:
        imag_t = iproj.plot([], [], 'o', color='C0')[0]
    
    if rproj:
        real_t = rproj.plot([], [], 'o', color='C0')[0]


    figs = (lines, phasor_points, circles, imag_t, real_t) 


    if Xlist == None:
        Xlist = [X]
    if Ylist == None:
        Ylist = [Y]
        
    ## Call the animation function
    anim = FuncAnimation(
        fig, lambda x: anim_superposition(x, X=X, Y=Y, Xlist=Xlist, Ylist=Ylist, tsteps=tsteps, figs=figs), interval=600, frames=len(tsteps))
 
    ## Make a video!     
    vid = HTML(anim.to_html5_video())
    return vid


## Now Let's animate it
def anim_superposition(i, X, Y, Xlist, Ylist, tsteps, figs):
    #line.set_data(X[i, :], Y[i,:])
    lines, phasor_points, circles, imag_t, real_t = figs
    if imag_t:
        imag_t.set_data(tsteps[i], Y[i, 1])
        
    if real_t: 
        real_t.set_data(X[i,1], tsteps[i])


    
    if Xlist != []:
        currXs = [Xlist[0][i,0], Xlist[0][i,1]]
        currYs = [Ylist[0][i,0], Ylist[0][i,1]]


        lines[0].set_data(currXs, currYs)
        phasor_points[0].set_data(currXs[1], currYs[1])
        #print("len(Xlist)", len(Xlist))
        for n in range(1,len(Xlist)): 
            #phasor.add_artist(circles[n])
            #print(n, len(circles))
            circles[n].center = (currXs[1], currYs[1])
            currXs = [currXs[1], currXs[1]+Xlist[n][i,1]]
            currYs = [currYs[1], currYs[1]+Ylist[n][i,1]]
            
            lines[n].set_data(currXs, currYs)
            phasor_points[n].set_data(currXs[1], currYs[1])
        

## Create the background plot
def create_anim_bkg(tsteps, thetas, freqs, mags=1, dense_tstep=0.001, ymax=2): 
    fig, (phasor, sinusoid) = plt.subplots(1, 2, gridspec_kw={'width_ratios': [4, 7]}, figsize=(15,5))
    phasor.set(xlim=(-ymax, ymax), ylim=(-ymax, ymax))

    Tmin = np.min(tsteps)
    Tmax =np.max(tsteps)
    
    phasor.plot([-ymax,ymax], [0,0], color='grey')
    phasor.plot([0,0],[-ymax,ymax], color='grey')
    circle1 = plt.Circle((0, 0), 1, color='grey',fill=False)
    
    phasor.add_artist(circle1)

    sinusoid.set(xlim=(np.min(tsteps)-0.1, np.max(tsteps)+0.1), ylim=(-ymax, ymax))
    
    ## A higher resolution one for reference
    if type(freqs) is list:
        for k in range(len(freqs)):
            _, dense_thetas, dense_tsteps = gen_phasor_vals_freq(Tmin, Tmax, dense_tstep, freqs[k])
            if type(mags) is list:
                sinusoid.plot(dense_tsteps, mags[k]*np.sin(dense_thetas), color='grey')
            else:
                sinusoid.plot(dense_tsteps, mags*np.sin(dense_thetas), color='grey')
    else:
            _, dense_thetas, dense_tsteps = gen_phasor_vals_freq(Tmin, Tmax, dense_tstep, freqs)
            sinusoid.plot(dense_tsteps, np.sin(dense_thetas), color='grey')
    return fig, phasor, sinusoid

## Get those 'clockhand' lines
def get_line_coords(Xs, Ys):
    n_samples = Xs.size
    X = np.array(Xs).reshape(n_samples, 1)
    Y = np.array(Ys).reshape(n_samples, 1)
    zeros = np.zeros(n_samples).reshape(n_samples, 1)

    X = np.concatenate([zeros, X], axis=1)
    Y = np.concatenate([zeros, Y], axis=1)  
    return X, Y, n_samples

## Animate 
def anim_sinusoid(i, X, Y, tsteps, figs):
    line, sin_t = figs 
    line.set_data(X[i, :], Y[i,:])
    sin_t.set_data(tsteps[i], Y[i, 1])

def plot_phasor_static(zn, time_steps, ymax=1.5, plot_phasor=True, plot_real=False, plot_imag=True, color='grey'):
    ## Get the real and imaginary bits of each of these complex numbers so we can make a 2-D plot
    zn_real = np.real(zn )
    zn_imag = np.imag(zn )
    X, Y, n_samples = get_line_coords(zn_real , zn_imag )

    ## We know we're starting from 0 radians and going to 2pi radians in steps of 2pi/N
    Tmin = np.min(time_steps)
    Tmax = np.max(time_steps)

    ## Plot the phasor and corresponding sinusoid
    fig, phasor, iproj, rproj = create_phasor_sinusoid_bkg(Tmin, Tmax, ymax=ymax, plot_phasor=plot_phasor, plot_real=plot_real, plot_imag=plot_imag)

    ## Plot the complex numbers (i.e. the phasor)
    if plot_phasor:
        phasor.scatter(zn_real, zn_imag , color=color)
        phasor.set_xlabel('real component')
        phasor.set_ylabel('imaginary component')

    ## Plot the imaginary part of the complex numbers (i.e., the sinusoid)
    if plot_imag:
        iproj.plot(time_steps, zn_imag, color=color)
        iproj.scatter(time_steps, zn_imag, color=color)
        iproj.set_xlabel('time')
        iproj.set_ylabel('amplitude')
        
    if plot_real:
        if not plot_phasor: 
            rproj.plot(time_steps, zn_real,  color=color)
            rproj.scatter(time_steps, zn_real, color=color)
            rproj.set_xlabel('time')
            rproj.set_ylabel('amplitude')
        else:
            rproj.plot(zn_real, time_steps, color=color)
            rproj.scatter(zn_real, time_steps, color=color)
            
            rproj.set_xlabel('amplitude')
            rproj.set_ylabel('time')
    
    return X, Y, fig, phasor, iproj, rproj

def get_dft_phasors(N, centered=False):
    nsteps = np.array(range(N))
    if centered:
        nsteps = nsteps - floor(N/2)
        print(nsteps)
        
    theta_step = 2*np.pi/N
    theta_steps = theta_step * nsteps
    phasors = {}
    for k in range(N):
        zs = np.exp(k*-1j*theta_steps) 
        real = np.real(zs)
        imag = np.imag(zs)    
        phasors[k] = {'zs':zs, 'real':real, 'imag':imag, 'thetas':theta_steps, 'theta_step':theta_step}
        
    return phasors

def get_dft_outputs(x, phasors):
    DFT = []
    
    ## Go through our like of phasors
    for k, phasor in phasors.items():
        ## Do the dot product between the input and each phasor sequence
        DFT.append(np.sum(x * phasor['zs']))

    return DFT



def get_dft_mag_phase(x, seq_len):
    phasors = get_dft_phasors(seq_len)
    
    dft = get_dft_outputs(x, phasors)
    
    dft_polar = [cmath.polar(z) for z in dft]
    
    mags = np.array([m for m, _ in dft_polar])
    phases = np.array([ph if mag > 0.00001 else 0 for mag, ph in dft_polar])
    
    return mags, phases


def gen_sinusoid(frequency, phase, amplitude=1, sample_rate=64, seq_length=64, gen_function=np.cos): 
    
    # get a vector of indices representing the positions in the sequence we want to generate
    nsteps = np.array(range(seq_length))
    
    # calculate the time each sample takes given the sampling rate
    sample_time = 1/sample_rate
    time_steps = sample_time * nsteps
    
    # A sinusoid's wave length (aka period) is how long it takes to complete one cycle (in seconds)
    # which is just the inverse of the frequency.
    wavelen = 1/frequency 
    
    # Now we can calculate how many samples it will take to complete one cycle:
    samples_per_cycle = wavelen/sample_time
    
    # 1 cycle = 2pi radians. So if it takes samples_per_cycle steps to complete a cycle, 
    # we need each sample to correspond to 2pi/samples_per_cycle radians: 
    theta_step = 2*np.pi/samples_per_cycle
    
    # Calculate all the angle (theta) values for our desired sequence:
    theta_steps = theta_step * nsteps

    # Calculate the function for that sequence of angles with given phase adjustment
    # We made the actual function a variable so we can swap between sin and cos as we like. 
    
    x = amplitude * gen_function(theta_steps + phase)
    
    return x, time_steps

## Calculate the frequencies associated with each DFT output
def get_dft_freqs_all(sample_rate, seq_len):
    ## Get the minimum frequency
    f_min = sample_rate/seq_len
    
    ## All the other frequencies are just integer multiples of the minimum frequency
    ## We have 0,...,seq_len-1 outputs
    dft_outs = np.arange(seq_len)
    
    return f_min * dft_outs

def make_impulse_train(sample_rate, frequency, n_samples):    
    # make an arrange of n_samples, all zeros to start
    x = np.zeros(n_samples)
    
    # Determine where the impulses go based on the sample rate
    # The time between samples: sample_time = 1/sample_rate
    
    #A frequency of f cycles/second means the wavelength=1/f
    # So samples_per_cycle = wavelength/t_s = 1/frequency / 1/sample_rate = sample_rate/frequency
    
    ## We need to round to the nearest integer
    samples_per_cycle = round(sample_rate/frequency)
    
    # Set indices for impulses
    impulse_positions = np.arange(0, n_samples, samples_per_cycle)
    #print("impulse_positions:", impulse_positions)
    # set the impulses
    x[impulse_positions] = 1
    
    ## return the time steps associated with the impulse train samples
    nsteps = np.array(range(n_samples))
    time_steps = (1/sample_rate) * nsteps   
    
    return x, time_steps

def fir_filter(x, filter_coeffs):
    N = len(x)
    K = len(filter_coeffs)
    
    y = np.zeros(N)   
    for n in range(N):
        for k in range(K):
            if n-k >= 0: 
                #print("y[%d]=%f, b[%d]=%f, x[%d]=%f" % (n, y[n], k, filter_coeffs[k], n-k, x[n-k]))
                y[n] = y[n] + (filter_coeffs[k]*x[n-k])
        #print("y[%d]=%f" % (n, y[n]))
    return y    

