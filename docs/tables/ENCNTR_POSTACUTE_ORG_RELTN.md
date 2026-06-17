# ENCNTR_POSTACUTE_ORG_RELTN

> Post acute organization candidates for an encounter.

**Description:** Encounter Post Acute Organization Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the Long_text table that represents a comment for this relationship. |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the Encounter table. |
| 7 | `ENCNTR_POSTACUTE_ORG_RELTN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the Encntr_postacute_org_reltn table. |
| 8 | `FINAL_PLACEMENT_IND` | DOUBLE | NOT NULL |  | Indicates the post acute organization that was selected as the placement for the encounter. There can only be one row marked as TRUE per encounter. |
| 9 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the Organization table. |
| 10 | `PATIENT_REASON_CD` | DOUBLE | NOT NULL |  | The patients reason for selecting the post acute organization for final placement. |
| 11 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | The priority of the post acute organizations for the encounter. |
| 12 | `RESPONSE_CD` | DOUBLE | NOT NULL |  | The response from the post acute organization to the placement request. |
| 13 | `RESPONSE_REASON_CD` | DOUBLE | NOT NULL |  | The reason for the response from the post acute organization to the placement request. |
| 14 | `SELECTED_ORG_TYPE_CD` | DOUBLE | NOT NULL |  | The selected post acute organization type for this dandidate. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

