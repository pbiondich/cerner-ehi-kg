# AP_DIAG_RPT_REVIEW

> This activity table contains information about all of the report components that were automatically coded (in terms of diagnostic coding) and are verified. The information on this table is used when printing the Diagnostic Code Assignment Review Report.

**Description:** AP Diag Report Review  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification code assigned to the clinical event tables that contain the report text information for the coded report component. |
| 2 | `PREFIX_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the prefix assigned to the case number that is associated with the report component that was flagged for automatic coding. The purpose of this field is to provide "filtering" options when printing the Diagnostic Code Assignment Review Report option of the Pathology QA Reports application. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 8 | `VERIFIED_DT_TM` | DATETIME | NOT NULL |  | This field contains the date and time the report was verified. |
| 9 | `VERIFIED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the user who initiated the report verification event. Information about the user can be obtained by viewing or joining to the PERSON and/or PRSNL tables. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREFIX_ID` | [AP_PREFIX](AP_PREFIX.md) | `PREFIX_ID` |
| `VERIFIED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

