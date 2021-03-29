// Auto-generated. Do not edit!

// (in-package controller.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class navigateToCoordsGoal {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.goalCoords = null;
    }
    else {
      if (initObj.hasOwnProperty('goalCoords')) {
        this.goalCoords = initObj.goalCoords
      }
      else {
        this.goalCoords = new geometry_msgs.msg.Point();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type navigateToCoordsGoal
    // Serialize message field [goalCoords]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.goalCoords, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type navigateToCoordsGoal
    let len;
    let data = new navigateToCoordsGoal(null);
    // Deserialize message field [goalCoords]
    data.goalCoords = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'controller/navigateToCoordsGoal';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd08a333c455297ea0bde92f400f795a7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    # Goal
    geometry_msgs/Point goalCoords
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
    float64 x
    float64 y
    float64 z
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new navigateToCoordsGoal(null);
    if (msg.goalCoords !== undefined) {
      resolved.goalCoords = geometry_msgs.msg.Point.Resolve(msg.goalCoords)
    }
    else {
      resolved.goalCoords = new geometry_msgs.msg.Point()
    }

    return resolved;
    }
};

module.exports = navigateToCoordsGoal;
