Title: Secure Email For The Masses - Towards A Magical PGP Workflow - Part 1
Date: 2014-06-13 02:30
Category: security
Tags: security, pgp, mail
Slug: secure-email-for-the-masses-1

## TL;DR

PGP encryption of emails is to cumbersome for global adoption. We need a 
workflow that magically enhances email communication with PGP (or similar) if 
the possibility is there. In this post I will outline the obstacles on the way
to secure email for everyone. I will follow up with posts containing detailed 
and concrete suggestions on how to get rid of these.

## The State of Affairs: Sorry

Emails are like postcards. Not all people realize that.

For a long time, email providers sent these postcards around in open trucks. 
Every node between the mail server of the sender and the mail server 
of the recipient had the possibility to read and analyze the content. 

Massive amounts of corporate, national and personal secrets were accessible to 
any big backbone provider. The SMTP protocol was developed in happier days when 
all email was used for the free exchange of scientific research.

Open trucks got the job done and nobody cared about envelopes. Some people got 
worried about this and devised a [standard][ietf] that gave the sender the 
possibility to send the postcard in a sealed truck.

Using this method, the sender could make sure that not everyone on the highway 
could read the postcards. However a recent [study][cnet] showed how few mail 
providers make use of even this basic protection.

Of course, even with mail servers using opportunistic encryption in their 
communication among each other, there was this glaring hole. The receiving mail 
server had access to the complete communication. Interested parties could 
therefore learn the contents of a conversation by bribing or strong-arming the 
mail provider. Worse, on the servers of big mail providers like Gmail, Hotmail 
and others, the complete mail history is accessible and can be retrieved using 
this tactic. At least the NSA and the FBI chose to do so in many circumstances.

A prominent victim of these insecure practices was ironically the [CIA director 
General Petraeus][petraeus], whose indiscretions came to light because of the 
never-forgetting archive of Gmail.

Of course these deficiencies did not go unnoticed. As early as 1991 (before the 
invention of sealed trucks), the digital equivalent to an envelope was 
developed, PGP. Even better than an envelope, PGP was based on strong 
asymmetric encryption that could guarantee that only the intended receiver of a 
message would be able to read it. It also introduced a way of signing the 
message, ensuring integrity and certifying the origin. These advantages, 
however, were offset by a fundamental disadvantage that would lead to our 
current woes. It was incredibly complicated to use.

## The User's Perspective: Don't Bother Me!

In 1883, a Dutch professor of linguistics wrote 
[two articles on cryptography][kerckhoff] that would revolutionize the field. 
He outlined six design principles for military ciphers. And while the second one 
was promoted (and justifiedly so) to be known as _the_ 
[Kerckhoffs's principle][wikipedia], the sixth is arguably as important.

According to Kerckhoff's sixth principle, "it is necessary, given the 
circumstances that command its application, that the system be easy to use, 
requiring neither mental strain nor the knowledge of a long series of rules to 
observe." In short, it should _Work Like Magic&trade;_.

Unfortunately, PGP does anything but that. This is the normal workflow of 
writing an email:

1. Select recipient
2. Write email
3. Hit send

For the average user, the workflow for sending the first end-to-end secured 
message would be something like this:

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
10. Find out what signing your email means
11. Sign and encrypt your email
12. Hit Send 

These are nine additional steps, each of which is a mountain of complexity for 
the non-technical user. Of course some of the steps might only be necessary the 
first time, but that doesn't matter. The mountain range is high enough that 
only a select few high-energy individuals will make it to the other side.

The [email self defense tutorial][email-self-defense] by the FSF is a good start, but not enough.
To enable mass adoption of secure messaging, we have to make it possible to cut 
down the workflow for sending PGP mail to the original three steps: select 
recipient, write email and hit send.


## The Way Ahead: Moving One Rock At A Time

### Make Encrypted Email The Default

As a solution to the first three steps of the twelve step secure messaging 
workflow people usually call for educating the user. 
I disagree. Strongly. Everyone who has created user-facing software for a while 
recognizes at some point that sane defaults are by orders of magnitude more 
important than configuration options. We will not succeed by educating users 
to do something really cumbersome. PGP encryption has to be present and the 
default everywhere, from the Gmail web interface to the Thunderbird mail client.

Google is starting a laudable effort by creating [End-To-End][google-end-to-end],
but this is not enough. Encryption must be baked in. This will be hard to do 
in webmail clients with any sort of strong security guarantee, but it is 
critical for secure email to succeed. Initiatives like [Mailpile][mailpile] and
[cloudfleet][cloudfleet] will hopefully lead the way. 

### Make Encryption Transparent For The User

Step four must then be done by the mail client of your choice. Users do not 
need to know how the encryption works, much like car drivers do not need to 
know how an airbag works. It just has to be there and do its job.

A key pair will be created and shared on key servers. There are some hard 
problems to solve, though. 

How will the key pair be shared between different devices? With Mailpile and 
cloudfleet this is not a problem, but the vast majority of users will need a 
different solution.

How will the key be verified and signed by others? Again we don't want to 
require the user to do any out-of-band communication initially, which is the 
only way to establish identity beyond reasonable doubt. 

### Discover And Verify The Recipient's Key

A key server infrastructure already exists. However not all keys are present on 
each key server and the APIs to query a key associated with a specific email 
address are cumbersome (or even require a Captcha).

We need a clearing house for all published PGP keys, preferably a decentralized 
one. A great use case for a DHT or a blockchain.

How do we verify that the key we received really belongs to the person we want 
to contact? The traditional PGP way is the web of trust. People sign the keys 
of other people when they know the keys are associated with the right person.
And if there is a trusted path from you to the key, then you can trust it. 
Another method is publishing the key's fingerprint on a public site. This 
however, assumes that you can trust that the person in possession of the key is 
also in full control of the website where the fingerprint was published. Also 
there is no standardized way to discover this.

Still, even a mail encrypted with an untrusted key is no worse than a mail sent 
in plain text. And if the recipient responds by professing not to have access 
to the appropriate private key it can safely be blacklisted.


### Automatically Sign And Encrypt

At this point, all that is left for us to remove from the user's workflow is the 
encrypting and signing of the message. As we established in the above, the user 
will need a mail client that uses PGP by default. If all the other 
additional steps are automated, the mail client should be in possession of 
everything it needs: the private key of the sender to sign the message and the 
public key of the recipient to encrypt it. Doing this can be triggered by the 
user hitting the send button. Secure email FTW!  


## Conclusion: Magic Is A Lot Of Work

Almost all of the problems laid out above are hard. And the grail of secure 
email for everyone needs all of them obliterated. This will be a lot of work. 
But we can start moving a rock at a time, knowing that the intermediate steps 
will not generally solve the problem. 





[ietf]: https://tools.ietf.org/html/rfc3207 "SMTP over TLS"
[cnet]: http://www.cnet.com/news/how-web-mail-providers-leave-door-open-for-nsa-surveillance/
[petraeus]: http://swampland.time.com/2012/11/15/spyfall/ "Petraeus' Fall"
[kerckhoff]: http://petitcolas.net/fabien/kerckhoffs/ "Kerckhoff's papers"
[wikipedia]: https://en.wikipedia.org/wiki/Kerckhoffs's_principle "Kerckhoffs's principle"
[email-self-defense]: https://emailselfdefense.fsf.org/ "Email Self-Defense"
[google-end-to-end]: https://code.google.com/p/end-to-end/ "Google's PGP browser extension"
[mailpile]: https://mailpile.is/
[cloudfleet]: https://cloudfleet.io/
