; Auto-generated. Do not edit!


(cl:in-package controller-msg)


;//! \htmlinclude navigateToCoordsGoal.msg.html

(cl:defclass <navigateToCoordsGoal> (roslisp-msg-protocol:ros-message)
  ((goalCoords
    :reader goalCoords
    :initarg :goalCoords
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point)))
)

(cl:defclass navigateToCoordsGoal (<navigateToCoordsGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <navigateToCoordsGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'navigateToCoordsGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name controller-msg:<navigateToCoordsGoal> is deprecated: use controller-msg:navigateToCoordsGoal instead.")))

(cl:ensure-generic-function 'goalCoords-val :lambda-list '(m))
(cl:defmethod goalCoords-val ((m <navigateToCoordsGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader controller-msg:goalCoords-val is deprecated.  Use controller-msg:goalCoords instead.")
  (goalCoords m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <navigateToCoordsGoal>) ostream)
  "Serializes a message object of type '<navigateToCoordsGoal>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'goalCoords) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <navigateToCoordsGoal>) istream)
  "Deserializes a message object of type '<navigateToCoordsGoal>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'goalCoords) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<navigateToCoordsGoal>)))
  "Returns string type for a message object of type '<navigateToCoordsGoal>"
  "controller/navigateToCoordsGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'navigateToCoordsGoal)))
  "Returns string type for a message object of type 'navigateToCoordsGoal"
  "controller/navigateToCoordsGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<navigateToCoordsGoal>)))
  "Returns md5sum for a message object of type '<navigateToCoordsGoal>"
  "d08a333c455297ea0bde92f400f795a7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'navigateToCoordsGoal)))
  "Returns md5sum for a message object of type 'navigateToCoordsGoal"
  "d08a333c455297ea0bde92f400f795a7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<navigateToCoordsGoal>)))
  "Returns full string definition for message of type '<navigateToCoordsGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Goal~%geometry_msgs/Point goalCoords~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'navigateToCoordsGoal)))
  "Returns full string definition for message of type 'navigateToCoordsGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Goal~%geometry_msgs/Point goalCoords~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <navigateToCoordsGoal>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'goalCoords))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <navigateToCoordsGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'navigateToCoordsGoal
    (cl:cons ':goalCoords (goalCoords msg))
))
