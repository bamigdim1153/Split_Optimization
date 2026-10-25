# Public DVC teaching cache

This directory contains the actual DVC object pushed to the verified local remote, mirrored here to make the synthetic workshop dataset retrievable through a public HTTP remote. It contains only the already-public synthetic CSV, not company records. Do not edit object bytes manually. The full Git snapshot in data/synthetic is retained as an independently readable teaching copy; DVC restores data/versioned/blasts_SYNTHETIC.csv.

The public HTTP mirror is read-only for DVC users; new versions require the maintainer to DVC-push to a writable staging remote and publish the resulting object. GitHub storage is appropriate here only for this small teaching object, not a production large-data architecture.
