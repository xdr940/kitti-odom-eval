# Copyright (C) Huangying Zhan 2019. All rights reserved.

import argparse

from kitti_odometry import KittiEvalOdom

parser = argparse.ArgumentParser(description='KITTI evaluation')
parser.add_argument("--kitti_odo_poses_path",
                    default="/media/roit/hard_disk_2/Datasets/kitti_odometry_color/poses"
                    )
parser.add_argument('--pred_poses_dir', type=str,
                    default='/home/roit/aws/aprojects/kitti-odom-eval/dataset/kitti_odom/gt_poses',
                    help="pred_dir directory")

parser.add_argument('--result_dir', type=str,
                    default='./result_dir',
                    help="pred_dir directory")
parser.add_argument('--align', type=str,
                    default='6dof',
                    choices=['scale', 'scale_7dof', '7dof', '6dof'],
                    help="alignment type")
parser.add_argument('--seqs',
                    #default=[1,3,4,6,10,11,14,17,20],
                    default=[9])




#continue_flag = input("Evaluate result in {}? [y/n]".format(result_dir))
#if continue_flag == "y":

#else:
#    print("Double check the path!")


def main(opt):
    eval_tool = KittiEvalOdom()

    eval_tool.eval(
        gt_dir = opt.kitti_odo_poses_path,
        result_dir = opt.result_dir,
        pred_dir=opt.pred_poses_dir,
        alignment=opt.align,
        seqs=opt.seqs,
    )

if __name__ == '__main__':
    opt= parser.parse_args()
    main(opt)
