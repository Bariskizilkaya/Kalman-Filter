import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt


from kf import KF

plt.ion()
plt.figure()

kf = KF(initial_x=0.0, initial_v=0.1, accel_variance=0.1)

DT= 0.1
NUM_STEPS = 1000

mus = []
covs = []

for i in range(NUM_STEPS):
    covs.append(kf.cov)
    mus.append(kf.mean)

    kf.predict(dt=DT)

plt.subplot(2, 1, 1)
plt.title('Position')
plt.plot([mu[0] for mu in mus], 'r')

plt.subplot(2, 1, 2)
plt.title('Velocity')

plt.show()
plt.ginput(1)