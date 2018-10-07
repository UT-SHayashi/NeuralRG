import numpy as np

import matplotlib.pyplot as plt

T = np.array([2.0,2.1,2.2,2.269185314213022,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4.0])

loss4 = np.array([-660.8114624023438,-632.1803588867188,-606.3014526367188,-589.8558349609375,-582.8676147460938,-561.7283935546875,-542.5540771484375,-525.42822265625,-509.8653259277344,-495.833740234375,-483.4316101074219,-471.79595947265625,-460.8268127441406,-450.578125,-440.88507080078125,-431.655029296875,-422.89642333984375,-414.6001281738281,-406.6899719238281,-399.1446533203125,-391.9564208984375,-385.09051513671875])
error4 = np.array([1.7541759014129639,1.8155813217163086,1.9253315925598145,2.0584123134613037,2.0805788040161133,2.16274094581604,2.2931642532348633,2.5501935482025146,2.721217393875122,2.8084778785705566,2.8225061893463135,2.6416027545928955,2.5264179706573486,2.355006694793701,2.172619581222534,2.051321029663086,1.8871386051177979,1.7875169515609741,1.7098944187164307,1.655775785446167,1.572643518447876,1.5070385932922363])

loss3 = np.array([-660.7703857421875,-632.1431884765625,-606.2661743164062, -589.8319091796875,-582.8795166015625,-561.7555541992188,-542.6287841796875,-525.4150390625,-509.80499267578125,-495.8456726074219,-483.4354553222656,-471.7495422363281 ,-460.8287048339844,-450.5749816894531,-440.892578125,-431.66265869140625,-422.8913879394531,-414.60308837890625,-406.69451904296875,-399.16082763671875,-391.97930908203125,-385.0999755859375])
error3 = np.array([1.7489417791366577,1.8215904235839844,1.9426887035369873,2.045691728591919,2.0899007320404053,2.19616961479187,2.305957794189453,2.5562875270843506,2.724430799484253,2.8280515670776367,2.8204421997070312,2.671971559524536,2.4974122047424316,2.3413941860198975,2.1695358753204346,2.04917573928833,1.8850228786468506,1.7840720415115356,1.7057580947875977,1.6592161655426025,1.5546411275863647,1.5196353197097778])

loss2 = np.array([-660.5372314453125,-631.9585571289062,-606.1282958984375,-589.7266845703125,-582.7877197265625,-561.6671142578125,-542.4461059570312,-525.3724365234375,-509.6693420410156,-495.7134704589844,-483.3159484863281,-471.6287536621094,-460.7500305175781,-450.5279846191406,-440.8013916015625,-431.5873718261719, -422.8689880371094,-414.5578918457031,-406.69757080078125,-399.16082763671875,-391.96539306640625,-385.08447265625])
error2 = np.array([1.9227865934371948,1.9606374502182007,2.044910430908203,2.086923599243164,2.113051176071167,2.2301511764526367,2.382844924926758,2.5329272747039795,2.696244955062866,2.8303074836730957,2.8549323081970215,2.6560771465301514,2.480417013168335,2.336071014404297,2.202723264694214,2.0560712814331055,1.8849371671676636,1.7851262092590332,1.6854944229125977,1.6048671007156372,1.556736707687378,1.5381077527999878])

loss1 = np.array([-657.83349609375,-629.3168334960938,-603.5908203125,-587.3035278320312,-580.3790893554688,-559.396240234375,-540.4917602539062,-523.4420776367188,-508.196044921875,-494.52703857421875,-482.1485290527344,-470.4715270996094,-459.59222412109375,-449.3321533203125,-439.6451721191406, -430.4402770996094,-421.6690368652344,-413.3812255859375,-405.4845886230469,-397.9621276855469,-390.7708435058594,-383.8777770996094])
error1 = np.array([3.5358023643493652,3.4930570125579834,3.494251251220703,3.472852945327759,3.4716286659240723,3.492495059967041,3.5089499950408936,3.4747118949890137,3.593388319015503,3.570796251296997,3.2837181091308594,3.3675243854522705,3.1811258792877197,3.029836654663086,2.907766342163086,2.7808446884155273,2.6098499298095703,2.5168089866638184,2.44477915763855,2.418466091156006,2.343379259109497,2.2579026222229004])

exact = np.array([263.29621043402125,252.8952741554581,243.9756979903575,238.64225663513287,236.59802766605696,230.73226236763298,225.81063208450638,221.61042433293028,217.98034240765568,214.8124996751394,212.02620699629517,209.55912671601234,207.36199723365263,205.3952226411796,203.6265417951376,202.02937207957373,200.5815982852197,199.26466694507747,198.062896703667,196.96294518951674,195.95339152219043,195.02440568563682])

fix = np.array([399.418793393396,381.48763983688104,364.9500280838529,354.2334832224499,349.63580114185936,335.4021735990462,322.1283767570811,309.71152104410737,298.0633635462919,287.1077569484564,276.7786173540166,267.0182914050078,257.7762336924401,249.0079274825673,240.67399785651475,232.7394782121657,225.17319990633018,217.9472814559404,211.03669875668663,204.4189216344791,198.0736050203686,191.9823253518871])

res1 = np.abs(-loss1-exact-fix)
res2 = np.abs(-loss2-exact-fix)
res3 = np.abs(-loss3-exact-fix)
res4 = np.abs(-loss4-exact-fix)

error4 /= (512)**0.5
error3 /= (512)**0.5
error2 /= (512)**0.5
error1 /= (512)**0.5

'''
ax1 = plt.subplot(2,1,1)

ax1.plot(T,res1,label="depth = 1")
ax1.plot(T,res2,label="depth = 2")
ax1.plot(T,res3,label="depth = 3")
ax1.plot(T,res4,label="depth = 4")

ax1.legend()

plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off
plt.ylabel("$|loss-exact lnZ|/exact lnZ$")

ax2 = plt.subplot(2,1,2)

ax2.plot(T,error1,label="depth = 1")
ax2.plot(T,error2,label="depth = 2")
ax2.plot(T,error3,label="depth = 3")
ax2.plot(T,error4,label="depth = 4")

ax2.legend()

plt.xlabel("Temperature")
plt.ylabel("STD of loss")
'''
plt.errorbar(T,res1,label="depth = 1",yerr=error1)
plt.errorbar(T,res2,label="depth = 2",yerr=error2)
plt.errorbar(T,res3,label="depth = 3",yerr=error3)
plt.errorbar(T,res4,label="depth = 4",yerr=error4)

plt.legend()
plt.xlabel("Temperature")
plt.ylabel("$|loss-lnZ|$")

plt.show()


import pdb
pdb.set_trace()