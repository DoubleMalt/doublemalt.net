Title: Secure Messaging for The Masses - Towards A Magical PGP Workflow
Date: 2014-06-12 19:03
Category: security
Tags: security, pgp, mail
Slug: secure-messaging-for-the-masses

## tl;dr

PGP encryption of emails is to cumbersome for global adoption. We need a 
workflow that magically enhances email communication with PGP (or similar) if 
the possibility is there.

## The State of Affairs: Sorry

Emails are like post cards. Not all people realize that.

For a long time email provider sent these postcards around in open trucks. 
Every node between the mail server of the sender was created and the mail server 
of the recipient had the possibility to read and analyze the content. 

Massive amounts of corporate, national and personal secrets were accessible by 
any big backbone provider. The SMTP protocol was developed in happier days when 
all email was used for was the free exchange of scientific research.

Open trucks got the job done and nobody cared about envelopes. Some people got 
worried about this and devised a [standard][ietf] that gave the sender the 
possibility to send the postcard in a sealed truck.

Using this method the sender could make sure that not everyone on the highway 
could read the postcards. However a recent [study][cnet] showed how few mail 
providers made use of even this basic protection.

Of course even with mail servers using opportunistic encryption in there 
communication among each other, there was this glaring hole. The receiving mail 
server had access to the complete communication. Interested parties could 
therefore learn the contents of a conversation by bribing or strong arming the 
mail provider. Worse, on the servers of big mail providers like Gmail, Hotmail 
and others, the complete mail history is accessible and an be retrieved using 
this tactic. At least the NSA and the FBI chose to do so in many circumstances.

A prominent victim of these insecure practices was ironically the CIA director 
General Petraeus, whose indiscretions came to light because of the never 
forgetting archive of Gmail.

Of course these deficiencies did not go unnoticed. Already in 1991 (before the 
invention of sealed trucks), the digital equivalent to an envelope was 
developed, PGP. Even better than an envelope PGP, based on strong asymmetric 
encryption could guarantee that only the intended receiver of a message would 
be able to read it. It also introduced a way of signing the message, ensuring 
integrity and certifying the origin. These advantage however came at a 
fundamental disadvantage that would lead to our current woes. It was incredibly
complicated to use.

## The User's Perspective: Don't Bother Me!

In 1883 a Dutch professor of linguistics wrote 
[two articles on cryptography][kerckhoff] that would revolutionize the field. 
In them he outline 6 design principles for military ciphers. And while the 
second one was promoted (and justifiedly so) to be known as THE 
[Kerckhoffs's principle][wikipedia] the sixth is probably as important.

According to _Kerckhoff's sixth principle_ "it is necessary, given the 
circumstances that command its application, that the system be easy to use, 
requiring neither mental strain nor the knowledge of a long series of rules to 
observe." In short, it should _Work Like Magic&trade;_.

Unfortunately PGP is everything else. This is the normal workflow of writing an   
email:

1. Select recipient
2. Write email
3. Hit send

For the average user the workflow to sending the first end-to-end secured 
message would be something like this.

 1. Discover that the current method of messaging is insecure
 2. Find out about PGP
 3. Find a tool to send PGP encrypted mails  
 4. Find out what a keypair is and create one
 5. Select recipient
 6. Find out if recipient has a published public key on one of the public key 
    servers
 7. Find out if this key can be trusted
 8. Find out how to import this key into your tool
 9. Write mail
10. Find out what signing you email means
11. Sign and encrypt your email
12. Hit Send 

These are 9 additional steps, each of which is a mountain of complexity for the 
non-technical user. Of course some of the steps might only be necessary the 
first time, but that doesn't matter. The mountain range is high enough that 
only a select few high energy individuals will make it to the other side.

To enable mass adoption of secure messaging we have to make it possible to cut 
down the workflow for sending PGP mail to the original three steps, select 
recipient, write email and hit send.


## The Way Ahead: We Need Infrastructure

## Conclusion: Magic Is A Lot Of Work




[ietf]: https://tools.ietf.org/html/rfc3207 "SMTP over TLS"
[cnet]: http://www.cnet.com/news/how-web-mail-providers-leave-door-open-for-nsa-surveillance/
[kerckhoff]: http://petitcolas.net/fabien/kerckhoffs/ "Kerckhoff's papers"
[wikipedia]: https://en.wikipedia.org/wiki/Kerckhoffs's_principle "Kerckhoffs's principle"
