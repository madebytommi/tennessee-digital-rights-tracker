# Tracker Research Notes — Federal Election Administration and Tennessee's 2026 Election

This is an unpublished working evidence record for a possible Special Case. It is excluded from the public GitHub Pages site. Nothing in this file is publication-ready merely because it appears here.

AI-generated summaries, search-result snippets, and the original social-media lead are not evidence. Material claims must be reopened against the cited source and classified under the Tracker research protocol before publication.

Focused supporting notes:

- [`federal-election-administration-2026-doj-transfer.md`](federal-election-administration-2026-doj-transfer.md) — Tennessee voter-roll transfer to DOJ, fields, MOU status, safeguards, and federal onward-sharing architecture.
- [`federal-election-administration-2026-save.md`](federal-election-administration-2026-save.md) — Tennessee SAVE history, statewide list maintenance, 2025 bulk use, county portal, notice/appeal rules, and current litigation status.

## Investigation Metadata

| Field | Working value |
|---|---|
| Working title | Federal Election Administration and Tennessee's 2026 Election |
| Research status | Active research — Tennessee data-transfer and SAVE passes substantially complete |
| Date opened | 2026-08-24 |
| Last updated | 2026-08-24 |
| Researcher / agent | Tommi / ChatGPT-assisted research |
| Related GitHub issue | TBD |
| Related Tracker entry, if updating | None yet |
| Proposed Special Case ID | `federal-election-administration-2026` |
| Jurisdiction | Tennessee / Federal |
| Agencies / government bodies | Tennessee Coordinator of Elections / Secretary of State; county election commissions; Tennessee Department of Safety and Homeland Security; U.S. DOJ; DHS/USCIS; SSA; USPS; EAC; CISA; FBI; federal courts |
| Candidate Tracker category | `election-systems-data` |
| Candidate Tracker status | Monitoring |
| Candidate confidence | Medium, strengthening |

## Research Question

> How are federal changes involving voter-registration data, citizenship and eligibility verification, election-security institutions, voting-system oversight, federal enforcement, and mail-ballot administration interacting with Tennessee's administration of the 2026 federal election?

Secondary questions:

1. What Tennessee voter-registration data has been provided to the Department of Justice, when, under what authority, and with what fields or safeguards?
2. How does Tennessee actually use SAVE, which state/county actors are involved, what process follows a citizenship mismatch, and what parts of the system are operational versus still being built?
3. Has Tennessee voter data obtained by DOJ been shared with DHS, HSI, USCIS, SSA, a contractor, or another federal component for cross-checking?
4. Which provisions of Executive Order 14399 can currently affect Tennessee, and which are blocked, enjoined, pending, or not yet implemented?
5. Could current USPS ballot-mail rules change Tennessee absentee-ballot transmission or delivery, and what is their present legal status?
6. Do EAC, CISA, DOJ, DHS, or FBI institutional changes have a documented operational effect on Tennessee election administration, or are they context only?
7. Which relationships among these developments are documented, which are supported synthesis, and which remain merely possible or unestablished?

## Scope and Eligibility

| Question | Assessment |
|---|---|
| What is the Tennessee connection? | **Direct and now well established.** Tennessee gave its statewide voter-registration data to DOJ; Tennessee has long-standing statutory authority and documented operational use of SAVE for voter citizenship verification; Tennessee has also enacted a county-facing citizenship-verification portal that may incorporate SAVE through a secure web service. |
| What is the digital-rights relevance? | Voter databases, Social Security-number fragments, driver-license identifiers, identity/citizenship matching, federal-state data sharing, automated/database-assisted eligibility checks, notice/correction rules, election cybersecurity, voting-system oversight, and ballot-mail infrastructure. |
| Why does this belong in the Tracker? | The core questions concern government data architecture and technical election administration, not campaign strategy or political rhetoric by itself. |
| What remains out of scope? | National political events that lack a documented or conditional Tennessee technical/data connection should remain context only or be excluded. Mere chronology or partisan controversy is not sufficient. |

## Original Lead

| Field | Record |
|---|---|
| URL | Not preserved; screenshot supplied in research conversation |
| Title | Social-media graphic about Supreme Court action affecting Trump mail-voting restrictions |
| Publisher / source | Unknown from the screenshot alone |
| Publication date | 2026-08-24 |
| Retrieval date | 2026-08-24 |
| Archived URL | None |
| Relevant claim | The Supreme Court had removed a legal barrier to federal mail-voting restrictions. |
| Why the lead matters | Verification of the narrow claim led to a broader question about whether several federal election-administration developments connect to Tennessee data and election systems. |
| Reliability notes | Discovery lead only. The screenshot is not evidence for the Special Case. |

## Provisional Hypothesis

> Federal election-administration changes since 2025 form a multi-agency policy and data architecture involving voter-roll acquisition, citizenship/eligibility verification, federal enforcement, and mail-ballot rules. Tennessee has direct touchpoints through its DOJ voter-roll transfer, long-standing and enhanced SAVE use, and new state legislation authorizing a county citizenship-verification portal with potential SAVE integration. The exact downstream path of Tennessee's DOJ copy, current EO 14399/USPS legal effect, and Tennessee-specific operational effects of several federal institutional changes remain unresolved.

This is not a conclusion about partisan motive, election outcome, fraud, vote manipulation, or unlawful coordination. Evidence may confirm, narrow, contradict, or leave parts of the hypothesis unresolved.

## Claim Matrix

| ID | Atomic claim | Status | Best evidence currently in dossier | Source type | Notes |
|---|---|---|---|---|---|
| CLM-01 | On Dec. 18, 2025, Tennessee announced to DOJ its intent to voluntarily provide its full voter-registration list. | **Verified** | SRC-001 | DOJ official statement | Primary source establishes intent. |
| CLM-02 | Tennessee subsequently transmitted its voter-registration data to DOJ. | **Verified** | RTR-002; RTR-004 | Direct state-official interview + on-record Elections Coordinator statement | Hargett directly said Tennessee gave the information to DOJ; Goins separately confirmed sharing. Exact transmission date/file remains unresolved. |
| CLM-03 | The Tennessee file contained names, dates of birth, addresses, and last four SSN digits; driver-license/DMV identifiers were also included or requested. | **Partially verified / high confidence** | RTR-002; RTR-003; RTR-009 | Direct interview + reporting + neutral summary | Names/DOB/address/last-four SSN are very strongly supported. Driver/DMV ID is strongly supported but exact TN file manifest remains missing. No evidence of full SSNs. |
| CLM-04 | Tennessee declined DOJ's proposed voter-roll MOU. | **Verified** | RTR-004; RTR-010 | On-record state-official statement + corroboration | Goins cited NVRA/false-positive concerns. Do not import other states' MOU safeguards into Tennessee. |
| CLM-05 | Tennessee has actually used SAVE for voter citizenship verification, including a large-scale 2025 comparison. | **Verified** | SAV-001; SAV-009; SAV-010 | USCIS official correspondence + TN announcement + Hargett interview | TN was registered for voter SAVE use before 2025; in 2025 TN compared ~4 million records through enhanced SAVE; Hargett confirms federal SAVE work and last-four SSN use. |
| CLM-06 | The Public Chapter 473/775 county-facing citizenship portal is currently live and giving county administrators SAVE access. | **Not established; evidence indicates still in development** | SAV-004; SAV-005; SAV-006 | TN General Assembly + fiscal note | Fiscal note says portal is currently being created and must be implemented before Jan. 1, 2028. |
| CLM-07 | Under § 2-2-141, a registered voter flagged on citizenship grounds receives county notice and 30 days to provide proof, followed by purge if proof is not supplied and an appeal route to the State Election Commission when standard proof cannot be supplied. | **Verified** | SAV-002; SAV-003 | State code + official county guidance | Distinguish from new-applicant 10-day appeal under § 2-2-125. |
| CLM-08 | The 2025 enhanced SAVE system added natural-born citizen records, SSA/SSN access, and bulk search capabilities. | **Verified** | SAV-013 | Federal court opinion based on administrative record | This was the architecture used during Tennessee's 2025 large-scale comparison. |
| CLM-09 | The 2025 enhanced SAVE system was vacated June 22, 2026, and the district court denied a stay July 8. | **Verified** | SAV-013; SAV-014 | Federal court opinions | Vacatur restores prior regulatory status quo; appeal remains pending. |
| CLM-10 | Tennessee is included in the separate July 2026 order restoring enhanced SAVE bulk/SSN access to four states. | **Contradicted** | SAV-016; SAV-014 | Federal litigation records | Relief concerns Florida, Indiana, Iowa, Ohio; Tennessee is not included. |
| CLM-11 | DOJ has authority, according to a May 2026 OLC opinion, to share state voter lists with DHS for cross-checking against federal databases. | **Verified as DOJ legal position** | SRC-004 / RTR-006 | DOJ OLC opinion | This is DOJ's view, not proof Tennessee's file was shared onward. |
| CLM-12 | Tennessee voter data obtained by DOJ has actually been processed through DOJ's SAVE workflow or directly disclosed to DHS/HSI/USCIS/SSA or a contractor. | **Unresolved** | No TN-specific processing record located | — | General DOJ→SAVE/DHS architecture is documented; TN-specific batch/file movement is not. |
| CLM-13 | EO 14399 directs creation of State Citizenship Lists using federal citizenship/naturalization, SSA, SAVE, and other federal data. | **Verified** | SRC-003 | Executive order / Federal Register | Need provision-by-provision legal-status tracking. |
| CLM-14 | EO 14399 also creates a federal mail-ballot architecture involving USPS and voter/eligibility information. | **Verified at order-text level** | SRC-003 | Executive order / Federal Register | Operational implementation and current injunction status require separate verification. |
| CLM-15 | Current federal mail-ballot rules are presently changing how Tennessee absentee ballots are transmitted or delivered. | **Unresolved / conditional** | None sufficient yet | — | Must finish USPS rule/injunction/Tennessee compatibility pass. |
| CLM-16 | EAC leadership changes have directly changed Tennessee voting-system certification or 2026 voting-machine operation. | **Unresolved** | None sufficient yet | — | Do not infer from national institutional changes. |
| CLM-17 | CISA election-security reductions have directly reduced Tennessee election cybersecurity support. | **Partially informed but unresolved operationally** | RTR-002 (PBS Hargett CISA discussion) | Direct state-official interview | Hargett says TN worked with CISA in past but had no recent briefing; exact service reduction/effect still unknown. |
| CLM-18 | The federal developments documented here establish a plan to falsify, steal, or predetermine the 2026 election result. | **Unsupported** | None | — | Must not be presented as a Tracker conclusion without direct evidence. |
| CLM-19 | Statements by political officials about taking over, nationalizing, or changing elections caused the specific agency actions in this dossier. | **Unresolved / not established** | None sufficient for causation | — | Rhetoric may be context; causal linkage requires evidence. |

## Event Ledger

Evidence status here reflects what has actually been reopened for this dossier.

| ID | Date | Actor / institution | Atomic development | Tennessee nexus | Evidence status | Current treatment | Strongest source / next step |
|---|---|---|---|---|---|---|---|
| EVT-000 | 2009–2024 | USCIS / TN election authorities | SAVE had long been available to election authorities; USCIS identified Tennessee among ten states registered for voter registration/list maintenance before the 2025 overhaul. | **Direct** | **Verified** | Historical baseline | SAV-001. |
| EVT-001 | 2025-02 | CISA / DHS | Election-security personnel and/or programs were reduced or reassigned. | Context | Unverified in dossier | Discovery lead only | Reopen CISA/DHS primary material and AP/Reuters reporting; seek TN-specific support effects. |
| EVT-002 | 2025-02 | DOJ / FBI | Federal foreign-influence election work was reorganized or ended. | Context | Unverified in dossier | Discovery lead only | Reopen DOJ orders/statements and reporting. |
| EVT-003 | 2025-03-25 | President / federal agencies | EO 14248 attempted broad federal election-administration changes and drove a major SAVE overhaul. | Conditional / Direct through SAVE implementation | Partially verified; SAVE component verified | Background architecture | SAV-013 plus official EO during legal-status pass. |
| EVT-004 | 2025-04 to 2025-10 | Federal courts | Courts blocked portions of EO 14248. | Conditional | Unverified in dossier | Background lead | Collect opinions/orders. |
| EVT-005 | 2025-05-21 | Tennessee | Public Chapter 473 created a secure county-facing citizenship-verification portal to be implemented before Jan. 1, 2028 using Department of Safety records. | **Direct** | **Verified** | Core TN architecture | SAV-004. |
| EVT-006 | 2025-05 | DOJ Civil Rights Division | Voting Section priorities reportedly shifted toward election-integrity, citizenship, and fraud enforcement. | Context | Unverified in dossier | Discovery lead | Locate internal/official material plus independent reporting. |
| EVT-007 | 2025-07 onward | DOJ Civil Rights Division | DOJ sought statewide voter-registration lists from many states and litigated against noncompliant jurisdictions. | Context; later Direct for Tennessee | Verified generally | Active architecture context | SRC-001 and later DOJ records. |
| EVT-008 | 2025-08-18 | President | Public statements called for ending or sharply restricting mail voting and voting machines. | Context | Unverified in dossier | Rhetorical context only | Reopen transcript/reporting; no motive inference. |
| EVT-009 | 2025-10/11 | Tennessee / SAVE / FBI | Tennessee said it compared ~4 million voter records through enhanced SAVE and referred 42 people identified as potential non-U.S. citizens who voted to FBI. | **Direct** | **Verified for comparison/referral** | Core TN SAVE event; outcomes unresolved | SAV-009. |
| EVT-010 | 2025-12-18 | Tennessee / DOJ | Tennessee announced intent to voluntarily provide its full statewide voter-registration list to DOJ. | **Direct** | **Verified** | Core TN event | SRC-001. |
| EVT-011 | 2026-01-09 or earlier | Tennessee / DOJ | Tennessee completed transfer of voter-registration data to DOJ. | **Direct** | **Verified for transfer; fields partially verified** | Core TN event | RTR-002; RTR-004; field evidence RTR-003/RTR-009. |
| EVT-012 | 2026-01-28 | FBI / Fulton County, Georgia | FBI reportedly seized 2020 election materials in Fulton County. | Context | Unverified in dossier | Include only if necessary | Reopen warrant/affidavit and court records. |
| EVT-013 | 2026-02 | President | Public statements advocated federal or Republican 'take over' / 'nationalize' language for voting in certain places. | Context | Unverified in dossier | Rhetorical context only | Reopen transcript/reporting; no causal inference. |
| EVT-014 | 2026-03-10 | Tennessee General Assembly | HB1897, which would have required direct county SAVE checks for every applicant and quarterly entire-list checks, failed in House subcommittee. | **Direct** | **Verified** | Narrowing evidence | SAV-008. |
| EVT-015 | 2026-03-31 | President / DHS / SSA / DOJ / USPS | EO 14399 ordered State Citizenship Lists and additional federal election-administration measures. | Conditional | **Verified** | Core federal architecture | SRC-003. |
| EVT-016 | 2026-04-21 | Tennessee | Public Chapter 775 authorized the in-development county portal to incorporate SAVE through a secure web service if DHS/USCIS provides the data. | **Direct** | **Verified** | Core TN architecture; implementation not established | SAV-005; SAV-006. |
| EVT-017 | 2026-05-12 | DOJ OLC | OLC memorialized DOJ's view that federal law permits DOJ to obtain statewide voter lists and share them with DHS for voter-fraud cross-checking. | Context; potentially Direct if applied to TN file | **Verified as DOJ position** | Important architecture link | RTR-006. |
| EVT-018 | 2026-06-22 | D.D.C. | Court vacated the 2025 modified SAVE system and related SORNs, restoring prior regulatory status quo. | **Direct/Conditional** | **Verified** | Current TN capability boundary | SAV-013. |
| EVT-019 | 2026-07-07 | N.D. Fla. | Separate order restored enhanced SAVE bulk/SSN features to Florida, Indiana, Iowa, Ohio under settlement. | Context / narrowing | **Verified** | Tennessee not included | SAV-016. |
| EVT-020 | 2026-07-08 | D.D.C. | District court denied federal defendants' request to stay the SAVE vacatur pending appeal. | **Direct/Conditional** | **Verified** | Enhanced TN SAVE still not generally restored | SAV-014. |
| EVT-021 | 2026-07 | DOJ / DHS | Federal officials reportedly increased legal/enforcement pressure on state election officials and tied some funding to election requirements. | Conditional | Unverified in dossier | Potentially material if TN received/accepted conditions | Obtain letters/grant terms/TN grant records. |
| EVT-022 | 2026-07 | EAC / White House | EAC commissioners were removed/resigned amid reported disputes over election policy. | Context | Unverified in dossier | No TN operational effect established | Obtain EAC records and test TN impact. |
| EVT-023 | 2026-08-05 | Tennessee Secretary of State | Hargett directly confirmed TN's DOJ transfer and said TN has worked with federal government through SAVE using last-four SSN information. | **Direct** | **Verified** | Current state-official confirmation | RTR-002 / SAV-010. |
| EVT-024 | 2026-08 | USPS / federal courts | USPS finalized/prepared mail-ballot rules under EO 14399 while litigation continued. | Conditional | Unverified in master dossier | Next major pass | Obtain final rule and operative injunctions. |
| EVT-025 | 2026-08-24 | U.S. Supreme Court | Supreme Court removed one legal barrier in EO 14399 litigation without resolving all merits or the separate USPS injunction. | Conditional | Unverified in master dossier | Current-status trigger | Obtain Supreme Court order/opinion and map exact provisions. |

## Connection Matrix

| From | To | Proposed relationship | Current label | Evidence / limitation |
|---|---|---|---|---|
| Tennessee voter-registration list | DOJ | Tennessee supplied its statewide voter data to DOJ after initially announcing intent. | **Documented connection** | Hargett and Goins confirm completed transfer; exact file/date/manifest still missing. |
| DOJ state voter-roll collection | DOJ-controlled SAVE / DHS involvement | DOJ has documented a general architecture for processing collected voter data through SAVE/DHS. | **Documented general federal connection** | RTR-006 plus federal hearing evidence; TN-specific batch movement remains unestablished. |
| Tennessee DOJ copy | DOJ/DHS SAVE processing | Tennessee's specific DOJ file may have entered the general SAVE architecture. | **Possible relationship / not established** | No TN-named upload log, batch, or result file located. |
| Tennessee Coordinator of Elections | SAVE | State law authorizes statewide voter-database comparisons with SAVE; TN was registered before 2025 and actually used enhanced SAVE in 2025. | **Documented connection** | SAV-001; SAV-002; SAV-009; SAV-010. |
| SAVE result / citizenship evidence | TN registered-voter process | Evidence a registered voter may not be a citizen triggers county notice and state-law proof/appeal process rather than automatic SAVE removal. | **Documented connection** | SAV-002; SAV-003. |
| Public Chapter 473 portal | Department of Safety | County administrators will use secure portal for citizenship checks before processing applications. | **Documented connection** | SAV-004. |
| Public Chapter 775 | SAVE | Allows that in-development portal to integrate SAVE via secure web service if federally available. | **Documented conditional connection** | SAV-005; SAV-006. Portal is still being created. |
| 2025 enhanced SAVE | Tennessee 4m-record check | Tennessee used the enhanced system at statewide scale. | **Documented connection** | SAV-009; Hargett later confirms SAVE/last-four-SSN work. |
| June 22 SAVE vacatur | Tennessee current enhanced capabilities | Vacatur eliminated the 2025 modified system and restored prior status quo for ordinary users. | **Documented legal connection** | SAV-013; TN not within four-state exception SAV-016. |
| SAVE / SSA / federal citizenship records | EO 14399 State Citizenship Lists | EO 14399 directs federal citizenship lists to derive from specified federal data sources. | **Documented connection** | SRC-003. Current enforceability requires legal-status pass. |
| EO 14399 | USPS mail-ballot process | Order directs USPS-related election-mail measures. | **Documented order-text connection** | Final rule/current injunction status still needs verification. |
| EAC leadership changes | Tennessee voting systems | National EAC changes could matter to certification/standards. | **Possible relationship / not established** | Requires TN voting-system evidence. |
| CISA changes | Tennessee election cybersecurity | Hargett confirms past CISA interaction but not a recent briefing; exact operational effect of federal reductions is unestablished. | **Supported context; effect not established** | RTR-002. |
| Political statements | Agency actions | Temporal and policy similarity may be relevant context. | **Possible relationship / not established** | Statements do not prove causation, coordination, unlawful motive, or outcome intent. |

## Primary-Source Search

- [x] DOJ voter-roll announcement naming Tennessee
- [x] Direct Tennessee state-official confirmation of completed DOJ transfer
- [x] Evidence Tennessee declined proposed DOJ voter-roll MOU
- [ ] Exact Tennessee voter-file field/transmission manifest
- [ ] Tennessee-DOJ privacy/transmittal letter, receipt, or separate security agreement
- [x] Tennessee pre-2025 SAVE voter-use evidence
- [x] Tennessee statutory SAVE list-maintenance authority and voter notice/appeal process
- [x] Tennessee 2025 large-scale SAVE comparison evidence
- [x] Public Chapter 473 portal-creation record
- [x] Public Chapter 775 SAVE-integration authority
- [x] Fiscal-note evidence that county portal is still being created
- [ ] Tennessee's executed SAVE voter-verification MOA/CMA
- [ ] Current Tennessee SAVE credential/account/user-role list
- [ ] Portal vendor, implementation architecture, logging/audit rules, and launch milestone
- [x] Federal modified-SAVE architecture from administrative record
- [x] June 22 modified-SAVE vacatur and July 8 district-court stay denial
- [x] Four-state Florida enhanced-SAVE exception and confirmation Tennessee is not included
- [ ] Current D.C. Circuit status beyond latest Aug. 24 search / any later restoration for Tennessee
- [ ] Evidence whether TN voter data held by DOJ was processed through DOJ/DHS SAVE
- [ ] Final disposition of Tennessee's 42 SAVE/FBI referrals
- [ ] EO 14399 provision-by-provision court orders and current legal status
- [ ] USPS final rule and implementation guidance under EO 14399
- [ ] Tennessee absentee-ballot guidance responding to federal USPS changes, if any
- [ ] EAC termination/resignation records and Tennessee certification dependencies
- [ ] CISA program changes and Tennessee-specific operational effects
- [ ] DOJ/DHS letters or grant conditions received by Tennessee election officials

## Search Log

| Date | Location / site | Result | Follow-up |
|---|---|---|---|
| 2026-08-24 | justice.gov | DOJ Dec. 18 release: TN announced intent to provide full voter list. | Transfer later confirmed directly by Hargett/Goins. |
| 2026-08-24 | PBS / Stateline / TN reporting | Hargett and Goins confirm completed DOJ transfer; Goins says TN declined proposed MOU. | Find exact TN transmittal/privacy letter and file manifest. |
| 2026-08-24 | DOJ OLC / federal hearing | General DOJ→SAVE/DHS architecture documented. | Find TN-specific batch/upload/result record. |
| 2026-08-24 | USCIS | Official pre-2025 correspondence identifies TN as registered SAVE voter/list-maintenance user. | Locate TN's signed historical MOA/CMA. |
| 2026-08-24 | Tennessee Code / county election guidance | § 2-2-141 maps coordinator authority, notice, 30-day proof, purge, appeal; § 2-2-125 maps new-applicant appeal. | Verify any administrative guidance beyond statute. |
| 2026-08-24 | TN General Assembly | PC473 creates county portal; PC775 adds possible SAVE web-service integration; fiscal note says portal currently being created. | Search procurement/vendor/implementation records. |
| 2026-08-24 | TN 2025 SAVE announcement | ~4m records compared; 42 potential noncitizen voters referred to FBI. | Determine final disposition and notice/cure history. |
| 2026-08-24 | D.D.C. / N.D. Fla. litigation | Modified 2025 SAVE vacated; stay denied; FL/IN/IA/OH separately receive restored bulk/SSN features. | Monitor D.C. Circuit appeal; TN not included in exception. |

## Source Register and Provenance

### Core master sources

| Source ID | Title / issuer | Type | Document date | URL | Supports |
|---|---|---|---|---|---|
| SRC-001 | Justice Department Sues Four States for Failure to Produce Voter Rolls — U.S. DOJ | Official press release | 2025-12-18 | https://www.justice.gov/opa/pr/justice-department-sues-four-states-failure-produce-voter-rolls | CLM-01; DOJ campaign context |
| SRC-002 | HB2185 / Public Chapter 775 — Tennessee General Assembly | Official legislative record | 2026-04 | https://wapp.capitol.tn.gov/apps/BillInfo/Default?BillNumber=HB2185&ga=114 | SAVE portal integration |
| SRC-003 | Executive Order 14399, Ensuring Citizenship Verification and Integrity in Federal Elections | Executive order | 2026-03-31 | https://www.whitehouse.gov/wp-content/uploads/2026/03/eo-14399.pdf | Federal citizenship-list/mail architecture |
| SRC-004 | OLC Opinion on DOJ acquisition of statewide voter lists and sharing with DHS | DOJ OLC opinion | 2026-05-12 | https://www.justice.gov/olc/media/1440346/dl | DOJ legal/data-sharing architecture |
| SRC-005 | WPLN — Tennessee handed over voter data | Tennessee reporting | 2026-04-22 | https://wpln.org/post/tennessee-handed-over-voter-data-now-the-doj-faces-a-lawsuit-over-its-stockpile/ | Transfer fields |
| SRC-006 | CREW v. DOJ D.D.C. opinion / GovInfo | Federal court record | 2026-02-19 | https://www.govinfo.gov/content/pkg/USCOURTS-dcd-1_25-cv-04426/pdf/USCOURTS-dcd-1_25-cv-04426-0.pdf | Transfer-reporting context |
| SRC-007 | The Tennessean — TN sends voter data including sensitive fields to DOJ | Tennessee reporting | 2026-01-09 | https://www.tennessean.com/story/news/politics/2026/01/09/tennessee-voter-data-doj/88072297007/ | Transfer fields / discovery |

### DOJ-transfer focused sources

See `federal-election-administration-2026-doj-transfer.md` for full propositions and caveats. Key anchors include PBS/Hargett, Stateline/Goins, DOJ OLC, federal hearing transcript, Tennessee public-voter-record exclusions, and related public-record/FOIA materials.

### SAVE focused sources

See `federal-election-administration-2026-save.md`. Key anchors include:

- USCIS pre-2025 letter identifying Tennessee as a registered voter SAVE user;
- Tenn. Code Ann. § 2-2-141;
- Public Chapter 473 / HB0069;
- Public Chapter 775 / HB2185 and its fiscal note;
- § 2-2-125 current appeal text;
- HB1897/SB2124 failed direct-county SAVE proposal;
- Tennessee's 2025 ~4m-record / 42-referral announcement;
- PBS Aug. 5, 2026 Hargett interview;
- USCIS SAVE access/sample-MOA guidance;
- D.D.C. June 22 and July 8 SAVE opinions; and
- Florida v. DHS four-state restoration records.

## Current Status Verification

| Component | Best current-status evidence | Most defensible present state | Remaining uncertainty |
|---|---|---|---|
| Tennessee DOJ voter-roll cooperation | Hargett/Goins direct confirmation + reporting | **Completed transfer verified**; proposed DOJ MOU declined | Exact file/date/manifest; TN privacy letter; retention/contractor access; onward processing |
| TN statewide SAVE list maintenance | USCIS pre-2025 letter; § 2-2-141; TN 2025 use; Hargett 2026 | **Established, operational relationship**; TN used enhanced SAVE at large scale in 2025 | Current credential holders and exact legacy interface after June vacatur |
| TN county application portal | PC473 + PC775 + fiscal note | **In development**; must be implemented before Jan. 1, 2028; may integrate SAVE through secure web service | Production date, vendor, users, audit/logging/correction implementation |
| Enhanced 2025 SAVE | D.D.C. June 22 + July 8 | **Vacated; district-court stay denied; pre-2025 status quo restored generally** | D.C. Circuit appeal; any later order after research cutoff |
| Four-state SAVE exception | Florida litigation | FL/IN/IA/OH enhanced access restored under settlement | Tennessee is not included |
| DOJ→SAVE/DHS use of TN DOJ copy | General DOJ architecture + no TN-specific batch record | **Unresolved** | TN upload log, result file, DHS request, or contractor evidence |
| EO 14399 State Citizenship Lists | Executive order | Ordered, but current legal/operational status not fully mapped | Next legal-status pass |
| USPS ballot-mail measures | Not yet fully reopened in dossier | Unknown / actively litigated | Final rule, injunction scope, TN-specific effect |
| EAC institutional status | Not yet sufficiently verified | Context / unresolved for TN | TN certification effect |
| CISA support to TN | Hargett says past interaction but no recent briefing | Historical interaction verified; current operational reduction unresolved | Which services were lost/changed |

## Legal and Policy Authority

| Authority ID | Type | Citation / title | Date | Relevance |
|---|---|---|---|---|
| AUTH-01 | Federal executive order | EO 14399 | 2026-03-31 | Federal citizenship-list and election-mail architecture |
| AUTH-02 | Tennessee statute | Tenn. Code Ann. § 2-2-141 | Current | Coordinator statewide SAVE authority; notice/cure/purge/appeal process |
| AUTH-03 | Tennessee law | Public Chapter 473 / HB0069 | 2025-05-21 | Creates county application citizenship portal before 2028 |
| AUTH-04 | Tennessee law | Public Chapter 775 / HB2185 | 2026-04-21 | Authorizes SAVE web-service integration into county portal |
| AUTH-05 | Tennessee statute | Tenn. Code Ann. § 2-2-125 | Current | 10-day appeal for rejected voter-registration application |
| AUTH-06 | DOJ legal opinion | OLC voter-roll acquisition/sharing opinion | 2026-05-12 | DOJ's asserted authority to demand/share state voter files |
| AUTH-07 | D.D.C. judgment | League of Women Voters v. DHS | 2026-06-22 | Vacates 2025 modified SAVE and related SORNs |
| AUTH-08 | D.D.C. stay opinion | League of Women Voters v. DHS | 2026-07-08 | Denies stay of SAVE vacatur pending appeal |
| AUTH-09 | N.D. Fla. order | Florida v. DHS | 2026-07-07 | Restores enhanced SAVE features to four settlement states, not TN |

## Contradictory / Qualifying Evidence

| Issue | Evidence supporting a stronger inference | Evidence narrowing it | Current treatment |
|---|---|---|---|
| Tennessee DOJ transfer | Hargett/Goins directly confirm transfer and reporting describes sensitive fields. | Exact file manifest, transmission record, and TN-specific safeguards remain missing. | Transfer Verified; fields/safeguards qualified. |
| SAVE use in Tennessee | TN has statutory authority, was registered pre-2025, used SAVE on ~4m records, and Hargett confirms federal SAVE work. | This does **not** prove the PC775 county portal is live; fiscal note says it is being created. | Separate statewide SAVE use from future county portal. |
| Enhanced SAVE capability | TN demonstrably used enhanced system in 2025. | D.D.C. vacated 2025 modifications June 22; TN is not in four-state restoration. | Do not imply bulk/SSN capability remains currently available to TN. |
| SAVE match → voter removal | TN law can lead to purge if proof isn't supplied after notice. | SAVE itself does not automatically purge; state notice, proof, and appeal processes exist. | Describe procedural chain precisely. |
| 42 TN referrals | TN identified and referred 42 potential noncitizen voters. | "Potential" is not final adjudication; no final disposition located. | Do not call all 42 illegal/noncitizen voters. |
| DOJ→DHS data sharing | DOJ OLC and hearing describe general SAVE/DHS processing. | No TN-specific batch/upload/result record. | TN-specific onward flow unresolved. |
| National institutional changes | EAC/CISA/DOJ changes may alter federal architecture. | TN-specific operational effect is not established for several components. | Keep as Context unless evidence emerges. |
| Political statements | Rhetoric aligns with parts of policy agenda. | Statements do not prove agency causation, unlawful motive, or result manipulation. | Context only; no causal inference. |

## Important Unknowns

1. What exact Tennessee voter-registration file was provided to DOJ, on what date, and through what transmission mechanism?
2. Which fields were included/excluded in the DOJ file, and what does the missing Tennessee privacy/transmittal letter say?
3. Has DOJ processed Tennessee's copy through SAVE/DHS, HSI, USCIS, SSA, a contractor, or another federal component?
4. What is Tennessee's executed SAVE voter-verification MOA/CMA and what retention/access/audit terms apply?
5. Which Tennessee staff currently hold SAVE credentials, and what roles/permissions/interfaces do they use?
6. What exact legacy SAVE functionality is available to Tennessee after the June 22 vacatur while appeal is pending?
7. When will the PC473/775 county portal launch, who is building/hosting it, and what logging/audit/correction controls will it implement?
8. Will county administrators use direct SAVE credentials or only the Tennessee portal/web-service abstraction?
9. What happened to the 42 people referred to the FBI after Tennessee's 2025 SAVE comparison?
10. Did those 42 receive § 2-2-141 notice/cure procedures, and were any registrations purged/reinstated?
11. Has Tennessee received a federal State Citizenship List under EO 14399?
12. Which EO 14399 provisions are enforceable after June–August 2026 litigation?
13. What exactly does the final USPS rule require, and is any part operative for Tennessee's November 2026 absentee voting?
14. Has Tennessee changed absentee-ballot procedures because of federal requirements?
15. Have EAC leadership changes affected certification/testing of any TN voting system?
16. Has CISA reduced, ended, or materially changed services Tennessee actually used?
17. Did Tennessee accept any federal grant condition tied to SAVE, paper ballots, auditing, or election administration?

## Negative Findings

| Expected evidence | Search performed | Date | Careful finding | Follow-up |
|---|---|---|---|---|
| TN DOJ exact field manifest / transmittal / privacy terms | TN SOS, DOJ, reporting, court/FOIA material | 2026-08-24 | Completed transfer is verified, but exact primary manifest/transmission packet remains missing. | Continue targeted records/exhibit search; do not delay publication indefinitely if gap is disclosed. |
| TN-specific DOJ→DHS/SAVE processing record | DOJ/DHS/OLC/hearing/public records | 2026-08-24 | General federal architecture documented; no TN-specific batch/upload/results record located. | Keep unresolved unless later record emerges. |
| PC775 county portal production deployment | TN General Assembly, SOS, procurement/general web search | 2026-08-24 | Fiscal note says portal is currently being created; no production deployment evidence located. | Search procurement/vendor/launch records; treat as in development. |
| TN executed SAVE voter MOA/CMA | USCIS/SAVE web + TN search | 2026-08-24 | TN's registered participation is verified, but exact agreement not located. | Search FOIA releases/agency documents if useful. |
| Final disposition of 42 SAVE/FBI referrals | TN/FBI/reporting searches | 2026-08-24 | No reliable final disposition located in this pass. | Separate follow-up research. |
| General restoration of enhanced SAVE to TN after June 22 | D.D.C./D.C. Circuit/Florida litigation search | 2026-08-24 | No later order located restoring 2025 enhanced features to Tennessee; four-state order excludes TN. | Monitor appeal. |

## Digital-Rights Significance

| Implication | Evidence / reasoning | Classification | Source / uncertainty |
|---|---|---|---|
| Sensitive voter-data concentration | TN transferred statewide voter data with sensitive identifiers to DOJ. | Demonstrated transfer; exact fields partly qualified | DOJ-transfer note |
| Cross-agency processing | DOJ documents general SAVE/DHS architecture for collected state voter files. | Demonstrated general architecture; TN-specific DOJ copy unconfirmed | OLC/hearing |
| Database-assisted eligibility decisions | TN law authorizes SAVE comparisons; TN used enhanced SAVE at statewide scale. | Demonstrated | SAVE note |
| Notice/correction safeguards | TN law provides notice, 30-day proof process, and appeal for registered-voter citizenship cases; separate 10-day applicant appeal exists. | Demonstrated | §§ 2-2-141, 2-2-125 |
| Bulk/SSN matching legal risk | 2025 enhanced SAVE used SSA/SSN and bulk architecture; federal court vacated it under privacy/statutory law. | Demonstrated historical/current legal boundary | D.D.C. opinions |
| County access expansion | New portal will move citizenship verification closer to county application processing and may integrate SAVE. | Enacted but not yet operationally established | PC473/775/fiscal note |
| Election-mail infrastructure | EO 14399 includes USPS-related election measures that could affect ballots if operative. | Conditional | Next pass required |
| Federal-state accountability | Multiple systems cross state/federal institutional boundaries, making provenance, access, logs, correction, and authority important. | Supported implication | Multiple sources |

## Affected Groups

| Group | Evidence-supported basis | Limits / uncertainty |
|---|---|---|
| Tennessee registered voters | Statewide voter data transfer and SAVE list-maintenance processes directly concern their records. | Exact downstream uses of DOJ copy unresolved. |
| Voters flagged on citizenship grounds | § 2-2-141 can trigger notice/proof/purge/appeal process. | No evidence every SAVE flag leads to purge; 42-case outcomes unknown. |
| New Tennessee registration applicants | Future county portal will check citizenship before application processing. | Portal not established as production-live today. |
| Tennessee county election administrators | Will use portal under § 2-2-401; currently administer statutory notices/appeals. | Direct current SAVE credentials not established. |
| Tennessee absentee/mail voters | Federal USPS rules may apply if legally operative. | Present TN effect not yet established. |
| People with stale/inconsistent federal citizenship records | Enhanced data matching and state proof processes can surface discrepancies. | No specific TN wrongful-match case established here. |

## Confidence and Publication Readiness

### Provisional Assessment

- Candidate confidence: **Medium, strengthening toward publication-ready core**
- Proposed Tracker status: **Monitoring**
- Reasoning: The Tennessee nexus is now strong and reproducible. Completed DOJ transfer is directly confirmed. Tennessee's SAVE relationship, legal authority, large-scale 2025 use, voter notice/appeal framework, new county portal architecture, and current enhanced-SAVE legal boundary are substantially mapped. Remaining central work is now concentrated on EO 14399/USPS current legal status, one linked child entry, and final adversarial review rather than basic Tennessee eligibility.

### Readiness Checklist

- [x] A meaningful Tennessee nexus is established.
- [x] Digital-rights/election-systems relevance is established.
- [x] Completed Tennessee→DOJ transfer is directly verified.
- [x] Tennessee SAVE historical and operational use is verified.
- [x] Tennessee registered-voter notice/cure/appeal process is mapped.
- [x] PC473/775 county portal status is distinguished from existing statewide SAVE use.
- [x] Current enhanced-SAVE June/July legal boundary is mapped sufficiently for TN background.
- [x] DOJ-to-DHS Tennessee data flow has been systematically searched and is explicitly unresolved rather than assumed.
- [ ] Exact TN DOJ manifest/privacy letter obtained, **or publication explicitly states these remain unavailable**.
- [ ] Current D.C. Circuit SAVE status rechecked immediately before publication.
- [ ] EO 14399 litigation mapped provision by provision through Aug. 24, 2026.
- [ ] USPS final rule and current injunction status verified from primary documents.
- [ ] EAC/CISA events either tied to TN with evidence or kept/excluded as Context.
- [ ] At least one ordinary Tennessee Tracker entry is fully researched, drafted, and linked.
- [x] Material contradictory/qualifying evidence is preserved for DOJ/SAVE portions.
- [ ] Full-case adversarial review completed.

### Research Outcome

- [ ] Ready for Special Case publication
- [x] **Core Tennessee data/SAVE research is sufficiently mature for drafting**
- [x] More targeted research required on EO 14399/USPS/current legal status
- [x] Monitor for appellate developments
- [ ] Not suitable for publication
- [ ] Central claim contradicted / failed verification

## Adversarial Review Questions

- Are we treating Tennessee's long-standing SAVE use as if it began with the 2025 federal overhaul?
- Are we treating the in-development PC775 county portal as operational today?
- Are we treating SAVE as an automatic voter-purge system rather than preserving Tennessee's statutory notice/proof/appeal process?
- Are we treating the 42 FBI referrals as 42 proven noncitizen or fraudulent voters?
- Are we treating Tennessee's 2025 enhanced SAVE capability as still available after the June 22 vacatur?
- Are we treating DOJ's general SAVE/DHS architecture as proof Tennessee's DOJ copy was actually processed through it?
- Are we importing another state's MOU/SAVE safeguards into Tennessee without Tennessee's signed agreement?
- Are EAC/CISA developments genuinely needed to understand the Tennessee system, or do they merely make the chronology feel more alarming?
- Could Tennessee's DOJ voter-roll transfer and its own SAVE work be operationally separate even though both concern citizenship verification?
- Which findings would remain equally important if party control were reversed?

## Research Handoff

| Field | Handoff summary |
|---|---|
| Current conclusion | A Special Case is well justified on scope: Tennessee has direct voter-data and SAVE-system connections to the federal election-administration changes. The core TN SAVE architecture is now mapped; the exact DOJ-copy→DHS/SAVE link remains unestablished. |
| Strongest evidence | Hargett/Goins DOJ-transfer confirmation; pre-2025 USCIS TN SAVE registration; § 2-2-141; TN 4m-record SAVE use; PC473/775 + fiscal note; D.D.C. SAVE vacatur; EO 14399/DOJ OLC. |
| Weakest important claims | TN DOJ-copy onward processing; exact TN SAVE credential/account architecture; final 42-referral outcomes; current USPS/EO 14399 effect; EAC/CISA TN effects. |
| Contradictory / qualifying evidence | Portal is still being created; 42 were only potential matches; SAVE removal is not automatic; enhanced 2025 SAVE was vacated; TN declined DOJ MOU; authority/general architecture is not proof of TN-specific onward sharing. |
| Recommended next work | 1) EO 14399 + USPS current legal-status matrix; 2) first child entry draft (TN DOJ voter-roll transfer is strongest candidate); 3) optional 42-referral follow-up; 4) adversarial review and public Special Case draft. |
| Should Special Case drafting begin? | **Yes, after or in parallel with the EO/USPS legal-status pass. Do not publish until that current-status work and one child entry are complete.** |

## Next Research Pass — exact order

1. **EO 14399 + USPS legal-status matrix:** map relevant provisions against district/appellate/Supreme Court orders and USPS final rule through Aug. 24, 2026.
2. **First child entry:** draft the Tennessee voter-roll transfer entry with exact unknowns disclosed and link it to the future Special Case.
3. **Optional high-value follow-up:** determine what happened to Tennessee's 42 SAVE/FBI referrals and whether any were confirmed, cleared, purged, reinstated, or prosecuted.
4. **Tennessee-specific institutional context:** test EAC/CISA/grant/federal-monitor items; downgrade or exclude if no TN operational nexus.
5. **Public Special Case draft:** synthesize only verified/direct/conditional material; include mandatory `What is not established?` section.
6. **Adversarial review + validation:** challenge every causal/coordination inference, recheck current dockets, validate, then publish.