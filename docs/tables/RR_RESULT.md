# RR_RESULT

> Each row represents one task assay of a round robin instrument/procedure combo.

**Description:** Round Robin Result  
**Table type:** ACTIVITY  
**Primary key:** `RR_RESULT_ID`  
**Columns:** 15  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific round robin accession associated with the discrete task assay result. Creates a relationship to the accession table. |
| 2 | `EXCLUDE_IND` | DOUBLE |  |  | Indicates whether this result is included or excluded from the calculation of the Mean and Standard Deviation. A value of 0 indicates the result should be included in the calculation. A value of 1 indicates the result should be excluded from the calculation. |
| 3 | `MEANDIFF` | DOUBLE |  |  | Stores the difference from the mean value that is calculated in the Round Robin Inquiry application. |
| 4 | `RESULT_STATUS_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the current status (such as performed, verified, or corrected) of the round robin result. |
| 5 | `ROUND_ROBIN_REF_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific round robin template associated with the result. Creates a relationship to the round robin reference table. |
| 6 | `RR_RESULT_ID` | DOUBLE | NOT NULL | PK | A unique, internal, system-assigned number that identifies a specific round robin result. |
| 7 | `SAVED_IND` | DOUBLE |  |  | Indicates whether the statistics for this result have been saved. Statistics must be saved before viewing the QC Round Robin Graphs. A value of 0 indicates the statistics have not been saved. A value of 1 indicates the statistics have been saved. |
| 8 | `SDI` | DOUBLE |  |  | Stores the standard deviation interval value calculated in Round Robin Inquiry. |
| 9 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the specific service resource where the result was performed. |
| 10 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the specific discrete task assay associated with the round robin result. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCESSION_ID` | [RR_ACCESSION_R](RR_ACCESSION_R.md) | `ACCESSION_ID` |
| `ROUND_ROBIN_REF_ID` | [RR_ACCESSION_R](RR_ACCESSION_R.md) | `ROUND_ROBIN_REF_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [RR_PERFORM_RESULT](RR_PERFORM_RESULT.md) | `RR_RESULT_ID` |
| [RR_RESULT_EVENT](RR_RESULT_EVENT.md) | `RR_RESULT_ID` |

