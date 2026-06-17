# PM_POST_PROCESS

> Person or Encounters to be processed in off-peak hours.

**Description:** Person Management Post Process  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BATCH_SEQ` | DOUBLE | NOT NULL |  | Contains the batch number that was sent out. |
| 6 | `COMPARISON_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person ID of the comparison person data to be compared during off-peak hours. |
| 7 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Encounter to be processed during off-peak hours. |
| 8 | `ENCNTR_SLICE_ID` | DOUBLE | NOT NULL | FK→ | The encounter slice ID to be processed during off-peak hours. This is a foreign key back to the encntr_slice table. |
| 9 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key to the Organization table. |
| 10 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person to be processed during off-peak hours. |
| 11 | `PM_POST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Shows the date and time the status changed |
| 12 | `PM_POST_PROCESS_ID` | DOUBLE | NOT NULL |  | Person Management Post Process Unique Identifier |
| 13 | `PM_POST_PROCESS_TYPE_CD` | DOUBLE | NOT NULL |  | Type of off-peak processing to be done. |
| 14 | `PROCESS_RESULT_CD` | DOUBLE | NOT NULL |  | Contains a code to represent the result message returned after processing is attempted. |
| 15 | `PROCESS_STATUS_CD` | DOUBLE | NOT NULL |  | Contains the status of the row |
| 16 | `SOURCE_VERSION_NUMBER` | VARCHAR(255) |  |  | Version number assigned from a master system to this record. Added to support the UK's PDS serial change number. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMPARISON_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENCNTR_SLICE_ID` | [ENCNTR_SLICE](ENCNTR_SLICE.md) | `ENCNTR_SLICE_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

