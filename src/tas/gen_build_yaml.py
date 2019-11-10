#!/usr/bin/env python2.7

# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
import os
import sys
import yaml

os.chdir(os.path.dirname(sys.argv[0])+'/../..')

out = {}

try:

  out['libs'] = [{
      'name': 'tas',
      'defaults': 'tas',
      'build': 'private',
      'language': 'c',
      'secure': 'no',
      'src': [
        "third_party/tas/lib/tas/conn.c",
        "third_party/tas/lib/tas/connect.c",
        "third_party/tas/lib/tas/init.c",
        "third_party/tas/lib/tas/kernel.c",
        "third_party/tas/lib/utils/rng.c",
        "third_party/tas/lib/utils/timeout.c",
        "third_party/tas/lib/utils/utils.c",
        "third_party/tas/tas/config.c",
        "third_party/tas/tas/fast/fast_appctx.c",
        "third_party/tas/tas/fast/fast_flows.c",
        "third_party/tas/tas/fast/fast_kernel.c",
        "third_party/tas/tas/fast/fastemu.c",
        "third_party/tas/tas/fast/network.c",
        "third_party/tas/tas/fast/qman.c",
        "third_party/tas/tas/fast/tests/tcp_common.c",
        "third_party/tas/tas/fast/trace.c",
        "third_party/tas/tas/shm.c",
        "third_party/tas/tas/slow/appif.c",
        "third_party/tas/tas/slow/appif_ctx.c",
        "third_party/tas/tas/slow/arp.c",
        "third_party/tas/tas/slow/cc.c",
        "third_party/tas/tas/slow/kernel.c",
        "third_party/tas/tas/slow/kni.c",
        "third_party/tas/tas/slow/nicif.c",
        "third_party/tas/tas/slow/packetmem.c",
        "third_party/tas/tas/slow/routing.c",
        "third_party/tas/tas/slow/tcp.c",
        "third_party/tas/tas/tas.c"
      ],
      'headers': [
        "third_party/tas/doc/index.h",
        "third_party/tas/include/kernel_appif.h",
        "third_party/tas/include/packet_defs.h",
        "third_party/tas/include/tas_memif.h",
        "third_party/tas/include/tas_trace.h",
        "third_party/tas/include/utils.h",
        "third_party/tas/include/utils_circ.h",
        "third_party/tas/include/utils_nbqueue.h",
        "third_party/tas/include/utils_rng.h",
        "third_party/tas/include/utils_sync.h",
        "third_party/tas/include/utils_timeout.h",
        "third_party/tas/lib/tas/include/tas_ll.h",
        "third_party/tas/lib/tas/include/tas_ll_connect.h",
        "third_party/tas/lib/tas/internal.h",
        "third_party/tas/tas/fast/dma.h",
        "third_party/tas/tas/fast/fastemu.h",
        "third_party/tas/tas/fast/internal.h",
        "third_party/tas/tas/fast/network.h",
        "third_party/tas/tas/fast/tcp_common.h",
        "third_party/tas/tas/include/config.h",
        "third_party/tas/tas/include/fastpath.h",
        "third_party/tas/tas/include/tas.h",
        "third_party/tas/tas/slow/appif.h",
        "third_party/tas/tas/slow/internal.h"
    ]
  }, {
      'name': 'tas_sockets',
      'defaults': 'tas',
      'build': 'private',
      'language': 'c',
      'secure': 'no',
      'src': [
        "third_party/tas/lib/sockets/interpose.c",
        "third_party/tas/lib/sockets/control.c",
        "third_party/tas/lib/sockets/context.c",
        "third_party/tas/lib/sockets/epoll.c",
        "third_party/tas/lib/sockets/manage_fd.c",
        "third_party/tas/lib/sockets/libc.c",
        "third_party/tas/lib/sockets/transfer.c",
        "third_party/tas/lib/utils/rng.c",
        "third_party/tas/lib/utils/timeout.c",
        "third_party/tas/lib/utils/utils.c",
        "third_party/tas/tas/config.c",
        "third_party/tas/tas/fast/fast_appctx.c",
        "third_party/tas/tas/fast/fast_flows.c",
        "third_party/tas/tas/fast/fast_kernel.c",
        "third_party/tas/tas/fast/fastemu.c",
        "third_party/tas/tas/fast/network.c",
        "third_party/tas/tas/fast/qman.c",
        "third_party/tas/tas/fast/tests/tcp_common.c",
        "third_party/tas/tas/fast/trace.c",
        "third_party/tas/tas/shm.c",
        "third_party/tas/tas/slow/appif.c",
        "third_party/tas/tas/slow/appif_ctx.c",
        "third_party/tas/tas/slow/arp.c",
        "third_party/tas/tas/slow/cc.c",
        "third_party/tas/tas/slow/kernel.c",
        "third_party/tas/tas/slow/kni.c",
        "third_party/tas/tas/slow/nicif.c",
        "third_party/tas/tas/slow/packetmem.c",
        "third_party/tas/tas/slow/routing.c",
        "third_party/tas/tas/slow/tcp.c",
        "third_party/tas/tas/tas.c"
      ],
      'headers': [
        "third_party/tas/doc/index.h",
        "third_party/tas/include/kernel_appif.h",
        "third_party/tas/include/packet_defs.h",
        "third_party/tas/include/tas_memif.h",
        "third_party/tas/include/tas_trace.h",
        "third_party/tas/include/utils.h",
        "third_party/tas/include/utils_circ.h",
        "third_party/tas/include/utils_nbqueue.h",
        "third_party/tas/include/utils_rng.h",
        "third_party/tas/include/utils_sync.h",
        "third_party/tas/include/utils_timeout.h",
        "third_party/tas/lib/sockets/include/tas_sockets.h",
        "third_party/tas/lib/sockets/internal.h",
        "third_party/tas/lib/tas/include/tas_ll.h",
        "third_party/tas/lib/tas/include/tas_ll_connect.h",
        "third_party/tas/lib/tas/internal.h",
        "third_party/tas/tas/fast/dma.h",
        "third_party/tas/tas/fast/fastemu.h",
        "third_party/tas/tas/fast/internal.h",
        "third_party/tas/tas/fast/network.h",
        "third_party/tas/tas/fast/tcp_common.h",
        "third_party/tas/tas/include/config.h",
        "third_party/tas/tas/include/fastpath.h",
        "third_party/tas/tas/include/tas.h",
        "third_party/tas/tas/slow/appif.h",
        "third_party/tas/tas/slow/internal.h"
    ]
  }]
except:
  pass

print yaml.dump(out)
