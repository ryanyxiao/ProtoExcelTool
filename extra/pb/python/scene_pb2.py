# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scene.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='scene.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bscene.proto\"H\n\x0bRoleJumpReq\x12\x0b\n\x03\x64ir\x18\x01 \x01(\x02\x12\r\n\x05pos_x\x18\x02 \x01(\x05\x12\r\n\x05pos_y\x18\x03 \x01(\x05\x12\x0e\n\x06height\x18\x04 \x01(\x02\"X\n\x0bRoleJumpAck\x12\x0e\n\x06obj_id\x18\x01 \x01(\x05\x12\x0b\n\x03\x64ir\x18\x02 \x01(\x02\x12\r\n\x05pos_x\x18\x03 \x01(\x05\x12\r\n\x05pos_y\x18\x04 \x01(\x05\x12\x0e\n\x06height\x18\x05 \x01(\x02\"P\n\x11RoleReAliveNotify\x12\x0e\n\x06obj_id\x18\x01 \x01(\x05\x12\r\n\x05pos_x\x18\x02 \x01(\x02\x12\r\n\x05pos_y\x18\x03 \x01(\x02\x12\r\n\x05pos_z\x18\x04 \x01(\x02\"`\n\x0e\x43hannelChatReq\x12\x14\n\x0c\x63ontent_type\x18\x01 \x01(\x05\x12\x11\n\tfrom_type\x18\x02 \x01(\x05\x12\x14\n\x0c\x63hannel_type\x18\x03 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\"\x91\x01\n\x0e\x43hannelChatAck\x12\x10\n\x08\x66rom_uid\x18\x01 \x01(\x05\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0b\n\x03sex\x18\x03 \x01(\x05\x12\x14\n\x0c\x63ontent_type\x18\x04 \x01(\x05\x12\x14\n\x0c\x63hannel_type\x18\x05 \x01(\x05\x12\x11\n\tfrom_type\x18\x06 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x07 \x01(\t\"R\n\x13\x41\x63tivityReadyNotify\x12\x12\n\nactivityId\x18\x01 \x01(\x05\x12\x12\n\ncount_down\x18\x02 \x01(\x05\x12\x13\n\x0bswitch_type\x18\x03 \x01(\x05\"\xa7\x01\n\x13\x41\x63tivityStartNotify\x12\x12\n\nactivityId\x18\x01 \x01(\x05\x12\x13\n\x0bswitch_type\x18\x02 \x01(\x05\x12\n\n\x02Ip\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\x05\x12\x11\n\tmaze_seed\x18\x05 \x01(\x05\x12\x12\n\ntown_pos_x\x18\x06 \x01(\x02\x12\x12\n\ntown_pos_y\x18\x07 \x01(\x02\x12\x12\n\ntown_pos_z\x18\x08 \x01(\x02\":\n\x0fJoinActivityReq\x12\x12\n\nactivityId\x18\x01 \x01(\x05\x12\x13\n\x0bjoin_status\x18\x02 \x01(\x05\"7\n\x0fJoinActivityAck\x12\x12\n\nactivityId\x18\x01 \x01(\x05\x12\x10\n\x08\x65rrocode\x18\x02 \x01(\x05\"\x0f\n\rMazeGetGemReq\"M\n\x0e\x41reaInitNotify\x12\x0f\n\x07\x65rrCode\x18\x01 \x01(\x05\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\x1b\n\x08\x61reaItem\x18\x03 \x03(\x0b\x32\t.AreaItem\"?\n\x08\x41reaItem\x12\x0f\n\x07\x61rea_id\x18\x01 \x01(\t\x12\x0f\n\x07role_id\x18\x02 \x01(\x05\x12\x11\n\tuser_uuid\x18\x03 \x01(\t\"F\n\x0f\x41reaTradeNotify\x12\x0f\n\x07\x61rea_id\x18\x01 \x01(\t\x12\x0f\n\x07role_id\x18\x02 \x01(\x05\x12\x11\n\tuser_uuid\x18\x03 \x01(\t\"\x0f\n\rServerTimeReq\"y\n\rServerTimeAck\x12\x13\n\x0bserver_time\x18\x01 \x01(\x05\x12\x1e\n\x16server_real_start_time\x18\x02 \x01(\x05\x12\x11\n\topen_days\x18\x03 \x01(\x05\x12 \n\x18server_real_combine_time\x18\x04 \x01(\x05\"\'\n\x0cTransportReq\x12\x17\n\x0ftransport_index\x18\x01 \x01(\x05\"\"\n\x0eSwitchSceneReq\x12\x10\n\x08scene_id\x18\x01 \x01(\x05\x62\x06proto3'
)




_ROLEJUMPREQ = _descriptor.Descriptor(
  name='RoleJumpReq',
  full_name='RoleJumpReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dir', full_name='RoleJumpReq.dir', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pos_x', full_name='RoleJumpReq.pos_x', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pos_y', full_name='RoleJumpReq.pos_y', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='RoleJumpReq.height', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=87,
)


_ROLEJUMPACK = _descriptor.Descriptor(
  name='RoleJumpAck',
  full_name='RoleJumpAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='obj_id', full_name='RoleJumpAck.obj_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dir', full_name='RoleJumpAck.dir', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pos_x', full_name='RoleJumpAck.pos_x', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pos_y', full_name='RoleJumpAck.pos_y', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='RoleJumpAck.height', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=177,
)


_ROLEREALIVENOTIFY = _descriptor.Descriptor(
  name='RoleReAliveNotify',
  full_name='RoleReAliveNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='obj_id', full_name='RoleReAliveNotify.obj_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pos_x', full_name='RoleReAliveNotify.pos_x', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pos_y', full_name='RoleReAliveNotify.pos_y', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pos_z', full_name='RoleReAliveNotify.pos_z', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=179,
  serialized_end=259,
)


_CHANNELCHATREQ = _descriptor.Descriptor(
  name='ChannelChatReq',
  full_name='ChannelChatReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content_type', full_name='ChannelChatReq.content_type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='from_type', full_name='ChannelChatReq.from_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel_type', full_name='ChannelChatReq.channel_type', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='ChannelChatReq.content', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=261,
  serialized_end=357,
)


_CHANNELCHATACK = _descriptor.Descriptor(
  name='ChannelChatAck',
  full_name='ChannelChatAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_uid', full_name='ChannelChatAck.from_uid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='username', full_name='ChannelChatAck.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sex', full_name='ChannelChatAck.sex', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content_type', full_name='ChannelChatAck.content_type', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel_type', full_name='ChannelChatAck.channel_type', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='from_type', full_name='ChannelChatAck.from_type', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='ChannelChatAck.content', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=360,
  serialized_end=505,
)


_ACTIVITYREADYNOTIFY = _descriptor.Descriptor(
  name='ActivityReadyNotify',
  full_name='ActivityReadyNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='activityId', full_name='ActivityReadyNotify.activityId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='count_down', full_name='ActivityReadyNotify.count_down', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='switch_type', full_name='ActivityReadyNotify.switch_type', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=507,
  serialized_end=589,
)


_ACTIVITYSTARTNOTIFY = _descriptor.Descriptor(
  name='ActivityStartNotify',
  full_name='ActivityStartNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='activityId', full_name='ActivityStartNotify.activityId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='switch_type', full_name='ActivityStartNotify.switch_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Ip', full_name='ActivityStartNotify.Ip', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='ActivityStartNotify.port', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='maze_seed', full_name='ActivityStartNotify.maze_seed', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='town_pos_x', full_name='ActivityStartNotify.town_pos_x', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='town_pos_y', full_name='ActivityStartNotify.town_pos_y', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='town_pos_z', full_name='ActivityStartNotify.town_pos_z', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=592,
  serialized_end=759,
)


_JOINACTIVITYREQ = _descriptor.Descriptor(
  name='JoinActivityReq',
  full_name='JoinActivityReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='activityId', full_name='JoinActivityReq.activityId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='join_status', full_name='JoinActivityReq.join_status', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=761,
  serialized_end=819,
)


_JOINACTIVITYACK = _descriptor.Descriptor(
  name='JoinActivityAck',
  full_name='JoinActivityAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='activityId', full_name='JoinActivityAck.activityId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errocode', full_name='JoinActivityAck.errocode', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=821,
  serialized_end=876,
)


_MAZEGETGEMREQ = _descriptor.Descriptor(
  name='MazeGetGemReq',
  full_name='MazeGetGemReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=878,
  serialized_end=893,
)


_AREAINITNOTIFY = _descriptor.Descriptor(
  name='AreaInitNotify',
  full_name='AreaInitNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='errCode', full_name='AreaInitNotify.errCode', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='count', full_name='AreaInitNotify.count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='areaItem', full_name='AreaInitNotify.areaItem', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=895,
  serialized_end=972,
)


_AREAITEM = _descriptor.Descriptor(
  name='AreaItem',
  full_name='AreaItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='area_id', full_name='AreaItem.area_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='AreaItem.role_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_uuid', full_name='AreaItem.user_uuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=974,
  serialized_end=1037,
)


_AREATRADENOTIFY = _descriptor.Descriptor(
  name='AreaTradeNotify',
  full_name='AreaTradeNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='area_id', full_name='AreaTradeNotify.area_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='AreaTradeNotify.role_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_uuid', full_name='AreaTradeNotify.user_uuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1039,
  serialized_end=1109,
)


_SERVERTIMEREQ = _descriptor.Descriptor(
  name='ServerTimeReq',
  full_name='ServerTimeReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1111,
  serialized_end=1126,
)


_SERVERTIMEACK = _descriptor.Descriptor(
  name='ServerTimeAck',
  full_name='ServerTimeAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_time', full_name='ServerTimeAck.server_time', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='server_real_start_time', full_name='ServerTimeAck.server_real_start_time', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='open_days', full_name='ServerTimeAck.open_days', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='server_real_combine_time', full_name='ServerTimeAck.server_real_combine_time', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1128,
  serialized_end=1249,
)


_TRANSPORTREQ = _descriptor.Descriptor(
  name='TransportReq',
  full_name='TransportReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transport_index', full_name='TransportReq.transport_index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1251,
  serialized_end=1290,
)


_SWITCHSCENEREQ = _descriptor.Descriptor(
  name='SwitchSceneReq',
  full_name='SwitchSceneReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scene_id', full_name='SwitchSceneReq.scene_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1292,
  serialized_end=1326,
)

_AREAINITNOTIFY.fields_by_name['areaItem'].message_type = _AREAITEM
DESCRIPTOR.message_types_by_name['RoleJumpReq'] = _ROLEJUMPREQ
DESCRIPTOR.message_types_by_name['RoleJumpAck'] = _ROLEJUMPACK
DESCRIPTOR.message_types_by_name['RoleReAliveNotify'] = _ROLEREALIVENOTIFY
DESCRIPTOR.message_types_by_name['ChannelChatReq'] = _CHANNELCHATREQ
DESCRIPTOR.message_types_by_name['ChannelChatAck'] = _CHANNELCHATACK
DESCRIPTOR.message_types_by_name['ActivityReadyNotify'] = _ACTIVITYREADYNOTIFY
DESCRIPTOR.message_types_by_name['ActivityStartNotify'] = _ACTIVITYSTARTNOTIFY
DESCRIPTOR.message_types_by_name['JoinActivityReq'] = _JOINACTIVITYREQ
DESCRIPTOR.message_types_by_name['JoinActivityAck'] = _JOINACTIVITYACK
DESCRIPTOR.message_types_by_name['MazeGetGemReq'] = _MAZEGETGEMREQ
DESCRIPTOR.message_types_by_name['AreaInitNotify'] = _AREAINITNOTIFY
DESCRIPTOR.message_types_by_name['AreaItem'] = _AREAITEM
DESCRIPTOR.message_types_by_name['AreaTradeNotify'] = _AREATRADENOTIFY
DESCRIPTOR.message_types_by_name['ServerTimeReq'] = _SERVERTIMEREQ
DESCRIPTOR.message_types_by_name['ServerTimeAck'] = _SERVERTIMEACK
DESCRIPTOR.message_types_by_name['TransportReq'] = _TRANSPORTREQ
DESCRIPTOR.message_types_by_name['SwitchSceneReq'] = _SWITCHSCENEREQ
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoleJumpReq = _reflection.GeneratedProtocolMessageType('RoleJumpReq', (_message.Message,), {
  'DESCRIPTOR' : _ROLEJUMPREQ,
  '__module__' : 'scene_pb2'
  # @@protoc_insertion_point(class_scope:RoleJumpReq)
  })
_sym_db.RegisterMessage(RoleJumpReq)

RoleJumpAck = _reflection.GeneratedProtocolMessageType('RoleJumpAck', (_message.Message,), {
  'DESCRIPTOR' : _ROLEJUMPACK,
  '__module__' : 'scene_pb2'
  # @@protoc_insertion_point(class_scope:RoleJumpAck)
  })
_sym_db.RegisterMessage(RoleJumpAck)

RoleReAliveNotify = _reflection.GeneratedProtocolMessageType('RoleReAliveNotify', (_message.Message,), {
  'DESCRIPTOR' : _ROLEREALIVENOTIFY,
  '__module__' : 'scene_pb2'
  # @@protoc_insertion_point(class_scope:RoleReAliveNotify)
  })
_sym_db.RegisterMessage(RoleReAliveNotify)

ChannelChatReq = _reflection.GeneratedProtocolMessageType('ChannelChatReq', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELCHATREQ,
  '__module__' : 'scene_pb2'
  # @@protoc_insertion_point(class_scope:ChannelChatReq)
  })
_sym_db.RegisterMessage(ChannelChatReq)

ChannelChatAck = _reflection.GeneratedProtocolMessageType('ChannelChatAck', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELCHATACK,
  '__module__' : 'scene_pb2'
  # @@protoc_insertion_point(class_scope:ChannelChatAck)
  })
_sym_db.RegisterMessage(ChannelChatAck)

ActivityReadyNotify = _reflection.GeneratedProtocolMessageType('ActivityReadyNotify', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITYREADYNOTIFY,
  '__module__' : 'scene_pb2'
  # @@protoc_insertion_point(class_scope:ActivityReadyNotify)
  })
_sym_db.RegisterMessage(ActivityReadyNotify)

ActivityStartNotify = _reflection.GeneratedProtocolMessageType('ActivityStartNotify', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITYSTARTNOTIFY,
  '__module__' : 'scene_pb2'
  # @@protoc_insertion_point(class_scope:ActivityStartNotify)
  })
_sym_db.RegisterMessage(ActivityStartNotify)

JoinActivityReq = _reflection.GeneratedProtocolMessageType('JoinActivityReq', (_message.Message,), {
  'DESCRIPTOR' : _JOINACTIVITYREQ,
  '__module__' : 'scene_pb2'
  # @@protoc_insertion_point(class_scope:JoinActivityReq)
  })
_sym_db.RegisterMessage(JoinActivityReq)

JoinActivityAck = _reflection.GeneratedProtocolMessageType('JoinActivityAck', (_message.Message,), {
  'DESCRIPTOR' : _JOINACTIVITYACK,
  '__module__' : 'scene_pb2'
  # @@protoc_insertion_point(class_scope:JoinActivityAck)
  })
_sym_db.RegisterMessage(JoinActivityAck)

MazeGetGemReq = _reflection.GeneratedProtocolMessageType('MazeGetGemReq', (_message.Message,), {
  'DESCRIPTOR' : _MAZEGETGEMREQ,
  '__module__' : 'scene_pb2'
  # @@protoc_insertion_point(class_scope:MazeGetGemReq)
  })
_sym_db.RegisterMessage(MazeGetGemReq)

AreaInitNotify = _reflection.GeneratedProtocolMessageType('AreaInitNotify', (_message.Message,), {
  'DESCRIPTOR' : _AREAINITNOTIFY,
  '__module__' : 'scene_pb2'
  # @@protoc_insertion_point(class_scope:AreaInitNotify)
  })
_sym_db.RegisterMessage(AreaInitNotify)

AreaItem = _reflection.GeneratedProtocolMessageType('AreaItem', (_message.Message,), {
  'DESCRIPTOR' : _AREAITEM,
  '__module__' : 'scene_pb2'
  # @@protoc_insertion_point(class_scope:AreaItem)
  })
_sym_db.RegisterMessage(AreaItem)

AreaTradeNotify = _reflection.GeneratedProtocolMessageType('AreaTradeNotify', (_message.Message,), {
  'DESCRIPTOR' : _AREATRADENOTIFY,
  '__module__' : 'scene_pb2'
  # @@protoc_insertion_point(class_scope:AreaTradeNotify)
  })
_sym_db.RegisterMessage(AreaTradeNotify)

ServerTimeReq = _reflection.GeneratedProtocolMessageType('ServerTimeReq', (_message.Message,), {
  'DESCRIPTOR' : _SERVERTIMEREQ,
  '__module__' : 'scene_pb2'
  # @@protoc_insertion_point(class_scope:ServerTimeReq)
  })
_sym_db.RegisterMessage(ServerTimeReq)

ServerTimeAck = _reflection.GeneratedProtocolMessageType('ServerTimeAck', (_message.Message,), {
  'DESCRIPTOR' : _SERVERTIMEACK,
  '__module__' : 'scene_pb2'
  # @@protoc_insertion_point(class_scope:ServerTimeAck)
  })
_sym_db.RegisterMessage(ServerTimeAck)

TransportReq = _reflection.GeneratedProtocolMessageType('TransportReq', (_message.Message,), {
  'DESCRIPTOR' : _TRANSPORTREQ,
  '__module__' : 'scene_pb2'
  # @@protoc_insertion_point(class_scope:TransportReq)
  })
_sym_db.RegisterMessage(TransportReq)

SwitchSceneReq = _reflection.GeneratedProtocolMessageType('SwitchSceneReq', (_message.Message,), {
  'DESCRIPTOR' : _SWITCHSCENEREQ,
  '__module__' : 'scene_pb2'
  # @@protoc_insertion_point(class_scope:SwitchSceneReq)
  })
_sym_db.RegisterMessage(SwitchSceneReq)


# @@protoc_insertion_point(module_scope)
