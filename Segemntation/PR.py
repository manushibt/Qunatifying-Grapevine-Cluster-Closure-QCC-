from visualdl import LogWriter
import numpy as np

# ?????????
with LogWriter("./output/PPLiteSeg/pr_curve_test/train") as writer:
    for step in range(3):
        labels = np.random.randint(2, size=100)
        predictions = np.random.rand(100)
        # ????pr curve????
        writer.add_pr_curve(tag='pr_curve',
                            labels=labels,
                            predictions=predictions,
                            step=step,
                            num_thresholds=5)
                            