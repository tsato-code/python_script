"""
ROS
トピックメッセージを購読/配信するノード
"""
# ------------------
# モジュールインポート
# ------------------
import pcl
import rospy
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2


# ------------------
# グローバル変数の設定
# ------------------
pub = rospy.Publisher("", PointCloud2, queue_size=100)


# ------------------
# 自作関数
# ------------------
def callback(data):
    point = list(pc2.read_points(data))[0]
    rospy.loginfo(rospy.get_caller_id()+"x, y, z: %.4f, %.4f, %.4f"%(point[0], point[1], point[2]))
    pub.publish(data)
    cloud = ros_to_pcl(data)


def ros_to_pcl(data):
    pc = pc2.read_points(data, field_names=("x","y","z"))
    pc_list = [[p[0], p[1], p[2]] for p in pc]
    cloud = pcl.PointCloud()
    cloud.from_list(pc_list)
    return cloud


# ------------------
#  メイン処理
# ------------------
def main():
    rospy.init_node("pub_sub_node_name", anonymous=True)
    rospy.Subscriber("subscribe_topic_name", PointCloud2, callback)
    rospy.spin()


if __name__ == "__main__":
    main()