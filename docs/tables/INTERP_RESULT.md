# INTERP_RESULT

> A reference of the result associated with the interpretation pattern.

**Description:** Interpretation Result  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `DAYS_INELIGIBLE` | DOUBLE | NOT NULL |  | This field will only be used for donor interpretations. It will be used to indicate the number of days the donor should be deferred if the result is a temporary deferral. |
| 6 | `DONOR_ELIGIBILITY_CD` | DOUBLE | NOT NULL |  | This is the eligibility code that will post to the donor's record for the defined hash pattern. |
| 7 | `HASH_PATTERN` | VARCHAR(255) |  |  | The hash pattern defined for this interpretation (ex. "1, 0, 1, 0, 1"). |
| 8 | `INTERP_ID` | DOUBLE | NOT NULL | FK→ | The primary key to the INTERP_TASK_ASSAY table. An internal system-assigned number that ties each row in this table to the INTERP_TASK_ASSAY table. |
| 9 | `INTERP_RESULT_ID` | DOUBLE | NOT NULL |  | The primary key to this table. An internal system-assigned number that ensures the uniqueness of each row on this table. |
| 10 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Links the long text for an interpretation pattern to the row on the LONG_TEXT table where the actual text is stored. |
| 11 | `RESULT_CD` | DOUBLE | NOT NULL |  | The code value that represents the result which should be associated with this interpretation pattern. The code set will vary depending on the result. |
| 12 | `RESULT_NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Links this table to the nomenclature table for the result associated with this pattern. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INTERP_ID` | [INTERP_TASK_ASSAY](INTERP_TASK_ASSAY.md) | `INTERP_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `RESULT_NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

