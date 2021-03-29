
(cl:in-package :asdf)

(defsystem "controller-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "navigateToCoordsAction" :depends-on ("_package_navigateToCoordsAction"))
    (:file "_package_navigateToCoordsAction" :depends-on ("_package"))
    (:file "navigateToCoordsActionFeedback" :depends-on ("_package_navigateToCoordsActionFeedback"))
    (:file "_package_navigateToCoordsActionFeedback" :depends-on ("_package"))
    (:file "navigateToCoordsActionGoal" :depends-on ("_package_navigateToCoordsActionGoal"))
    (:file "_package_navigateToCoordsActionGoal" :depends-on ("_package"))
    (:file "navigateToCoordsActionResult" :depends-on ("_package_navigateToCoordsActionResult"))
    (:file "_package_navigateToCoordsActionResult" :depends-on ("_package"))
    (:file "navigateToCoordsFeedback" :depends-on ("_package_navigateToCoordsFeedback"))
    (:file "_package_navigateToCoordsFeedback" :depends-on ("_package"))
    (:file "navigateToCoordsGoal" :depends-on ("_package_navigateToCoordsGoal"))
    (:file "_package_navigateToCoordsGoal" :depends-on ("_package"))
    (:file "navigateToCoordsResult" :depends-on ("_package_navigateToCoordsResult"))
    (:file "_package_navigateToCoordsResult" :depends-on ("_package"))
  ))