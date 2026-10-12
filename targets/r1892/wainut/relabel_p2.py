"""WAINUT comparison of the R1892 p2 word signs (see ../NOTES.md, "Additions from an independent reading").

Reads ../transcription_p2.txt and writes, next to this script:
  transcription_p2_wainut.txt     the same tokens, with the sign labels split where two shapes share one label
                                  (shape names as in the NOTES section); no digit pair changed
  transcription_p2_wainut_tr.txt  the same, plus three image-checked digit re-readings
                                  (line 13 'myn vader'; line 20 'ras'; line 24 'myn vertrek blood-')
Line numbers below are the lines of ../transcription_p2.txt.  usage: python relabel_p2.py
"""
import os
NL = chr(10)
HERE = os.path.dirname(os.path.abspath(__file__))
L = open(os.path.join(HERE, '..', 'transcription_p2.txt'), encoding='utf8').read().split('\n')


def sub(i, old, new):
    s = L[i - 1]; k = s.index(old)          # first occurrence still carrying the old label
    L[i - 1] = s[:k] + new + s[k + len(old):]


# label splits: Bourdeau label -> shape (value in apply.py here)
sub(4, '<hook>', '<zo-I>'); sub(4, '<c-symbol>', '<c~>')
sub(6, '<delta>', '<Delta>'); sub(6, '<gamma>', '<gamma-z>'); sub(6, '<c-symbol>', '<c~>')
sub(7, '<cross>', '<r-sign>'); sub(7, '<gamma>', '<Yplain>')
sub(8, '<hook>', '<r-sign>'); sub(8, '<G>', '<C-loop>')
sub(9, '<phi>', '<phi-stem>'); sub(9, '<c-symbol>', '<c~>')
sub(10, '<gamma>', '<gamma-z>')
sub(11, '<slash>', '<dot-stroke>')
sub(12, '<c-symbol>', '<c~>'); sub(12, '<G>', '<C-loop>')
sub(13, '<G>', '<C-loop>'); sub(13, '<c-symbol>', '<c~>'); sub(13, '<Y>', '<Y-bar>'); sub(13, '<phi>', '<phi-stem>')
sub(13, '<check>', '<leaf-check>')
sub(15, '<8>', '<inf>'); sub(15, '<psi>', '<Psi>'); sub(15, '<cf>', '<e-ess>'); sub(15, '<H>', '<zo-I>')
sub(16, '<slash>', '<dot-stroke>'); sub(16, '<cf>', '<e-ess>'); sub(16, '<hook>', '<r-sign>'); sub(16, '<G>', '<C-loop>')
sub(17, '<hook>', '<r-sign>'); sub(17, '<Y-cross>', '<Y-bar>'); sub(17, '<G>', '<C-loop>')
sub(18, '<I>', '<I-sign>'); sub(18, '<Y-cross>', '<Y-bar>')
sub(19, '<cf>', '<e-ess>')
sub(20, '<cross>', '<cross-m>'); sub(20, '<psi>', '<phi-stem>'); sub(20, '<hook>', '<r-sign>')
sub(20, '<gamma>', '<gamma-z>'); sub(20, '<H>', '<zo-I>')
sub(21, '<H>', '<zo-I>'); sub(21, '<G>', '<C-loop>'); sub(21, '<cf>', '<e-ess>'); sub(21, '<hook>', '<r-sign>')
sub(21, '<H>', '<zo-I>')
sub(22, '<hook>', '<r-sign>'); sub(22, '<Y-cross>', '<Y-bar>')
sub(24, '<slash>', '<dot-stroke>'); sub(24, '<G>', '<C-loop>')
open(os.path.join(HERE, 'transcription_p2_wainut.txt'), 'w', encoding='utf8', newline=NL).write('\n'.join(L))

# digit re-readings, checked on the full-resolution image (NOTES section)
sub(13, '25 13 32 32 43 31 65 52', '25 13 32 33 43 31 65 52')          # myn vader (4th pair 3 over 3)
sub(20, '2? 63? 44', '52 43 44')                                        # ras
sub(24, '25 33? 32? 6? 55? 12? 51? 62? 25? 33? 15? 25? 22? 32?',
    '25 13 32 33 65 52 11 52 65 23 35 15 22 22 31')                     # myn vertrek bloot-
sub(24, '12 61? 65 44 11?', '12 65 65 44 11')                           # geweest
open(os.path.join(HERE, 'transcription_p2_wainut_tr.txt'), 'w', encoding='utf8', newline=NL).write('\n'.join(L))
print('wrote transcription_p2_wainut.txt and transcription_p2_wainut_tr.txt')
