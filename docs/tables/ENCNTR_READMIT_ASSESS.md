# ENCNTR_READMIT_ASSESS

> The readmission assessment for the encounter

**Description:** encounter readmission asssessment  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AVOIDABLE_READMISSION_IND` | DOUBLE | NOT NULL |  | Indicates if the readmission was avoidable. |
| 2 | `CLASSIFICATION_CD` | DOUBLE | NOT NULL |  | Code value that defines the classification of the readmission. Code set is 4002598. |
| 3 | `COMMENT_ID` | DOUBLE | NOT NULL | FK→ | identifier of the row on the long_text that holds the comment text for the readmission. |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the Encounter table that relates to the readmission. |
| 5 | `ENCNTR_READMIT_ASSESS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the encntr_readmit_assess table. |
| 6 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | identifier of the organization associated to the readmission. |
| 7 | `POST_ACUTE_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related post-acute provider. |
| 8 | `PREVIOUS_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the Encounter table. This identifier represents the original encounter that was prior to the readmitted encounter. |
| 9 | `READMISSION_REASON_CD` | DOUBLE | NOT NULL |  | Code value that defines the reason for the readmission. Code set is 4002603. |
| 10 | `TLC_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The uniquely identifies facility data on the table will represent long term care facilities that total living choices (tlc) is using to place patients. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `POST_ACUTE_PROVIDER_ID` | [RCM_POST_ACUTE_PROVIDER](RCM_POST_ACUTE_PROVIDER.md) | `RCM_POST_ACUTE_PROVIDER_ID` |
| `PREVIOUS_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `TLC_FACILITY_ID` | [RCM_TLC_FACILITY](RCM_TLC_FACILITY.md) | `RCM_TLC_FACILITY_ID` |

