# Adversarial review — Tennessee secretary of state confirms voter-data transfer to DOJ

This is an unpublished editorial review of `2026-08-05-tennessee-confirms-voter-data-transfer-to-doj.md` before the draft is moved into `_entries/`.

Review cutoff: late August 24, 2026 Central Time.

## Verdict

**Verdict: publication-ready in substance after final source-link/current-status check and simultaneous publication of the linked Special Case. No fatal evidentiary defect found.**

The entry has one narrow, reproducible event: on August 5, Secretary of State Tre Hargett directly confirmed that Tennessee had provided voter information to DOJ. The event date is therefore the date of direct official confirmation, not an invented date for the underlying transmission.

## Challenge 1 — Does the title overstate what is proven?

**Finding:** No. Hargett directly confirms Tennessee gave the information to DOJ. Goins independently confirms Tennessee shared voter data.

The title says the secretary of state **confirms** the transfer rather than claiming an exact transfer date or transmission mechanism.

## Challenge 2 — Is the entry pretending DOJ's December 2025 announcement proves the completed transfer?

**Finding:** No. The draft explicitly distinguishes DOJ's December statement of Tennessee's intent from Hargett's later direct confirmation that the information was actually provided.

Preserve this distinction.

## Challenge 3 — Are the transferred fields overstated?

**Finding:** Mostly no. Names, dates of birth, addresses, and last-four Social Security digits are strongly and consistently supported by Tennessee reporting. The exact Tennessee file manifest remains unavailable.

The draft appropriately keeps driver's-license/DMV information qualified and explicitly says there is no evidence of full Social Security numbers.

**Publication rule:** Never shorten the last-four finding to a claim that Tennessee transferred "Social Security numbers" without qualification.

## Challenge 4 — Does the missing MOU imply there were no safeguards?

**Finding:** No. The draft says Tennessee declined DOJ's proposed MOU but expressly leaves open the existence of other correspondence, privacy instructions, retention policies, security controls, or internal procedures.

That is the correct treatment. The absence of a public Tennessee-specific agreement is a documentation gap, not proof of no safeguards.

## Challenge 5 — Does the entry convert DOJ's general SAVE workflow into proof Tennessee's file was processed through SAVE?

**Finding:** No. The draft repeatedly states that DOJ's OLC opinion describes a general federal workflow and that no Tennessee-specific upload/batch/result record has been located.

This is essential and should remain prominent.

## Challenge 6 — Is the entry unfairly implying the transfer itself removed voters or changed votes?

**Finding:** No. It expressly says no evidence establishes misuse, an individual Tennessee removal caused by this transferred copy, or any alteration of votes or ballots.

## Challenge 7 — Is the confidence level too high?

**Finding:** `High` is appropriate for the entry's central event because the completed transfer is directly confirmed by Tennessee's secretary of state and independently by the state elections coordinator. The entry does not assign High confidence to every disputed field or downstream use; those are separately qualified.

## Challenge 8 — Is `event_date: 2026-08-05` misleading because the transfer happened earlier?

**Finding:** No, provided the title and prose continue to frame August 5 as the **confirmation event**. The exact transfer date remains unresolved. This is preferable to inventing an event date for a transmission whose contemporaneous primary record has not been located.

## Challenge 9 — Does this belong in `election-systems-data` rather than general politics?

**Finding:** Yes. The entry concerns a statewide voter-registration dataset, nonpublic identifiers, intergovernmental data transfer, retention/access rules, possible database matching, correction, and accountability. Its core is data governance rather than campaign rhetoric.

## Challenge 10 — What would materially change the entry?

The entry should be revised if a later primary record establishes any of the following:

- a materially different Tennessee field manifest;
- a Tennessee-specific signed agreement governing the transfer;
- a definite retention/deletion schedule or access-control framework;
- proof that Tennessee's DOJ copy was or was not processed through SAVE/DHS;
- a correction by Hargett, Goins, DOJ, or Tennessee regarding whether the transfer occurred; or
- a court ruling that materially changes the legal characterization of DOJ's voter-roll collection program.

## Publication blockers

1. Recheck all cited links immediately before publication.
2. Recheck for a newly released Tennessee transmittal/privacy letter or exact field manifest.
3. Recheck whether any new court order or DOJ/Tennessee statement materially changes the present downstream-use description.
4. Publish the linked Special Case in the same change so `special_case_id: federal-election-administration-2026` resolves under repository validation.
5. Run the repository validator after moving the file to `_entries/`.

## Final assessment

The entry is sufficiently narrow and well supported to serve as the required ordinary Tennessee child entry for the Special Case. Its strongest feature is that the central event is directly confirmed while the harder questions—exact fields, Tennessee-specific safeguards, and onward processing—remain visible as unresolved rather than being inferred.
