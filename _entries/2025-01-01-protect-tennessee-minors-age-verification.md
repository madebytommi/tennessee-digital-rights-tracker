---
title: "Tennessee requires age verification for websites covered by the Protect Tennessee Minors Act"
date: 2026-07-18
event_date: 2025-01-01
last_reviewed: 2026-07-18
status: "Active"
level: "State"
category: "online-identity-age-verification"
jurisdiction: "Tennessee"
confidence: "Medium"
summary: "Tennessee Code § 39-17-912 requires websites containing a statutorily substantial portion of covered material to verify that users are adults through a photo-to-ID match or a commercially reasonable transactional-data method. The law prohibits retaining personally identifying information after access but requires at least seven years of anonymized verification evidence. It remains in effect while a federal challenge continues, and a 2025 amendment deleted the law’s section-specific definition of covered content, leaving important scope, implementation, and privacy questions unresolved."
primary_source_url: "https://wapp.capitol.tn.gov/apps/BillInfo/Default?BillNumber=SB1792&GA=113"
primary_source_type: "law"
source_archive_url: ""
tags:
  - age-verification
  - identity
  - privacy
  - online-speech
  - adult-content
  - biometrics
revision_history:
  - date: 2026-07-18
    note: "Initial publication based on Public Chapters 1021 and 405, the current statutory history, federal court records, the Supreme Court’s Paxton decision, and publicly available technical and civil-liberties analysis."
---

## Research and legal limitations

This entry is public-record research, not legal advice. The project and its contributors:

- are not acting as attorneys and cannot provide a binding legal opinion;
- cannot guarantee that Tennessee, a website operator, or an age-verification provider has publicly disclosed every implementation detail;
- cannot independently verify nonpublic identity checks, data flows, deletion processes, security controls, vendor contracts, access logs, or enforcement investigations; and
- recommend review by a qualified Tennessee attorney, privacy professional, security expert, accessibility specialist, or age-assurance expert before drawing especially strong legal or technical conclusions.

The absence of a public document does not prove that no safeguard or restriction exists. Unknowns are identified rather than filled with assumptions.

## What happened?

Governor Bill Lee signed Senate Bill 1792, the companion to House Bill 1614, on May 28, 2024. It became Public Chapter 1021 and took effect on January 1, 2025. The final bill passed the Senate 31-0 and the House 96-0.

The law, codified at Tennessee Code § 39-17-912 and titled the Protect Tennessee Minors Act, requires covered website publishers and distributors to verify that users are at least eighteen years old. It also imposes data-handling obligations, civil liability, criminal penalties, and attorney-general enforcement authority.

A federal district court preliminarily blocked enforcement on December 30, 2024. On January 13, 2025, the United States Court of Appeals for the Sixth Circuit stayed that injunction, allowing the law to take effect while litigation continued.

On May 8, 2025, Public Chapter 405 amended the statute by deleting its section-specific definition of “content harmful to minors.” The statute’s operative provisions continue to use that phrase.

On June 27, 2025, the United States Supreme Court upheld a different age-verification law in *Free Speech Coalition, Inc. v. Paxton*. The Tennessee challenge was not automatically resolved by that decision. The plaintiffs later stated that they intended to continue the case, and their current public lawsuit tracker lists the Tennessee case as in progress and the law as in effect.

## What the primary source says

### Which websites are covered?

The statute applies to an individual or commercial entity that publishes or distributes in Tennessee a website containing a “substantial portion” of content harmful to minors.

“Substantial portion” is defined as at least thirty-three and one-third percent of the total amount of data available on the website.

The original 2024 enactment contained a detailed definition of “content harmful to minors.” Public Chapter 405 deleted that section-specific definition in 2025 without removing the phrase from the age-verification requirement.

Tennessee’s obscenity statutes contain a separate general definition of “harmful to minors” elsewhere in the same statutory part. Whether and precisely how that general definition governs § 39-17-912 after the 2025 deletion is a question of statutory interpretation. This tracker does not provide a binding conclusion about the law’s current coverage.

### Required age-verification methods

A covered publisher must verify the age of each active user before allowing access and must verify the user again after the end of an “age-verified session.” That session lasts for the lesser of:

- the user’s current website session; or
- sixty minutes from the previous verification.

The statute identifies two permitted categories of verification:

| Verification route | What the statute describes |
|---|---|
| Photo and government identification | A photograph taken during the access attempt is matched to the photograph on a valid state-issued form of identification. |
| Transactional-data method | A commercially reasonable method uses public or private transactional data to determine that the person is at least eighteen. The statutory examples of transactional data include mortgage, education, or employment records. |

The law does **not** require every covered website to use a government-ID upload or facial comparison. It allows the transactional-data alternative. At the same time, the statute does not provide detailed technical standards for either route.

### Data retention and deletion

A website owner, commercial entity, or third party performing the verification must:

- retain at least seven years of historical anonymized age-verification data; and
- not retain personally identifying information after access to the covered content has been granted.

The statute defines the retained anonymized evidence to include, at minimum:

- architectural diagrams showing the technological assets and logical verification process; and
- data demonstrating a volume of verification executions consistent with the website’s overall volume of visits.

The law does not specify a particular technical de-identification standard, deletion deadline measured in seconds or minutes, independent audit requirement, encryption standard, breach-notification rule, or method for proving that personal data were deleted.

### Liability and enforcement

The statute creates several forms of potential liability:

- A covered publisher that fails to perform the required age check may be liable for damages resulting from a minor accessing covered material, including court costs and attorney fees.
- A website owner, commercial entity, or verification provider that knowingly retains personally identifying information after access may be liable to the affected user for resulting damages, court costs, and attorney fees.
- A violation of the age-verification or data-handling subsections is classified as a Class C felony.
- The Tennessee Attorney General may bring an appropriate action or proceeding against a noncompliant commercial entity.

These provisions regulate publishers, website owners, commercial entities, and verification providers. This entry does not find language making an ordinary adult viewer a felon merely for visiting a website or attempting to avoid an age gate.

### Exemptions and limitations

The statute does not apply to a bona fide news or public-interest broadcast, website video, report, or event, and it states that it does not affect the rights of news-gathering organizations.

Internet service providers, search engines, and cloud providers are not liable solely for providing access, transmission, intermediate storage, or related services for content outside their control when they are not responsible for creating that content.

## What officials say

Tennessee officials describe the law as a child-protection measure intended to keep minors from accessing online material that is legally available to adults but considered harmful to children.

Attorney General Jonathan Skrmetti has characterized age verification as a common-sense way to keep adult websites adults-only and has argued that the law protects both minors and adult privacy. The legislature’s unanimous final votes indicate broad political support for the original enactment.

Those statements describe the government’s objective and legal position. They do not independently establish how effective the law is at preventing access by minors, how consistently companies implement it, or how much personal information moves through particular verification systems.

## What advocates and critics say

The Free Speech Coalition and several co-plaintiffs—including adult-content businesses, a sexual-wellness retailer, an educator, and a sex-education platform—argue that the law burdens adults’ access to lawful speech and creates privacy and security risks by requiring age or identity verification before access.

Critics also argue that:

- some users may avoid lawful content rather than disclose identity-linked information;
- websites may block Tennessee users entirely rather than accept criminal and civil exposure;
- VPNs and alternative platforms may make the requirement less effective for technologically capable minors;
- people without a suitable state ID, conventional credit history, mortgage, employment, or education records may face exclusion or extra friction;
- facial matching and identity-data systems may produce errors or unequal outcomes;
- a breach could reveal both identity information and a user’s interest in sensitive content; and
- repeated verification can expose more data than a privacy-preserving proof that a user is over eighteen.

The Supreme Court held in *Paxton* that Texas may require age verification for certain sexually explicit websites and applied intermediate scrutiny because the burden on adult speech was incidental to the state’s power to shield minors from sexual material. The dissent and civil-liberties advocates warned that privacy concerns and verification friction may chill adults’ lawful access.

*Paxton* is important precedent, but Tennessee’s statutory text, its seven-year evidence requirement, its felony provision, and the 2025 deletion of its section-specific content definition are not identical to the Texas law. The Tennessee case therefore requires its own legal analysis.

## What is confirmed?

- Public Chapter 1021 was signed on May 28, 2024, and took effect on January 1, 2025.
- The final bill passed the Tennessee Senate 31-0 and House 96-0.
- Covered websites must verify users before access and again after the lesser of the current session or sixty minutes.
- A covered website is one with at least thirty-three and one-third percent of its available data within the statute’s covered-content category.
- The statute permits either a photo-to-state-ID comparison or a commercially reasonable transactional-data method.
- Government ID and facial matching are therefore permitted but are not the only authorized method.
- Verification executors must retain at least seven years of anonymized verification evidence.
- They must not retain personally identifying information after access has been granted.
- The statute creates private civil remedies, attorney-general enforcement authority, and Class C felony exposure for violations of the age-verification or data-handling subsections.
- Public Chapter 405, effective May 8, 2025, deleted the statute’s section-specific definition of “content harmful to minors.”
- A district court initially granted a preliminary injunction, but the Sixth Circuit stayed it on January 13, 2025, allowing the law to take effect.
- The Supreme Court upheld Texas’s age-verification law in *Free Speech Coalition v. Paxton* on June 27, 2025.
- The Tennessee plaintiffs’ current public tracker lists their case as in progress and the Tennessee law as in effect.

## What remains uncertain?

As of the last review date, the following questions remained unresolved or were not established by publicly available records reviewed for this entry:

- Which current definition and interpretive rules govern “content harmful to minors” after Public Chapter 405 deleted the section-specific definition
- Which websites the Attorney General currently considers covered
- Whether Tennessee has published formal enforcement guidance, safe harbors, technical standards, or compliance examples
- Whether the state has opened investigations, brought enforcement actions, referred criminal cases, or received complaints under the law
- How a website reliably determines that a user is accessing it from Tennessee
- Which companies and subcontractors process identity, selfie, device, network, or transactional data during each verification route
- Whether personal data are processed locally, transmitted to a vendor, or compared against external databases
- How quickly personally identifying information is deleted after access is granted
- Whether backups, logs, fraud records, telemetry, support tickets, or security records contain information that could identify a user
- What de-identification method is used for the seven-year historical evidence
- Whether retained volume records can be linked to specific visits, devices, networks, accounts, or content categories
- What independent testing or audits verify deletion, accuracy, security, accessibility, and bias
- How users without conventional identification or transactional histories can obtain access
- How minors, adults, and verification errors are handled when an automated system reaches the wrong result
- Whether photo matching creates or retains biometric templates under a particular implementation
- What breach-notification, incident-response, vendor-risk, and insurance requirements apply
- How often users are actually required to repeat verification under real-world session designs
- Whether websites are choosing to block Tennessee traffic instead of implementing verification
- How *Paxton* and the 2025 statutory amendment will ultimately affect the Tennessee lawsuit

The statute’s prohibition on retaining personal information is a meaningful privacy safeguard. Its practical strength depends on system design, data minimization, deletion verification, vendor practices, and enforcement evidence that are not fully visible from the statutory text alone.

## Who may be affected?

People and organizations potentially affected include:

- adults in Tennessee seeking lawful access to covered online material;
- minors whom the law is intended to prevent from accessing that material;
- website owners, publishers, creators, and distributors;
- sexual-health, sexual-wellness, education, artistic, and expressive websites that may be uncertain about coverage;
- age-verification, identity, biometric, and data-broker vendors;
- people who lack state identification or conventional transactional histories;
- people whose appearance differs from an identification photograph;
- people with disabilities who encounter inaccessible camera, document, or verification workflows;
- privacy-conscious users who may avoid lawful content rather than disclose personal data; and
- people whose identity or verification information could be exposed through error, misuse, or a security incident.

A successful age check establishes or estimates that a user is an adult. It should not be treated as proof of the user’s identity, interests, intentions, or conduct beyond what the particular system actually verifies.

## Privacy and civil-liberties significance

Age verification creates a genuine policy conflict:

1. Tennessee has a legitimate interest in restricting minors’ access to sexual material.
2. Adults have lawful speech, privacy, security, and anonymity interests when accessing sensitive content.

The central privacy question is not merely whether a website promises to delete an uploaded ID. It is whether the complete verification system can prove adulthood while minimizing collection, disclosure, linkage, retention, and misuse across the website, verification vendor, databases, logs, and devices involved.

The statute contains a notable tension. It prohibits retention of personally identifying information after access while requiring at least seven years of anonymized evidence demonstrating the architecture and volume of age checks. Those two obligations can coexist, but only if the retained evidence is genuinely separated from identities, visits, devices, and content interests.

The most defensible current conclusion is:

> Tennessee’s Protect Tennessee Minors Act requires meaningful age verification and contains an express ban on retaining personal identifying information after access. It does not require every user to upload an ID, but it permits identity- and transactional-data-based methods. Because the law leaves key technical standards unspecified and its content definition changed during ongoing litigation, its privacy, accessibility, coverage, and enforcement effects cannot be judged from the statute alone.

Privacy-preserving age assurance is technically possible in principle—for example, through systems that disclose only an over-eighteen result rather than an identity or document—but the Tennessee statute does not require a particular privacy-preserving architecture.

## Lawful actions and resources

- Read Public Chapters 1021 and 405 and the current statutory history rather than relying on descriptions of the original bill alone.
- Monitor *Free Speech Coalition, Inc. v. Skrmetti* for Tennessee-specific rulings following the Supreme Court’s *Paxton* decision.
- Ask the Tennessee Attorney General to publish nonconfidential enforcement guidance, coverage criteria, complaint totals, enforcement statistics, and data-security expectations.
- Ask covered websites and verification vendors to publish clear data-flow diagrams, processor lists, deletion timelines, retention categories, accessibility information, error-appeal procedures, security certifications, and breach-notification commitments.
- Prefer age-assurance designs that return only the minimum necessary fact—such as “over eighteen”—without disclosing a name, identification number, document image, exact birth date, or browsing history to the website.
- Do not submit, collect, or publish copies of users’ identification, selfies, verification records, or sensitive browsing histories through this tracker.
- Submit newly issued court decisions, statutory amendments, official guidance, or independently verified technical documentation through the repository’s source-update process.
- For questions about compliance, criminal exposure, constitutional rights, privacy claims, or an individual dispute, consult a qualified attorney.

## Sources

### Tennessee law and legislative history

1. [Tennessee General Assembly — SB 1792 / HB 1614, Public Chapter 1021](https://wapp.capitol.tn.gov/apps/BillInfo/Default?BillNumber=SB1792&GA=113)
2. [Tennessee Code § 39-17-912 — 2024 enacted text](https://law.justia.com/codes/tennessee/title-39/chapter-17/part-9/section-39-17-912/)
3. [Tennessee General Assembly — SB 448 / HB 761, Public Chapter 405](https://wapp.capitol.tn.gov/apps/BillInfo/Default?BillNumber=SB0448&ga=114)
4. [Tennessee Code § 39-17-901 — general Part 9 definitions](https://law.justia.com/codes/tennessee/title-39/chapter-17/part-9/section-39-17-901/)
5. [Current statutory history for Tennessee Code § 39-17-912](https://content.next.westlaw.com/Document/N9662E94039D411F09D01E2242D77FF7E/View/FullText.html)

### Court records and legal status

6. [Federal district-court order discussing the preliminary injunction and stay](https://docs.justia.com/cases/federal/district-courts/tennessee/tnwdce/2%3A2024cv02933/104414/55)
7. [Sixth Circuit docket — Free Speech Coalition, Inc. v. Skrmetti](https://dockets.justia.com/docket/circuit-courts/ca6/24-6158)
8. [United States Supreme Court — Free Speech Coalition, Inc. v. Paxton, 606 U.S. 461](https://www.supremecourt.gov/opinions/slipopinion/24)
9. [Free Speech Coalition lawsuit tracker — Tennessee case](https://action.freespeechcoalition.com/age-verification-resources/av-lawsuits/)

### Reporting and technical context

10. [Associated Press — district-court ruling and competing arguments](https://apnews.com/article/2fdc2563836315c6d4e8eb4d57ab9913)
11. [Adequately Tailoring Age Verification Regulations — technical and policy research](https://arxiv.org/abs/2601.20241)

## Revision history

- **2026-07-18:** Initial publication. Verified enactment and current statutory history, incorporated the 2025 definition amendment, documented the law’s verification and data-handling requirements, reviewed the federal litigation and *Paxton* decision, and recorded unresolved privacy, accessibility, coverage, and enforcement questions.
