---
title: End-to-Same-End Encryption
categories: Events
date: 2022-12-20
tags: Computer Security
draft: false
---
![slide]({static}/images/e2se.png "talkslide")

**Spekaer:** [**Dr.Qiang Tang**](https://alkistang.github.io/)  is currently a Senior Lecturer at the School of Compuuter Science at USYD doing research on cryptography and blockchain. From 2016-2021, he was an assistant professor at New Jersey Institute of Tech in the US and Director of JD-NJIT-ISCAS Joint Blockchain Lab. Before join NJIT, he was a postdoc at Cornell. 

**Time:** Monday 4:00 ~ 6:00 pm, 20 Dec 2022

**Location:** J12 Lecture Theatre, 1 Cleveland St, Darlington NSW 2008 OR Via [ZOOM](https://zoom.us)

**Abstract:** The cloud has become pervasive, and we ask: how can we protect cloud data against the cloud itself? For messaging Apps, facilitating user-to-user private communication via a cloud server, security has been formulated and solved efficiently via End-to-End encryption, building on existing channels between end-users via servers (i.e., exploiting TLS, certificates, and encryption, without the need to program new primitives). However, the analogous problem for Apps employing servers for storing and retrieving end-user data privately, solving the analogous "privacy from the server itself" (cloud-blind storage) where (1) based on existing messaging/infrastructure and (2) allowing user mobility, is, in fact, still open. Existing proposals, like password protected secret sharing (PPSS), target end-to-same-end encryption of storage, but need new protocols, whereas most popular commercial cloud storage services are not programmable. Namely, they lack the simplicity needed for being portable over any cloud storage service.

Here, we propose a novel system for storing private data in the cloud storage with the help of a key server (necessary given the requirements). In our system, the user data will be secure from any of: the cloud server, the key server, or any illegitimate users, while the authenticated user can access the data on any devices just via a correct passphrase. The most attractive feature of our system is that it does not require the cloud storage server to support any newly programmable operations, except the existing client login and the data storing. Moreover, our system is simply built on top of the existing App password login system, so the user only needs one passphrase to login the App and access his secure storage. The security of our protocol, in turn, is proved under our rigorous models, and the efficiency is further demonstrated by real-world network experiments over Amazon S3. We remark that a very preliminary variant, based on our principles, was deployed by Snapchat in their My Eyes Only module, serving hundreds of millions of users!



**Relevant Papers:** Chen, Long, et al. "{End-to-Same-End} Encryption: Modularly Augmenting an App with an Efficient, Portable, and Blind Cloud Storage." 31st USENIX Security Symposium (USENIX Security 22). 2022.