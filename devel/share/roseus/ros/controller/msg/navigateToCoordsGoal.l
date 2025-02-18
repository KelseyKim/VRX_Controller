;; Auto-generated. Do not edit!


(when (boundp 'controller::navigateToCoordsGoal)
  (if (not (find-package "CONTROLLER"))
    (make-package "CONTROLLER"))
  (shadow 'navigateToCoordsGoal (find-package "CONTROLLER")))
(unless (find-package "CONTROLLER::NAVIGATETOCOORDSGOAL")
  (make-package "CONTROLLER::NAVIGATETOCOORDSGOAL"))

(in-package "ROS")
;;//! \htmlinclude navigateToCoordsGoal.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass controller::navigateToCoordsGoal
  :super ros::object
  :slots (_goalCoords ))

(defmethod controller::navigateToCoordsGoal
  (:init
   (&key
    ((:goalCoords __goalCoords) (instance geometry_msgs::Point :init))
    )
   (send-super :init)
   (setq _goalCoords __goalCoords)
   self)
  (:goalCoords
   (&rest __goalCoords)
   (if (keywordp (car __goalCoords))
       (send* _goalCoords __goalCoords)
     (progn
       (if __goalCoords (setq _goalCoords (car __goalCoords)))
       _goalCoords)))
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Point _goalCoords
    (send _goalCoords :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Point _goalCoords
       (send _goalCoords :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Point _goalCoords
     (send _goalCoords :deserialize buf ptr-) (incf ptr- (send _goalCoords :serialization-length))
   ;;
   self)
  )

(setf (get controller::navigateToCoordsGoal :md5sum-) "d08a333c455297ea0bde92f400f795a7")
(setf (get controller::navigateToCoordsGoal :datatype-) "controller/navigateToCoordsGoal")
(setf (get controller::navigateToCoordsGoal :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Goal
geometry_msgs/Point goalCoords

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

")



(provide :controller/navigateToCoordsGoal "d08a333c455297ea0bde92f400f795a7")


