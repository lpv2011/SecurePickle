# SecurePickle

The idea behind this project is to on enhancing the security of Python's pickle module. 
The main security concerns behind the current pickle module are:
  1. Pickle files allow arbitrary code execution – Pickle can store arbitrary Python objects, an attacker can craft a malicious pickle file that, when loaded, executes arbitrary code on the system.
  2. Pickles are not integrity-protected – There’s no built-in way to verify whether a pickle file has been tampered with, meaning an attacker could modify an ML model’s weights or logic.
  3. Pickles do not provide confidentiality – Pickled ML models can be easily deserialized and inspected, making proprietary models vulnerable to reverse engineering.
  4. Pickles lack authentication – There’s no way to verify that a given pickle file comes from a trusted source, leading to supply chain risks.

Pickle module implementation of serialization and de-serialization
![picklemodule](https://github.com/user-attachments/assets/fbcd4cf8-38a5-4d04-ac31-1614f68a6ff1)

Implementation of SecurePickle v0.1.0
![spicklev010](https://github.com/user-attachments/assets/56bcaf00-4dd1-432d-a091-9accdb4d8007)
