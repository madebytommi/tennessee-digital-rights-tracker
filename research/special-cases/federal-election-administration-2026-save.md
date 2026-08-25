# Research Note — Tennessee SAVE voter-verification architecture

This is an unpublished working evidence record supporting the possible Special Case **Federal Election Administration and Tennessee's 2026 Election**. It is not a public Tracker entry and is not publication-ready by itself.

This note addresses one narrow research pass: **how Tennessee uses the federal Systematic Alien Verification for Entitlements (SAVE) program for voter citizenship verification, who has or may have access, what data/workflows are documented, what notice and appeal rules apply, how the in-development county portal differs from the existing statewide workflow, and what the June–July 2026 federal litigation means for Tennessee.**

## Bottom-line findings

| Question | Finding | Evidence status |
|---|---|---|
| Did Tennessee only begin using SAVE after the Trump administration's 2025 changes? | **No.** USCIS identified Tennessee as one of ten states registered to use SAVE for voter registration and/or voter-list maintenance before the 2025 overhaul. | **Verified** |
| Who is authorized by Tennessee law to compare the statewide voter file with SAVE? | The **Coordinator of Elections** is expressly authorized under Tenn. Code Ann. § 2-2-141(a) to compare the statewide voter-registration database with SAVE and other federal/state records. | **Verified** |
| Has Tennessee actually used SAVE at statewide scale? | **Yes.** In 2025 Tennessee said it compared about **4 million records** through enhanced SAVE and referred **42 people identified as potential non-U.S. citizens who voted** to the FBI for further review. | **Verified for the comparison/referral; the 42 were potential matches, not final adjudications** |
| Does SAVE itself automatically purge a Tennessee voter? | **No.** Tennessee law provides a state process after evidence suggests a registered voter may not be a citizen: county notice, 30 days to provide citizenship proof, purge if proof is not provided, and a State Election Commission appeal route when standard documents cannot be supplied. | **Verified statutory process** |
| Is the Public Chapter 775 county-facing SAVE portal already live? | **No public evidence establishes that.** The Tennessee fiscal note says the underlying portal is **currently being created** and must be implemented before Jan. 1, 2028. Public Chapter 775 allows that in-development portal to incorporate SAVE via secure web service if DHS/USCIS makes the data available. | **Portal implementation not established; development status verified** |
| Who will use the new county portal? | **Each county administrator of elections** may use it before processing a voter-registration application. The portal was originally created by 2025 Public Chapter 473 using Department of Safety citizenship records; 2026 Public Chapter 775 adds potential SAVE integration. | **Verified** |
| Did Tennessee enact a requirement that every county directly query SAVE for every applicant and quarterly for its entire voter roll? | **No.** HB1897/SB2124 proposed that model in 2026, but HB1897 failed in House subcommittee. | **Verified narrowing evidence** |
| Can SAVE be accessed through both a browser and machine-to-machine interface? | USCIS says all SAVE users can use a web browser and some agencies can use a **web-services application**. Public Chapter 775 specifically contemplates SAVE data being available to Tennessee's portal through a secure web service. | **Verified generally; Tennessee implementation details unresolved** |
| What happened to the 2025 enhanced SAVE features Tennessee used? | A D.D.C. court on June 22, 2026 vacated the 2025 modified SAVE system, including its natural-born-citizen/SSA data, SSN-search, and bulk-search architecture, restoring the prior regulatory status quo. The district court denied a stay July 8. | **Verified** |
| Is Tennessee covered by the separate July 7 order restoring bulk/SSN features to four states? | **No.** That order applies to Florida, Indiana, Iowa, and Ohio under their settlement; Tennessee is not a party to that restoration order. | **Verified** |
| What SAVE capabilities are most defensibly available to Tennessee now? | The June 22 vacatur restores the pre-2025 baseline, under which SAVE generally depended on DHS-issued immigration identifiers and individual queries rather than SSA-backed SSN/bulk searches. The federal appeal remains pending; this pass found no later order restoring the 2025 enhanced features to Tennessee. | **High confidence as of Aug. 24, 2026; monitor appellate docket** |

## Finding 1 — Tennessee's SAVE relationship predates the 2025 overhaul

An official USCIS letter dated in 2024 states that election authorities have used SAVE for voter registration and/or voter-list maintenance since 2009 and identifies **Tennessee** among the ten states then registered for that purpose.

That older SAVE model was materially narrower than the 2025 version. According to the later D.D.C. administrative-record opinion, the pre-2025 system generally required a DHS numeric identifier (for example, an A-number), did not use SSA's master file for initial searches, generally could not query natural-born citizens, and supported individual rather than bulk searches.

### Consequence for the Tracker

Do **not** write that Public Chapter 775 or the Trump administration created Tennessee's first SAVE voter-verification relationship. Tennessee already had a lawful/statutory SAVE list-maintenance pathway. The 2025 federal overhaul changed the scale and identifiers available; the 2025–2026 Tennessee portal legislation creates a separate county-facing application-verification layer.

## Finding 2 — Tennessee law already assigns statewide SAVE comparison to the Coordinator of Elections

Tenn. Code Ann. § 2-2-141(a) requires the Coordinator of Elections to compare the statewide voter-registration database with the Tennessee Department of Safety database and further authorizes comparisons with relevant federal and state agencies, expressly including **SAVE**, for the purpose of ensuring non-U.S. citizens are not registered.

If evidence exists that a specific registered voter may not be a U.S. citizen, the coordinator notifies the county election commission where that voter is registered.

This establishes an important architectural point:

```text
Existing / statewide list-maintenance path

Statewide voter-registration database
             │
             ▼
     Coordinator of Elections
             │
             ├── Department of Safety records
             ├── SAVE
             └── other authorized federal/state/county records
             │
             ▼
 evidence concerning a specific registered voter
             │
             ▼
   county election commission notice process
```

The public record located in this pass does **not** establish that each county election commission currently has its own direct SAVE account for this statewide list-maintenance process.

## Finding 3 — Tennessee used enhanced SAVE to compare about four million records in 2025

Tennessee's October 2025 announcement said the state compared approximately **4 million records through the SAVE program** after federal enhancements and identified **42 individuals as potential non-U.S. citizens who voted**. The Secretary of State's office said it transmitted those 42 names to the FBI for investigation and possible enforcement action.

This proves Tennessee was not merely enrolled in SAVE on paper. It used the enhanced 2025 system at very large scale.

### Important qualification

The 42 were described by Tennessee as **potential** non-U.S. citizens. Referral to the FBI is not a final determination that a person was a noncitizen, was illegally registered, or committed voter fraud.

This pass did **not** locate a reliable final accounting showing:

- how many of the 42 were ultimately confirmed to be noncitizens;
- how many were U.S. citizens or false/incomplete matches;
- whether any were prosecuted;
- whether any were removed from Tennessee's voter rolls;
- whether all received the § 2-2-141 notice/cure process; or
- what the FBI ultimately did with the referrals.

Those are separate follow-up questions.

## Finding 4 — Tennessee's registered-voter notice, cure, purge, and appeal process is explicit

For a **registered voter** flagged through the Coordinator's citizenship-verification authority, § 2-2-141 establishes the following process:

1. The Coordinator notifies the appropriate county election commission that evidence exists the registered voter may not be a U.S. citizen.
2. The county sends written notice asking whether the voter is eligible.
3. The voter has **30 days from receipt** to provide proof of citizenship.
4. Statutorily listed proof includes a birth certificate, U.S. passport, naturalization documentation/certificate number (with USCIS verification when only the number is supplied), or a method permitted under the federal Immigration Reform and Control Act.
5. If the voter does not provide proof within the 30-day period, the county administrator **shall purge** the voter from the registration database.
6. If the person cannot supply the listed documentation, the person may appeal to the **State Election Commission** and submit additional proof in person or in writing. The commission holds a hearing and sends its decision to the county administrator, who updates the database accordingly.
7. Citizenship documentation and the government records used are confidential and not open for public inspection.

Hamilton County's official voter-registration guide independently describes the same notice → 30 days → potential purge → State Election Commission appeal sequence.

### SAVE's federal-side procedure

The USCIS 2025 sample voter-verification MOA and the D.D.C. administrative record describe a separate federal verification expectation: a nonfinal/inconclusive SAVE result can require **additional verification**, and when citizenship is not verified the user agency is directed to contact the registrant or registered voter to obtain citizenship proof.

However, this is a **sample MOA / federal template**. Tennessee's exact historical SAVE voter-verification MOA or current CMA/MOA was not located in this pass, so its precise contractual language must not be attributed to Tennessee as if we possessed the signed agreement.

## Finding 5 — The new county portal is a different system and is still being built

A major source of confusion was treating Public Chapter 775 as though it created Tennessee's SAVE workflow from scratch. It did not.

### Public Chapter 473 (2025): creates the county application portal

HB0069/SB0133 became **Public Chapter 473**, effective May 21, 2025. It requires the Coordinator of Elections, working with the Department of Safety, to create before **Jan. 1, 2028** a secure electronic portal that each county administrator of elections can use **before processing a voter-registration application**.

The underlying citizenship check is based on Department of Safety records reflecting citizenship status at the time of the applicant's most recent Tennessee driver license, ID card, or other Department of Safety credential.

The required state agreement is to define, among other things:

- what applicant information the administrator submits so the correct applicant is identified;
- what information the portal returns;
- temporary alternatives during outages;
- misuse rules and penalties; and
- confidentiality of information sent and returned through the portal.

If a county administrator rejects a registration application based on portal information, the applicant receives written notice of appeal rights.

### Public Chapter 775 (2026): permits SAVE integration

HB2185/SB2204, enacted as **Public Chapter 775**, authorizes this same portal to access SAVE data **if DHS/USCIS makes that data available through a secure web service**.

The February 2026 fiscal note is especially useful because it says the portal **"is currently being created"** and must be implemented before Jan. 1, 2028. It says the portal can incorporate SAVE data without additional state expenditure.

That gives us the most defensible current status:

> The county-facing citizenship-verification portal exists as an enacted development requirement and is being built, but the public record located does not establish that the production portal is live or that county administrators are currently querying SAVE through it.

## Finding 6 — New-applicant appeal rules differ from the registered-voter purge path

For a **new registration application** rejected by an administrator, Tenn. Code Ann. § 2-2-125 provides a different appeal route:

- written notice stating the reason for rejection and providing an appeal form;
- **10 days from the date notice was sent** to appeal to the county election commission;
- a hearing if necessary; and
- a written explanation if the commission sustains the rejection.

Public Chapter 473 explicitly ties portal-based application rejection to this appeal procedure.

So public drafting should distinguish:

```text
REGISTERED VOTER / LIST MAINTENANCE
§ 2-2-141
Coordinator flag → county notice → 30 days proof → purge if no proof
→ State Election Commission appeal when standard documents cannot be supplied

NEW APPLICANT / FUTURE COUNTY PORTAL
§§ 2-2-401 and 2-2-125
portal check → application rejection notice → 10-day appeal
→ county election commission
```

Conflating these two processes would materially misstate Tennessee law.

## Finding 7 — Tennessee rejected a more aggressive direct-county SAVE model in 2026

HB1897/SB2124 would have required **each county election commission** to:

- check every voter-registration applicant against SAVE before registration; and
- at least once per quarter, check the county's entire voter-registration list through SAVE.

HB1897 failed in the House Elections & Campaign Finance Subcommittee on March 10, 2026.

This is important narrowing evidence. Current Tennessee law should **not** be described as requiring every county to directly run quarterly SAVE sweeps of its voter roll. The enacted architecture is more centralized: statewide list-maintenance authority with the Coordinator, plus an in-development county portal for application checks.

## Finding 8 — Browser and web-services access exist generally, but Tennessee account ownership remains opaque

USCIS says:

- all SAVE users can access SAVE through a **web browser**; and
- some participating agencies can use a **web-services application**.

Public Chapter 775's language is consistent with system-to-system integration because it conditions Tennessee portal access on USCIS making SAVE data available via a **secure web service**.

What this pass could **not** establish:

- the exact Tennessee SAVE user-agency account name;
- how many Tennessee users currently have credentials;
- whether credentials belong only to state-level election staff or also to county staff;
- whether Tennessee currently uses browser access, API/web-services access, batch upload, or some combination;
- the vendor or internal state team building the § 2-2-401 portal;
- the portal's production hosting environment;
- whether a new SAVE MOA/CMA must be signed before Public Chapter 775 integration goes live; or
- exact logging/role permissions for Tennessee's account.

USCIS requires agencies to participate under an MOA or CMA. The D.D.C. administrative record specifically notes that user agencies execute such agreements before participating in modified SAVE. Tennessee's signed voter-verification agreement was not located.

## Finding 9 — What the 2025 enhanced SAVE system actually did

The June 22, 2026 D.D.C. opinion reconstructed the 2025 modified SAVE architecture from the administrative record.

The overhaul made three major changes:

1. included records of natural-born U.S. citizens;
2. added access to Social Security Administration records, including Social Security numbers; and
3. enabled **bulk searches**.

In the modified bulk workflow, a user could upload a spreadsheet containing first name, last name, date of birth, full or partial SSN, reason for verification (including voter verification), and optionally a DHS numeric identifier. SAVE then queried SSA data and could return match indicators, full SSN when a partial SSN matched, citizenship/foreign indicators, death information, and related identifiers. Potential noncitizen results with a DHS identifier could trigger queries to additional federal systems.

For inconclusive results, SAVE could require more information or supporting documents. The administrative record described responses including U.S. Citizen, Deceased, Immigration Enumerator Required, Unable to Return Record from SSA, or Full SSN Required.

This is the architecture Tennessee could use when it compared approximately four million records in 2025.

## Finding 10 — The 2025 enhanced architecture was vacated in June 2026

On **June 22, 2026**, the U.S. District Court for the District of Columbia held the 2025 modified SAVE system and related DHS/SSA system-of-records notices unlawful under the Social Security Act, Privacy Act, and APA, and **set aside/vacated** them.

The opinion expressly says that APA vacatur restores the prior regulatory status quo: the invalid modified system is eliminated and the preexisting regime returns.

On **July 8**, the same district court denied the federal government's request to stay that judgment pending appeal.

The federal government appealed to the D.C. Circuit (No. 26-5243). This research pass did not locate a later appellate order, through Aug. 24, granting a stay that would generally restore the 2025 modified features for Tennessee.

### Four-state exception does not include Tennessee

A different federal court in Florida enforced a settlement requiring DHS to restore **bulk-upload and SSN-search features** to **Florida, Indiana, Iowa, and Ohio**. The D.D.C. court itself later emphasized that the Florida settlement's equitable relief applied to those parties rather than other SAVE users.

Tennessee is not among those four states.

### Most defensible Aug. 24 status for Tennessee

As of the latest status located in this pass:

- Tennessee remains historically authorized/registered to use SAVE for voter verification under the pre-2025 model;
- the **2025 enhanced SSA/SSN/bulk system is vacated generally**;
- the district court denied a stay;
- Tennessee is not covered by the four-state Florida restoration order; and
- the appeal remains a live update trigger.

Do not describe Tennessee as currently possessing the same bulk/SSN capability it used for the 2025 four-million-record comparison unless a newer order or agency record establishes restoration.

## Current architecture diagram

```text
A. EXISTING / HISTORICAL STATEWIDE LIST-MAINTENANCE PATH

Tennessee statewide voter database
              │
              ▼
      Coordinator of Elections
              │
              ├── Department of Safety
              ├── SAVE (TN registered pre-2025)
              └── other authorized records
              │
              ▼
 evidence a specific registered voter may not be a citizen
              │
              ▼
 county notice → 30 days to prove citizenship
              │
              ├── proof accepted → registration retained/corrected
              └── no proof → purge
                       │
                       └── State Election Commission appeal route

2025 enhanced SAVE temporarily added:
    SSA/SSN matching + natural-born-citizen records + bulk upload
    Tennessee compared ~4 million records → 42 potential noncitizen voters
    → names referred to FBI

June 22, 2026:
    modified 2025 SAVE vacated; pre-2025 regulatory status quo restored
    (appeal pending; TN not in four-state Florida restoration)


B. IN-DEVELOPMENT COUNTY APPLICATION PATH

County administrator of elections
              │
              ▼
secure TN portal required before Jan. 1, 2028
(Coordinator of Elections + Department of Safety)
              │
              ├── Department of Safety citizenship record
              └── may integrate SAVE through secure web service
                  under Public Chapter 775 if federally available
              │
              ▼
application processed or rejected
              │
              └── rejection → 10-day county-election-commission appeal

PUBLIC STATUS: fiscal note says portal is currently being created;
no public evidence located that this production portal is live today.
```

## Master-dossier claim updates recommended

| Claim / event | Old treatment | Recommended treatment after this pass |
|---|---|---|
| CLM-02 — Tennessee completed DOJ voter-file transfer | Partially verified | **Verified** from Hargett/Goins direct statements in prior transfer pass. |
| CLM-05 — Tennessee SAVE use | Unresolved | Split claim: **Verified** that Tennessee has operationally used SAVE for voter verification; **Unresolved / not yet live in public record** for the specific Public Chapter 775 county portal. |
| New — Tennessee was a registered SAVE voter user before 2025 | — | **Verified.** |
| New — Coordinator has statutory authority to compare statewide voter DB with SAVE | — | **Verified.** |
| New — Tennessee compared ~4 million records through enhanced SAVE in 2025 and referred 42 potential noncitizen voters who voted to FBI | — | **Verified for comparison/referral; final status of 42 unresolved.** |
| EVT-013 — Public Chapter 775 | Verified | Keep Verified, but clarify it **adds SAVE capability to an existing in-development portal** created by Public Chapter 473; it does not prove operational deployment. |
| EVT-015 — SAVE litigation | Unverified | **Upgrade core SAVE portion to Verified:** modified 2025 SAVE vacated June 22; district-court stay denied July 8; appeal pending. |
| New — four-state restoration | — | **Context / narrowing:** Florida, Indiana, Iowa, Ohio got restored bulk/SSN access under separate settlement; Tennessee did not. |

## Source register

| ID | Source | Type | Key proposition | URL |
|---|---|---|---|---|
| SAV-001 | USCIS 2024 letter concerning SAVE voter-verification use | Official USCIS correspondence | Election authorities have used SAVE since 2009; Tennessee was one of ten registered voter-registration/list-maintenance states before 2025. | https://www.uscis.gov/sites/default/files/document/foia/RegisteredVoters-SecretaryNelson.pdf |
| SAV-002 | Tenn. Code Ann. § 2-2-141 | Tennessee statute compilation | Coordinator SAVE authority; notice; 30-day proof window; purge; State Election Commission appeal; confidentiality. | https://law.justia.com/codes/tennessee/title-2/chapter-2/part-1/section-2-2-141/ |
| SAV-003 | Hamilton County Voter Registration Guide | Official county election guidance | Independently describes SAVE/citizenship notice, 30-day proof period, purge, and appeal route. | https://elect.hamiltontn.gov/registration.aspx |
| SAV-004 | HB0069/SB0133 / Public Chapter 473 bill record | Official Tennessee General Assembly record | Creates secure county-facing application-verification portal before Jan. 1, 2028 using Department of Safety records; appeal/confidentiality architecture. | https://wapp.capitol.tn.gov/apps/BillInfo/Default?BillNumber=HB0069&ga=114 |
| SAV-005 | HB2185/SB2204 / Public Chapter 775 bill record | Official Tennessee General Assembly record | Allows the § 2-2-401 portal to access SAVE via secure web service if DHS/USCIS makes it available. | https://wapp.capitol.tn.gov/apps/Billinfo/Default?BillNumber=SB2204&ga=114 |
| SAV-006 | SB2204/HB2185 Fiscal Note, Feb. 21, 2026 | Official Fiscal Review Committee document | Says existing coordinator authority includes SAVE and that the county portal **is currently being created** and must be implemented before Jan. 1, 2028. | https://capitol.tn.gov/Bills/114/Fiscal/SB2204.pdf |
| SAV-007 | Tennessee 2026 codification, § 2-2-125 | Official Tennessee code bill compilation | 10-day appeal process after registration rejection; county election commission final administrative action. | https://capitol.tn.gov/Archives/Joint/publications/TNCodeBills/2026/TNCodeBill_Volume1_2026.pdf |
| SAV-008 | HB1897/SB2124 committee record | Official Tennessee General Assembly material | Proposed mandatory direct county SAVE checks for every applicant and quarterly entire-list sweeps; bill failed in House subcommittee. | https://capitol.tn.gov/Bills/114/Calendars/2026-3-9_SubcommH.pdf |
| SAV-009 | Tennessee Secretary of State 2025 SAVE announcement, reproduced in contemporaneous Tennessee press | State announcement / contemporaneous reproduction | Approximately 4 million records compared; 42 potential non-U.S. citizens who voted referred to FBI. | https://tennesseelookout.com/2025/11/03/tn-secretary-of-state-finds-42-possible-non-citizen-voters-out-states-4-3-million-voters/ |
| SAV-010 | PBS NewsHour interview with Secretary Tre Hargett, Aug. 5, 2026 | Direct state-official interview | Tennessee has worked with federal government through SAVE; last-four SSN used; confirms real operational use. | https://www.pbs.org/video/election-security-1785955610/ |
| SAV-011 | USCIS, Accessing SAVE | Official USCIS guidance | All users can use browser access; some agencies use web-services applications. | https://www.uscis.gov/save/current-user-agencies/guidance/save-user-resource-guide/3-accessing-save |
| SAV-012 | USCIS Voter Verification Agency Sample MOA, rev. June 9, 2025 | Official federal sample agreement | General voter-verification participation/additional-verification framework; **not proof of Tennessee's signed agreement**. | https://www.uscis.gov/sites/default/files/document/brochures/SAVE%20MOA%20Voter%20Registration%20and%20List%20Maintenance%20Sample.pdf |
| SAV-013 | League of Women Voters v. DHS, D.D.C. memorandum opinion, June 22, 2026 | Federal court opinion based on administrative record | Describes old vs modified SAVE, bulk/SSN workflow, and vacates 2025 modified system, restoring prior status quo. | https://law.justia.com/cases/federal/district-courts/district-of-columbia/dcdce/1:2025cv03501/285454/111/ |
| SAV-014 | League of Women Voters v. DHS, D.D.C. stay opinion, July 8, 2026 | Federal court opinion | Denies federal defendants' motion to stay June 22 vacatur pending appeal. | https://law.justia.com/cases/federal/district-courts/district-of-columbia/dcdce/1:2025cv03501/285454/123/ |
| SAV-015 | D.C. Circuit docket No. 26-5243 | Federal appellate docket index | Confirms appeal of SAVE judgment. | https://dockets.justia.com/docket/circuit-courts/cadc/26-5243 |
| SAV-016 | Florida v. DHS case summary/docket | Federal litigation record summary | July 7 order restored bulk-upload/SSN search features to Florida, Indiana, Iowa, and Ohio under their settlement. | https://clearinghouse.net/case/48353/ |

## Negative findings / records still missing

This pass did **not** locate:

1. Tennessee's executed historical SAVE voter-registration/list-maintenance MOA or CMA.
2. A definitive list of current Tennessee SAVE users, user roles, departments, or credential holders.
3. Proof that county administrators presently have direct SAVE accounts.
4. A production URL, screenshot, procurement record, system-design document, or launch notice showing the Public Chapter 473/775 county portal is live.
5. The exact vendor, hosting architecture, API specification, logging standard, or audit controls for the county portal under development.
6. A Tennessee-specific agreement adopting the June 2025 USCIS voter-verification MOA template.
7. A final disposition for the 42 people Tennessee referred to the FBI after the 2025 four-million-record SAVE comparison.
8. A record showing whether each of those 42 received § 2-2-141 notice/cure procedures.
9. A later D.C. Circuit order, through the Aug. 24 research cutoff, generally restoring the 2025 enhanced SAVE system to Tennessee.
10. Evidence that Tennessee is included in the four-state Florida restoration order; it is not a named party to that relief.

Failure to locate a record is not evidence that no such record exists.

## Research conclusion for this pass

The Tennessee SAVE question is now substantially resolved at the level needed for responsible public synthesis.

The state has **two distinct architectures** that must not be conflated:

1. a longstanding, state-level voter-list-maintenance relationship in which the Coordinator of Elections is authorized to compare the statewide voter database with SAVE and other records; and
2. a **new county-facing application-verification portal**, created in 2025 and still being built, that Public Chapter 775 authorizes to incorporate SAVE through a secure web service if available.

Tennessee demonstrably used the federal government's **enhanced 2025 SAVE** at statewide scale, comparing approximately four million records and referring 42 potential noncitizen voters to the FBI. But the specific enhanced features that enabled SSA-backed SSN matching and bulk search were vacated by a federal court on June 22, 2026; Tennessee is not included in the separate four-state restoration order.

The most important unresolved operational details are now narrower: the identity/roles of Tennessee's actual SAVE account holders, the signed Tennessee SAVE agreement, the exact status/architecture of the county portal, and the final disposition of the 42 referrals. Those gaps should remain visible, but they no longer prevent the Tracker from explaining **what Tennessee's SAVE architecture is, how voters can be affected under state law, and which portions are current versus still under development or litigation.**