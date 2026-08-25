# Research Note — Tennessee voter-roll transfer to DOJ

This is an unpublished working evidence record supporting the possible Special Case **Federal Election Administration and Tennessee's 2026 Election**. It is not a public Tracker entry and is not publication-ready by itself.

This note addresses one narrow research pass: **what Tennessee sent the U.S. Department of Justice, what agreement governed the transfer, what safeguards can be established, and whether the Tennessee data can be shown to have moved into another federal system.**

## Research question

> What can public records and direct statements establish about Tennessee's 2025–2026 transfer of statewide voter-registration data to DOJ, including the fact of transfer, data fields, agreement or MOU status, privacy/security safeguards, and any onward sharing with DHS/SAVE or another federal entity?

## Bottom-line findings

| Question | Finding | Evidence status |
|---|---|---|
| Did Tennessee actually send voter-roll data to DOJ? | **Yes.** Tennessee Secretary of State Tre Hargett directly confirmed in an Aug. 5, 2026 PBS NewsHour interview that Tennessee gave DOJ the requested voter information after relying on advice of counsel. Tennessee Elections Coordinator Mark Goins separately told Stateline that Tennessee had shared its voter data. | **Verified** |
| Did Tennessee sign DOJ's proposed MOU? | **No, based on the strongest public evidence located.** Goins told Stateline Tennessee declined to sign because of concern the MOU conflicted with NVRA voter-removal rules. | **Verified from direct on-record state-official statement reported by Stateline** |
| What data fields were sent? | Names, dates of birth, addresses, and last four digits of Social Security numbers are consistently reported as included. Driver's-license/DMV identifiers are also strongly supported, including by the PBS interview framing and neutral national summaries, but the exact Tennessee transmission manifest has not been located. | **High confidence; exact field manifest still missing** |
| Was a full Social Security number sent? | No evidence located. Sources describe **last four digits**, not full SSNs. | **No support for full SSN claim** |
| Was voting history sent? | One secondary Tennessee report says voting history was not included, but no primary file manifest or Tennessee response record located in this pass confirms that exclusion. | **Unresolved** |
| What Tennessee-specific contract governed retention/use? | No signed Tennessee DOJ MOU was located, and Goins says Tennessee declined the proposed MOU. No separate executed Tennessee-specific data-use, retention, security, deletion, or contractor-access agreement was located. | **No signed MOU established; other TN-specific terms unresolved** |
| What safeguards does DOJ say apply generally? | DOJ's May 12 OLC opinion says the Civil Rights Division intends to retain state lists in its Central Civil Rights Division Index File, says the records are covered by an existing Privacy Act SORN, and describes a DOJ-controlled SAVE account in which DOJ uploads files and a DHS employee accesses individual records without downloading the lists to a DHS-controlled server. The opinion also describes Privacy Act procedures for certain law-enforcement disclosures. | **Verified as DOJ representations/legal position, not an independent audit and not TN-specific contractual terms** |
| Did DOJ send Tennessee's particular file to DHS/SAVE? | **Not established.** DOJ has publicly described and defended a general plan to run collected voter-roll data against DHS's SAVE system, but no source located in this pass identifies Tennessee's file as one actually processed through that DOJ-to-SAVE pathway. | **Unresolved** |
| Is Tennessee using SAVE separately? | **Yes, at least in some voter-list citizenship-verification workflow.** Hargett said Tennessee has worked with the federal government through SAVE and that last-four SSN information was used as part of that work. The exact system path, timing, portal, users, queries, and relationship to the DOJ-transferred copy remain unresolved. | **Partially verified operational use; architecture unresolved** |

## Finding 1 — Completed transfer is now verified

The master dossier previously classified the completed Tennessee-to-DOJ transfer as only partially verified because DOJ's Dec. 18, 2025 press release established Tennessee's **intent** to provide its full registration list but did not itself prove completed transmission.

That can now be upgraded.

On Aug. 5, 2026, PBS NewsHour interviewer Amna Nawaz asked Secretary of State Tre Hargett about Tennessee having turned over its voter information. Hargett responded that Tennessee consulted counsel, counsel believed DOJ had a right to the information, and **"When my lawyers say, you need to give it to them, we did."**

This is a direct statement by Tennessee's secretary of state confirming completed transfer.

Stateline separately reported on March 13, 2026 that Elections Coordinator Mark Goins said in an interview that Tennessee **had shared its voter data** after concluding DOJ was legally entitled to it.

### Recommended master-dossier change

- `CLM-02` — **Partially verified → Verified.**
- `EVT-009` — completed transfer should be treated as **Verified**, while exact date/fields/terms remain separately qualified.

## Finding 2 — Data fields: what is established and what is not

### Strongly supported as transmitted

The public evidence supports the following fields in Tennessee's DOJ transfer:

- voter name;
- date of birth;
- address;
- last four digits of Social Security number.

WPLN reported on Apr. 22, 2026 that Tennessee provided DOJ voter records containing names, dates of birth, addresses, and last four SSN digits. The Tennessean was cited by federal-court filings and other reporting for the same transfer.

The PBS interview strengthens the evidence concerning sensitive identifiers. Nawaz described the transferred information to Hargett as including **last four digits of Social Security numbers and driver's-license numbers**. Hargett did not dispute that characterization and immediately discussed Tennessee's use of last-four SSN information in federal SAVE work.

Neutral NCSL reporting says DOJ's voter-list demands request names, dates of birth, last-four SSN digits, and DMV ID numbers, and lists Tennessee among states alleged to have provided the entire statewide list including sensitive PII. The Brennan Center's Aug. 24 tracker likewise lists Tennessee among states that provided or committed to provide complete lists including driver's-license and Social Security-number information.

### Driver's-license / DMV identifier

The evidence is strong but not as clean as for names/DOB/address/last-four SSN because this pass still did not locate Tennessee's actual file specification or transmission manifest.

**Current treatment:** include driver's-license/DMV identifier as **strongly supported / partially verified**, not as a field independently proven from a Tennessee transmission record.

### Not established

- **Full Social Security numbers:** no source located says Tennessee transmitted complete SSNs. Do not use "SSNs" without specifying that the evidence concerns the **last four digits**.
- **Voting history:** one secondary Tennessee report says voting history was excluded, but this is not yet supported by a primary manifest/response record. Keep unresolved.
- **Party affiliation, email, phone, signature images, naturalization number, citizenship date, place of birth, race, gender, or other Tennessee registration fields:** no evidence located in this pass establishing that those fields were in the DOJ file.

Tennessee's own voter-registration site states that voter-registration records are public **excluding** the Social Security number, driver's-license number, and Department of Safety and Homeland Security ID number. This helps establish that the sensitive identifiers at issue are not part of the ordinary public-facing voter record.

## Finding 3 — Tennessee did not sign DOJ's proposed MOU

This is an important correction to the vague earlier idea that Tennessee may have transferred the file under a federal data-use agreement.

Stateline reported on March 13, 2026 that Tennessee Elections Coordinator Mark Goins said Tennessee **decided against signing** DOJ's proposed memorandum of understanding. Goins said the state was concerned the MOU conflicted with the National Voter Registration Act's rules governing removal of voters.

Goins specifically raised false-positive risk, noting Tennessee has roughly four million registered voters and saying a "false flag" should not lead to an improper removal.

The proposed DOJ MOU used with other states called for DOJ to test/analyze the state file, notify the state of list-maintenance concerns, and for the state to remove ineligible voters and resubmit its list within a specified period (reported as 45 days). Tennessee's refusal means those proposed contractual obligations should **not** be described as Tennessee's governing agreement.

Brennan Center's Aug. 24 tracker independently states that Mississippi, South Dakota, and Tennessee refused to sign the agreement when providing voter rolls.

A Jan. 30, 2026 federal-court filing by CREW similarly described Tennessee as having provided its full voter rolls without executing an MOU. That filing is a party submission rather than an adjudicated factual finding, so it is corroboration rather than the primary basis for the conclusion.

### What this does and does not mean

**Established:** no signed Tennessee version of the proposed DOJ voter-roll MOU has been identified, and Tennessee's election coordinator directly said the state declined it.

**Not established:** that there was no other correspondence, privacy letter, transmission instruction, informal understanding, federal statutory condition, or separate security protocol governing the transfer.

CREW's released DOJ emails show that in September 2025 a DOJ official instructed staff to prepare a Utah "privacy letter" using a letter to Tennessee as the model. This proves that a Tennessee privacy-related letter existed in DOJ's correspondence, but this pass did not recover the Tennessee letter's full text. Its precise promises or safeguards therefore remain unknown.

## Finding 4 — Tennessee-specific safeguards remain unusually opaque

Because Tennessee declined the proposed MOU, safeguards from MOUs signed by Alaska, Texas, or other states cannot simply be imported into Tennessee's case.

No public Tennessee-specific record was located in this pass establishing all of the following:

- encryption or file-transfer channel used for the Tennessee upload;
- named authorized DOJ users;
- contractor identity or contractor access to Tennessee data;
- retention duration for the Tennessee copy;
- deletion/destruction requirements;
- logging and audit frequency;
- breach-notification procedure;
- prohibition on secondary use;
- prohibition on immigration-enforcement use;
- correction process for erroneous matches;
- Tennessee notification before DOJ/DHS acts on a match;
- onward-sharing limits specific to Tennessee.

That is a **negative finding about the public record located**, not proof that no such controls exist internally.

A pending public-record request on MuckRock, filed Feb. 18, 2026 with the Tennessee Secretary of State, specifically seeks executed/draft/rejected agreements and DOJ correspondence. Its currently indexed page shows the request as **Processing** with **0 files**, so it supplies no responsive records yet.

## Finding 5 — General DOJ safeguards and operational representations

The strongest official description found of how DOJ says the collected state files are handled is the May 12, 2026 Office of Legal Counsel opinion, **Authority to Obtain and Share Statewide Voter Roll Data**.

These are DOJ's own factual representations and legal conclusions. They should not be presented as an independent audit of security or proof that every representation was implemented exactly as described.

### Storage / system of records

OLC says the Civil Rights Division represented that it intends to retain the voter lists in the **Central Civil Rights Division Index File and Associated Records**. OLC says an existing Privacy Act System of Records Notice covers the relevant records and categories of individuals.

### SAVE access model described to OLC

OLC records the Division's representation that:

- DOJ accesses a SAVE account that DOJ controls;
- DOJ uploads the voter files;
- a DHS employee accesses individual records;
- no one at DHS downloads the state lists to a DHS-controlled server/directory;
- OLC characterizes the described DHS access as read-only for Privacy Act SORN analysis.

This is a much more concrete architecture than we had in the first dossier pass.

### Separate disclosure to HSI / DHS

OLC also analyzes a more direct form of disclosure from DOJ to HSI or another DHS component. It says the Privacy Act ordinarily restricts disclosure but identifies law-enforcement and routine-use exceptions that DOJ believes can permit sharing.

For the law-enforcement exception, the opinion says the agency seeking records must make a written request specifying the particular portion desired and the law-enforcement activity for which it is sought.

Crucially, OLC states that as of May 12 it **had not been provided a copy of any relevant HSI or other DHS request**. That means the opinion establishes a legally proposed pathway, not proof that a qualifying direct HSI request had already occurred.

### Immigration-enforcement purpose

OLC also records DOJ senior-leadership representations that, when the voter-list requests were made, DOJ did not intend to use the lists for immigration enforcement. The opinion simultaneously acknowledges that the proposed cross-checking could produce incidental immigration consequences.

For Tracker purposes, both facts must be preserved.

## Finding 6 — DOJ publicly confirmed a general SAVE plan

At a March 26, 2026 federal hearing in DOJ's Rhode Island voter-roll litigation, DOJ attorney Eric Neff told the court that DOJ's plan was to run the voter data against DHS's **SAVE** database.

The official hearing transcript records Neff explaining that SAVE retrieves information from other federal databases to cross-check records for possible noncitizen or deceased-person issues. He also described a follow-up confirmation process for flagged records.

Stateline reported the following day that Neff confirmed DOJ was sharing sensitive voter data with DHS and said DOJ and DHS had a use agreement for the process.

This substantially strengthens the general connection:

**DOJ collection of state voter files → DOJ/DHS SAVE cross-checking is a documented federal architecture, not merely speculation.**

It still does **not** answer the Tennessee-specific question.

## Finding 7 — Tennessee's file specifically going into DOJ/DHS SAVE is NOT established

This remains the most important unresolved link.

No public source located in this pass says any of the following:

- "DOJ uploaded Tennessee's voter file to SAVE";
- "DHS/HSI accessed Tennessee's file through DOJ's SAVE account";
- a named Tennessee file/date/batch was processed through the federal DOJ-DHS workflow;
- Tennessee received a DOJ/SAVE match-result file derived from the copy sent to DOJ.

So the evidence supports:

1. Tennessee gave its voter data to DOJ.
2. DOJ has a documented general plan/architecture to run collected state voter data against SAVE with DHS involvement.
3. Tennessee independently confirms working with the federal government through SAVE for voter citizenship verification.

But it does **not yet support collapsing those three propositions into a single proven data path**.

### Correct diagram today

```text
Tennessee voter file ───────────────▶ DOJ
                                      │
                                      │ DOJ's general, documented architecture
                                      ▼
                                  SAVE / DHS

Tennessee election administration ──▶ SAVE / federal government
       (Hargett confirms this relationship)

UNKNOWN: whether DOJ's Tennessee copy is the file/batch that traveled through the first SAVE path.
```

## Finding 8 — Tennessee SAVE use can now be partially verified

The initial master dossier classified Tennessee operational use of SAVE as unresolved.

Hargett's Aug. 5 PBS interview changes that. He said Tennessee **has worked together with the federal government through the SAVE system** to ensure citizens on Tennessee voter rolls and specifically said the last four digits of SSNs were used as part of that work.

This directly supports actual Tennessee participation in a SAVE-based voter-list process.

What it **does not** establish:

- whether the workflow is the electronic portal authorized by Public Chapter 775;
- when that workflow began;
- whether it is currently continuous, periodic, batch, or person-by-person;
- which Tennessee personnel have credentials;
- whether DOJ, USCIS, HSI, or another federal component is the immediate counterpart;
- exact query fields beyond Hargett's statement about last-four SSN;
- audit logs, match thresholds, false-positive handling, notice, cure, or removal procedures;
- whether Tennessee's DOJ-transferred file is involved at all.

### Recommended master-dossier change

- `CLM-05` — **Unresolved → Partially verified.** Tennessee operational SAVE work is directly acknowledged; the Public Chapter 775 portal and exact workflow remain unresolved.

## Updated claim recommendations for master dossier

| Master claim | Current status | Recommended treatment |
|---|---|---|
| CLM-02 Tennessee transmitted its voter-registration data to DOJ | Partially verified | **Upgrade to Verified** based on Hargett and Goins direct statements. |
| CLM-03 exact sensitive fields | Partially verified | Keep **Partially verified / High confidence** pending actual file manifest; names/DOB/address/last-four SSN are very strongly supported; DMV/driver ID strongly supported but exact manifest absent. |
| CLM-05 Tennessee operational SAVE use | Unresolved | **Upgrade to Partially verified**; Hargett confirms Tennessee/federal SAVE work and last-four SSN use, but portal/workflow details remain unknown. |
| CLM-07 Tennessee DOJ data was actually shared onward | Unresolved | **Remain Unresolved.** General DOJ→SAVE/DHS architecture is documented, but TN-specific batch/file movement is not. |
| New claim: Tennessee signed DOJ voter-roll MOU | — | Add as **Contradicted** if posed affirmatively; evidence says Tennessee declined the MOU. |
| New claim: Tennessee transferred data without signing DOJ's proposed MOU | — | Add as **Verified / High confidence** based on Goins's on-record statement plus corroboration. |

## Source register

| ID | Source | Type | Key proposition | URL |
|---|---|---|---|---|
| RTR-001 | U.S. DOJ, Justice Department Sues Four States for Failure to Produce Voter Rolls, Dec. 18, 2025 | Official DOJ release | Tennessee announced intent to voluntarily provide full registration list. | https://www.justice.gov/opa/pr/justice-department-sues-four-states-failure-produce-voter-rolls |
| RTR-002 | PBS NewsHour interview with Tennessee Secretary of State Tre Hargett, Aug. 5, 2026 | Direct state-official interview / transcript | Hargett confirms completed transfer; discusses sensitive fields; confirms Tennessee-federal SAVE work and last-four SSN use. | https://www.pbs.org/video/election-security-1785955610/ |
| RTR-003 | WPLN, Tennessee handed over voter data, Apr. 22, 2026 | Reputable Tennessee reporting | Names, DOB, addresses, last-four SSN reported in transfer. | https://wpln.org/post/tennessee-handed-over-voter-data-now-the-doj-faces-a-lawsuit-over-its-stockpile/ |
| RTR-004 | Stateline, In bid for voter data..., Mar. 13, 2026 | Reputable state-policy reporting / direct Goins interview | Goins confirms transfer; Tennessee declined proposed MOU due NVRA/false-positive concerns. | https://stateline.org/2026/03/13/in-bid-for-voter-data-trumps-doj-lays-groundwork-to-question-midterm-results/ |
| RTR-005 | Stateline, DOJ offers states confidential deal..., Dec. 18, 2025 | Reputable state-policy reporting | Proposed MOU terms: DOJ test/analyze/assess, state cleanup and resubmission. | https://stateline.org/2025/12/18/trumps-doj-offers-states-confidential-deal-to-wipe-voters-flagged-by-feds-as-ineligible/ |
| RTR-006 | DOJ OLC, Authority to Obtain and Share Statewide Voter Roll Data, May 12, 2026 | Official DOJ legal opinion | General storage, SORN, DOJ-controlled SAVE account, DHS access model, and asserted disclosure authority. | https://www.justice.gov/olc/media/1440346/dl |
| RTR-007 | Mar. 26, 2026 Rhode Island federal hearing transcript | Official court transcript | DOJ attorney states plan is to run collected voter data against DHS SAVE; describes SAVE verification process. | https://www.brennancenter.org/media/15517/download/ri-hearing-transcript-2026-03-26.pdf?inline=1 |
| RTR-008 | Stateline, DOJ confirms voter data sharing with Homeland Security, Mar. 27, 2026 | Reputable state-policy reporting | Reports DOJ confirmation of DHS/SAVE sharing architecture and use agreement. | https://stateline.org/2026/03/27/doj-confirms-voter-data-sharing-with-homeland-security-but-denies-building-national-list/ |
| RTR-009 | NCSL, Federal Requests for Statewide Voter Lists, updated Aug. 21, 2026 | Neutral legislative-policy summary | Requested fields include name, DOB, last-four SSN, DMV ID; Tennessee listed among states providing/allegedly providing full list with PII. | https://www.ncsl.org/elections-and-campaigns/federal-requests-for-statewide-voter-lists |
| RTR-010 | Brennan Center DOJ voter-information tracker, updated Aug. 24, 2026 | Civil-rights research/advocacy tracker | Tennessee listed among full-file providers; says Tennessee refused DOJ MOU; summarizes DOJ SAVE plan. | https://www.brennancenter.org/our-work/research-reports/tracker-justice-department-requests-voter-information |
| RTR-011 | Tennessee Online Voter Registration System | Official Tennessee election system | Public voter records exclude SSN, driver's-license number, and TN Department of Safety/Homeland Security ID number. | https://ovr.govote.tn.gov/Registration/RegistrationDetails |
| RTR-012 | MuckRock, Records Related to DOJ Voter Data Requests — Tennessee Secretary of State | Public-record-request tracker | Feb. 18 request seeks TN/DOJ agreements/correspondence; indexed status Processing with 0 files. | https://www.muckrock.com/foi/tennessee-155/records-related-to-doj-voter-data-requests-tennessee-secretary-of-state-205370/ |
| RTR-013 | CREW DOJ production, released Apr. 2026 | FOIA production / discovery lead | DOJ internal email says a Utah privacy letter should use the letter to Tennessee as a model; exact Tennessee letter remains to be extracted. | https://www.citizensforethics.org/wp-content/uploads/2026/04/2026.03.31-Combined-OCR_Part2.pdf |
| RTR-014 | CREW v. DOJ filing, Jan. 30, 2026 | Federal-court party filing | Corroborates that Tennessee provided voter rolls without an executed MOU; not an adjudicated finding. | https://www.citizensforethics.org/wp-content/uploads/2026/02/gov.uscourts.dcd_.287887.8.1_Redacted.pdf |

## Negative findings / records still missing

The following were **not located** in this pass:

1. Tennessee's actual transmitted file or safe field manifest describing every column.
2. Exact date/time and transmission method for the Tennessee file.
3. Tennessee's initial DOJ demand letter in a clean primary copy.
4. Tennessee's complete response/transmittal letter and receipt acknowledgment.
5. Full text of the Tennessee-specific DOJ "privacy letter" later used as a model for Utah.
6. Any executed Tennessee-specific data-use/security/retention agreement other than the proposed MOU Tennessee declined.
7. Any record naming a DOJ contractor with access to Tennessee data.
8. Any Tennessee-specific record showing DOJ uploaded Tennessee's file to SAVE.
9. Any Tennessee-specific DHS/HSI request for the file or a portion of it.
10. Any return match/results file sent from DOJ/DHS to Tennessee based on the DOJ copy.

Failure to locate these records does not establish that they do not exist.

## Next highest-value searches

1. Extract the **Tennessee privacy letter** from the CREW DOJ production and identify concrete security/Privacy Act promises.
2. Locate the Tennessee **transmittal/response correspondence**, ideally through an existing public-record release, court exhibit, archived SOS material, or the pending MuckRock request.
3. Search federal litigation exhibits/FOIA productions for a **state-by-state processing log, SAVE batch name, upload log, or match-results record** that names Tennessee.
4. Determine whether any DOJ/DHS **use agreement or MOU governing SAVE** is public and whether it describes state-file identifiers, retention, audit logs, or access controls.
5. In the separate SAVE implementation pass, map Hargett's confirmed Tennessee SAVE use to Public Chapter 775: who has accounts, what interface those accounts touch, what is queried, and what audit/correction rules apply.

## Research conclusion for this pass

The public evidence now establishes more than the initial dossier did:

- Tennessee **did** transmit statewide voter data to DOJ.
- Tennessee did so after state officials concluded DOJ was legally entitled to it, not because Tennessee had signed DOJ's proposed voter-maintenance MOU.
- Tennessee **declined that MOU**, specifically citing NVRA/false-positive concerns.
- The transferred data very strongly includes name, date of birth, address, and last-four SSN; driver's-license/DMV identifiers are strongly supported but should remain qualified until the actual field manifest is located.
- DOJ has publicly documented an architecture in which collected state voter files can be processed through a DOJ-controlled SAVE account with DHS personnel participating, and DOJ has defended additional DHS/HSI sharing pathways under the Privacy Act.
- Tennessee's secretary of state separately confirms that Tennessee itself has worked with the federal government through SAVE for voter citizenship verification using last-four SSN information.
- **No public evidence located in this pass proves that the particular Tennessee file sent to DOJ was actually the file uploaded into DOJ's SAVE workflow or directly transferred to DHS/HSI.** That distinction must remain explicit.

The next decisive document would be a Tennessee-specific transmittal/file manifest, DOJ processing record, SAVE upload/batch log, or HSI/DHS request identifying Tennessee data.