---
title: "Greenbrier Police Department operates a Flock Safety license plate reader program"
date: 2026-07-31
event_date: 2026-07-28
last_reviewed: 2026-07-31
status: "Monitoring"
level: "Local"
category: "government-surveillance"
jurisdiction: "Greenbrier, Tennessee"
confidence: "Medium"
summary: "Greenbrier Police Department has publicly acknowledged using fixed Flock Safety automated license plate readers for real-time alerts and retrospective vehicle searches. Publicly available records reviewed for this entry do not establish the program's original authorization, current camera count, contract terms, retention setting, complete sharing network, audit practices, or enabled optional features."
primary_source_url: "https://www.atlasofsurveillance.org/search?location=Greenbrier+Police+Department%2C+TN"
primary_source_type: "dataset"
source_archive_url: ""
tags:
  - alpr
  - flock-safety
  - law-enforcement
  - location-data
  - data-sharing
  - public-records
  - local-government
revision_history:
  - date: 2026-07-28
    note: "Initial draft based on Greenbrier Police statements reported by WSMV, Tennessee law, the Atlas of Surveillance, Flock Safety policies, and publicly available city records."
  - date: 2026-07-31
    note: "Refreshed city, news, legal, vendor, and transparency-portal sources; clarified the direction of documented network sharing, narrowed SignalTrace claims, synchronized the branch with main, and confirmed local validation."
---

## Research and legal limitations

This entry is public-record research, not legal advice. The project and its contributors:

- are not acting as attorneys and cannot provide a binding legal opinion;
- cannot guarantee that the City of Greenbrier, Greenbrier Police Department, Flock Safety, or another organization has publicly disclosed every implementation detail;
- cannot independently inspect nonpublic camera configurations, search logs, sharing settings, cybersecurity controls, retention settings, hotlists, internal investigations, or disciplinary records; and
- recommend review by a qualified Tennessee attorney, privacy professional, security expert, or law-enforcement policy specialist before drawing especially strong legal or technical conclusions.

A July 31, 2026 source refresh reviewed Greenbrier's police page, Board of Mayor and Aldermen information and agenda center, city records-request materials, recent reporting, the Atlas of Surveillance, current Flock policy and transparency pages, Tennessee legislative sources, Leonardo's SignalTrace materials, and the Supreme Court's 2026 location-data decision. It did not locate a publicly posted Greenbrier ALPR policy, contract, governing-body authorization, Tennessee Department of Transportation approval, audit report, usage report, or Greenbrier-specific Flock transparency portal. That evidence gap is documented rather than treated as proof that no such record, safeguard, or approval exists.

The Atlas of Surveillance entry used in the front matter is an open-source dataset maintained by the Electronic Frontier Foundation. It cites a September 2025 public record from the Pittsboro Police Department in Indiana. This review was able to verify the Atlas entry but not independently inspect the complete underlying shared-device record, so the Atlas data are not used to infer Greenbrier's complete sharing configuration.

## What happened?

On July 28, 2026, WSMV published an explanation from the Greenbrier Police Department concerning its use of fixed Flock Safety automated license plate reader cameras. The department described the cameras as tools for real-time alerts and retrospective investigations rather than speed-enforcement, red-light, facial-recognition, or ticket-generating devices.

According to the department's statements reported by WSMV, the cameras capture still images of passing vehicles and record license plate numbers, make, model, color, distinguishing features, direction of travel, time, and camera location. The department said officers may receive alerts involving stolen vehicles, wanted people, missing or endangered people, AMBER Alerts, Silver Alerts, and vehicles connected to active investigations. It also said investigators can search historical records after a reported crime using a partial plate or general vehicle description.

The Electronic Frontier Foundation's Atlas of Surveillance separately reports that Greenbrier Police operated two Flock Safety automated license plate readers as of September 2025. The Atlas cites a shared-device record produced by the Pittsboro Police Department in Indiana. The original date of Greenbrier's approval, purchase, installation, and first operational use remains unresolved.

This entry uses July 28, 2026, as the `event_date` because that is the date of the clearest publicly accessible departmental acknowledgment reviewed for this draft. It should be replaced with an earlier authorization or deployment date if a contract, resolution, meeting record, invoice, or permit establishes one.

## What the primary source says

### Best available operational record

The Atlas of Surveillance lists Greenbrier Police Department as operating two Flock Safety automated license plate readers as of September 2025. Its source link identifies a Pittsboro Police Department public record concerning Flock Safety shared devices.

The Atlas entry supports the conclusion that Greenbrier had an operational Flock presence by September 2025. It does not, by itself, establish:

- whether two cameras remain the current total;
- whether Greenbrier owns, leases, manages, or merely receives access to every listed device;
- which agencies can search Greenbrier-generated records;
- whether access is reciprocal;
- which optional Flock features are enabled; or
- how often Greenbrier personnel search cameras belonging to other agencies.

The Piperton Police Department's Flock transparency portal, last updated July 24, 2026, lists Greenbrier TN PD under "Sharing Network Data With." That is evidence that Piperton represents itself as sharing network data with Greenbrier. It does not establish Greenbrier's outgoing sharing settings, every source Greenbrier can search, whether the relationship is reciprocal, or how often any access is used.

### Tennessee collection and retention law

Tennessee Code § 55-10-302 defines an automated license plate recognition system as fixed high-speed cameras combined with computer algorithms that convert license plate images into computer-readable data.

The statute defines captured plate data to include:

- GPS coordinates;
- date and time;
- a photograph;
- the license plate number; and
- other data captured by or derived from the ALPR system.

Tennessee generally prohibits a governmental entity from storing captured plate data for more than 90 days. Data may be retained longer when it is part of an ongoing investigation. In that situation, the law requires destruction at the conclusion of an investigation that produces no criminal charges or at the conclusion of the related criminal action.

The 90-day period is a legal maximum, not proof of Greenbrier's actual routine setting. Flock Safety states that its default retention period is 30 days and that a customer's law or policy may require a different period. Publicly available Greenbrier records reviewed for this draft do not establish whether the department uses 30 days, another period below the Tennessee maximum, or investigative preservation procedures.

### Confidentiality under Tennessee public-records law

Tennessee law treats captured plate data as confidential and not open for public inspection. Public Chapter 672, signed in April 2026, removed the former July 1, 2026 expiration date from that confidentiality provision.

That restriction applies to captured plate data themselves. It does not necessarily make every contract, policy, camera inventory, general placement description, aggregate statistic, audit summary, training document, sharing configuration, or procurement record confidential. The availability of any particular record may depend on its contents and applicable exemptions.

### Flock's published baseline policies

Flock Safety's LPR policy, last updated June 30, 2026, says LPR data include plate and vehicle images, vehicle characteristics, plate number and state, date, time, and camera location. It says queries are logged with the username, date, time, purpose, and search elements, and that customers choose whether to share LPR data with other customers.

Flock also states that LPR data are hard-deleted on a rolling 30-day basis by default unless a customer's law or policy requires another schedule. The company acknowledges that plate translations may be incomplete or inaccurate and instructs users to confirm the computer translation before taking action.

These are vendor-wide statements. They do not independently prove Greenbrier's local configuration, supervisory practices, entered search reasons, account-security procedures, audit schedule, or disciplinary enforcement.

## What officials say

Greenbrier Police told WSMV that its cameras:

- capture still vehicle images and publicly visible vehicle details;
- do not determine vehicle ownership or identify drivers or passengers;
- do not use facial recognition;
- do not track vehicles through a GPS transmitter;
- do not measure speed, enforce red lights, or automatically issue tickets;
- may create alerts involving stolen vehicles, wanted people, missing or endangered people, AMBER Alerts, Silver Alerts, and active investigations; and
- may be searched retrospectively using a partial plate or vehicle description after a reported crime.

The department also said an officer must verify an alert through the National Crime Information Center or another official law-enforcement source before taking action.

These are official claims reported by WSMV. This review did not locate Greenbrier's written policy, training materials, audit records, or alert logs needed to verify how these safeguards operate in practice.

The statement that the cameras do not use GPS tracking should not be read to mean the system cannot reconstruct vehicle movement. Each fixed-camera observation includes a camera location and timestamp. Multiple observations across a network may therefore reveal where a vehicle was observed over time even when no GPS transmitter is attached to the vehicle.

## What advocates and critics say

The Electronic Frontier Foundation describes automated license plate readers as a form of mass surveillance because they record time-and-location information about every visible vehicle, including vehicles not connected to suspected wrongdoing.

EFF argues that searchable ALPR histories may reveal visits to sensitive locations such as healthcare facilities, immigration clinics, houses of worship, protests, political events, union halls, support groups, workplaces, and private residences. Critics also raise concerns about:

- mistaken plate reads or stale hotlist information contributing to unsafe stops;
- broad interstate, private-sector, or federal sharing;
- searches conducted for purposes outside the program's stated justification;
- insufficient review of audit logs;
- retention or investigative preservation that extends the useful life of location records;
- limited public visibility into systems whose raw plate data are confidential; and
- combining plate observations with other databases or investigative platforms.

These are general privacy and oversight concerns, not findings that Greenbrier personnel have misused the system. This review found no public evidence establishing misuse by Greenbrier Police Department employees.

Supporters and law-enforcement agencies argue that ALPR systems can help locate stolen vehicles, find missing or endangered people, identify vehicles associated with reported crimes, and narrow investigations when witnesses provide only partial vehicle information. Greenbrier Police presented those uses as the purpose of its system.

## What is confirmed?

- Greenbrier Police Department has publicly acknowledged using fixed Flock Safety cameras.
- According to the department's statements reported by WSMV, the cameras record still vehicle images, license plates, vehicle characteristics, direction, time, and camera location.
- According to the department, the system supports real-time alerts and retrospective vehicle searches.
- According to the department, officers must verify alerts through NCIC or another official source before acting.
- The Atlas of Surveillance reports that Greenbrier Police operated two Flock Safety ALPRs as of September 2025.
- Piperton Police Department's current Flock transparency portal lists Greenbrier TN PD among agencies with which Piperton says it shares network data.
- Tennessee law defines captured plate data to include location, time, photographs, plate numbers, and derived data.
- Tennessee generally limits government retention of captured plate data to 90 days, with an exception for data retained as part of an ongoing investigation.
- Tennessee law treats captured plate data as confidential, and the former expiration date for that confidentiality provision was removed in 2026.
- Flock states that its default retention period is 30 days, logs query details, allows customers to control sharing, and acknowledges that plate translations may be incomplete or inaccurate.
- Leonardo's SignalTrace is a separate vendor product from Flock Safety's camera system.
- The final public-source sweep did not locate evidence that Greenbrier uses SignalTrace or collects phone, smartwatch, fitness-tracker, RFID, vehicle-system, or other device-signal identifiers through its documented Flock deployment.

## What remains uncertain?

As of the last review date, the following questions remain unresolved:

### Authorization, procurement, and inventory

- When Greenbrier first considered, approved, purchased, installed, and activated the system
- Whether the Board of Mayor and Aldermen formally approved the purchase or contract
- The current contract, cost, funding source, term, renewal date, and termination provisions
- Whether competitive bids or alternative vendors were considered
- Whether any cameras on state highway rights-of-way received required Tennessee Department of Transportation approval
- The current number of active, inactive, planned, city-owned, privately owned, mobile, or partner-accessible cameras
- The camera models, software subscriptions, integrations, and optional features included

### Collection and retention

- Greenbrier's exact routine retention setting
- The procedure and legal threshold for preserving records beyond routine deletion
- Whether surrounding people, occupants, or other vehicles appear incidentally in captured images
- Whether vehicle-feature search, convoy analysis, national network search, custom hotlists, or other optional tools are enabled
- Whether Greenbrier exports records into CrimeTracer, a real-time crime center, a fusion center, or another investigative platform

### Access, searches, and auditing

- Which employees, dispatchers, analysts, task-force members, contractors, or outside personnel may search the system
- What users must enter as a search reason and whether a case or incident number is required
- Whether warrants, subpoenas, supervisory approval, or written investigative thresholds are required for particular searches
- How frequently audit logs are reviewed, by whom, and using what sampling or alert criteria
- Whether Greenbrier publishes or internally tracks the number of searches, alerts, recoveries, arrests, false alerts, rejected alerts, and complaints
- Whether misuse has ever been alleged, investigated, substantiated, or disciplined
- How inaccurate plate reads, cloned plates, stolen plates, registration transfers, and stale hotlist entries are handled

### Sharing and sensitive uses

- The complete list of agencies that can search Greenbrier-generated records
- Whether statewide, nationwide, radius-based, reciprocal, one-to-one, federal, or private-camera sharing is enabled
- Whether ICE, CBP, HSI, FBI, ATF, DEA, U.S. Marshals, federal task-force officers, or other federal entities can directly or indirectly search the system
- Whether Greenbrier has written restrictions involving immigration enforcement, reproductive healthcare, gender-affirming healthcare, religious activity, protests, political activity, or other First Amendment-protected association
- Whether private businesses, homeowners associations, schools, churches, or residents share privately owned Flock cameras with Greenbrier
- Whether the Pittsboro shared-device record reflects current access and what the direction and scope of that access were

### SignalTrace and device-signal collection

Leonardo markets SignalTrace as a separate system that captures and correlates signals emitted by mobile phones, smartwatches, fitness trackers, RFID tags, vehicle systems, and other electronics. The vendor says SignalTrace can group signals frequently observed together into an "electronic fingerprint" and correlate those groups with license plate reader data when present.

The circulating social-media image that prompted part of this research describes SignalTrace, not a documented Greenbrier capability. This review did not locate evidence that Greenbrier Police has purchased, tested, or connected SignalTrace or a comparable signal-collection system to its Flock cameras.

It remains appropriate to request records concerning any purchase, demonstration, trial, proposal, information request, or integration involving:

- Leonardo SignalTrace or its former EOC Plus name;
- Bluetooth or Wi-Fi signal collection;
- phone, smartwatch, fitness-tracker, RFID, AirTag, or other device identifiers;
- tire-pressure-monitoring-system identifiers;
- vehicle or occupant electronic fingerprints; or
- signal-intelligence sensors used alongside license plate readers.

Absence of a located public record is not proof that no agency has considered such technology.

### Legal questions

This research did not locate a Tennessee appellate or Sixth Circuit decision squarely resolving whether law enforcement must obtain a warrant before searching a networked ALPR database for historical vehicle-location information.

In June 2026, the United States Supreme Court held in *Chatrie v. United States* that police conducted a Fourth Amendment search when they acquired a person's Google cell-phone location history. The decision concerns cell-phone location information, not automated license plate reader databases. Its effect on future ALPR litigation is therefore an open legal question rather than a settled answer.

## Who may be affected?

The system may affect anyone whose vehicle passes a participating camera, not only people suspected of crimes.

Potentially affected groups include:

- Greenbrier residents and commuters;
- visitors and people traveling through Robertson County;
- drivers of borrowed, rented, employer-owned, or family-owned vehicles;
- passengers whose presence may be inferred from other evidence;
- people visiting healthcare facilities, houses of worship, protests, political meetings, attorneys, support groups, workplaces, or private residences;
- people incorrectly associated with a misread, cloned, stolen, transferred, or outdated plate;
- crime victims, missing or endangered people, and vehicle owners who may benefit from faster identification or recovery;
- private camera owners participating in law-enforcement sharing; and
- neighboring, state, federal, and out-of-state agencies that contribute to or search networked records.

A plate observation does not by itself establish who was driving, who else was present, why the vehicle was at a location, whether the registered owner was involved, or whether any unlawful activity occurred.

## Privacy and civil-liberties significance

A license plate is displayed publicly, and a single observation on a public road generally reveals less than continuous phone-location tracking. The privacy significance changes when large numbers of observations become searchable across time, agencies, private camera networks, and jurisdictions.

The available evidence supports two conclusions at once:

1. ALPR technology can help investigators locate vehicles connected to reported crimes or endangered people and can provide leads when witnesses have incomplete vehicle information.
2. A networked historical database can expose the movements and associations of people who are not suspected of wrongdoing, especially when retention, sharing, search standards, and auditing are not publicly documented.

Tennessee's 90-day maximum and confidentiality rule are meaningful safeguards, but each has limits. The retention law permits investigative preservation, and the confidentiality rule prevents public disclosure of raw plate histories while also limiting residents' ability to inspect the underlying data for accuracy and scale. Public policies, contracts, aggregate statistics, access lists, audit summaries, and transparency portals therefore become especially important.

Greenbrier's reported two-camera inventory may appear small in isolation. Its practical reach can be larger if officers can search cameras operated by other Tennessee or out-of-state agencies, if other agencies can search Greenbrier records, or if privately owned cameras participate in the network. Current public evidence confirms that at least one Tennessee agency says it shares network data with Greenbrier, but it is insufficient to map the complete direction, scope, or oversight of Greenbrier's network relationships.

The strongest defensible current conclusion is:

> Greenbrier Police Department operates a documented Flock Safety ALPR program and participates in a broader Flock network. The department has publicly described legitimate investigative uses and alert-verification safeguards, while Tennessee law limits retention and protects raw plate records from public disclosure. The public record is not yet sufficient to evaluate Greenbrier's current camera inventory, contract, retention configuration, sharing scope, search standards, audit rigor, error controls, effectiveness, or compliance in practice.

Resolving those questions requires local policy, procurement, configuration, and audit records rather than assumptions about either good faith or misconduct.

## Lawful actions and resources

- Read the WSMV report and distinguish the department's stated practices from independently verified records.
- Review Greenbrier Board of Mayor and Aldermen agendas, minutes, budget materials, and meeting videos for ALPR authorization or funding.
- Submit a Tennessee Public Records Act request to the City Recorder for contracts, policies, retention settings, sharing lists, audit procedures, aggregate statistics, TDOT records, and SignalTrace-related procurement communications.
- Request records at the policy and aggregate level rather than individual plate histories, named-driver movements, or active-investigation material.
- Ask Greenbrier to publish its ALPR policy, current retention period, camera count, sharing categories, prohibited uses, aggregate usage statistics, and a public search-audit or transparency portal.
- Attend a Board of Mayor and Aldermen meeting or submit a public-comment request under the city's published procedure.
- Ask elected officials to require periodic public reporting, independent audit review, written restrictions for sensitive investigations, and documented human verification before enforcement action.
- Report suspected misuse through appropriate local oversight channels and consult a qualified Tennessee attorney or civil-liberties organization for individual legal advice.

## Sources

1. [Electronic Frontier Foundation, Atlas of Surveillance — Greenbrier Police Department](https://www.atlasofsurveillance.org/search?location=Greenbrier+Police+Department%2C+TN)
2. [WSMV, "Middle Tennessee police department explains use of Flock cameras amid privacy concerns. Here's what we know" (July 28, 2026)](https://www.wsmv.com/2026/07/28/middle-tennessee-police-department-explains-use-flock-cameras-amid-privacy-concerns-heres-what-we-know/)
3. [City of Greenbrier Police Department](https://greenbriertn.org/166/Police)
4. [City of Greenbrier Board of Mayor and Aldermen](https://www.greenbriertn.org/176/Mayor-Aldermen)
5. [City of Greenbrier Agenda Center — Mayor and Aldermen](https://greenbriertn.org/AgendaCenter/Mayor-Aldermen-2)
6. [City of Greenbrier Records Request information](https://www.greenbriertn.org/228/Records-Request)
7. [City of Greenbrier Public Records Request Form](https://greenbriertn.org/DocumentCenter/View/443)
8. [Tennessee General Assembly, SB 1664 / HB 2101, Public Chapter 625 (2014)](https://wapp.capitol.tn.gov/apps/BillInfo/Default?BillNumber=SB1664&ga=108)
9. [Tennessee General Assembly, SB 699 / HB 809, Public Chapter 201 (2021)](https://wapp.capitol.tn.gov/apps/BillInfo/Default?BillNumber=SB0699&ga=112)
10. [Tennessee General Assembly, SB 1879 / HB 1642, Public Chapter 672 (2026)](https://wapp.capitol.tn.gov/apps/Billinfo/Default?BillNumber=SB1879&ga=114)
11. [Flock Safety License Plate Reader Policy](https://www.flocksafety.com/legal/lpr-policy)
12. [Flock Safety Piperton TN PD Transparency Portal](https://transparency.flocksafety.com/piperton-tn-pd)
13. [Electronic Frontier Foundation, "What Is ALPR?"](https://www.eff.org/pages/what-alpr)
14. [Leonardo, ELSAG SignalTrace](https://www.leonardocompany-us.com/lpr/elsag-signaltrace)
15. [Leonardo, SignalTrace product sheet](https://www.leonardocompany-us.com/hubfs/LPR/LPR-Product-Sheets/US/eocplus-us.pdf)
16. [United States Supreme Court, *Chatrie v. United States* (June 29, 2026)](https://www.supremecourt.gov/opinions/25pdf/25-112_0am4.pdf)

## Revision history

- **2026-07-28:** Initial research draft prepared for Issue #13. No pull request opened. Local authorization, contract, policy, retention, sharing, and audit records remain outstanding.
- **2026-07-31:** Completed a final public-source sweep; clarified documented network-sharing direction, narrowed SignalTrace claims, updated legal and vendor descriptions, synchronized the research branch with `main`, and confirmed the repository validator passes. No pull request opened.
