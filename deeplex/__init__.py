"""
Author: OrigamiDream
Date: 2024-04-19

Copyright © 2024 by OrigamiDream, All Rights Reserved.
"""
from deeplex.deeplex import _translate, _TooManyRequestsError

translate = _translate
TooManyRequestsError = _TooManyRequestsError

__all__ = ['translate', 'TooManyRequestsError']
