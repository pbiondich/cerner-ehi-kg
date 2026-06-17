# CHARGE_BATCH_DETAIL_FIELD

> Store additional data element fields related to CHARGE_BATCH_DETAIL.

**Description:** Charge Batch Detail Field  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CHARGE_BATCH_DETAIL_FIELD_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a data element field. |
| 3 | `CHARGE_BATCH_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related Charge Batch Detail record. |
| 4 | `FIELD_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the field that is being used. |
| 5 | `FIELD_VALUE_CD` | DOUBLE | NOT NULL |  | Stores the related code value. The code values that are stored here could be from different code sets. |
| 6 | `FIELD_VALUE_CHAR` | VARCHAR(200) | NOT NULL |  | Stores the related string values. |
| 7 | `FIELD_VALUE_DT_TM` | DATETIME |  |  | Stores related date and time values. |
| 8 | `FIELD_VALUE_END_DT_TM` | DATETIME |  |  | Stores the related end date and time values. |
| 9 | `FIELD_VALUE_IND` | DOUBLE | NOT NULL |  | Store related short numeric values. |
| 10 | `FIELD_VALUE_NBR` | DOUBLE | NOT NULL |  | Stores related numeric values. |
| 11 | `FIELD_VALUE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Store the related personnel id. |
| 12 | `FIELD_VALUE_START_DT_TM` | DATETIME |  |  | Sortes related start date and time values. |
| 13 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | Identifies a sequencing priority to be used when there is more than one set of related rows. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHARGE_BATCH_DETAIL_ID` | [CHARGE_BATCH_DETAIL](CHARGE_BATCH_DETAIL.md) | `CHARGE_BATCH_DETAIL_ID` |
| `FIELD_VALUE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

