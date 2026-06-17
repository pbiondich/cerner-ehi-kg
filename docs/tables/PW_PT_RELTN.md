# PW_PT_RELTN

> This table holds the relationship between a PowerPlan and PowerTrial.

**Description:** Pathway PowerTrial Relation  
**Table type:** REFERENCE  
**Primary key:** `PW_PT_RELTN_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `MINIMUM_ENROLLMENT_STATUS_FLAG` | DOUBLE | NOT NULL |  | Minimum enrollment status of the PowerTrial needed in order for the PowerPlan to be considered. 0 - None 1 - Consent Pending 2 - Enrolled |
| 5 | `ORDERING_POLICY_FLAG` | DOUBLE | NOT NULL |  | The Action that should be taken when the PowerPlan is added. 0 - No Action 1 - Warn - Consent Pending 2 - Warn 3 - Stop |
| 6 | `PATHWAY_CATALOG_ID` | DOUBLE | NOT NULL | FK→ | Pathway catalog identification. Unique id of the pathway catalog entry referenced by an entry on this table. |
| 7 | `PREV_PW_PT_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The id of the most of to date row in this table that shares the same history. |
| 8 | `PROT_MASTER_ID` | DOUBLE | NOT NULL | FK→ | PowerTrial identification. Unique id of the PowerTrial entry referenced by an entry on this table. |
| 9 | `PW_PT_RELTN_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 10 | `REQUIRE_OVERRIDE_REASON_IND` | DOUBLE | NOT NULL |  | Indicator for whether the user can provide an override reason when adding the PowerPlan. |
| 11 | `SEQUENCE` | DOUBLE | NOT NULL |  | The sequence number of the entry. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PATHWAY_CATALOG_ID` | [PATHWAY_CATALOG](PATHWAY_CATALOG.md) | `PATHWAY_CATALOG_ID` |
| `PREV_PW_PT_RELTN_ID` | [PW_PT_RELTN](PW_PT_RELTN.md) | `PW_PT_RELTN_ID` |
| `PROT_MASTER_ID` | [PROT_MASTER](PROT_MASTER.md) | `PROT_MASTER_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PW_PT_RELTN](PW_PT_RELTN.md) | `PREV_PW_PT_RELTN_ID` |

