Title: Make Encrypted Email The Default - Towards A Magical PGP Workflow - Part 2
Date: 2014-06-23 09:30
Category: security
Tags: security, pgp, mail
Slug: secure-email-for-the-masses-2
Ycombinatorid_: 7898406

## TL;DR


## It's Difficult - So Let's Start Working On It

In the [last post][secure-emails-1] I laid out a multi step program to achieve
the mass adoption of secure end-to-end messaging.

As the first step I demanded to make encrypted email the default.

To achieve this all (or at least all major) email clients and services must 
incorporate this policy. It will be a long march to achieve this, but that just 
makes it more important to get started on the task.

Three things have to be solved for this to be successful:

1. Discovery if there is a key for a email address the user wants to use
2. Creating a key pair if none exists
3. Distributing the secret key to all the user's devices

## Desktop Clients

Until seven years ago, desktop email clients where all that mattered. Outlook 
Express and Thunderbird ruled the private machines while Outlook was omnipresent
in corporate environments with the odd Lotus Notes installation sprinkled in.

And while Outlook still profits from the inertia of its users, Thunderbird and 
Outlook Express are mostly wiped out by the advent of webmail services, the 
demise of Windows XP and the increased usage of mobile devices for personal 
communication.

The Mozilla Foundation pulled most of the support from Thunderbird years ago and
Windows Live Mail (like WIndows 8) did not appela to all users. For completenes'
sake there exists an [extension for Thunderbird that enables PGP][enigmail] but 
like its host program it's hard to imagine a bright future for it.

In some corporate environments there exists infrastructure for encrypted emails
(often enabled chipcards), but it is usually not turned on by default and very 
often not even within the organization the rollout is pervasive.

## Mobile CLients

Mobile clients come in three flavours. 

1. Default operating system clients (Android Mail, the iOS mail client, Windows)


## Centralized Web Clients



 





[ietf]: https://tools.ietf.org/html/rfc3207 "SMTP over TLS"
[cnet]: http://www.cnet.com/news/how-web-mail-providers-leave-door-open-for-nsa-surveillance/
[petraeus]: http://swampland.time.com/2012/11/15/spyfall/ "Petraeus' Fall"
[kerckhoff]: http://petitcolas.net/fabien/kerckhoffs/ "Kerckhoff's papers"
[wikipedia]: https://en.wikipedia.org/wiki/Kerckhoffs's_principle "Kerckhoffs's principle"
[email-self-defense]: https://emailselfdefense.fsf.org/ "Email Self-Defense"
[google-end-to-end]: https://code.google.com/p/end-to-end/ "Google's PGP browser extension"
[mailpile]: https://mailpile.is/
[cloudfleet]: https://cloudfleet.io/
