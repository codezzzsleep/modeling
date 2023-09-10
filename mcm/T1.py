from model import T1_model
import math

θ = math.radians(120)
α = math.radians(1.5)
H = 110
distance = [-3345.36088471125, -2852.07273457418, -2391.03084093323, -1960.12726533958, -1557.39186532410,
            -1180.98328667126, -829.180544528389, -500.375154857951, -193.063780256945, 94.1586434807467,
            362.605331485260, 613.503653986728, 848.000747998154, 1067.16876216246, 1272.00975874380, 1463.46029517554,
            1642.39570611240, 1809.63410556480, 1965.94012741346, 2112.02842140667, 2248.56692062400, 2376.17989534589,
            2495.45080729175, 2606.92497727643, 2711.11207848189, 2808.48846674376, 2899.49935850691, 2984.56086640808,
            3064.06190179238, 3138.36595286236, 3207.81274658926, 3272.71980198527, 3333.38388183824, 3390.08234954646,
            3443.07443725722, 3492.60243110700, 3538.89277898256, 3582.15712586767, 3622.59328150918, 3660.38612482670,
            3695.70844920109]

ans = T1_model(θ, α, H, distance)
deep = ans.deep_calculate()
width, X, Y = ans.width_calculate(D=deep)
overlap = ans.overlap_calculate(W=width, X=X, Y=Y)
format_deep = []
format_width = []
format_overlap = []
# 对输出格式进行格式化处理
for item in deep:
    tmp = "{:.2f}".format(item)
    format_deep.append(tmp)
for item in width:
    tmp = "{:.2f}".format(item)
    format_width.append(tmp)
for item in overlap:
    tmp = "{:.2%}".format(item)
    format_overlap.append(tmp)
print("海水深度(/m):")
print(format_deep)
print("覆盖宽度(/m):")
print(format_width)
print("与前一条测线的重叠率(/%)")
print(format_overlap)
