class AirdropClaimHistory:
    def __init__(self, airdrop_id, airdrop_window_id, address, txn_status, txn_hash, claimable_amount, claimed_on, airdrop_window_registration, action_type):
        self._airdrop_id = airdrop_id
        self._airdrop_window_id = airdrop_window_id
        self._address = address
        self._txn_status = txn_status
        self._txn_hash = txn_hash
        self._claimable_amount = claimable_amount
        self._claimed_on = claimed_on
        self._registered_at = str(airdrop_window_registration.registered_at)
        self._is_eligible = None
        self._action_type = action_type

    def is_eligible(self):
        return True if int(self._claimable_amount) > 0 else False

    def to_dict(self):
        return {
            "airdrop_id": self._airdrop_id,
            "airdrop_window_id": self._airdrop_window_id,
            "user_address": self._address,
            "txn_hash": self._txn_hash,
            "txn_status": self._txn_status,
            "claimable_amount": self._claimable_amount,
            "claimed_on": self._claimed_on,
            "registered_at": self._registered_at,
            "is_eligible": self.is_eligible(),
            "action_type": self._action_type
        }
