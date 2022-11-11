# Primetime
**Category:** Crypto
**Difficulty:** Medium?
**Author:** puzzler7

## Description

Alice and Bob are meeting up to watch TV, but they've neglected to invite Elise and Gamal! Elise and Gamal intercepted the network traffic between the two, and managed to extract an encrypted message. Can you help them figure out what TV show Alice and Bob will be watching, and when?

Wrap the decrypted message in the flag format before submitting.

## Distribution

primetime.py, output.txt

## Deploy notes

N/A

## Solution

The encryption is ElGamal encryption, implemented on a custom group. Each element of the group is essentially a number mod `2**128`, encoded in the following way:

1. The number is split into bytes
2. Starting with the least significant byte, raise the smallest prime to that power.
3. Repeat step 2 for more significant bytes.

Thus, the bytestring `ictf` can be encoded as `2**105 * 3**99 * 5**116 * 7**102`. While the numbers mod `2**128` is not a cyclic group, the generator point is coprime to `2**128`, and so are `akey` and `bkey`, as they are both odd.

Rather than raising the points to the power of the secret keys, as in normal El Gamal, this encryption simply multiplies, so the secret keys can be determined by finding the multiplicative inverse of the generator point, and multiplying it into the public keys. The plaintext can then be determined.
