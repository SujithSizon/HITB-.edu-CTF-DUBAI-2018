# HITB .edu CTF DUBAI 2018 Writeups

> Medium and hard challenge solutions solved by Team Cartel, 2nd prize winners. My other team member Sachin Samuel is a bitbucket fanboi.

## CAPTURE VENZUELA
Open executable with Ollydbg

![](https://lh3.googleusercontent.com/GU_IzNj0lEMfxJZzrmNrJDNjk995L1kiiqTOrH4TjRg6E0PBnv37sZ61aYeMtNm0oWPC5f90ZIG0J74FZZ08njPTwhvE-pIYLlfmx2OcVZ5lZNmSGJWiUyjIJ6jyl_UrxFoXRk9n_II)

Set appropriate breakpoints

![](https://lh6.googleusercontent.com/QiHSRWuDIxQSZd-BDKLjLh8WRcb4N8leR20r1RoBsG-IbMstwN23cVauh1vsr781iCtI2Yp8cbAzybdWOVQ_K3GRJ0InxZ7ATgtUkOsQlxdG94p03FOw6OmYDccYOp1Vf85ptGRj8IU)

Inspect Memory

![](https://lh6.googleusercontent.com/6cFRWyg6UpYDwU4HH0aUCIelg7zoAXAhGJGpDUIjQrqVviG0ICmUXwKZWNZT_e-fA5ZPxO3tx1Lxl8OZuyop0C8YPuQgAcJei946xJz53BiTSjj6btYF7h0bAMml1eMKnedAccMAQH4)

Some python scripting

![](https://lh6.googleusercontent.com/vTkpivkkJ6fh2ctonZKOacIWKzmNUNxxgpcK0ITDtvXYvTsyGzGxwYuU6dL75aJR7qCBketRGKv9arnQlvnzAk-PcfD7m9k3L3_A5aPdBzO7zlT6m-92OkHua_hVG_lUEe6uPwfLd08)



## ALIEN WAV
Use the hint Slow scanning television

![](https://lh5.googleusercontent.com/Ofv7vaVG9x4TO9IeygYMJWeM0_zoDlFHD8qHuL84e7TXitEUfvLDCifZP-Rq-dugiPuioiy5khuWo6EtDx8LgcG5MCJAxZt112Du80t5hRZMwsHZgqElkk-WEEgrsgb97tqwpR6hle4)

Play the file to get the flag

![](https://lh3.googleusercontent.com/4wb1kCKRoW4s7SKjREwpKovmeacDWyA0v8jBqHcJRSgStuyV69W3VhwyEO-HSdqOeXbxHIfYP9FbhMBPQwGA3iUoErSnDL3gmPU86-R10ywdz-mP9i5SywCK9WrGwYHUE0Ge-h0vvPM)

ROT13 the string and base64 decode

![](https://lh3.googleusercontent.com/TmI0ZLhWYtHOeIG32v5nQnii_Xv6MgWffmQ1KqgqGN_eqr2CDVcv9Uqnef3nHvvpyZ01v2ohn9K0JCKSVOVQQfo05zMlJGxyTvojFMu7DUZpoG12kLA_8mex4p8S_lk1ItoKUYhxSAw)
![](https://lh3.googleusercontent.com/aZ1SPPLOyQgqYLMyzZSp2I_PU0DIuEKZ4BqArFg4kZYtXYNHKhtTVXVv4Uwbj6GyWC_ti4DABmbLZ7NwBuyEQ5jc0Te1mx-FoSalZ_nG56oOzaT97CpumFXOcWRrUuYSonfK1BKoIn0)


## FUNNY VIDEO
Check exiftool output

![](https://lh4.googleusercontent.com/oXqXUYeb08oXA-A8DXCrCbTTvorytk1u6XJMSWdQ4oDNcCjFu4fT4tMO5kPZWWyw7ZcpzVjew1Vk9qaFzzYowbWt4plSUvyI1_mdZl_jAOhs0l6hFH9X9wS7euwpizoMonbEItHHQWM)

Use MKVToolNix to recon the contents

![](https://lh5.googleusercontent.com/5qV4QRJrmIYeSjTR_7Nbnph_HgaFeQ-apAY--vWvs57UcecTa1JpBPaUA9w7E-wIO_tLRE47aiO5LtFwKtyOpRFjaXOj3133lxrHIYdRyspG6wjFrPq5y8ihttMTx6CHhc0vDNAjFJk)

Extract the hidden audio file

![](https://lh4.googleusercontent.com/UalWtCdq-3TTDG0wa2mijFbb_scZBacKpUjxYUB1hrb1e9bxVkW-a4siauLPyOutpV7IpiUHmjgqgf1Xd4pRjKPByoZlb8qRuouPDslzHEdqx2gGp7Y9CDqZ9TnyppQ93G8-CP9GfVU)

Pane > Add Spectogram > Channel 1

![](https://lh3.googleusercontent.com/fPrF0ueFojghIPDCQ24o4q4QAE8Xu1LiI73jbz4E0QZJhKF1k23-5Rah3z87j1JlZa89E6mbm7JTztpUi0UCurfhIArt5MQ6cAndcNOdAqrZUVaLBvMaKdafca7Z4jfGx0oMRDb85B0)

## NORMAL ZIP
Initial recon of the zip file

![](https://lh3.googleusercontent.com/JtAmXCXOTrYH-tijb__TRZKRU9a046cWNPtvhTtF1Bs4MtlOb9QC9XWZWNSNYk-UoIMOxzCM0akO1GwP-t4PwgLkhmvNckUyhPKhH2ZRO34U1VxZ9Ad8sDEZkYO3mVmWJ-YKGKMfT6Y)

Download a CRC32 cracker

![](https://lh3.googleusercontent.com/0fHk4HR9-l7JQstDgXnp882bmGiPPmH4uN-rDOKTYwmg0rYNcv2Zp1awv7C3cUWfrBPXWia4P3VNGpepCI5P1hiDLAQ5-1LJaF8s0t_cHuqwNASd2zkjPg1BC6DgqHA4Hb3yEbvYvgo)

Extract flag in the correct order

![](https://lh4.googleusercontent.com/3sBQq8Q6t0R0PMvr5mLHXThAd64N4qdxy-ilmJgeRB2tp6h6-DE4JqEbtvI7BBt0yOsI5uEM8GEiXslssCZ3mTT2Jm0mFLYb-mMCUOwsUzTBhfFO-wneYwndlMVJl9oSGSDd48DOSYE)
