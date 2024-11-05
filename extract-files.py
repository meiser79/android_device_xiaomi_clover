#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixup_remove_arch_suffix,
    lib_fixup_remove_proto_version_suffix,
    lib_fixup_vendorcompat,
    lib_fixups_user_type,
    libs_clang_rt_ubsan,
    libs_proto_3_9_1,
    libs_proto_21_12,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'vendor/xiaomi/sdm660-common',
    'device/xiaomi/sdm660-common',
    'hardware/qcom-caf/msm8998',
    'hardware/qcom-caf/wlan',
    'hardware/xiaomi',
    'vendor/qcom/opensource/data-ipa-cfg-mgr-legacy-um',
    'vendor/qcom/opensource/dataservices',
]

lib_fixups: lib_fixups_user_type = {
    libs_clang_rt_ubsan: lib_fixup_remove_arch_suffix,
    libs_proto_3_9_1: lib_fixup_vendorcompat,
    libs_proto_21_12: lib_fixup_remove_proto_version_suffix,
    (
        'libllvd_smore',
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    (
        'vendor/lib/hw/camera.sdm660.so',
    ): blob_fixup()
        .add_needed('libcamera_sdm660_shim.so'),
    (
        'vendor/lib/libFaceGrade.so',
        'vendor/lib/libXMFD_AgeGender.so',
        'vendor/lib/lib_lowlight.so',
        'vendor/lib/libarcsoft_beautyshot.so',
        'vendor/lib/libchromaflash.so',
        'vendor/lib/libdualcameraddm.so',
        'vendor/lib/libmmcamera_hdr_gb_lib.so',
        'vendor/lib/liboptizoom.so',
        'vendor/lib/libseemore.so',
        'vendor/lib/libtrueportrait.so',
        'vendor/lib/libts_detected_face_hal.so',
        'vendor/lib/libts_face_beautify_hal.so',
        'vendor/lib/libubifocus.so',
        'vendor/lib/libvideobokeh.so',
        'vendor/lib64/libchromaflash.so',
        'vendor/lib64/libdualcameraddm.so',
        'vendor/lib64/liboptizoom.so',
        'vendor/lib64/libseemore.so',
        'vendor/lib64/libts_detected_face_hal.so',
        'vendor/lib64/libts_face_beautify_hal.so',
        'vendor/lib64/libubifocus.so',
        'vendor/lib64/libvideobokeh.so',
    ): blob_fixup()
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'clover',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sdm660-common', module.vendor
    )
    utils.run()
