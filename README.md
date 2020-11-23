# SEApy

*A tool for sonar equation analysis in Python.*

SEApy will allow monostatic sonar detections to be characterised for simple scenarios. Passive sonars, and eventually active sonars, will be modelled at the sonar equation level. Propagation of the signals through the environment will be handled using the [arlpy](https://github.com/org-arl/arlpy) package in Python, which has modules for handling underwater acoustics. Other data regarding the environment and sonars will be sourced from literature. Outputs will include sonar metrics such as signal excess or detection range, as well as environmental data. 
