// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: game.proto

#include "game.pb.h"

#include <algorithm>

#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/wire_format_lite.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>

PROTOBUF_PRAGMA_INIT_SEG
constexpr EnterGameAck::EnterGameAck(
  ::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized){}
struct EnterGameAckDefaultTypeInternal {
  constexpr EnterGameAckDefaultTypeInternal()
    : _instance(::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized{}) {}
  ~EnterGameAckDefaultTypeInternal() {}
  union {
    EnterGameAck _instance;
  };
};
PROTOBUF_ATTRIBUTE_NO_DESTROY PROTOBUF_CONSTINIT EnterGameAckDefaultTypeInternal _EnterGameAck_default_instance_;
constexpr EnterGameReq::EnterGameReq(
  ::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized)
  : userid_(int64_t{0}){}
struct EnterGameReqDefaultTypeInternal {
  constexpr EnterGameReqDefaultTypeInternal()
    : _instance(::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized{}) {}
  ~EnterGameReqDefaultTypeInternal() {}
  union {
    EnterGameReq _instance;
  };
};
PROTOBUF_ATTRIBUTE_NO_DESTROY PROTOBUF_CONSTINIT EnterGameReqDefaultTypeInternal _EnterGameReq_default_instance_;
static ::PROTOBUF_NAMESPACE_ID::Metadata file_level_metadata_game_2eproto[2];
static const ::PROTOBUF_NAMESPACE_ID::EnumDescriptor* file_level_enum_descriptors_game_2eproto[1];
static constexpr ::PROTOBUF_NAMESPACE_ID::ServiceDescriptor const** file_level_service_descriptors_game_2eproto = nullptr;

const ::PROTOBUF_NAMESPACE_ID::uint32 TableStruct_game_2eproto::offsets[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::EnterGameAck, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  ~0u,  // no _inlined_string_donated_
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::EnterGameReq, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  ~0u,  // no _inlined_string_donated_
  PROTOBUF_FIELD_OFFSET(::EnterGameReq, userid_),
};
static const ::PROTOBUF_NAMESPACE_ID::internal::MigrationSchema schemas[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  { 0, -1, -1, sizeof(::EnterGameAck)},
  { 6, -1, -1, sizeof(::EnterGameReq)},
};

static ::PROTOBUF_NAMESPACE_ID::Message const * const file_default_instances[] = {
  reinterpret_cast<const ::PROTOBUF_NAMESPACE_ID::Message*>(&::_EnterGameAck_default_instance_),
  reinterpret_cast<const ::PROTOBUF_NAMESPACE_ID::Message*>(&::_EnterGameReq_default_instance_),
};

const char descriptor_table_protodef_game_2eproto[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) =
  "\n\ngame.proto\"\016\n\014EnterGameAck\"\036\n\014EnterGam"
  "eReq\022\016\n\006UserId\030\001 \001(\003*N\n\tGameMsgId\022\017\n\013Gam"
  "e_MSG_ID\020\000\022\027\n\022GAME_ENTERGAME_ACK\020\322\017\022\027\n\022G"
  "AME_ENTERGAME_REQ\020\321\017b\006proto3"
  ;
static ::PROTOBUF_NAMESPACE_ID::internal::once_flag descriptor_table_game_2eproto_once;
const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable descriptor_table_game_2eproto = {
  false, false, 148, descriptor_table_protodef_game_2eproto, "game.proto", 
  &descriptor_table_game_2eproto_once, nullptr, 0, 2,
  schemas, file_default_instances, TableStruct_game_2eproto::offsets,
  file_level_metadata_game_2eproto, file_level_enum_descriptors_game_2eproto, file_level_service_descriptors_game_2eproto,
};
PROTOBUF_ATTRIBUTE_WEAK const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable* descriptor_table_game_2eproto_getter() {
  return &descriptor_table_game_2eproto;
}

// Force running AddDescriptors() at dynamic initialization time.
PROTOBUF_ATTRIBUTE_INIT_PRIORITY static ::PROTOBUF_NAMESPACE_ID::internal::AddDescriptorsRunner dynamic_init_dummy_game_2eproto(&descriptor_table_game_2eproto);
const ::PROTOBUF_NAMESPACE_ID::EnumDescriptor* GameMsgId_descriptor() {
  ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(&descriptor_table_game_2eproto);
  return file_level_enum_descriptors_game_2eproto[0];
}
bool GameMsgId_IsValid(int value) {
  switch (value) {
    case 0:
    case 2001:
    case 2002:
      return true;
    default:
      return false;
  }
}


// ===================================================================

class EnterGameAck::_Internal {
 public:
};

EnterGameAck::EnterGameAck(::PROTOBUF_NAMESPACE_ID::Arena* arena,
                         bool is_message_owned)
  : ::PROTOBUF_NAMESPACE_ID::internal::ZeroFieldsBase(arena, is_message_owned) {
  // @@protoc_insertion_point(arena_constructor:EnterGameAck)
}
EnterGameAck::EnterGameAck(const EnterGameAck& from)
  : ::PROTOBUF_NAMESPACE_ID::internal::ZeroFieldsBase() {
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
  // @@protoc_insertion_point(copy_constructor:EnterGameAck)
}





const ::PROTOBUF_NAMESPACE_ID::Message::ClassData EnterGameAck::_class_data_ = {
    ::PROTOBUF_NAMESPACE_ID::internal::ZeroFieldsBase::CopyImpl,
    ::PROTOBUF_NAMESPACE_ID::internal::ZeroFieldsBase::MergeImpl,
};
const ::PROTOBUF_NAMESPACE_ID::Message::ClassData*EnterGameAck::GetClassData() const { return &_class_data_; }







::PROTOBUF_NAMESPACE_ID::Metadata EnterGameAck::GetMetadata() const {
  return ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(
      &descriptor_table_game_2eproto_getter, &descriptor_table_game_2eproto_once,
      file_level_metadata_game_2eproto[0]);
}

// ===================================================================

class EnterGameReq::_Internal {
 public:
};

EnterGameReq::EnterGameReq(::PROTOBUF_NAMESPACE_ID::Arena* arena,
                         bool is_message_owned)
  : ::PROTOBUF_NAMESPACE_ID::Message(arena, is_message_owned) {
  SharedCtor();
  if (!is_message_owned) {
    RegisterArenaDtor(arena);
  }
  // @@protoc_insertion_point(arena_constructor:EnterGameReq)
}
EnterGameReq::EnterGameReq(const EnterGameReq& from)
  : ::PROTOBUF_NAMESPACE_ID::Message() {
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
  userid_ = from.userid_;
  // @@protoc_insertion_point(copy_constructor:EnterGameReq)
}

void EnterGameReq::SharedCtor() {
userid_ = int64_t{0};
}

EnterGameReq::~EnterGameReq() {
  // @@protoc_insertion_point(destructor:EnterGameReq)
  if (GetArenaForAllocation() != nullptr) return;
  SharedDtor();
  _internal_metadata_.Delete<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

inline void EnterGameReq::SharedDtor() {
  GOOGLE_DCHECK(GetArenaForAllocation() == nullptr);
}

void EnterGameReq::ArenaDtor(void* object) {
  EnterGameReq* _this = reinterpret_cast< EnterGameReq* >(object);
  (void)_this;
}
void EnterGameReq::RegisterArenaDtor(::PROTOBUF_NAMESPACE_ID::Arena*) {
}
void EnterGameReq::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}

void EnterGameReq::Clear() {
// @@protoc_insertion_point(message_clear_start:EnterGameReq)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  userid_ = int64_t{0};
  _internal_metadata_.Clear<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

const char* EnterGameReq::_InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) {
#define CHK_(x) if (PROTOBUF_PREDICT_FALSE(!(x))) goto failure
  while (!ctx->Done(&ptr)) {
    ::PROTOBUF_NAMESPACE_ID::uint32 tag;
    ptr = ::PROTOBUF_NAMESPACE_ID::internal::ReadTag(ptr, &tag);
    switch (tag >> 3) {
      // int64 UserId = 1;
      case 1:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 8)) {
          userid_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint64(&ptr);
          CHK_(ptr);
        } else
          goto handle_unusual;
        continue;
      default:
        goto handle_unusual;
    }  // switch
  handle_unusual:
    if ((tag == 0) || ((tag & 7) == 4)) {
      CHK_(ptr);
      ctx->SetLastTag(tag);
      goto message_done;
    }
    ptr = UnknownFieldParse(
        tag,
        _internal_metadata_.mutable_unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(),
        ptr, ctx);
    CHK_(ptr != nullptr);
  }  // while
message_done:
  return ptr;
failure:
  ptr = nullptr;
  goto message_done;
#undef CHK_
}

::PROTOBUF_NAMESPACE_ID::uint8* EnterGameReq::_InternalSerialize(
    ::PROTOBUF_NAMESPACE_ID::uint8* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const {
  // @@protoc_insertion_point(serialize_to_array_start:EnterGameReq)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // int64 UserId = 1;
  if (this->_internal_userid() != 0) {
    target = stream->EnsureSpace(target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteInt64ToArray(1, this->_internal_userid(), target);
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormat::InternalSerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(::PROTOBUF_NAMESPACE_ID::UnknownFieldSet::default_instance), target, stream);
  }
  // @@protoc_insertion_point(serialize_to_array_end:EnterGameReq)
  return target;
}

size_t EnterGameReq::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:EnterGameReq)
  size_t total_size = 0;

  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  // int64 UserId = 1;
  if (this->_internal_userid() != 0) {
    total_size += ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::Int64SizePlusOne(this->_internal_userid());
  }

  return MaybeComputeUnknownFieldsSize(total_size, &_cached_size_);
}

const ::PROTOBUF_NAMESPACE_ID::Message::ClassData EnterGameReq::_class_data_ = {
    ::PROTOBUF_NAMESPACE_ID::Message::CopyWithSizeCheck,
    EnterGameReq::MergeImpl
};
const ::PROTOBUF_NAMESPACE_ID::Message::ClassData*EnterGameReq::GetClassData() const { return &_class_data_; }

void EnterGameReq::MergeImpl(::PROTOBUF_NAMESPACE_ID::Message* to,
                      const ::PROTOBUF_NAMESPACE_ID::Message& from) {
  static_cast<EnterGameReq *>(to)->MergeFrom(
      static_cast<const EnterGameReq &>(from));
}


void EnterGameReq::MergeFrom(const EnterGameReq& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:EnterGameReq)
  GOOGLE_DCHECK_NE(&from, this);
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  if (from._internal_userid() != 0) {
    _internal_set_userid(from._internal_userid());
  }
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
}

void EnterGameReq::CopyFrom(const EnterGameReq& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:EnterGameReq)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool EnterGameReq::IsInitialized() const {
  return true;
}

void EnterGameReq::InternalSwap(EnterGameReq* other) {
  using std::swap;
  _internal_metadata_.InternalSwap(&other->_internal_metadata_);
  swap(userid_, other->userid_);
}

::PROTOBUF_NAMESPACE_ID::Metadata EnterGameReq::GetMetadata() const {
  return ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(
      &descriptor_table_game_2eproto_getter, &descriptor_table_game_2eproto_once,
      file_level_metadata_game_2eproto[1]);
}

// @@protoc_insertion_point(namespace_scope)
PROTOBUF_NAMESPACE_OPEN
template<> PROTOBUF_NOINLINE ::EnterGameAck* Arena::CreateMaybeMessage< ::EnterGameAck >(Arena* arena) {
  return Arena::CreateMessageInternal< ::EnterGameAck >(arena);
}
template<> PROTOBUF_NOINLINE ::EnterGameReq* Arena::CreateMaybeMessage< ::EnterGameReq >(Arena* arena) {
  return Arena::CreateMessageInternal< ::EnterGameReq >(arena);
}
PROTOBUF_NAMESPACE_CLOSE

// @@protoc_insertion_point(global_scope)
#include <google/protobuf/port_undef.inc>