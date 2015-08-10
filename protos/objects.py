# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: objects.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import countries


DESCRIPTOR = _descriptor.FileDescriptor(
  name='objects.proto',
  package='',
  serialized_pb=_b('\n\robjects.proto\x1a\x0f\x63ountries.proto\"^\n\x04Node\x12\x0c\n\x04guid\x18\x01 \x02(\x0c\x12\x17\n\x0fsignedPublicKey\x18\x02 \x02(\x0c\x12\n\n\x02ip\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\r\x12\x15\n\x06vendor\x18\x05 \x01(\x08:\x05\x66\x61lse\"1\n\x05Value\x12\x10\n\x08valueKey\x18\x01 \x02(\x0c\x12\x16\n\x0eserializedData\x18\x02 \x02(\x0c\"\xba\x05\n\x07Profile\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x1e\n\x08location\x18\x02 \x02(\x0e\x32\x0c.CountryCode\x12\x13\n\x04nsfw\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x15\n\x06vendor\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x18\n\tmoderator\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x0e\n\x06handle\x18\x06 \x01(\t\x12\r\n\x05\x61\x62out\x18\x07 \x01(\t\x12\x0f\n\x07website\x18\x08 \x01(\t\x12\r\n\x05\x65mail\x18\t \x01(\t\x12&\n\x06social\x18\n \x03(\x0b\x32\x16.Profile.SocialAccount\x12\x1e\n\rprimary_color\x18\x0b \x01(\r:\x07\x34\x38\x36\x38\x31\x36\x38\x12 \n\x0fsecondary_color\x18\x0c \x01(\r:\x07\x35\x37\x32\x33\x37\x33\x34\x12!\n\x10\x62\x61\x63kground_color\x18\r \x01(\r:\x07\x32\x37\x36\x33\x33\x30\x36\x12\x1c\n\ntext_color\x18\x0e \x01(\r:\x08\x31\x36\x37\x37\x37\x32\x31\x35\x12\x19\n\x0e\x66ollower_count\x18\x0f \x01(\r:\x01\x30\x12\x1a\n\x0f\x66ollowing_count\x18\x10 \x01(\r:\x01\x30\x12 \n\x07pgp_key\x18\x11 \x01(\x0b\x32\x0f.Profile.PGPKey\x12\x13\n\x0b\x61vatar_hash\x18\x12 \x01(\x0c\x12\x13\n\x0bheader_hash\x18\x13 \x01(\x0c\x1a\x9d\x01\n\rSocialAccount\x12/\n\x04type\x18\x01 \x02(\x0e\x32!.Profile.SocialAccount.SocialType\x12\x10\n\x08username\x18\x02 \x02(\t\x12\x11\n\tproof_url\x18\x03 \x02(\t\"6\n\nSocialType\x12\x0c\n\x08\x46\x41\x43\x45\x42OOK\x10\x01\x12\x0b\n\x07TWITTER\x10\x02\x12\r\n\tINSTAGRAM\x10\x03\x1a.\n\x06PGPKey\x12\x11\n\tpublicKey\x18\x01 \x02(\x0c\x12\x11\n\tsignature\x18\x02 \x02(\x0c\"K\n\x08Metadata\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0e\n\x06handle\x18\x02 \x02(\t\x12\x13\n\x0b\x61vatar_hash\x18\x03 \x02(\x0c\x12\x0c\n\x04nsfw\x18\x04 \x02(\x08\"\x8c\x02\n\x08Listings\x12*\n\x07listing\x18\x01 \x03(\x0b\x32\x19.Listings.ListingMetadata\x1a\xd3\x01\n\x0fListingMetadata\x12\x15\n\rcontract_hash\x18\x01 \x02(\x0c\x12\r\n\x05title\x18\x02 \x02(\t\x12\x16\n\x0ethumbnail_hash\x18\x03 \x01(\x0c\x12\x10\n\x08\x63\x61tegory\x18\x04 \x01(\t\x12\r\n\x05price\x18\x05 \x02(\x02\x12\x15\n\rcurrency_code\x18\x06 \x02(\t\x12\x0c\n\x04nsfw\x18\x07 \x02(\x08\x12\x1c\n\x06origin\x18\x08 \x02(\x0e\x32\x0c.CountryCode\x12\x1e\n\x08ships_to\x18\t \x03(\x0e\x32\x0c.CountryCode\"\x81\x01\n\tFollowers\x12&\n\tfollowers\x18\x01 \x03(\x0b\x32\x13.Followers.Follower\x1aL\n\x08\x46ollower\x12\x15\n\rfollower_guid\x18\x01 \x02(\x0c\x12\x16\n\x0e\x66ollowing_guid\x18\x02 \x02(\x0c\x12\x11\n\tsignature\x18\x03 \x02(\x0c')
  ,
  dependencies=[countries.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PROFILE_SOCIALACCOUNT_SOCIALTYPE = _descriptor.EnumDescriptor(
  name='SocialType',
  full_name='Profile.SocialAccount.SocialType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FACEBOOK', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TWITTER', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSTAGRAM', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=778,
  serialized_end=832,
)
_sym_db.RegisterEnumDescriptor(_PROFILE_SOCIALACCOUNT_SOCIALTYPE)


_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='guid', full_name='Node.guid', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signedPublicKey', full_name='Node.signedPublicKey', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip', full_name='Node.ip', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='Node.port', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vendor', full_name='Node.vendor', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=128,
)


_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='valueKey', full_name='Value.valueKey', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serializedData', full_name='Value.serializedData', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=179,
)


_PROFILE_SOCIALACCOUNT = _descriptor.Descriptor(
  name='SocialAccount',
  full_name='Profile.SocialAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Profile.SocialAccount.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='username', full_name='Profile.SocialAccount.username', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proof_url', full_name='Profile.SocialAccount.proof_url', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PROFILE_SOCIALACCOUNT_SOCIALTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=675,
  serialized_end=832,
)

_PROFILE_PGPKEY = _descriptor.Descriptor(
  name='PGPKey',
  full_name='Profile.PGPKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='publicKey', full_name='Profile.PGPKey.publicKey', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='Profile.PGPKey.signature', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=834,
  serialized_end=880,
)

_PROFILE = _descriptor.Descriptor(
  name='Profile',
  full_name='Profile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Profile.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='Profile.location', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nsfw', full_name='Profile.nsfw', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vendor', full_name='Profile.vendor', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='moderator', full_name='Profile.moderator', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='handle', full_name='Profile.handle', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='about', full_name='Profile.about', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='website', full_name='Profile.website', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='email', full_name='Profile.email', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='social', full_name='Profile.social', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='primary_color', full_name='Profile.primary_color', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=4868168,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='secondary_color', full_name='Profile.secondary_color', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=5723734,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='background_color', full_name='Profile.background_color', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=2763306,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='text_color', full_name='Profile.text_color', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=16777215,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='follower_count', full_name='Profile.follower_count', index=14,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='following_count', full_name='Profile.following_count', index=15,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pgp_key', full_name='Profile.pgp_key', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar_hash', full_name='Profile.avatar_hash', index=17,
      number=18, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header_hash', full_name='Profile.header_hash', index=18,
      number=19, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PROFILE_SOCIALACCOUNT, _PROFILE_PGPKEY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=880,
)


_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Metadata.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='handle', full_name='Metadata.handle', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar_hash', full_name='Metadata.avatar_hash', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nsfw', full_name='Metadata.nsfw', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=882,
  serialized_end=957,
)


_LISTINGS_LISTINGMETADATA = _descriptor.Descriptor(
  name='ListingMetadata',
  full_name='Listings.ListingMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contract_hash', full_name='Listings.ListingMetadata.contract_hash', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='Listings.ListingMetadata.title', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thumbnail_hash', full_name='Listings.ListingMetadata.thumbnail_hash', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category', full_name='Listings.ListingMetadata.category', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price', full_name='Listings.ListingMetadata.price', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currency_code', full_name='Listings.ListingMetadata.currency_code', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nsfw', full_name='Listings.ListingMetadata.nsfw', index=6,
      number=7, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='origin', full_name='Listings.ListingMetadata.origin', index=7,
      number=8, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ships_to', full_name='Listings.ListingMetadata.ships_to', index=8,
      number=9, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1017,
  serialized_end=1228,
)

_LISTINGS = _descriptor.Descriptor(
  name='Listings',
  full_name='Listings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='listing', full_name='Listings.listing', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_LISTINGS_LISTINGMETADATA, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=960,
  serialized_end=1228,
)


_FOLLOWERS_FOLLOWER = _descriptor.Descriptor(
  name='Follower',
  full_name='Followers.Follower',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='follower_guid', full_name='Followers.Follower.follower_guid', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='following_guid', full_name='Followers.Follower.following_guid', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='Followers.Follower.signature', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1284,
  serialized_end=1360,
)

_FOLLOWERS = _descriptor.Descriptor(
  name='Followers',
  full_name='Followers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='followers', full_name='Followers.followers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_FOLLOWERS_FOLLOWER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1231,
  serialized_end=1360,
)

_PROFILE_SOCIALACCOUNT.fields_by_name['type'].enum_type = _PROFILE_SOCIALACCOUNT_SOCIALTYPE
_PROFILE_SOCIALACCOUNT.containing_type = _PROFILE
_PROFILE_SOCIALACCOUNT_SOCIALTYPE.containing_type = _PROFILE_SOCIALACCOUNT
_PROFILE_PGPKEY.containing_type = _PROFILE
_PROFILE.fields_by_name['location'].enum_type = countries._COUNTRYCODE
_PROFILE.fields_by_name['social'].message_type = _PROFILE_SOCIALACCOUNT
_PROFILE.fields_by_name['pgp_key'].message_type = _PROFILE_PGPKEY
_LISTINGS_LISTINGMETADATA.fields_by_name['origin'].enum_type = countries._COUNTRYCODE
_LISTINGS_LISTINGMETADATA.fields_by_name['ships_to'].enum_type = countries._COUNTRYCODE
_LISTINGS_LISTINGMETADATA.containing_type = _LISTINGS
_LISTINGS.fields_by_name['listing'].message_type = _LISTINGS_LISTINGMETADATA
_FOLLOWERS_FOLLOWER.containing_type = _FOLLOWERS
_FOLLOWERS.fields_by_name['followers'].message_type = _FOLLOWERS_FOLLOWER
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['Profile'] = _PROFILE
DESCRIPTOR.message_types_by_name['Metadata'] = _METADATA
DESCRIPTOR.message_types_by_name['Listings'] = _LISTINGS
DESCRIPTOR.message_types_by_name['Followers'] = _FOLLOWERS

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), dict(
  DESCRIPTOR = _NODE,
  __module__ = 'objects_pb2'
  # @@protoc_insertion_point(class_scope:Node)
  ))
_sym_db.RegisterMessage(Node)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), dict(
  DESCRIPTOR = _VALUE,
  __module__ = 'objects_pb2'
  # @@protoc_insertion_point(class_scope:Value)
  ))
_sym_db.RegisterMessage(Value)

Profile = _reflection.GeneratedProtocolMessageType('Profile', (_message.Message,), dict(

  SocialAccount = _reflection.GeneratedProtocolMessageType('SocialAccount', (_message.Message,), dict(
    DESCRIPTOR = _PROFILE_SOCIALACCOUNT,
    __module__ = 'objects_pb2'
    # @@protoc_insertion_point(class_scope:Profile.SocialAccount)
    ))
  ,

  PGPKey = _reflection.GeneratedProtocolMessageType('PGPKey', (_message.Message,), dict(
    DESCRIPTOR = _PROFILE_PGPKEY,
    __module__ = 'objects_pb2'
    # @@protoc_insertion_point(class_scope:Profile.PGPKey)
    ))
  ,
  DESCRIPTOR = _PROFILE,
  __module__ = 'objects_pb2'
  # @@protoc_insertion_point(class_scope:Profile)
  ))
_sym_db.RegisterMessage(Profile)
_sym_db.RegisterMessage(Profile.SocialAccount)
_sym_db.RegisterMessage(Profile.PGPKey)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), dict(
  DESCRIPTOR = _METADATA,
  __module__ = 'objects_pb2'
  # @@protoc_insertion_point(class_scope:Metadata)
  ))
_sym_db.RegisterMessage(Metadata)

Listings = _reflection.GeneratedProtocolMessageType('Listings', (_message.Message,), dict(

  ListingMetadata = _reflection.GeneratedProtocolMessageType('ListingMetadata', (_message.Message,), dict(
    DESCRIPTOR = _LISTINGS_LISTINGMETADATA,
    __module__ = 'objects_pb2'
    # @@protoc_insertion_point(class_scope:Listings.ListingMetadata)
    ))
  ,
  DESCRIPTOR = _LISTINGS,
  __module__ = 'objects_pb2'
  # @@protoc_insertion_point(class_scope:Listings)
  ))
_sym_db.RegisterMessage(Listings)
_sym_db.RegisterMessage(Listings.ListingMetadata)

Followers = _reflection.GeneratedProtocolMessageType('Followers', (_message.Message,), dict(

  Follower = _reflection.GeneratedProtocolMessageType('Follower', (_message.Message,), dict(
    DESCRIPTOR = _FOLLOWERS_FOLLOWER,
    __module__ = 'objects_pb2'
    # @@protoc_insertion_point(class_scope:Followers.Follower)
    ))
  ,
  DESCRIPTOR = _FOLLOWERS,
  __module__ = 'objects_pb2'
  # @@protoc_insertion_point(class_scope:Followers)
  ))
_sym_db.RegisterMessage(Followers)
_sym_db.RegisterMessage(Followers.Follower)


# @@protoc_insertion_point(module_scope)
