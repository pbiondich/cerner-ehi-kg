# CV_EXT_IDENTIFIER

> This table holds the external identifiers for the document sent from external sources (e.g. FHIR)

**Description:** Cardiovascular External Identifier  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSIGNER_ORG_ID` | DOUBLE |  |  | Unique identifier of the EXTERNAL organization that issued/managed the external identifier. |
| 2 | `CV_EXT_IDENTIFIER_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `CV_STG_METADATA_ID` | DOUBLE |  | FK→ | Unique identifier of the staging metadata. |
| 4 | `EVENT_ID` | DOUBLE |  |  | Identifies an event from the clinical event table |
| 5 | `EXT_IDENTIFIER_VALUE` | DOUBLE |  |  | *** OBSOLETE ***The Value of the external identifier. |
| 6 | `SYSTEM_URI` | VARCHAR(255) |  |  | Namespace for the identifier value. |
| 7 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `VALUE_TXT` | VARCHAR(255) |  |  | Value of the external identifier. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CV_STG_METADATA_ID` | [CV_STG_METADATA](CV_STG_METADATA.md) | `CV_STG_METADATA_ID` |

