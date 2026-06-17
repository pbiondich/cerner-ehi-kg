# REPORT_HISTORY_GROUPING_R

> This reference table contains the associations between pathology history groupings, defined on codeset 1311, and the report component procedures (discrete tasks) that are associated with the groupings.

**Description:** Report History Grouping Reltn  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLLATING_SEQ` | DOUBLE |  |  | This field is used to sequence the report sections. |
| 2 | `GROUPING_CD` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to reference the report history grouping value to which the associated report component procedures (discrete tasks) are assigned. Report history grouping parameters are stored on codeset 1311. |
| 3 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to reference the discrete task report component that is assigned to a report history grouping. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GROUPING_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

