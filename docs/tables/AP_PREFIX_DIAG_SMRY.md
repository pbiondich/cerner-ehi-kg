# AP_PREFIX_DIAG_SMRY

> Contains a record which stores diagnosis summary information of an AP Prefix. Diagnosis summary is used for non cytology cases only and will allow the user to enter in a description within an alpha response or free text comment.

**Description:** Anatomic Pathology Prefix Diagnosis Summary  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `COMMENT_IND` | DOUBLE | NOT NULL |  | This field contains an indicator documenting whether to allow a free text comment for the summary or not. |
| 3 | `COMMENT_LENGTH_QTY` | DOUBLE | NOT NULL |  | This field contains the maximum length or characters the free text field will hold. |
| 4 | `PREFIX_DIAG_SMRY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies diagnosis summary information for an AP Prefix. |
| 5 | `PREFIX_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the row in the AP_PREFIX table related to this summary record. |
| 6 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | This field contains an indicator documenting whether the summary report component procedure is required or optional. |
| 7 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the specific discrete task assay related to this summary record. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREFIX_ID` | [AP_PREFIX](AP_PREFIX.md) | `PREFIX_ID` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

