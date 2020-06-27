# Copyright (C) Huangying Zhan 2019. All rights reserved.

import argparse

from kitti_odometry import KittiEvalOdom

parser = argparse.ArgumentParser(description='KITTI evaluation')
parser.add_argument("--kitti_odo_poses_path",
                    default="/home/roit/datasets/kitti_odo_poses"
                    )
parser.add_argument('--pred_poses_dir', type=str,
                    default='/home/roit/aws/aprojects/kitti-odom-eval/pred_poses',
                    help="pred_dir directory")

parser.add_argument('--out_dir', type=str,
                    default='./output',
                    help="pred_dir directory")
parser.add_argument('--align', type=str,
                    default='7dof',
                    choices=['scale',#scale是根据gt来的, visual results 用了gt信息
                             'scale_7dof',
                             '7dof',#尺度学习?
                             '6dof'],#选择这个, 尺度不知道, 绘图尺寸有区别.
                    help="alignment type")

parser.add_argument('--plot_keys',default=
                        ["Ours","Ground Truth"]
                        #["Ours"]
                    )
parser.add_argument('--seqs',
                    #default=[1,3,4,6,10,11,14,17,20],
                    default=[0])




#continue_flag = input("Evaluate result in {}? [y/n]".format(result_dir))
#if continue_flag == "y":

#else:
#    print("Double check the path!")


def main(opt):
    eval_tool = KittiEvalOdom(plot_keys=opt.plot_keys)

    eval_tool.run(
        gt_dir = opt.kitti_odo_poses_path,
        out_dir = opt.out_dir,
        pred_dir=opt.pred_poses_dir,
        alignment=opt.align,
        seqs=opt.seqs
    )

if __name__ == '__main__':
    opt= parser.parse_args()
    main(opt)
