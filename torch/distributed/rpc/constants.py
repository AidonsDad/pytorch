from datetime import timedelta

from . import (
    _DEFAULT_INIT_METHOD,
    _DEFAULT_NUM_SEND_RECV_THREADS,
    _DEFAULT_RPC_TIMEOUT_SEC,
    _UNSET_RPC_TIMEOUT,
)

try:
    from . import TensorPipeAgent, _TensorPipeRpcBackendOptionsBase
    _USE_TENSORPIPE = True
except ImportError:
    _USE_TENSORPIPE = False

# For TensorPipeAgent.
if _USE_TENSORPIPE:
    from . import _DEFAULT_NUM_WORKER_THREADS
    DEFAULT_NUM_WORKER_THREADS = _DEFAULT_NUM_WORKER_THREADS

# For any RpcAgent.
DEFAULT_RPC_TIMEOUT_SEC = _DEFAULT_RPC_TIMEOUT_SEC
DEFAULT_INIT_METHOD = _DEFAULT_INIT_METHOD

# For ProcessGroupAgent.
DEFAULT_NUM_SEND_RECV_THREADS = _DEFAULT_NUM_SEND_RECV_THREADS
# Ensure that we don't time out when there are long periods of time without
# any operations against the underlying ProcessGroup.
DEFAULT_PROCESS_GROUP_TIMEOUT = timedelta(milliseconds=2 ** 31 - 1)
# Value indicating that timeout is not set for RPC call, and the default should be used.
UNSET_RPC_TIMEOUT = _UNSET_RPC_TIMEOUT
